# ---------------------------------------------------------------------
# Alcatel.7324RU.get_fqdn
# ---------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
from noc.sa.profiles.Generic.get_fqdn import Script as BaseScript

# NOC modules
from noc.sa.interfaces.igetfqdn import IGetFQDN


class Script(BaseScript):
    name = "Alcatel.7324RU.get_fqdn"
    interface = IGetFQDN
