from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel, Field

DISCLAIMER = "Yatırım tavsiyesi değildir."


class DisclaimerMixin(BaseModel):
    disclaimer: str = Field(default=DISCLAIMER, description="Regulatory disclaimer")


class HealthResponse(DisclaimerMixin):
    status: str
    timestamp: datetime


class AuthRequest(BaseModel):
    email: str
    password: str


class AuthResponse(DisclaimerMixin):
    access_token: str
    token_type: str = "bearer"


class Holding(BaseModel):
    symbol: str
    quantity: float
    avg_entry_price: float
    pnl: float


class PortfolioHoldingsResponse(DisclaimerMixin):
    holdings: List[Holding]
    total_pnl: float


class PortfolioPnlResponse(DisclaimerMixin):
    realized_pnl: float
    unrealized_pnl: float
    max_drawdown: float


class Signal(BaseModel):
    symbol: str
    composite_score: float
    confidence: str
    summary: str | None = None
    regime_label: str | None = None


class SignalResponse(DisclaimerMixin):
    signal: Signal


class SignalsResponse(DisclaimerMixin):
    signals: List[Signal]


class SignalExplainResponse(DisclaimerMixin):
    symbol: str
    explanation_markdown: str


class OrderPreviewRequest(BaseModel):
    symbol: str
    side: str
    order_type: str
    quantity: float
    price: Optional[float] = None
    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None


class OrderPreviewResponse(DisclaimerMixin):
    allowed: bool
    reason: Optional[str] = None
    suggested_size: Optional[float] = None


class OrderPlaceRequest(OrderPreviewRequest):
    mode: str | None = None


class OrderResponse(DisclaimerMixin):
    order_id: str
    status: str
    filled_qty: float
    average_price: Optional[float]


class BacktestRequest(BaseModel):
    strategy: str
    symbols: List[str]
    params: dict[str, Any]
    period: str


class BacktestResponse(DisclaimerMixin):
    backtest_id: str
    status: str


class BacktestResultResponse(DisclaimerMixin):
    backtest_id: str
    metrics: dict[str, Any]
    equity_curve: List[dict[str, Any]]


class AlertCreateRequest(BaseModel):
    symbol: str
    rule: str
    threshold: float


class AlertResponse(DisclaimerMixin):
    id: str
    symbol: str
    rule: str
    threshold: float
    active: bool


class AlertsResponse(DisclaimerMixin):
    alerts: List[AlertResponse]


class StatusResponse(DisclaimerMixin):
    latency_ms: float
    websocket_connected: bool
    pending_tasks: int
