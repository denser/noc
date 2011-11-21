# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Cisco.IOS.get_interfaces test
## Auto-generated by ./noc debug-script at 2011-11-21 15:04:35
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Cisco_IOS_get_interfaces_Test(ScriptTestCase):
    script = "Cisco.IOS.get_interfaces"
    vendor = "Cisco"
    platform = 'EGR'
    version = '12.3(23)BC5'
    input = {}
    result = [{'forwarding_instance': 'default',
  'interfaces': [{'admin_status': True,
                  'mac': '00:15:C6:4F:45:00',
                  'name': 'Fa 0/0',
                  'oper_status': True,
                  'subinterfaces': [{'admin_status': True,
                                     'mac': '00:15:C6:4F:45:00',
                                     'name': 'Fa 0/0',
                                     'oper_status': True,
                                     'vlan_ids': [9,
                                                  231,
                                                  219,
                                                  208,
                                                  356,
                                                  201,
                                                  204,
                                                  251,
                                                  222,
                                                  246,
                                                  202,
                                                  211,
                                                  206,
                                                  249,
                                                  226]},
                                    {'admin_status': True,
                                     'ipv4_addresses': ['10.160.0.1/24'],
                                     'is_ipv4': True,
                                     'mac': '00:15:C6:4F:45:00',
                                     'name': 'Fa 0/0.201',
                                     'oper_status': True},
                                    {'admin_status': True,
                                     'mac': '00:15:C6:4F:45:00',
                                     'name': 'Fa 0/0.202',
                                     'oper_status': True},
                                    {'admin_status': True,
                                     'mac': '00:15:C6:4F:45:00',
                                     'name': 'Fa 0/0.203',
                                     'oper_status': True},
                                    {'admin_status': True,
                                     'mac': '00:15:C6:4F:45:00',
                                     'name': 'Fa 0/0.210',
                                     'oper_status': True},
                                    {'admin_status': True,
                                     'ipv4_addresses': ['10.200.252.1/24'],
                                     'is_ipv4': True,
                                     'mac': '00:15:C6:4F:45:00',
                                     'name': 'Fa 0/0.252',
                                     'oper_status': True,
                                     'vlan_ids': [252]},
                                    {'admin_status': True,
                                     'ipv4_addresses': ['10.200.254.101/24'],
                                     'is_ipv4': True,
                                     'mac': '00:15:C6:4F:45:00',
                                     'name': 'Fa 0/0.254',
                                     'oper_status': True,
                                     'vlan_ids': [254]},
                                    {'admin_status': True,
                                     'ipv4_addresses': ['10.110.0.1/24'],
                                     'is_ipv4': True,
                                     'is_ospf': True,
                                     'mac': '00:15:C6:4F:45:00',
                                     'name': 'Fa 0/0.255',
                                     'oper_status': True,
                                     'vlan_ids': [255]}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'mac': '00:15:C6:4F:45:01',
                  'name': 'Fa 0/1',
                  'oper_status': True,
                  'subinterfaces': [{'admin_status': True,
                                     'ipv4_addresses': ['10.255.254.1/30'],
                                     'is_ipv4': True,
                                     'mac': '00:15:C6:4F:45:01',
                                     'name': 'Fa 0/1',
                                     'oper_status': True}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'mac': '00:15:C6:4F:45:1C',
                  'name': 'Ca 1/0',
                  'oper_status': True,
                  'subinterfaces': [{'admin_status': True,
                                     'ipv4_addresses': ['172.16.0.1/16',
                                                        '10.100.0.1/16'],
                                     'is_ipv4': True,
                                     'mac': '00:15:C6:4F:45:1C',
                                     'name': 'Ca 1/0',
                                     'oper_status': True}],
                  'type': 'physical'}],
  'type': 'ip'}]
    motd = ' \n\n'
    cli = {
## 'show ip interface FastEthernet0/0.255'
'show ip interface FastEthernet0/0.255': """show ip interface FastEthernet0/0.255
FastEthernet0/0.255 is up, line protocol is up
  Internet address is 10.110.0.1/24
  Broadcast address is 255.255.255.255
  Address determined by non-volatile memory
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Multicast reserved groups joined: 224.0.0.2 224.0.0.5 224.0.0.6
  Outgoing access list is not set
  Inbound  access list is not set
  Proxy ARP is enabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are always sent
  ICMP unreachables are always sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP fast switching on the same interface is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP Feature Fast switching turbo vector
  IP Feature CEF switching turbo vector
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Policy routing is disabled
  Network address translation is disabled
  WCCP Redirect outbound is disabled
  WCCP Redirect inbound is disabled
  WCCP Redirect exclude is disabled
  BGP Policy Mapping is disabled""", 
## 'show ip interface FastEthernet0/1'
'show ip interface FastEthernet0/1': """show ip interface FastEthernet0/1
FastEthernet0/1 is up, line protocol is up
  Internet address is 10.255.254.1/30
  Broadcast address is 255.255.255.255
  Address determined by non-volatile memory
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Outgoing access list is not set
  Inbound  access list is not set
  Proxy ARP is disabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are never sent
  ICMP unreachables are never sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP fast switching on the same interface is disabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP Feature Fast switching turbo vector
  IP Feature CEF switching turbo vector
  IP multicast fast switching is disabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Policy routing is disabled
  Network address translation is disabled
  WCCP Redirect outbound is disabled
  WCCP Redirect inbound is disabled
  WCCP Redirect exclude is disabled
  BGP Policy Mapping is disabled""", 
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

cisco uptime is 7 weeks, 1 day, 23 hours, 45 minutes
System returned to ROM by power-on
System restarted at 15:30:46 EET Sat Oct 1 2011
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
## 'show cable l2-vpn dot1q-vc-map'
'show cable l2-vpn dot1q-vc-map': """show cable l2-vpn dot1q-vc-map
MAC Address    Ethernet Interface      VLAN ID   Cable Intf  SID  Customer Name
0000.ca48.35b3 FastEthernet0/0              9    NOT MAPPED  0    Kr_Telekom
0013.11fc.3ef8 FastEthernet0/0            231    NOT MAPPED  0    eldorad
0018.c017.cc3e FastEthernet0/0            219    NOT MAPPED  0    kr_bank
0019.5eec.d634 FastEthernet0/0            208    NOT MAPPED  0    ubrp
000f.9fed.90b6 FastEthernet0/0            356    Cable1/0    14   UkrSocBank
0000.caaa.2d10 FastEthernet0/0            201    NOT MAPPED  0    alfa
0013.11fc.2fbf FastEthernet0/0            204    NOT MAPPED  0    foxtrot
0000.ca48.5caa FastEthernet0/0            251    NOT MAPPED  0    1ukr
0000.cac9.4237 FastEthernet0/0            222    NOT MAPPED  0    ukrprofbank
0018.c017.bff0 FastEthernet0/0            246    NOT MAPPED  0    PIB
0013.11fc.2953 FastEthernet0/0            202    NOT MAPPED  0    balbert
0013.11fc.2c56 FastEthernet0/0            211    NOT MAPPED  0    eldorad_kr
0018.c017.fe9a FastEthernet0/0            206    NOT MAPPED  0    ultimatraid
0019.5bf9.4239 FastEthernet0/0            249    Cable1/0    6    Dongorbank
0019.5bf9.344c FastEthernet0/0            226    NOT MAPPED  0    sat
""", 
'show ip ospf interface brief':  'show ip ospf interface brief\nInterface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C\nFa0/0.255    100   0               10.110.0.1/24      1     DR    0/0\n', 
## 'show interface'
'show interface': """show interface
FastEthernet0/0 is up, line protocol is up 
  Hardware is DEC21140A, address is 0015.c64f.4500 (bia 0015.c64f.4500)
  MTU 1500 bytes, BW 100000 Kbit, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 17/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  1., loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, 100BaseTX/FX
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 1/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 6817000 bits/sec, 834 packets/sec
  5 minute output rate 588000 bits/sec, 542 packets/sec
     3281127921 packets input, 90624971 bytes
     Received 61769136 broadcasts, 0 runts, 0 giants, 0 throttles
     252 input errors, 0 CRC, 0 frame, 0 overrun, 85926884 ignored
     0 watchdog
     0 input packets with dribble condition detected
     2167627461 packets output, 2452880952 bytes, 0 underruns
     38 output errors, 0 collisions, 3 interface resets
     0 babbles, 0 late collision, 0 deferred
     39 lost carrier, 33 no carrier
     0 output buffer failures, 0 output buffers swapped out
FastEthernet0/0.201 is up, line protocol is up 
  Hardware is DEC21140A, address is 0015.c64f.4500 (bia 0015.c64f.4500)
  Internet address is 10.160.0.1/24
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 17/255
  Encapsulation ARPA
  ARP type: ARPA, ARP Timeout 04:00:00
  Last clearing of "show interface" counters never
FastEthernet0/0.202 is up, line protocol is up 
  Hardware is DEC21140A, address is 0015.c64f.4500 (bia 0015.c64f.4500)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 17/255
  Encapsulation ARPA
  ARP type: ARPA, ARP Timeout 04:00:00
  Last clearing of "show interface" counters never
FastEthernet0/0.203 is up, line protocol is up 
  Hardware is DEC21140A, address is 0015.c64f.4500 (bia 0015.c64f.4500)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 17/255
  Encapsulation ARPA
  ARP type: ARPA, ARP Timeout 04:00:00
  Last clearing of "show interface" counters never
FastEthernet0/0.210 is up, line protocol is up 
  Hardware is DEC21140A, address is 0015.c64f.4500 (bia 0015.c64f.4500)
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 17/255
  Encapsulation ARPA
  ARP type: ARPA, ARP Timeout 04:00:00
  Last clearing of "show interface" counters never
FastEthernet0/0.252 is up, line protocol is up 
  Hardware is DEC21140A, address is 0015.c64f.4500 (bia 0015.c64f.4500)
  Internet address is 10.200.252.1/24
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 17/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  252.
  ARP type: ARPA, ARP Timeout 04:00:00
  Last clearing of "show interface" counters never
FastEthernet0/0.254 is up, line protocol is up 
  Hardware is DEC21140A, address is 0015.c64f.4500 (bia 0015.c64f.4500)
  Internet address is 10.200.254.101/24
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 17/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  254.
  ARP type: ARPA, ARP Timeout 04:00:00
  Last clearing of "show interface" counters never
FastEthernet0/0.255 is up, line protocol is up 
  Hardware is DEC21140A, address is 0015.c64f.4500 (bia 0015.c64f.4500)
  Internet address is 10.110.0.1/24
  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 17/255
  Encapsulation 802.1Q Virtual LAN, Vlan ID  255.
  ARP type: ARPA, ARP Timeout 04:00:00
  Last clearing of "show interface" counters never
FastEthernet0/1 is up, line protocol is up 
  Hardware is DEC21140A, address is 0015.c64f.4501 (bia 0015.c64f.4501)
  Internet address is 10.255.254.1/30
  MTU 1500 bytes, BW 100000 Kbit, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, 100BaseTX/FX
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:01, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes
     Received 0 broadcasts, 0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog
     0 input packets with dribble condition detected
     440536 packets output, 26432160 bytes, 0 underruns
     9 output errors, 0 collisions, 2 interface resets
     0 babbles, 0 late collision, 0 deferred
     10 lost carrier, 7 no carrier
     0 output buffer failures, 0 output buffers swapped out
Cable1/0 is up, line protocol is up 
  Hardware is BCM3210 ASIC, address is 0015.c64f.451c (bia 0015.c64f.451c)
  Internet address is 172.16.0.1/16
  MTU 1500 bytes, BW 26000 Kbit, DLY 1000 usec, 
     reliability 255/255, txload 66/255, rxload 5/255
  Encapsulation MCNS, loopback not set
  Keepalive set (10 sec)
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:00, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 1350301
  Queueing strategy: weighted fair
  Output queue: 0/1000/64/1350021 (size/max total/threshold/drops) 
     Conversations  0/3/256 (active/max active/max total)
     Reserved Conversations 9/9 (allocated/max allocated)
     Available Bandwidth 19500 kilobits/sec
  5 minute input rate 599000 bits/sec, 555 packets/sec
  5 minute output rate 6814000 bits/sec, 832 packets/sec
     2248998993 packets input, 3543830556 bytes, 3650 no buffer
     Received 4268076 broadcasts, 0 runts, 5 giants, 0 throttles
     277327 input errors, 475 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     3287181561 packets output, 167390518 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     0 output buffer failures, 0 output buffers swapped out""", 
## 'show ip interface FastEthernet0/0.254'
'show ip interface FastEthernet0/0.254': """show ip interface FastEthernet0/0.254
FastEthernet0/0.254 is up, line protocol is up
  Internet address is 10.200.254.101/24
  Broadcast address is 255.255.255.255
  Address determined by non-volatile memory
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Outgoing access list is not set
  Inbound  access list is not set
  Proxy ARP is disabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are never sent
  ICMP unreachables are never sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP fast switching on the same interface is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP Feature Fast switching turbo vector
  IP Feature CEF switching turbo vector
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Policy routing is disabled
  Network address translation is disabled
  WCCP Redirect outbound is disabled
  WCCP Redirect inbound is disabled
  WCCP Redirect exclude is disabled
  BGP Policy Mapping is disabled""", 
## 'show ip interface FastEthernet0/0.252'
'show ip interface FastEthernet0/0.252': """show ip interface FastEthernet0/0.252
FastEthernet0/0.252 is up, line protocol is up
  Internet address is 10.200.252.1/24
  Broadcast address is 255.255.255.255
  Address determined by non-volatile memory
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Outgoing access list is not set
  Inbound  access list is not set
  Proxy ARP is disabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are never sent
  ICMP unreachables are never sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP fast switching on the same interface is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP Feature Fast switching turbo vector
  IP Feature CEF switching turbo vector
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Policy routing is disabled
  Network address translation is disabled
  WCCP Redirect outbound is disabled
  WCCP Redirect inbound is disabled
  WCCP Redirect exclude is disabled
  BGP Policy Mapping is disabled""", 
## 'show ip interface Cable1/0'
'show ip interface Cable1/0': """show ip interface Cable1/0
Cable1/0 is up, line protocol is up
  Internet address is 172.16.0.1/16
  Broadcast address is 255.255.255.255
  Address determined by non-volatile memory
  MTU is 1500 bytes
  Helper address is 10.110.0.2
  Directed broadcast forwarding is disabled
  Secondary address 10.100.0.1/16
  Outgoing access list is 102
  Inbound  access list is 101
  Proxy ARP is disabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are never sent
  ICMP unreachables are never sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP fast switching on the same interface is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP Feature Fast switching turbo vector
  IP Feature CEF switching turbo vector
  IP multicast fast switching is disabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Policy routing is disabled
  Network address translation is disabled
  WCCP Redirect outbound is disabled
  WCCP Redirect inbound is disabled
  WCCP Redirect exclude is disabled
  BGP Policy Mapping is disabled""", 
## 'show ip interface FastEthernet0/0.201'
'show ip interface FastEthernet0/0.201': """show ip interface FastEthernet0/0.201
FastEthernet0/0.201 is up, line protocol is up
  Internet address is 10.160.0.1/24
  Broadcast address is 255.255.255.255
  Address determined by non-volatile memory
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Outgoing access list is not set
  Inbound  access list is not set
  Proxy ARP is enabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are always sent
  ICMP unreachables are always sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP fast switching on the same interface is disabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP Feature Fast switching turbo vector
  IP Feature CEF switching turbo vector
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Policy routing is disabled
  Network address translation is disabled
  WCCP Redirect outbound is disabled
  WCCP Redirect inbound is disabled
  WCCP Redirect exclude is disabled
  BGP Policy Mapping is disabled""", 
## 'show interfaces status | i ^Po[0-9]+'
'show interfaces status | i ^Po[0-9]+': """show interfaces status | i ^Po[0-9]+
                          ^
% Invalid input detected at '^' marker.
""", 
}
    snmp_get = {}
    snmp_getnext = {}
