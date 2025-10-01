"""Telegram bot bootstrap."""

from __future__ import annotations

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from shared.utils import get_settings

from .commands import alert, backtest, mode, risk, start, watchlist

logger = logging.getLogger(__name__)


def build_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(watchlist.router)
    dp.include_router(alert.router)
    dp.include_router(backtest.router)
    dp.include_router(risk.router)
    dp.include_router(mode.router)
    return dp


async def main() -> None:
    settings = get_settings()
    if not settings.telegram_bot_token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN missing")
    bot = Bot(token=settings.telegram_bot_token, parse_mode=ParseMode.MARKDOWN)
    dp = build_dispatcher()
    logger.info("Starting Crypto Guard bot in %s mode", settings.mode)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
