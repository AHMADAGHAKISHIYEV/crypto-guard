"""Send alerts via Telegram or email."""

from __future__ import annotations

from api.app.services import alerts, signal_engine
from worker.worker import celery_app


@celery_app.task(name="tasks.send_alerts")
def send_alerts_task() -> dict:
    signals = signal_engine.get_top_picks(limit=3)
    active_alerts = alerts.list_alerts()
    triggered = [alert for alert in active_alerts if any(s.symbol == alert.symbol for s in signals)]
    return {"alerts": [a.id for a in triggered], "count": len(triggered)}
