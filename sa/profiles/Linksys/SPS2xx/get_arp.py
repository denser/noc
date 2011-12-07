# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Linksys.SPS2xx.get_arp
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
import re
## NOC modules
from noc.sa.script import Script as NOCScript
from noc.sa.interfaces import IGetARP


class Script(NOCScript):
    name = "Linksys.SPS2xx.get_arp"
    implements = [IGetARP]
    cache = True

    rx_line = re.compile(
        r"^vlan\s+\d+\s+(?P<interface>\S+)\s+(?P<ip>\S+)\s+(?P<mac>\S+)\s+\S+",
        re.MULTILINE)

    def execute(self):
        r = []
        # BUG http://bt.nocproject.org/browse/NOC-36
        # Try SNMP first
        #        if self.snmp and self.access_profile.snmp_ro:
        #            try:
        #                for i, mac, ip in self.snmp.join_tables("1.3.6.1.2.1.4.22.1.1", "1.3.6.1.2.1.4.22.1.2", "1.3.6.1.2.1.4.22.1.3", bulk=True, cached=True): # IP-MIB
        #                    r.append( {"ip" : ip, "mac" : mac, "interface" : self.snmp.get("1.3.6.1.2.1.31.1.1.1.1."+i, cached=True) } ) # IF-MIB
        #                return r
        #            except self.snmp.TimeOutError:
        #                pass

        # Fallback to CLI
        for match in self.rx_line.finditer(self.cli("show arp", cached=True)):
            mac = match.group("mac")
            if mac.lower() == "incomplete":
                r += [{
                    "ip": match.group("ip"),
                    "mac": None,
                    "interface": None
                }]
            else:
                r += [{
                    "ip": match.group("ip"),
                    "mac": match.group("mac"),
                    "interface": match.group("interface")
                }]
        return r
