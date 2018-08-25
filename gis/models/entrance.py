# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Entrance object
# ---------------------------------------------------------------------
# Copyright (C) 2007-2014 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Third-party modules
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import StringField, IntField, BooleanField


class Entrance(EmbeddedDocument):
    meta = {
        "strict": False,
        "auto_create_index": False
    }
    number = StringField()
    # Floors
    first_floor = IntField()
    last_floor = IntField()
    #
    first_home = StringField()
    last_home = StringField()
    # @todo: Managing company

    def __unicode__(self):
        return self.number
