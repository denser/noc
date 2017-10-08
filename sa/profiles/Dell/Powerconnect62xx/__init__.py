# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Vendor: Dell
# OS:     Powerconnect62xx
# Compatible:
# ---------------------------------------------------------------------
# Copyright (C) 2007-2013 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# NOC modules
from noc.core.profile.base import BaseProfile


class Profile(BaseProfile):
    name = "Dell.Powerconnect62xx"
    pattern_username = "[Uu]ser( [Nn]ame)?:"
    pattern_more = "--More--"
    pattern_unprivileged_prompt = r"^\S+>"
    pattern_syntax_error = r"% Invalid input detected at"
    pattern_prompt = r"^(?P<hostname>\S+(:\S+)*)#"
    command_super = "enable"
    command_enter_config = "configure"
    command_leave_config = "end"
    command_more = " "
    command_exit = "logout"
    command_save_config = "copy running-config startup-config"
    config_volatile = ["^%.*?$"]

    def convert_interface_name(self, interface):
        if interface.lower().startswith("vlan "):
            return "vlan" + interface[6:]
        else:
            return interface
