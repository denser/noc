# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# <describe module here>
# ----------------------------------------------------------------------
# Copyright (C) 2007-2019 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Third-part modules
import six
from mongoengine.document import Document
from mongoengine.fields import StringField, BooleanField, IntField, GeoPointField


@six.python_2_unicode_compatible
class Area(Document):
    meta = {"strict": False, "auto_create_index": False, "collection": "noc.gis.areas"}

    name = StringField()
    is_active = BooleanField(default=True)
    min_zoom = IntField(default=0)
    max_zoom = IntField(default=18)
    # (EPSG:4326) coordinates
    SW = GeoPointField()
    NE = GeoPointField()
    description = StringField(required=False)

    def __str__(self):
        return self.name
