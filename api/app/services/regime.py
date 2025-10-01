"""Simple regime classification stub."""

from __future__ import annotations

_REGIME_STATE = {
    "BTCUSDT": "bull",
    "ETHUSDT": "bull",
}


def get_regime(symbol: str) -> str:
    return _REGIME_STATE.get(symbol.upper(), "sideways")


def set_regime(symbol: str, regime_label: str) -> None:
    _REGIME_STATE[symbol.upper()] = regime_label


def kill_switch() -> None:
    for symbol in list(_REGIME_STATE.keys()):
        _REGIME_STATE[symbol] = "kill"
