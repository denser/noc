# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Cisco.IOS.get_vlans test
## Auto-generated by manage.py debug-script at 2010-12-13 14:56:40
##----------------------------------------------------------------------
## Copyright (C) 2007-2010 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
from noc.lib.test import ScriptTestCase
class Cisco_IOS_get_vlans_Test(ScriptTestCase):
    script="Cisco.IOS.get_vlans"
    vendor="Cisco"
    platform='uBR7114'
    version='12.3(32)BC5'
    input={}
    result=[{'name': 'XXXTelekom', 'vlan_id': 9},
 {'name': 'bldxrad', 'vlan_id': 231},
 {'name': 'xxxbank', 'vlan_id': 219},
 {'name': 'ubrp', 'vlan_id': 208},
 {'name': 'xxxxxxBank', 'vlan_id': 356},
 {'name': 'sat', 'vlan_id': 226}]
    motd=' \n\n'
    cli={
## 'show version'
'show version': """show version
Cisco Internetwork Operating System Software 
IOS (tm) EGR Software (UBR7100-IK8SU2-M), Version 12.3(17b)BC3, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 27-Oct-06 16:39 by ccai
Image text-base: 0x60008EB8, data-base: 0x61E98000

ROM: System Bootstrap, Version 12.0(5r)XE2, RELEASE SOFTWARE (fc1)
BOOTLDR: EGR Software (UBR7100-BOOT-M), Version 12.1(7)EC, EARLY DEPLOYMENT RELEASE SOFTWARE (fc1)

cisco uptime is 1 year, 24 weeks, 5 days, 1 hour, 10 minutes
System returned to ROM by power-on
System restarted at 14:42:46 EET Tue Jun 23 2009
System image file is "disk0:ubr7100-ik8su2-mz.123-17b.BC3.bin"


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

cisco uBR7114 (EGR) processor (revision A) with 122880K/73728K bytes of memory.
Processor board ID 33810749
R527x CPU at 225MHz, Implementation 40, Rev 10.0, 2048KB L2 Cache
Last reset from power-on
Bridging software.
X.25 software, Version 3.0.0.
2 FastEthernet/IEEE 802.3 interface(s)
1 Cable Modem network interface(s)
125K bytes of non-volatile configuration memory.

47040K bytes of ATA PCMCIA card at slot 0 (Sector size 512 bytes).
8192K bytes of Flash internal SIMM (Sector size 256K).
Configuration register is 0x2102
""",
'terminal length 0':  'terminal length 0\n',
## 'show running-config | include cable dot1q-vc-map'
'show running-config | include cable dot1q-vc-map': """show running-config | include cable dot1q-vc-map
cable dot1q-vc-map 0000.ca48.35b3 FastEthernet0/0 9 XXXTelekom
cable dot1q-vc-map 0013.11fc.3ef8 FastEthernet0/0 231 bldxrad
cable dot1q-vc-map 0018.c017.cc3e FastEthernet0/0 219 xxxbank
cable dot1q-vc-map 0019.5eec.d634 FastEthernet0/0 208 ubrp
cable dot1q-vc-map 000f.9fed.90b6 FastEthernet0/0 356 xxxxxxBank
cable dot1q-vc-map 0019.5bf9.344c FastEthernet0/0 226 sat""",
}
    snmp_get={}
    snmp_getnext={}
