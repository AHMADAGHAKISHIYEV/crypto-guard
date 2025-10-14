from __future__ import annotations

from aiogram import Router, types

from api.app.config import get_settings

router = Router()


@router.message(commands=["risk"])
async def risk_handler(message: types.Message) -> None:
    settings = get_settings()
    parts = message.text.split()
    if len(parts) == 4 and parts[1] == "set" and parts[2] == "max_r":
        try:
            value = float(parts[3])
        except ValueError:
            await message.answer("Geçersiz değer")
            return
        await message.answer(
            f"İstek alındı: max R per trade {value}. Lütfen .env ve yönetim paneli üzerinden güncelleyin. Mevcut: {settings.risk_max_r_per_trade}"
        )
    else:
        await message.answer(
            f"Risk parametreleri → max_r: {settings.risk_max_r_per_trade}, max_dd: {settings.risk_max_portfolio_drawdown}"
        )
