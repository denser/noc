# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Normative Document object
# ---------------------------------------------------------------------
# Copyright (C) 2007-2019 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Third-party modules
from mongoengine.document import Document
from mongoengine.fields import DateField, StringField


class NormativeDocument(Document):
    meta = {"collection": "noc.normative_documents", "strict": False, "auto_create_index": False}
    name = StringField()
    doc_date = DateField()
    number = StringField()
    # @todo: Type
