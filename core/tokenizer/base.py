# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# BaseTokenizer
# ----------------------------------------------------------------------
# Copyright (C) 2007-2019 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------


class BaseTokenizer(object):
    name = None

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        raise StopIteration
