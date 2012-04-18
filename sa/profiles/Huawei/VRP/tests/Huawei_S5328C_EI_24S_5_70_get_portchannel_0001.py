# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Huawei.VRP.get_portchannel test
## Auto-generated by ./noc debug-script at 18.04.2012 12:51:54
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Huawei_VRP_get_portchannel_Test(ScriptTestCase):
    script = "Huawei.VRP.get_portchannel"
    vendor = "Huawei"
    platform = "S5328C-EI-24S"
    version = "5.70"
    input = {}
    result = [{'interface': 'Eth-Trunk0',
  'members': ['GigabitEthernet0/0/1', 'GigabitEthernet0/0/2'],
  'type': 'S'}]
    motd = ''
    cli = {
'screen-length 0 temporary':  'screen-length 0 temporary\nInfo: The configuration takes effect on the current user terminal interface only.\n', 
## 'display version'
'display version': """display version
Huawei Versatile Routing Platform Software
VRP (R) software, Version 5.70 (S5300 V100R005C01SPC100)
Copyright (C) 2000-2011 HUAWEI TECH CO., LTD
Quidway S5328C-EI-24S Routing Switch uptime is 24 weeks, 5 days, 18 hours, 26 minutes

EFGF 0(Master) : uptime is 24 weeks, 5 days, 18 hours, 26 minutes
256M bytes DDR Memory
32M bytes FLASH
Pcb      Version :  VER A
Basic  BOOTROM  Version :  107 Compiled at Jan 18 2011, 22:52:53
CPLD   Version : 69 
Software Version : VRP (R) Software, Version 5.70 (S5300 V100R005C01SPC100)
FANCARD information
Pcb      Version : FAN VER B
PWRCARD I information
Pcb      Version : PWR VER A
PWRCARD II information
Pcb      Version : PWR VER A
""", 
## 'display eth-trunk'
'display eth-trunk': """display eth-trunk
Eth-Trunk0's state information is:
WorkingMode: NORMAL         Hash arithmetic: According to SA-XOR-DA           
Least Active-linknumber: 1  Max Bandwidth-affected-linknumber: 8              
Operate status: up          Number Of Up Port In Trunk: 1                     
--------------------------------------------------------------------------------
PortName                      Status      Weight 
GigabitEthernet0/0/1          Up          1      
GigabitEthernet0/0/2          Down        1      
  """, 
}
    snmp_get = {}
    snmp_getnext = {}
    http_get = {}
