# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# peer.PrefixListCache tests
# ----------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
from __future__ import absolute_import
# NOC modules
from .base import BaseDocumentTest
from noc.peer.models.prefixlistcache import PrefixListCache


class TestPeerPrefixListCache(BaseDocumentTest):
    model = PrefixListCache
