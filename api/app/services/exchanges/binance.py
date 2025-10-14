"""Thin Binance wrapper using ccxt."""

from __future__ import annotations

from typing import Any, Dict

import ccxt

from ...config import get_settings


def _get_client() -> ccxt.binance:
    settings = get_settings()
    client = ccxt.binance({
        "apiKey": settings.binance_api_key,
        "secret": settings.binance_api_secret,
        "enableRateLimit": True,
    })
    if settings.mode == "paper":
        client.set_sandbox_mode(True)
    return client


def get_last_price(symbol: str) -> float:
    client = _get_client()
    ticker = client.fetch_ticker(symbol)
    return float(ticker.get("last") or ticker.get("close") or 0.0)


def place_order(payload) -> Dict[str, Any]:
    client = _get_client()
    params: Dict[str, Any] = {}
    if payload.take_profit and payload.stop_loss:
        params["oco_order"] = True
    order = client.create_order(
        symbol=payload.symbol,
        type=payload.order_type,
        side=payload.side,
        amount=payload.quantity,
        price=payload.price,
        params=params,
    )
    return order


def close_position(symbol: str, quantity: float) -> Dict[str, Any]:
    client = _get_client()
    order = client.create_order(
        symbol=symbol,
        type="market",
        side="sell",
        amount=quantity,
    )
    return order
