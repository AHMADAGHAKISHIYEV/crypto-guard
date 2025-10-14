"""Backtest service stub generating deterministic metrics."""

from __future__ import annotations

import uuid
from typing import Dict, Optional

from ..models.schemas import BacktestRequest, BacktestResultResponse

_BACKTEST_RESULTS: Dict[str, BacktestResultResponse] = {}


def enqueue_backtest(request: BacktestRequest) -> str:
    backtest_id = str(uuid.uuid4())
    metrics = {
        "CAGR": 0.32,
        "Sharpe": 1.8,
        "Sortino": 2.4,
        "MaxDrawdown": -0.12,
        "WinRate": 0.58,
    }
    equity_curve = [
        {"timestamp": i, "equity": 100000 * (1 + 0.001 * i)}
        for i in range(0, 100, 5)
    ]
    result = BacktestResultResponse(
        backtest_id=backtest_id,
        metrics=metrics,
        equity_curve=equity_curve,
    )
    _BACKTEST_RESULTS[backtest_id] = result
    return backtest_id


def get_backtest(backtest_id: str) -> Optional[BacktestResultResponse]:
    return _BACKTEST_RESULTS.get(backtest_id)
