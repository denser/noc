# ----------------------------------------------------------------------
# sa.ManagedObject diagnostics tests
# ----------------------------------------------------------------------
# Copyright (C) 2007-2023 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Third-party modules
from dataclasses import dataclass

# NOC modules
from noc.core.wf.diagnostic import (
    DiagnosticConfig,
    DiagnosticState,
    diagnostic,
    SNMP_DIAG,
    CheckData,
    Check,
)


@dataclass
@diagnostic
class Object(object):
    id = 10
    diagnostics = {
        "D2": {"diagnostic": "D2", "state": "failed", "reason": "1"},
        "Access": {"diagnostic": "Access", "state": "failed", "reason": "2"},
    }

    def iter_diagnostic_configs(self):
        """
        Iterate over object diagnostics
        :return:
        """
        yield DiagnosticConfig(diagnostic="D1")
        yield DiagnosticConfig(diagnostic="D2")
        ac = "C"
        yield DiagnosticConfig(
            SNMP_DIAG,
            display_description="Check Device response by SNMP request",
            checks=[Check(name="SNMPv1"), Check(name="SNMPv2c")],
            blocked=ac == "C",
            run_policy="F",
            run_order="S",
            discovery_box=True,
            alarm_class="NOC | Managed Object | Access Lost",
            alarm_labels=["noc::access::method::SNMP"],
            reason="Blocked by AccessPreference" if ac == "C" else None,
        )
        yield DiagnosticConfig(
            "Access",
            dependent=["SNMP", "CLI", "HTTP"],
            show_in_display=False,
            alarm_class="NOC | Managed Object | Access Degraded",
        )


def test_set_state():
    o = Object()
    assert o.diagnostic.D2.state == DiagnosticState.failed
    o.diagnostic.set_state("D1", DiagnosticState.enabled)
    assert o.diagnostic.D1.state == DiagnosticState.enabled
    o.diagnostic.update_checks([CheckData(name="SNMPv1", status=False)])
    assert o.diagnostic.SNMP.state == DiagnosticState.failed
    o.diagnostic.update_checks([CheckData(name="SNMPv1", status=False), CheckData(name="SNMPv1", status=True)])
    assert o.diagnostic.SNMP.state == DiagnosticState.enabled
    assert o.diagnostic.Access.state == DiagnosticState.enabled
    assert o.diagnostics["Access"]["state"] == "enabled"
