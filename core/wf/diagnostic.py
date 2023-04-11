# ----------------------------------------------------------------------
# @diagnostic decorator
# ----------------------------------------------------------------------
# Copyright (C) 2007-2022 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
import enum
import datetime
import logging
from dataclasses import dataclass
from typing import Optional, List, Dict, Any, Set, Iterable

# Third-party modules
from pydantic import BaseModel

# NOC modules
from noc.core.checkers.base import Check
from noc.models import is_document

logger = logging.getLogger(__name__)

EVENT_TRANSITION = {
    "disable": {"unknown": "blocked", "enabled": "blocked", "failed": "blocked"},
    "fail": {"unknown": "failed", "enabled": "failed"},
    "ok": {"unknown": "enabled", "failed": "enabled"},
    "allow": {"blocked": "unknown"},
    "expire": {"enabled": "unknown", "failed": "unknown"},
}

# BuiltIn Diagnostics
SA_DIAG = "SA"
EVENT_DIAG = "PROC_EVENT"
ALARM_DIAG = "PROC_ALARM"
TT_DIAG = "TT"
#
SNMP_DIAG = "SNMP"
PROFILE_DIAG = "Profile"
CLI_DIAG = "CLI"
HTTP_DIAG = "HTTP"
SYSLOG_DIAG = "SYSLOG"
SNMPTRAP_DIAG = "SNMPTRAP"
#
DIAGNOCSTIC_LABEL_SCOPE = "diag"


class DiagnosticEvent(str, enum.Enum):
    disable = "disable"
    fail = "fail"
    ok = "ok"
    allow = "allow"
    expire = "expire"

    def get_state(self, state: "DiagnosticState") -> Optional["DiagnosticState"]:
        if state.value not in EVENT_TRANSITION[self.value]:
            return
        return DiagnosticState(EVENT_TRANSITION[self.value][state.value])


class DiagnosticState(str, enum.Enum):
    unknown = "unknown"
    blocked = "blocked"
    enabled = "enabled"
    failed = "failed"

    def fire_event(self, event: str) -> "DiagnosticState":
        return DiagnosticEvent(event).get_state(self)

    @property
    def is_blocked(self) -> bool:
        return self.value == "blocked"


@dataclass(frozen=True)
class DiagnosticConfig(object):
    diagnostic: str
    blocked: bool = False  # Block by config
    # Check config
    checks: Optional[List[Check]] = None  # CheckItem name, param
    dependent: Optional[List[str]] = None  # Dependency diagnostic
    # ANY - Any check has OK, ALL - ALL checks has OK
    state_policy: str = "ANY"  # Calculate State on checks.
    reason: Optional[str] = None  # Reason current state
    # Discovery Config
    run_policy: str = "A"  # A - Always, M - manual, F - Unknown or Failed, D - Disable
    run_order: str = "S"  # S - Before all discovery, E - After all discovery
    discovery_box: bool = False  # Run on periodic discovery
    discovery_periodic: bool = False  # Run on box discovery
    #
    save_history: bool = False
    # Display Config
    show_in_display: bool = True  # Show diagnostic on UI
    display_description: Optional[str] = None  # Description for show User
    display_order: int = 0  # Order on displayed list
    # FM Config
    alarm_class: Optional[str] = None  # Default AlarmClass for raise alarm
    alarm_labels: Optional[List[str]] = None


DIAGNOSTIC_CHECK_STATE: Dict[bool, DiagnosticState] = {
    True: DiagnosticState("enabled"),
    False: DiagnosticState("failed"),
}


class CheckStatus(BaseModel):
    name: str
    status: bool  # True - OK, False - Fail
    arg0: Optional[str] = None
    skipped: bool = False
    error: Optional[str] = None  # Description if Fail


class DiagnosticItem(BaseModel):
    diagnostic: str
    state: DiagnosticState = DiagnosticState("unknown")
    checks: Optional[List[CheckStatus]]
    # scope: Literal["access", "all", "discovery", "default"] = "default"
    # policy: str = "ANY
    reason: Optional[str] = None
    changed: Optional[datetime.datetime] = None


class DiagnosticHub(object):
    """
    Diagnostic Hub
    Methods:
    * Configured Diagnostic - state detected config only - unknown -> blocked
    * Checked Diagnostic - state detected as checks -> unknown -> blocked -> enable -> failed
    * set_diagnostic for change diagnostic state ? state/checks
    * reset_diagnostic - delete diagnostic record from field - as Unknown state

    * sync_diagnostic - check diagnostic state, and update it
    ? question - update depended diagnostic
    Discovery update only checks on diagnostic, after in - run sync_diagnostic
    ? update_diagnostic_checks
    ? Custom diagnostic - change labels: reset diagnostic by not match current label
    ? Change affected config ? can_XXXXX method, -
        can_block_diagnostic(<name>) -> return True/False, reason ... blocked, reason

    Depended - if high diagnostic blocked - blocks low

    """

    def __init__(self, o: Any):
        self.logger = logging.getLogger(__name__)
        self.__all_diagnostics: Optional[Set[str]] = set()
        self.__diagnostics: Optional[Dict[str, DiagnosticItem]] = None
        if not hasattr(o, "diagnostics"):
            raise NotImplementedError("Diagnostic Interface not supported")
        self.__object = o
        # diagnostic state

    def get(self, name: str) -> Optional[Any]:
        if self.__diagnostics is None:
            self.__diagnostics = self.__load_diagnostics()
        if name in self.__diagnostics:
            return self.__diagnostics[name]
        elif name in self.__all_diagnostics:
            # Unknown State
            return DiagnosticItem(diagnostic=name)

    def __getitem__(self, name: str) -> "DiagnosticItem":
        v = self.get(name)
        if v is None:
            raise KeyError
        return v

    def __getattr__(self, name: str, default: Optional[Any] = None) -> Optional["DiagnosticItem"]:
        v = self.get(name)
        if v is None:
            raise AttributeError(f"Unknown diagnostic")
        return v

    def __contains__(self, name: str) -> bool:
        return self.get(name) is not None

    def iter_diagnostic_configs(self) -> Iterable[DiagnosticConfig]:
        for dc in self.__object.iter_diagnostic_configs():
            yield dc

    def __load_diagnostics(self) -> Dict[str, DiagnosticItem]:
        r = {}
        if is_document(self.__object):
            return r
        for dc in self.iter_diagnostic_configs():
            self.__all_diagnostics.add(dc.diagnostic)
            if dc.diagnostic in self.__object.diagnostics:
                r[dc.diagnostic] = self.__object.diagnostics[dc.diagnostic]
        return r

    def set_state(
        self,
        diagnostic: str,
        state: DiagnosticState = DiagnosticState("unknown"),
        reason: Optional[str] = None,
        changed_ts: Optional[datetime.datetime] = None,
        data: Optional[Dict[str, Any]] = None,
        bulk: Optional[List[Any]] = None,
    ):
        """
        Set diagnostic ok/fail state
        :param diagnostic: Diagnotic Name
        :param state: True - Enabled; False - Failed
        :param reason: Reason state changed
        :param changed_ts: Timestamp changed
        :param data: Collected checks data
        :param bulk: Return changed diagnostic without saved
        :return:
        """
        d = self[diagnostic]
        if d.state.is_blocked or d.state == state:
            return
        logger.info("[%s] Change diagnostic state: %s -> %s", diagnostic, d.state, state)
        last_state = d.state
        changed = changed_ts or datetime.datetime.now()
        d.state = state
        d.reason = reason
        d.changed = changed.isoformat(sep=" ")
        self.__diagnostics[diagnostic] = d

    def reset_diagnostics(self, diagnostics: List[str]):
        """
        Remove diagnostic data.
        """

    def sync_diagnostics(self):
        """
        Save diagnostic to object
        """

    def sync_alarms(self, diagnostics: Optional[List[str]] = None):
        """
        Raise & clear Alarm for diagnostic. Only diagnostics with alarm_class set will be synced.
        If diagnostics param is set and alarm_class is not set - clear alarm
         For dependent - Group alarm base on diagnostic with alarm for depended
        :param diagnostics: If set - sync only params diagnostic and depends
        :return:
        """

    def register_diagnostic_change(
        self,
        diagnostic: str,
        state: str,
        from_state: str = DiagnosticState.unknown,
        reason: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None,
        ts: Optional[datetime.datetime] = None,
    ):
        """
        Save diagnostic state changes to Archive.
        1. Send data to BI Model
        2. Register MX Message
        3. Register object notification
        :param diagnostic: - Diagnostic name
        :param state: Current state
        :param from_state: Previous State
        :param data: Checked data
        :param reason:
        :param ts:
        :return:
        """
        from noc.core.service.loader import get_service

        svc = get_service()
        if isinstance(ts, str):
            ts = datetime.datetime.fromisoformat(ts)
        now = ts or datetime.datetime.now()


def diagnostic(cls):
    """
    Diagnostic decorator.
     If model supported diagnostic (diagnostics field) add DiagnosticHub
    :param cls:
    :return:
    """

    def diagnostic(self) -> "DiagnosticHub":
        diagnostics = getattr(self, "_diagnostics", None)
        if diagnostics:
            return diagnostics
        self._diagnostics = DiagnosticHub(self)
        return self._diagnostics

    cls.diagnostic = property(diagnostic)
    return cls
