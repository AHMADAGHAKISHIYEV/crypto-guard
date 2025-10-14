"""Signal generation utilities."""

from __future__ import annotations

from typing import Dict, List, Optional

from ..config import get_settings
from ..models.schemas import Signal
from . import regime

_SAMPLE_SIGNALS: Dict[str, Signal] = {
    "BTCUSDT": Signal(
        symbol="BTCUSDT",
        composite_score=87.5,
        confidence="High",
        summary="Momentum + volume confirmation",
        regime_label="bull",
    ),
    "ETHUSDT": Signal(
        symbol="ETHUSDT",
        composite_score=78.2,
        confidence="Medium",
        summary="Breakout setup with positive funding",
        regime_label="bull",
    ),
}


def get_latest_signal(symbol: str) -> Optional[Signal]:
    return _SAMPLE_SIGNALS.get(symbol.upper())


def get_top_picks(limit: int = 10) -> List[Signal]:
    signals = sorted(_SAMPLE_SIGNALS.values(), key=lambda s: s.composite_score, reverse=True)
    return signals[:limit]


def refresh_signals(symbol: str) -> Signal:
    current_regime = regime.get_regime(symbol)
    base_signal = Signal(
        symbol=symbol,
        composite_score=50.0,
        confidence="Low",
        summary=f"Baseline regime {current_regime}",
        regime_label=current_regime,
    )
    _SAMPLE_SIGNALS[symbol] = base_signal
    return base_signal
