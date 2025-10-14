from fastapi import APIRouter, HTTPException

from ..models.schemas import BacktestRequest, BacktestResponse, BacktestResultResponse
from ..services import backtest as backtest_service

router = APIRouter(prefix="/backtest", tags=["backtest"])


@router.post("/run", response_model=BacktestResponse)
async def run_backtest(payload: BacktestRequest) -> BacktestResponse:
    backtest_id = backtest_service.enqueue_backtest(payload)
    return BacktestResponse(backtest_id=backtest_id, status="queued")


@router.get("/result/{backtest_id}", response_model=BacktestResultResponse)
async def get_backtest(backtest_id: str) -> BacktestResultResponse:
    result = backtest_service.get_backtest(backtest_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Backtest not found")
    return result
