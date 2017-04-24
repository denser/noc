# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Vendor: Raisecom
## OS:     ROS
##----------------------------------------------------------------------
## Copyright (C) 2007-2016 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""
"""
## Python modules
import re
## NOC modules
from noc.core.profile.base import BaseProfile


class Profile(BaseProfile):
    name = "Raisecom.ROS"
    pattern_more = "^ --More--\s*"
    pattern_unpriveleged_prompt = r"^\S+?>"
    command_super = "enable"
    pattern_prompt = r"^\S+?#"
    command_more = " "
    command_exit = "exit"
    rogue_chars = [re.compile(r"\x08+\s+\x08+"), "\r"]

    rx_ver = re.compile(
        r"Product name: (?P<platform>\S+)\s*\n"
        r"(ROS|QOS)\s+Version\s*(?P<version>\S+)\.\s*\(Compiled.+\)\s*\n"
        r"(Support ipv6\s*:\s*\S+\s*\n)?"
        r"Bootstrap\s*Version\s*(?P<bootstrap>\S+)\s*\n"
        r"FPGA Version\s*\n"
        r"Hardware\s*\S+\s*Version Rev\.\s*(?P<hw_rev>\S+)\s*\n\n"
        r"System MacAddress is\s*:\s*(?P<mac>\S+)\s*\n"
        r"Serial number\s*:\s*(?P<serial>\S+)\s*\n",
        re.MULTILINE)

    rx_ver2 = re.compile(
        r"Product Name: (?P<platform>\S+)\s*\n"
        r"Hardware Version: (?P<hw_rev>\S+)\s*\n"
        r"Bootstrap Version: (?P<bootstrap>\S+)\s*\n"
        r"Software Version: (?P<version>\S+)\s*\n"
        r"PCB Version:.+\n"
        r"CPLD Version:.+\n"
        r"REAP Version:.+\n"
        r"Compiled.+\n\n"
        r"System MacAddress: (?P<mac>\S+)\s*\n"
        r"Serial number: (?P<serial>\S+)\s*\n",
        re.MULTILINE)

    def get_version(self, script):
        c = script.cli("show version", cached=True)
        match = self.rx_ver.search(c)
        if match:
            return match.groupdict()
        else:
            match = self.rx_ver2.search(c)
            return match.groupdict()

    def get_interface_names(self, name):
        r = []
        if name.startswith("port "):
            r += [name[5:]]
        else:
            r += ["port %s" % name]
        return r
