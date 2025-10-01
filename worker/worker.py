"""Celery application entrypoint."""

from __future__ import annotations

import os

from celery import Celery

from api.app.config import get_settings

settings = get_settings()

celery_app = Celery(
    "crypto_guard",
    broker=settings.redis_url,
    backend=settings.redis_url,
)
celery_app.conf.update(task_track_started=True, worker_hijack_root_logger=False)


def autodiscover() -> None:
    celery_app.autodiscover_tasks(["worker.tasks"])


autodiscover()


@celery_app.task(name="worker.health")
def health_check() -> str:
    return "ok"
