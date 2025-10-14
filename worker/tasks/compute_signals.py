"""Compute composite scores for early warning signals."""

from __future__ import annotations

from datetime import datetime

from worker.worker import celery_app
from api.app.services import signal_engine


@celery_app.task(name="tasks.compute_signals")
def compute_signals() -> dict:
    picks = signal_engine.get_top_picks(limit=10)
    return {
        "generated": len(picks),
        "top_symbol": picks[0].symbol if picks else None,
        "timestamp": datetime.utcnow().isoformat(),
    }
