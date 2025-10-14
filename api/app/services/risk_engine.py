"""Risk management service implementing capital guard heuristics."""

from __future__ import annotations

from ..config import get_settings
from ..models.schemas import OrderPreviewRequest, OrderPreviewResponse
from . import regime


def _calculate_stop_distance(price: float, stop_loss: float | None) -> float:
    if stop_loss is None:
        return price * 0.02
    return abs(price - stop_loss)


def preview_order(payload: OrderPreviewRequest) -> OrderPreviewResponse:
    settings = get_settings()
    regime_label = regime.get_regime(payload.symbol)

    risk_per_trade = settings.risk_max_r_per_trade
    stop_distance = _calculate_stop_distance(payload.price or 0.0, payload.stop_loss)

    account_equity = 100_000  # demo equity
    risk_amount = account_equity * risk_per_trade
    suggested_size = risk_amount / max(stop_distance, 1e-6)

    if settings.mode == "paper":
        allowed = True
        reason = None
    else:
        allowed = regime_label != "kill"
        reason = None if allowed else "Kill-switch active"

    if regime_label == "kill":
        allowed = False
        reason = "Kill-switch active due to drawdown"

    if payload.side.lower() == "buy" and regime_label == "bear":
        allowed = False
        reason = "Bear regime prohibits long entries"

    if payload.side.lower() == "sell" and settings.mode == "paper":
        # allow paper shorting but limit size
        suggested_size = min(suggested_size, account_equity * 0.0005)

    leverage = 1.0
    if payload.side.lower() == "buy" and settings.mode == "live":
        leverage = min(settings.leverage_max, 3)

    if leverage > settings.leverage_max:
        allowed = False
        reason = "Leverage exceeds policy"

    return OrderPreviewResponse(allowed=allowed, reason=reason, suggested_size=round(suggested_size, 4))
