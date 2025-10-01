"""System status aggregator."""

from __future__ import annotations

import random

from ..models.schemas import StatusResponse


def get_status() -> StatusResponse:
    latency_ms = random.uniform(40, 120)
    websocket_connected = True
    pending_tasks = random.randint(0, 5)
    return StatusResponse(latency_ms=latency_ms, websocket_connected=websocket_connected, pending_tasks=pending_tasks)
