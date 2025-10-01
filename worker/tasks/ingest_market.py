"""Market data ingestion task."""

from __future__ import annotations

from datetime import datetime

from worker.worker import celery_app
from api.app.services import news_ingest, signal_engine


@celery_app.task(bind=True, name="tasks.ingest_market")
def ingest_market(self) -> dict:
    """Fetch market data and refresh signals."""
    refreshed = [signal_engine.refresh_signals(symbol) for symbol in ["BTCUSDT", "ETHUSDT"]]
    news = news_ingest.fetch_recent_news(hours=6)
    return {"symbols": [s.symbol for s in refreshed], "news_items": len(news), "timestamp": datetime.utcnow().isoformat()}
