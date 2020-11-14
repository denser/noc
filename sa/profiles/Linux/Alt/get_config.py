# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Linux.Alt.get_config
# ---------------------------------------------------------------------
# Copyright (C) 2007-2020 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules

# NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetconfig import IGetConfig


class Script(BaseScript):
    name = "Linux.Alt.get_config"
    interface = IGetConfig

    always_prefer = "С"

    def execute(self, **kwargs):
        config = ""
        sstring = "-----BEGIN CONFIG BLOCK-----"
        estring = "-----END CONFIG BLOCK-----"
        clicommands = [
            "rpm -qa | sort",
            "cat /etc/fstab",
            'systemctl --all --no-pager | grep -v "session-.*Session"',
        ]
        for command in clicommands:
            config = config + (sstring + "\n" + self.cli(command) + estring + "\n")
        return config
