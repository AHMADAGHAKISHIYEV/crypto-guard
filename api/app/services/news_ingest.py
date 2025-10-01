"""Minimal RSS ingest stub with OpenAI enrichment."""

from __future__ import annotations

import feedparser
from datetime import datetime, timedelta
from typing import List

from . import sentiment

RSS_SOURCES = [
    "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "https://cointelegraph.com/rss",
]


def fetch_recent_news(hours: int = 24) -> List[dict]:
    cutoff = datetime.utcnow() - timedelta(hours=hours)
    articles: List[dict] = []
    for url in RSS_SOURCES:
        feed = feedparser.parse(url)
        for entry in feed.entries[:10]:
            published = datetime(*entry.published_parsed[:6]) if getattr(entry, "published_parsed", None) else datetime.utcnow()
            if published < cutoff:
                continue
            enriched = sentiment.summarize_news(entry.get("summary", ""))
            articles.append(
                {
                    "source": url,
                    "url": entry.get("link"),
                    "title": entry.get("title"),
                    "published": published.isoformat(),
                    **enriched,
                }
            )
    return articles
