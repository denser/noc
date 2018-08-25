# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Platform
# ---------------------------------------------------------------------
# Copyright (C) 2007-2017 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
from __future__ import absolute_import
import os
import threading
import operator
import uuid
import datetime
# Third-party modules
from mongoengine.document import Document
from mongoengine.fields import StringField, LongField, UUIDField
from mongoengine.errors import NotUniqueError
import cachetools
# NOC modules
from .vendor import Vendor
from noc.lib.nosql import PlainReferenceField, DateField
from noc.core.model.decorator import on_delete_check
from noc.core.bi.decorator import bi_sync
from noc.lib.prettyjson import to_json

id_lock = threading.Lock()


@bi_sync
@on_delete_check(check=[
    ("sa.ManagedObject", "platform")
])
class Platform(Document):
    meta = {
        "collection": "noc.platforms",
        "strict": False,
        "auto_create_index": False,
        "json_collection": "inv.platforms",
        "json_unique_fields": ["vendor", "name"],
        "indexes": [
            {
                "fields": ["vendor", "name"],
                "unique": True
            }
        ]
    }
    vendor = PlainReferenceField(Vendor)
    name = StringField()
    description = StringField(required=False)
    # Full name, combined from vendor platform
    full_name = StringField(unique=True)
    # Platform start of sale date
    start_of_sale = DateField()
    # Platform end of sale date
    end_of_sale = DateField()
    # Platform end of support date
    end_of_support = DateField()
    # End of extended support date (installation local)
    end_of_xsupport = DateField()
    # SNMP OID value
    # sysObjectID.0
    snmp_sysobjectid = StringField(regex=r"^1.3.6(\.\d+)+$")
    # Global ID
    uuid = UUIDField(binary=True)
    # Object id in BI
    bi_id = LongField(unique=True)

    _id_cache = cachetools.TTLCache(1000, ttl=60)
    _bi_id_cache = cachetools.TTLCache(1000, ttl=60)
    _ensure_cache = cachetools.TTLCache(1000, ttl=60)

    def __unicode__(self):
        return self.full_name

    def clean(self):
        self.full_name = "%s %s" % (self.vendor.name, self.name)
        super(Platform, self).clean()

    @classmethod
    @cachetools.cachedmethod(operator.attrgetter("_id_cache"),
                             lock=lambda _: id_lock)
    def get_by_id(cls, id):
        return Platform.objects.filter(id=id).first()

    @classmethod
    @cachetools.cachedmethod(operator.attrgetter("_bi_id_cache"),
                             lock=lambda _: id_lock)
    def get_by_bi_id(cls, id):
        return Platform.objects.filter(bi_id=id).first()

    def to_json(self):
        r = {
            "$collection": self._meta["json_collection"],
            "vendor__name": self.vendor.name,
            "name": self.name,
            "uuid": self.uuid
        }
        if self.description:
            r["description"] = self.description
        if self.start_of_sale:
            r["start_of_sale"] = self.start_of_sale.strftime("%Y-%m-%d")
        if self.end_of_sale:
            r["end_of_sale"] = self.end_of_sale.strftime("%Y-%m-%d")
        if self.end_of_support:
            r["end_of_support"] = self.end_of_support.strftime("%Y-%m-%d")
        if self.snmp_sysobjectid:
            r["snmp_sysobjectid"] = self.snmp_sysobjectid
        return to_json(r, order=[
            "vendor__name", "name", "$collection", "uuid", "description",
            "start_of_sale", "end_of_sale", "end_of_support",
            "snmp_sysobjectid"])

    def get_json_path(self):
        return os.path.join(self.vendor.code,
                            "%s.json" % self.code)

    @classmethod
    @cachetools.cachedmethod(
        operator.attrgetter("_ensure_cache"),
        key=lambda s, v, n: "%s-%s" % (v.id, n),
        lock=lambda _: id_lock)
    def ensure_platform(cls, vendor, name):
        """
        Get or create platform by vendor and code
        :param vendor:
        :param name:
        :return:
        """
        while True:
            platform = Platform.objects.filter(
                vendor=vendor.id,
                name=name
            ).first()
            if platform:
                return platform
            try:
                platform = Platform(
                    vendor=vendor,
                    name=name,
                    uuid=uuid.uuid4()
                )
                platform.save()
                return platform
            except NotUniqueError:
                pass  # Already created by concurrent process, reread

    @property
    def is_end_of_sale(self):
        """
        Check if platform reached end-of-sale mark
        :return:
        """
        if not self.end_of_sale:
            return False
        return datetime.date.today() > self.end_of_sale

    @property
    def is_end_of_support(self):
        """
        Check if platform reached end-of-support mark
        :return:
        """
        deadline = []
        if self.end_of_support:
            deadline += [self.end_of_support]
        if self.end_of_xsupport:
            deadline += [self.end_of_xsupport]
        if deadline:
            return datetime.date.today() > max(deadline)
        else:
            return False
