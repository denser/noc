# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## EdgeCore.ES.get_interface_status test
## Auto-generated by ./noc debug-script at 01.08.2012 16:57:36
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class EdgeCore_ES_get_interface_status_Test(ScriptTestCase):
    script = "EdgeCore.ES.get_interface_status"
    vendor = "EdgeCore"
    platform = "ES3526XA-V2"
    version = "1.1.0.37"
    input = {}
    result = [{'interface': 'Eth 1/1', 'mac': '70:72:CF:3E:CA:61', 'status': False},
 {'interface': 'Eth 1/2', 'mac': '70:72:CF:3E:CA:62', 'status': False},
 {'interface': 'Eth 1/3', 'mac': '70:72:CF:3E:CA:63', 'status': True},
 {'interface': 'Eth 1/4', 'mac': '70:72:CF:3E:CA:64', 'status': True},
 {'interface': 'Eth 1/5', 'mac': '70:72:CF:3E:CA:65', 'status': False},
 {'interface': 'Eth 1/6', 'mac': '70:72:CF:3E:CA:66', 'status': True},
 {'interface': 'Eth 1/7', 'mac': '70:72:CF:3E:CA:67', 'status': True},
 {'interface': 'Eth 1/8', 'mac': '70:72:CF:3E:CA:68', 'status': True},
 {'interface': 'Eth 1/9', 'mac': '70:72:CF:3E:CA:69', 'status': True},
 {'interface': 'Eth 1/10', 'mac': '70:72:CF:3E:CA:6A', 'status': False},
 {'interface': 'Eth 1/11', 'mac': '70:72:CF:3E:CA:6B', 'status': False},
 {'interface': 'Eth 1/12', 'mac': '70:72:CF:3E:CA:6C', 'status': False},
 {'interface': 'Eth 1/13', 'mac': '70:72:CF:3E:CA:6D', 'status': False},
 {'interface': 'Eth 1/14', 'mac': '70:72:CF:3E:CA:6E', 'status': False},
 {'interface': 'Eth 1/15', 'mac': '70:72:CF:3E:CA:6F', 'status': False},
 {'interface': 'Eth 1/16', 'mac': '70:72:CF:3E:CA:70', 'status': False},
 {'interface': 'Eth 1/17', 'mac': '70:72:CF:3E:CA:71', 'status': False},
 {'interface': 'Eth 1/18', 'mac': '70:72:CF:3E:CA:72', 'status': False},
 {'interface': 'Eth 1/19', 'mac': '70:72:CF:3E:CA:73', 'status': False},
 {'interface': 'Eth 1/20', 'mac': '70:72:CF:3E:CA:74', 'status': False},
 {'interface': 'Eth 1/21', 'mac': '70:72:CF:3E:CA:75', 'status': False},
 {'interface': 'Eth 1/22', 'mac': '70:72:CF:3E:CA:76', 'status': False},
 {'interface': 'Eth 1/23', 'mac': '70:72:CF:3E:CA:77', 'status': False},
 {'interface': 'Eth 1/24', 'mac': '70:72:CF:3E:CA:78', 'status': False},
 {'interface': 'Eth 1/25', 'mac': '70:72:CF:3E:CA:79', 'status': True},
 {'interface': 'Eth 1/26', 'mac': '70:72:CF:3E:CA:7A', 'status': True},
 {'interface': 'VLAN 1', 'mac': '70:72:CF:3E:CA:60', 'status': True}]
    motd = ''
    cli = {
## 'show version'
'show version': """show version
 Serial Number:           115001959
 Service Tag:             
 Hardware Version:        R01
 EPLD Version:            0.00
 Number of Ports:         26
 Main Power Status:       Up
 Loader Version:          1.0.0.2
 Boot ROM Version:        1.0.0.5
 Operation Code Version:  1.1.0.37
""", 
'terminal length 0':  "terminal length 0\n      ^\n% Invalid input detected at '^' marker.\n", 
## 'show interface status'
'show interface status': """show interface status
Information of Eth 1/1
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-61
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/2
 Basic Information: 
 Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-62
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/3
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-63
Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Up
  Port Operation Status:  Up
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/4
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-64
 Configuration: 
 Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Up
  Port Operation Status:  Up
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/5
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-65
 Configuration: 
  Name:                   
 Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/6
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-66
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
 Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Up
  Port Operation Status:  Up
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/7
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-67
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
 Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Up
  Port Operation Status:  Up
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/8
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-68
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
 Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Up
  Port Operation Status:  Up
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/9
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-69
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
 Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Up
  Port Operation Status:  Up
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/10
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-6A
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
 LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/11
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-6B
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
 Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/12
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-6C
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/13
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-6D
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Down
 Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/14
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-6E
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/15
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-6F
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/16
Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-70
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/17
 Basic Information: 
  Port Type:              100TX
 Mac Address:            70-72-CF-3E-CA-71
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/18
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-72
 Configuration: 
 Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/19
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-73
 Configuration: 
  Name:                   
  Port Admin:             Up
 Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/20
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-74
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
 Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/21
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-75
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
 Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/22
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-76
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
 Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/23
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-77
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
 Port Security Action:   None
 Current Status: 
  Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/24
 Basic Information: 
  Port Type:              100TX
  Mac Address:            70-72-CF-3E-CA-78
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           10half, 10full, 100half, 100full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
 Link Status:            Down
  Operation Speed-duplex: 100full
  Flow Control Type:      None

Information of Eth 1/25
 Basic Information: 
  Port Type:              1000Base SFP
  Mac Address:            70-72-CF-3E-CA-79
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           1000full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Up
  Port Operation Status:  Up
 Operation Speed-duplex: 1000full
  Flow Control Type:      Dot3X

Information of Eth 1/26
 Basic Information: 
  Port Type:              1000Base SFP
  Mac Address:            70-72-CF-3E-CA-7A
 Configuration: 
  Name:                   
  Port Admin:             Up
  Speed-duplex:           Auto
  Capabilities:           1000full
  Broadcast Storm:        Enabled
  Broadcast Storm Limit:  scale:8K level:8 octets/second
  Flow Control:           Disabled
  LACP:                   Disabled
  Port Security:          Disabled
  Max MAC Count:          0
  Port Security Action:   None
 Current Status: 
  Link Status:            Up
  Port Operation Status:  Up
  Operation Speed-duplex: 1000full
 Flow Control Type:      None

Information of VLAN 1
 MAC Address:             70-72-CF-3E-CA-60
""", 
## 'show system'
'show system': """show system
System Description: Layer2+ Fast Ethernet Standalone Switch ES3526XA
System OID String: 1.3.6.1.4.1.259.8.1.5
System Information
 System Up Time:          54 days, 23 hours, 4 minutes, and 58.76 seconds
 System Name:             Vasenko-12-1-DK-sw1
 System Location:         [NONE]
 System Contact:          [NONE]
 MAC Address (Unit1):     70-72-CF-3E-CA-60
 Web Server:              Enabled
 Web Server Port:         80
 Web Secure Server:       Enabled
 Web Secure Server Port:  443
 Telnet Server:           Enable
 Telnet Server Port:      23
 Jumbo Frame:             Disabled 

 POST Result:              
DUMMY Test 1 ................. PASS
UART Loopback Test ........... PASS
DRAM Test .................... PASS
I2C Bus Initialization ....... PASS

Done All Pass.""", 
}
    snmp_get = {}
    snmp_getnext = {}
    http_get = {}
