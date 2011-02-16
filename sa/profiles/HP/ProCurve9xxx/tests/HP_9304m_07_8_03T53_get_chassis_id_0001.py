# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## HP.ProCurve9xxx.get_chassis_id test
## Auto-generated by manage.py debug-script at 2011-01-17 11:14:33
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
from noc.lib.test import ScriptTestCase
class HP_ProCurve9xxx_get_chassis_id_Test(ScriptTestCase):
    script="HP.ProCurve9xxx.get_chassis_id"
    vendor="HP"
    platform='9304m'
    version='07.8.03T53'
    input={}
    result='00:0C:DB:7B:6C:00'
    motd=' \n'
    cli={
'terminal length 1000':  'terminal length 1000\n',
## 'show chassis'
'show chassis': """show chassis
power supply 1 ok
power supply 2 ok
power supply 1 to 2 from left to right
fan 1 (left side panel, back fan) ok
fan 2 (left side panel, front fan) ok
fan 3 (rear/back panel, left fan) ok
fan 4 (rear/back panel, right fan) ok
Current temperature : 24.5 C degrees
Warning level : 45 C degrees, shutdown level : 55 C degrees
Boot Prom MAC: 000c.db7b.6c00""",
}
    snmp_get={}
    snmp_getnext={}
