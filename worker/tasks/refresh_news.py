"""Refresh news feed using RSS sources."""

from __future__ import annotations

from api.app.services import news_ingest
from worker.worker import celery_app


@celery_app.task(name="tasks.refresh_news")
def refresh_news_task(hours: int = 24) -> dict:
    articles = news_ingest.fetch_recent_news(hours=hours)
    return {"articles": len(articles)}
