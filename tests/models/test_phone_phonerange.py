# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# phone.PhoneRange tests
# ----------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
from __future__ import absolute_import
# NOC modules
from .base import BaseDocumentTest
from noc.phone.models.phonerange import PhoneRange


class TestPhonePhoneRange(BaseDocumentTest):
    model = PhoneRange
