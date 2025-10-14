from __future__ import annotations

from aiogram import Router, types

router = Router()

_WATCHLIST: set[str] = {"BTCUSDT", "ETHUSDT"}


@router.message(commands=["watchlist"])
async def watchlist_handler(message: types.Message) -> None:
    parts = message.text.split()
    if len(parts) > 2 and parts[1] == "add":
        _WATCHLIST.add(parts[2].upper())
        await message.answer(f"{parts[2].upper()} eklendi")
    else:
        symbols = ", ".join(sorted(_WATCHLIST))
        await message.answer(f"İzleme listesi: {symbols}")
