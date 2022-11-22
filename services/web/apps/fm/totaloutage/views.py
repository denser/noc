# ---------------------------------------------------------------------
# fm.totaloutage
# ---------------------------------------------------------------------
# Copyright (C) 2007-2016 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# NOC modules
from noc.services.web.base.extapplication import ExtApplication
from noc.core.translation import ugettext as _
from noc.config import config


class TotalOutageApplication(ExtApplication):
    title = _("Total Outages")
    menu = _("Total Outages")
    glyph = "bolt"
    link = "/api/card/view/totaloutage/1/?refresh=%s" % config.fm.total_outage_refresh
