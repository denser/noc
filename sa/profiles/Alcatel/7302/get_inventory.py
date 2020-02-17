# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Alcatel.7302.get_inventory
# ---------------------------------------------------------------------
# Copyright (C) 2007-2020 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetinventory import IGetInventory


class Script(BaseScript):
    name = "Alcatel.7302.get_inventory"
    interface = IGetInventory
    port_map = {
        7: "7330",
        14: "7330",
        18: "7302",
        19: "7302",
        21: "7302",
    }  # show equipment slot for 7302 with one control plate return 19 slots

    def execute_snmp(self, **kwargs):
        r = []
        slots = 0
        for b_index, b_type, b_revision, b_serial in self.snmp.get_tables(
            [
                "1.3.6.1.4.1.637.61.1.23.3.1.3",
                "1.3.6.1.4.1.637.61.1.23.3.1.17",
                "1.3.6.1.4.1.637.61.1.23.3.1.19",
            ]
        ):
            slots += 1
            if b_type == "EMPTY":
                continue
            if b_revision is None:
                b_revision = ""
            if b_serial is None:
                b_serial = ""
            r += [
                {
                    "num": slots,
                    "type": "BOARD",
                    "vendor": "Alcatel",
                    "part_no": b_type,
                    "revision": b_revision,
                    "serial": b_serial.strip().strip("\x00"),
                }
            ]
        r.insert(
            0,
            {
                "num": "0",
                "type": "CHASSIS",
                "vendor": "Alcatel",
                "part_no": self.port_map[slots],
                "revision": "",
                "serial": "",
            },
        )
        return r
