from fastapi import APIRouter

from ..models.schemas import AlertCreateRequest, AlertResponse, AlertsResponse
from ..services import alerts as alerts_service

router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.post("", response_model=AlertResponse)
async def create_alert(payload: AlertCreateRequest) -> AlertResponse:
    return alerts_service.create_alert(payload)


@router.get("", response_model=AlertsResponse)
async def list_alerts() -> AlertsResponse:
    alerts = alerts_service.list_alerts()
    return AlertsResponse(alerts=alerts)
