# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# vc.VPN tests
# ----------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
from __future__ import absolute_import
# NOC modules
from .base import BaseDocumentTest
from noc.vc.models.vpn import VPN


class TestVcVPN(BaseDocumentTest):
    model = VPN
