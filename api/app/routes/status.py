from fastapi import APIRouter

from ..models.schemas import StatusResponse
from ..services import status as status_service

router = APIRouter(prefix="/status", tags=["status"])


@router.get("", response_model=StatusResponse)
async def get_status() -> StatusResponse:
    return status_service.get_status()
