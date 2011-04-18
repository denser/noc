# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Cisco.IOS.get_version test
## Auto-generated by manage.py debug-script at 2011-02-02 14:03:56
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
from noc.lib.test import ScriptTestCase
class Cisco_IOS_get_version_Test(ScriptTestCase):
    script="Cisco.IOS.get_version"
    vendor="Cisco"
    platform='CBS31X0'
    version='12.2(55)SE'
    input={}
    result={'attributes': {'image': 'CBS31X0-UNIVERSALK9-M'},
 'platform': 'CBS31X0',
 'vendor': 'Cisco',
 'version': '12.2(55)SE'}
    motd=' \nC\nThe system is a property of Acme Inc.\nPlease disconnect immediately if you are not authorized staff\n\n'
    cli={
## 'show version'
'show version': """show version
Cisco IOS Software, CBS31X0 Software (CBS31X0-UNIVERSALK9-M), Version 12.2(55)SE, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Sun 08-Aug-10 01:16 by prod_rel_team
Image text-base: 0x00003000, data-base: 0x02800000

ROM: Bootstrap program is CBS31X0 boot loader
BOOTLDR: CBS31X0 Boot Loader (CBS31X0-HBOOT-M) Version 12.2(0.0.951)SE3, CISCO DEVELOPMENT TEST VERSION

sw-6-x2 uptime is 1 day, 2 hours, 1 minute
System returned to ROM by power-on
System restarted at 12:02:29 MSK Tue Feb 1 2011
System image file is "flash:cbs31x0-universalk9-mz.122-55.SE.bin"


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
Processor board ID FOC1247T043
Last reset from power-on
2 Virtual Ethernet interfaces
1 FastEthernet interface
52 Gigabit Ethernet interfaces
4 Ten Gigabit Ethernet interfaces
The password-recovery mechanism is enabled.

512K bytes of flash-simulated non-volatile configuration memory.
Base ethernet MAC Address       : 00:23:EA:D6:1D:80
Motherboard assembly number     : 73-10920-08
Motherboard serial number       : FOC12461JEZ
Model revision number           : C0
Motherboard revision number     : A0
Model number                    : WS-CBS3120X-S
System serial number            : FOC1247T043
Top Assembly Part Number        : 800-28520-01
Top Assembly Revision Number    : F0
Version ID                      : V01
CLEI Code Number                : COUIAN1CAA
Hardware Board Revision Number  : 0x00


Switch Ports Model              SW Version            SW Image                 
------ ----- -----              ----------            ----------               
*    1 28    WS-CBS3120X-S      12.2(55)SE            CBS31X0-UNIVERSALK9-M    
     2 28    WS-CBS3120X-S      12.2(55)SE            CBS31X0-UNIVERSALK9-M    


Switch 02
---------
Switch Uptime                   : 1 day, 2 hours, 1 minute 
Base ethernet MAC Address       : 00:23:EA:D7:3D:00
Motherboard assembly number     : 73-10920-08
Motherboard serial number       : FOC12461KCA
Model revision number           : C0
Motherboard revision number     : A0
Model number                    : WS-CBS3120X-S
System serial number            : FOC1249T025
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
}
    snmp_get={}
    snmp_getnext={}
