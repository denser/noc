# ----------------------------------------------------------------------
# ResourceGroup model
# ----------------------------------------------------------------------
# Copyright (C) 2007-2020 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
import operator
import threading
from typing import List

# Third-party modules
import bson
from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import StringField, LongField, ListField, EmbeddedDocumentField
from mongoengine.errors import ValidationError
from pymongo import UpdateMany
import cachetools

# NOC modules
from noc.config import config
from noc.models import get_model, is_document
from noc.core.mongo.fields import PlainReferenceField
from noc.core.model.decorator import on_delete_check, on_save, tree
from noc.core.change.decorator import change
from noc.core.bi.decorator import bi_sync
from noc.main.models.remotesystem import RemoteSystem
from noc.main.models.label import Label
from .technology import Technology

id_lock = threading.Lock()
_path_cache = cachetools.TTLCache(maxsize=100, ttl=60)


def check_rg_parent(parent: "ResourceGroup"):
    if not parent.technology.allow_children:
        raise ValidationError(f"[{parent}] Parent technology is not allowed children")


class MatchLabels(EmbeddedDocument):
    labels = ListField(StringField())

    def __str__(self):
        return ", ".join(self.labels)

    def get_labels(self):
        return list(Label.objects.filter(name__in=self.labels))


@tree()
@Label.model
@bi_sync
@change
@on_save
@on_delete_check(
    check=[
        ("inv.ResourceGroup", "parent"),
        # sa.ManagedObject
        ("sa.ManagedObject", "static_service_groups"),
        ("sa.ManagedObject", "effective_service_groups"),
        ("sa.ManagedObject", "static_client_groups"),
        ("sa.ManagedObject", "effective_client_groups"),
        # sa.ManagedObjectSelector
        ("sa.ManagedObjectSelector", "filter_service_group"),
        ("sa.ManagedObjectSelector", "filter_client_group"),
        # phone.PhoneRange
        ("phone.PhoneRange", "static_service_groups"),
        ("phone.PhoneRange", "effective_service_groups"),
        ("phone.PhoneRange", "static_client_groups"),
        ("phone.PhoneRange", "effective_client_groups"),
        # phone.PhoneNumber
        ("phone.PhoneNumber", "static_service_groups"),
        ("phone.PhoneNumber", "effective_service_groups"),
        ("phone.PhoneNumber", "static_client_groups"),
        ("phone.PhoneNumber", "effective_client_groups"),
        # sa.Service
        ("sa.Service", "static_service_groups"),
        ("sa.Service", "effective_service_groups"),
        ("sa.Service", "static_client_groups"),
        ("sa.Service", "effective_client_groups"),
        # SA
        ("sa.CommandSnippet", "resource_group"),
        ("sa.ObjectNotification", "resource_group"),
        # FM
        ("fm.AlarmDiagnosticConfig", "resource_group"),
        ("fm.AlarmEscalation", "escalations__resource_group"),
        ("fm.AlarmTrigger", "resource_group"),
        ("fm.EventTrigger", "resource_group"),
        #
        ("vc.VCDomainProvisioningConfig", "resource_group"),
    ]
)
class ResourceGroup(Document):
    """
    Technology

    Abstraction to restrict ResourceGroup links
    """

    meta = {
        "collection": "resourcegroups",
        "strict": False,
        "auto_create_index": False,
        "indexes": [
            "dynamic_service_labels.labels",
            "dynamic_client_labels.labels",
            "labels",
            "effective_labels",
        ],
    }

    # Group | Name
    name = StringField()
    technology = PlainReferenceField(Technology)
    parent = PlainReferenceField("inv.ResourceGroup", validation=check_rg_parent)
    description = StringField()
    dynamic_service_labels = ListField(EmbeddedDocumentField(MatchLabels))
    dynamic_client_labels = ListField(EmbeddedDocumentField(MatchLabels))
    # @todo: FM integration
    # Integration with external NRI and TT systems
    # Reference to remote system object has been imported from
    remote_system = PlainReferenceField(RemoteSystem)
    # Object id in remote system
    remote_id = StringField()
    # Object id in BI
    bi_id = LongField(unique=True)
    # Labels
    labels = ListField(StringField())
    effective_labels = ListField(StringField())

    _id_cache = cachetools.TTLCache(maxsize=100, ttl=60)
    _bi_id_cache = cachetools.TTLCache(maxsize=100, ttl=60)
    _nested_cache = cachetools.TTLCache(maxsize=1000, ttl=60)

    def __str__(self):
        return "%s (%s)" % (self.name, self.technology.name)

    @classmethod
    @cachetools.cachedmethod(operator.attrgetter("_id_cache"), lock=lambda _: id_lock)
    def get_by_id(cls, id):
        return ResourceGroup.objects.filter(id=id).first()

    @classmethod
    @cachetools.cachedmethod(operator.attrgetter("_bi_id_cache"), lock=lambda _: id_lock)
    def get_by_bi_id(cls, id):
        return ResourceGroup.objects.filter(bi_id=id).first()

    @classmethod
    def _reset_caches(cls, id):
        try:
            del cls._id_cache[
                str(id),  # Tuple
            ]
        except KeyError:
            pass

    @cachetools.cached(_path_cache, key=lambda x: str(x.id), lock=id_lock)
    def get_path(self):
        """
        Returns list of parent segment ids
        :return:
        """
        if self.parent:
            return self.parent.get_path() + [self.id]
        return [self.id]

    def iter_changed_datastream(self, changed_fields=None):
        if config.datastream.enable_resourcegroup:
            yield "resourcegroup", self.id

    @property
    def has_children(self):
        return bool(ResourceGroup.objects.filter(parent=self.id).only("id").first())

    @classmethod
    @cachetools.cachedmethod(operator.attrgetter("_nested_cache"), lock=lambda _: id_lock)
    def get_nested_ids(cls, resource_group):
        """
        Return id of this and all nested segments
        :return:
        """
        if hasattr(resource_group, "id"):
            resource_group = resource_group.id
        elif isinstance(resource_group, str):
            resource_group = bson.ObjectId(resource_group)

        # $graphLookup hits 100Mb memory limit. Do not use it
        seen = {resource_group}
        wave = {resource_group}
        max_level = 10
        coll = ResourceGroup._get_collection()
        for _ in range(max_level):
            # Get next wave
            wave = (
                set(d["_id"] for d in coll.find({"parent": {"$in": list(wave)}}, {"_id": 1})) - seen
            )
            if not wave:
                break
            seen |= wave
        return list(seen)

    @classmethod
    def can_set_label(cls, label):
        return Label.get_effective_setting(label, setting="enable_resourcegroup")

    def on_save(self):
        self._reset_caches(self.id)
        if (
            hasattr(self, "_changed_fields")
            and "dynamic_service_labels" in self._changed_fields
            and self.technology.service_model
        ):
            self.unset_service_group(self.technology.service_model)
        if (
            hasattr(self, "_changed_fields")
            and "dynamic_client_labels" in self._changed_fields
            and self.technology.client_model
        ):
            self.unset_cient_group(self.technology.client_model)

    def unset_service_group(self, model_id: str):
        from django.db import connection

        model = get_model(model_id)
        if is_document(model):
            coll = model._get_collection()
            coll.bulk_write(
                [
                    UpdateMany(
                        {"effective_service_groups": {"$in": [self.id]}},
                        {"$pull": {"effective_service_groups": {"$in": [self.id]}}},
                    )
                ]
            )
        else:
            sql = f"UPDATE {model._meta.db_table} SET effective_service_groups=array_remove(effective_service_groups, '{str(self.id)}') WHERE '{str(self.id)}'=ANY (effective_service_groups)"
            cursor = connection.cursor()
            cursor.execute(sql)

    def unset_cient_group(self, model_id: str):
        from django.db import connection

        model = get_model(model_id)
        if is_document(model):
            coll = model._get_collection()
            coll.bulk_write(
                [
                    UpdateMany(
                        {"effective_client_groups": {"$in": [self.id]}},
                        {"$pull": {"effective_client_groups": {"$in": [self.id]}}},
                    )
                ]
            )
        else:
            sql = f"UPDATE {model._meta.db_table} SET effective_client_groups=array_remove(effective_client_groups, '{str(self.id)}') WHERE '{str(self.id)}'=ANY (effective_service_groups)"
            cursor = connection.cursor()
            cursor.execute(sql)

    @classmethod
    def get_dynamic_service_groups(cls, labels: List[str], model: str) -> List[str]:
        coll = cls._get_collection()
        r = []
        if not model:
            return r
        print(labels, model)
        for rg in coll.aggregate(
            [
                {"$match": {"dynamic_service_labels.labels": {"$in": labels}}},
                {
                    "$lookup": {
                        "from": "technologies",
                        "localField": "technology",
                        "foreignField": "_id",
                        "as": "tech",
                    }
                },
                {
                    "$match": {
                        "tech.service_model": model,
                    }
                },
                {
                    "$project": {
                        "bool_f": {
                            "$anyElementTrue": [
                                {
                                    "$map": {
                                        "input": "$dynamic_service_labels.labels",
                                        "as": "item",
                                        "in": {"$setIsSubset": ["$$item", labels]},
                                    }
                                }
                            ]
                        }
                    }
                },
                {"$match": {"bool_f": True}},
            ]
        ):
            r.append(rg["_id"])
        return r

    @classmethod
    def get_dynamic_client_groups(cls, labels: List[str], model: str) -> List[str]:
        coll = cls._get_collection()
        r = []
        if not model:
            return r
        for rg in coll.aggregate(
            [
                {"$match": {"dynamic_client_labels.labels": {"$in": labels}}},
                {
                    "$lookup": {
                        "from": "technologies",
                        "localField": "technology",
                        "foreignField": "_id",
                        "as": "tech",
                    }
                },
                {
                    "$match": {
                        "tech.client_model": model,
                    }
                },
                {
                    "$project": {
                        "bool_f": {
                            "$anyElementTrue": [
                                {
                                    "$map": {
                                        "input": "dynamic_client_labels.labels",
                                        "as": "item",
                                        "in": {"$setIsSubset": ["$$item", labels]},
                                    }
                                }
                            ]
                        }
                    }
                },
                {"$match": {"bool_f": True}},
            ]
        ):
            rg.append(rg["_id"])
        return r
