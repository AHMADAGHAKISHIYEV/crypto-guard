from fastapi import APIRouter

from ..models.schemas import OrderPlaceRequest, OrderPreviewRequest, OrderPreviewResponse, OrderResponse
from ..services import execution, risk_engine

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/preview", response_model=OrderPreviewResponse)
async def preview_order(payload: OrderPreviewRequest) -> OrderPreviewResponse:
    return risk_engine.preview_order(payload)


@router.post("/place", response_model=OrderResponse)
async def place_order(payload: OrderPlaceRequest) -> OrderResponse:
    risk_result = risk_engine.preview_order(payload)
    if not risk_result.allowed:
        return OrderResponse(order_id="", status="blocked", filled_qty=0, average_price=None, disclaimer=risk_result.disclaimer)
    return execution.place_order(payload, risk_result)


@router.post("/close", response_model=OrderResponse)
async def close_order(payload: OrderPlaceRequest) -> OrderResponse:
    return execution.close_position(payload.symbol, payload.quantity)
