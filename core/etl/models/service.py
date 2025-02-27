# ----------------------------------------------------------------------
# ServiceModel
# ----------------------------------------------------------------------
# Copyright (C) 2007-2022 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
from typing import Optional, List, Union
from datetime import datetime

# NOC modules
from .base import BaseModel, _BaseModel
from .typing import Reference
from .serviceprofile import ServiceProfile
from .managedobject import ManagedObject
from .subscriber import Subscriber


class CapsItem(_BaseModel):
    name: str
    value: Union[str, bool, int]


class Service(BaseModel):
    id: str
    profile: Reference["ServiceProfile"]
    parent: Optional[Reference["Service"]] = None
    subscriber: Optional[Reference["Subscriber"]] = None
    ts: Optional[datetime] = None
    # Workflow state
    state: Optional[str] = None
    # Last state change
    state_changed: Optional[datetime] = None
    # Workflow event
    event: Optional[str] = None
    agreement_id: Optional[str] = None
    order_id: Optional[str] = None
    stage_id: Optional[str] = None
    stage_name: Optional[str] = None
    stage_start: Optional[datetime] = None
    account_id: Optional[str] = None
    address: Optional[str] = None
    managed_object: Optional[Reference["ManagedObject"]] = None
    nri_port: Optional[str] = None
    cpe_serial: Optional[str] = None
    cpe_mac: Optional[str] = None
    cpe_model: Optional[str] = None
    cpe_group: Optional[str] = None
    labels: Optional[List[str]] = None
    description: Optional[str] = None
    capabilities: Optional[List[CapsItem]] = None
    checkpoint: Optional[str] = None

    class Config:
        fields = {"state_changed": "logical_status_start", "state": "logical_status"}
        populate_by_name = True

    _csv_fields = [
        "id",
        "parent",
        "subscriber",
        "profile",
        "ts",
        "state",
        "state_changed",
        "agreement_id",
        "order_id",
        "stage_id",
        "stage_name",
        "stage_start",
        "account_id",
        "address",
        "managed_object",
        "nri_port",
        "cpe_serial",
        "cpe_mac",
        "cpe_model",
        "cpe_group",
        "description",
        "labels",
    ]
