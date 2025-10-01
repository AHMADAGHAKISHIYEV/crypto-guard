from __future__ import annotations

from aiogram import Router, types

from api.app.models.schemas import AlertCreateRequest
from api.app.services import alerts

router = Router()


@router.message(commands=["alert"])
async def alert_handler(message: types.Message) -> None:
    parts = message.text.split()
    if len(parts) < 4 or parts[1] != "set":
        await message.answer("Kullanım: /alert set BTCUSDT score>80")
        return
    symbol = parts[2].upper()
    rule, _, threshold = parts[3].partition(">")
    alert = alerts.create_alert(
        payload=AlertCreateRequest(symbol=symbol, rule=rule, threshold=float(threshold or 80))
    )
    await message.answer(f"Alert oluşturuldu: {alert.symbol} {alert.rule}>{alert.threshold}")
