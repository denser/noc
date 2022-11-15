# ---------------------------------------------------------------------
# peer.maintainer application
# ---------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# NOC modules
from noc.services.web.app.extmodelapplication import ExtModelApplication
from noc.peer.models.maintainer import Maintainer
from noc.services.web.app.repoinline import RepoInline
from noc.core.translation import ugettext as _


class MaintainerApplication(ExtModelApplication):
    """
    Maintainers application
    """

    title = _("Maintainers")
    menu = [_("Setup"), _("Maintainers")]
    model = Maintainer

    rpsl = RepoInline("rpsl")
