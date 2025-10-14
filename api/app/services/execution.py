"""Execution adapter for paper and live trading."""

from __future__ import annotations

from datetime import datetime

from ..config import get_settings
from ..models.schemas import OrderPlaceRequest, OrderPreviewResponse, OrderResponse
from .exchanges import binance


def place_order(payload: OrderPlaceRequest, risk: OrderPreviewResponse) -> OrderResponse:
    settings = get_settings()
    if settings.mode == "paper":
        fill_price = payload.price or binance.get_last_price(payload.symbol)
        filled_qty = min(payload.quantity, risk.suggested_size or payload.quantity)
        return OrderResponse(
            order_id=f"paper-{datetime.utcnow().timestamp()}",
            status="filled",
            filled_qty=filled_qty,
            average_price=fill_price,
        )
    result = binance.place_order(payload)
    return OrderResponse(
        order_id=result["id"],
        status=result.get("status", "submitted"),
        filled_qty=float(result.get("filled", 0.0)),
        average_price=float(result.get("avgPrice", 0.0)) or None,
    )


def close_position(symbol: str, quantity: float) -> OrderResponse:
    settings = get_settings()
    if settings.mode == "paper":
        return OrderResponse(
            order_id=f"paper-close-{datetime.utcnow().timestamp()}",
            status="closed",
            filled_qty=quantity,
            average_price=binance.get_last_price(symbol),
        )
    result = binance.close_position(symbol, quantity)
    return OrderResponse(
        order_id=result.get("id", "close"),
        status=result.get("status", "submitted"),
        filled_qty=float(result.get("filled", 0.0)),
        average_price=float(result.get("avgPrice", 0.0)) or None,
    )
