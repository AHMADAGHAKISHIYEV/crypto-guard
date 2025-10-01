"""Portfolio service with paper trading defaults."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from ..config import get_settings
from ..models.schemas import Holding, PortfolioPnlResponse


@dataclass
class PortfolioState:
    holdings: List[Holding]
    realized_pnl: float = 0.0
    unrealized_pnl: float = 0.0
    max_drawdown: float = 0.0


_state = PortfolioState(
    holdings=[
        Holding(symbol="BTCUSDT", quantity=0.5, avg_entry_price=25000, pnl=1500),
        Holding(symbol="ETHUSDT", quantity=2.0, avg_entry_price=1500, pnl=400),
    ],
    realized_pnl=1200,
    unrealized_pnl=700,
    max_drawdown=0.08,
)


def get_holdings() -> List[Holding]:
    return _state.holdings


def get_pnl() -> PortfolioPnlResponse:
    return PortfolioPnlResponse(
        realized_pnl=_state.realized_pnl,
        unrealized_pnl=_state.unrealized_pnl,
        max_drawdown=_state.max_drawdown,
    )


def sync_holdings() -> List[Holding]:
    settings = get_settings()
    if settings.mode == "live":
        # Placeholder for exchange sync
        pass
    return get_holdings()
