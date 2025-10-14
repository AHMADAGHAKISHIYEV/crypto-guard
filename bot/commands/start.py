from __future__ import annotations

from aiogram import Router, types

from shared.constants import DISCLAIMER_TEXT

router = Router()


@router.message(commands=["start"])
async def start_handler(message: types.Message) -> None:
    text = (
        "Crypto Guard botuna hoş geldiniz!\n"
        "Paper trading modu varsayılan.\n"
        f"{DISCLAIMER_TEXT}"
    )
    await message.answer(text)
