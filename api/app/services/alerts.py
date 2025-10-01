"""Alert orchestration layer."""

from __future__ import annotations

import uuid
from typing import List

from ..models.schemas import AlertCreateRequest, AlertResponse

_ALERTS: List[AlertResponse] = []


def create_alert(payload: AlertCreateRequest) -> AlertResponse:
    alert = AlertResponse(
        id=str(uuid.uuid4()),
        symbol=payload.symbol,
        rule=payload.rule,
        threshold=payload.threshold,
        active=True,
    )
    _ALERTS.append(alert)
    return alert


def list_alerts() -> List[AlertResponse]:
    return _ALERTS
