"""Recalculate composite risk scores."""

from __future__ import annotations

from datetime import datetime

from worker.worker import celery_app
from api.app.services import signal_engine


@celery_app.task(name="tasks.compute_scores")
def compute_scores() -> dict:
    signals = signal_engine.get_top_picks(limit=5)
    scores = {s.symbol: s.composite_score for s in signals}
    return {"scores": scores, "timestamp": datetime.utcnow().isoformat()}
