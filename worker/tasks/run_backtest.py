"""Execute queued backtests."""

from __future__ import annotations

from api.app.models.schemas import BacktestRequest
from api.app.services import backtest
from worker.worker import celery_app


@celery_app.task(name="tasks.run_backtest")
def run_backtest_task(request_data: dict) -> str:
    request = BacktestRequest(**request_data)
    return backtest.enqueue_backtest(request)
