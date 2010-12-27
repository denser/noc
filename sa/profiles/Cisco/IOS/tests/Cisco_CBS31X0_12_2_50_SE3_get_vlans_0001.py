# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Cisco.IOS.get_vlans test
## Auto-generated by manage.py debug-script at 2010-12-27 11:51:58
##----------------------------------------------------------------------
## Copyright (C) 2007-2010 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
from noc.lib.test import ScriptTestCase
class Cisco_IOS_get_vlans_Test(ScriptTestCase):
    script="Cisco.IOS.get_vlans"
    vendor="Cisco"
    platform='CBS31X0'
    version='12.2(50)SE3'
    input={}
    result=[{'name': 'default', 'vlan_id': 1},
 {'name': 'Management', 'vlan_id': 2},
 {'name': 'Server_Management', 'vlan_id': 3},
 {'name': 'VPN_Pool', 'vlan_id': 4},
 {'name': 'Local_Internet', 'vlan_id': 5},
 {'name': 'Server_Staging', 'vlan_id': 6},
 {'name': 'BIGVLAN____1', 'vlan_id': 1302}]
    motd=' \nC\nThe system is a property of Innova Distribution LLC.\nPlease disconnect immediately if you are not authorized staff\n\n'
    cli={
## 'show version'
'show version': """show version
Cisco IOS Software, CBS31X0 Software (CBS31X0-UNIVERSALK9-M), Version 12.2(50)SE3, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2009 by Cisco Systems, Inc.
Compiled Wed 22-Jul-09 09:10 by prod_rel_team
Image text-base: 0x00003000, data-base: 0x02400000

ROM: Bootstrap program is CBS31X0 boot loader
BOOTLDR: CBS31X0 Boot Loader (CBS31X0-HBOOT-M) Version 12.2(40r)EX7, RELEASE SOFTWARE (fc1)

sw-8-xx uptime is 17 weeks, 5 days, 23 hours, 31 minutes
System returned to ROM by power-on
System restarted at 13:22:03 MSD Tue Aug 24 2010
System image file is "flash:cbs31x0-universalk9-mz.122-50.SE3/cbs31x0-universalk9-mz.122-50.SE3.bin"


This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

License Level: ipbase
License Type: Permanent
Next reload license Level: ipbase

cisco WS-CBS3120X-S (PowerPC405) processor (revision C0) with 262144K bytes of memory.
Processor board ID FOC1241T0ZM
Last reset from power-on
2 Virtual Ethernet interfaces
1 FastEthernet interface
52 Gigabit Ethernet interfaces
4 Ten Gigabit Ethernet interfaces
The password-recovery mechanism is enabled.

512K bytes of flash-simulated non-volatile configuration memory.
Base ethernet MAC Address       : 00:23:AB:53:1C:80
Motherboard assembly number     : 73-10920-08
Motherboard serial number       : FOC1241133Q
Model revision number           : C0
Motherboard revision number     : A0
Model number                    : WS-CBS3120X-S
System serial number            : FOC1241T0ZM
Top Assembly Part Number        : 800-28520-01
Top Assembly Revision Number    : F0
Version ID                      : V01
CLEI Code Number                : COUIAN1CAA
Hardware Board Revision Number  : 0x00


Switch Ports Model              SW Version            SW Image                 
------ ----- -----              ----------            ----------               
*    1 28    WS-CBS3120X-S      12.2(50)SE3           CBS31X0-UNIVERSALK9-M    
     2 28    WS-CBS3120X-S      12.2(50)SE3           CBS31X0-UNIVERSALK9-M    


Switch 02
---------
Switch Uptime                   : 17 weeks, 5 days, 23 hours, 29 minutes 
Base ethernet MAC Address       : 00:23:EA:D6:57:00
Motherboard assembly number     : 73-10920-08
Motherboard serial number       : FOC12461YC6
Model revision number           : C0
Motherboard revision number     : A0
Model number                    : WS-CBS3120X-S
System serial number            : FOC1247T06J
Top assembly part number        : 800-28520-01
Top assembly revision number    : F0
Version ID                      : V01
CLEI Code Number                : COUIAN1CAA
License Level                   : ipbase
License Type                    : Permanent
Next reboot licensing Level     : ipbase


Configuration register is 0xF
""",
'terminal length 0':  'terminal length 0\n',
## 'show vlan brief'
'show vlan brief': """show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi1/0/4, Gi1/0/17, Gi1/0/18
                                                Gi1/0/23, Gi1/0/24, Gi1/0/25
                                                Gi1/0/26, Te1/0/2, Gi2/0/4
                                                Gi2/0/5, Gi2/0/17, Gi2/0/18
                                                Gi2/0/23, Gi2/0/24, Gi2/0/25
                                                Gi2/0/26, Te2/0/2
2    Management                       active    
3    Server_Management                active    
4    VPN_Pool                         active    
5    Local_Internet                   active    
6    Server_Staging                   active    Gi1/0/5, Gi1/0/6, Gi2/0/6
1302 BIGVLAN____1                     active    """,
}
    snmp_get={}
    snmp_getnext={}
