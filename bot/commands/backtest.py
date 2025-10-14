from __future__ import annotations

from aiogram import Router, types

from api.app.models.schemas import BacktestRequest
from api.app.services import backtest

router = Router()


@router.message(commands=["backtest"])
async def backtest_handler(message: types.Message) -> None:
    parts = message.text.split()
    if len(parts) < 5:
        await message.answer("Kullanım: /backtest run capital_guard BTCUSDT 90d")
        return
    _, action, strategy, symbol, period = parts[:5]
    if action != "run":
        await message.answer("Desteklenen tek aksiyon: run")
        return
    request = BacktestRequest(strategy=strategy, symbols=[symbol], params={}, period=period)
    identifier = backtest.enqueue_backtest(request)
    await message.answer(f"Backtest kuyruğa alındı: {identifier}")
