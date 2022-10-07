# ----------------------------------------------------------------------
# Linux.Linux.get_interface_properties script
# ----------------------------------------------------------------------
# Copyright (C) 2007-2022 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# NOC modules
from noc.sa.profiles.Generic.get_interface_properties import Script as BaseScript


class Script(BaseScript):
    name = "Linux.Linux.get_interface_properties"
    SNMP_NAME_TABLE = "IF-MIB::ifName"
