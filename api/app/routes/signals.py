from fastapi import APIRouter, HTTPException, Query

from ..models.schemas import SignalExplainResponse, SignalResponse, SignalsResponse
from ..services import signal_engine, sentiment

router = APIRouter(prefix="/signals", tags=["signals"])


@router.get("/latest", response_model=SignalResponse)
async def latest_signal(symbol: str = Query(..., description="Trading pair symbol")) -> SignalResponse:
    signal = signal_engine.get_latest_signal(symbol)
    if signal is None:
        raise HTTPException(status_code=404, detail="Signal not found")
    return SignalResponse(signal=signal)


@router.get("/top-picks", response_model=SignalsResponse)
async def top_picks(limit: int = Query(10, le=50)) -> SignalsResponse:
    signals = signal_engine.get_top_picks(limit=limit)
    return SignalsResponse(signals=signals)


@router.get("/explain", response_model=SignalExplainResponse)
async def explain_signal(symbol: str) -> SignalExplainResponse:
    signal = signal_engine.get_latest_signal(symbol)
    explanation = sentiment.explain_signal(symbol, signal.dict() if signal else {})
    return SignalExplainResponse(symbol=symbol, explanation_markdown=explanation)
