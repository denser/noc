# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# cm.ValidationPolicySettings tests
# ----------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
from __future__ import absolute_import
# NOC modules
from .base import BaseDocumentTest
from noc.cm.models.validationpolicysettings import ValidationPolicySettings


class TestCmValidationPolicySettings(BaseDocumentTest):
    model = ValidationPolicySettings
