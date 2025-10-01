from __future__ import annotations

from aiogram import Router, types

from api.app.config import get_settings

router = Router()


@router.message(commands=["mode"])
async def mode_handler(message: types.Message) -> None:
    settings = get_settings()
    parts = message.text.split()
    if len(parts) == 3 and parts[1] == "set":
        mode = parts[2]
        if mode not in {"paper", "live"}:
            await message.answer("Geçersiz mod (paper|live)")
            return
        await message.answer(
            f"İstek alındı: {mode}. Lütfen MODE değişkenini güncelleyip servisleri yeniden başlatın. Mevcut mod: {settings.mode}"
        )
    else:
        await message.answer(f"Aktif mod: {settings.mode}")
