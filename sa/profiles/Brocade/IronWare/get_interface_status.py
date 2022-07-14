# ---------------------------------------------------------------------
# Brocade.IronWare.get_interface_status
# ---------------------------------------------------------------------
# Copyright (C) 2007-2019 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
import re

# NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetinterfacestatus import IGetInterfaceStatus


class Script(BaseScript):
    name = "Brocade.IronWare.get_interface_status"
    interface = IGetInterfaceStatus
    rx_interface_status = re.compile(r"^(?P<interface>\S+)\s+(?P<status>\S+).+$", re.IGNORECASE)

    def execute_snmp(self, interface=None):
        r = []
        # IF-MIB::ifName, IF-MIB::ifOperStatus
        for i, n, s in self.snmp.join(["1.3.6.1.2.1.31.1.1.1.1", "1.3.6.1.2.1.2.2.1.8"]):
            # ifOperStatus up(1)
            r += [{"interface": n, "status": int(s) == 1}]
        return r

    def execute_cli(self, interface=None):
        r = []
        if interface:
            cmd = "show interface brief | include ^%s" % interface
        else:
            cmd = "show interface brief | excl Port"

        for ln in self.cli(cmd).splitlines():
            ln = ln.replace("Disabled", " Disabled ")
            ln = ln.replace("Up", " Up ")
            ln = ln.replace("DisabN", " Disabled N")
            match = self.rx_interface_status.match(ln)
            if match:
                r += [
                    {
                        "interface": match.group("interface"),
                        "status": match.group("status").lower() == "up",
                    }
                ]
        return r
