# ----------------------------------------------------------------------
# sa.ManagedObject diagnostics tests
# ----------------------------------------------------------------------
# Copyright (C) 2007-2023 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Third-party modules
from dataclasses import dataclass

# NOC modules
from noc.core.wf.diagnostic import DiagnosticConfig, diagnostic, DiagnosticState


@dataclass
@diagnostic
class Object(object):
    diagnostics = {}

    def iter_diagnostic_configs(self):
        """
        Iterate over object diagnostics
        :return:
        """
        yield DiagnosticConfig(diagnostic="D1")


def test_set_state():
    o = Object()
    o.diagnostic.set_state("D1", DiagnosticState.enabled)
    assert o.diagnostic.D1.state == DiagnosticState.enabled
