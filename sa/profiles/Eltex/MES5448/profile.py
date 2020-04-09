# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Vendor: Eltex
# OS:     MES5448
# ---------------------------------------------------------------------
# Copyright (C) 2007-2020 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------
import re

# NOC modules
from noc.core.profile.base import BaseProfile
from noc.core.comp import smart_text

rx_cpu = re.compile(
    r"5\s+Secs\s+\((?:\s+|)(?P<cpu5sec>\S+)\%\)\s+60\s+\Secs\s+\((?:\s+|)(?P<cpu60sec>\S+)\%\)\s+300\s+\Secs\s+\((?:\s+|)(?P<cpu300sec>\S+)\%\)"
)


def render_regexp(oid, value):
    value = smart_text(value, errors="ignore")
    match = rx_cpu.search(value)
    if match:
        return int(float(match.group("cpu60sec")))


class Profile(BaseProfile):
    name = "Eltex.MES5448"
    pattern_more = [(r"--More-- or \(q\)uit", " ")]
    pattern_unprivileged_prompt = r"^(?P<hostname>\S+)>"
    pattern_prompt = r"^(?P<hostname>\S+)#"
    pattern_syntax_error = (
        r"^% (Unrecognized command|Incomplete command|"
        r"Wrong number of parameters or invalid range, size or "
        r"characters entered)$"
    )
    command_super = "enable"
    command_disable_pager = "terminal length 0"
    snmp_display_hints = {"1.3.6.1.4.1.4413.1.1.1.1.4.9.0": render_regexp}
