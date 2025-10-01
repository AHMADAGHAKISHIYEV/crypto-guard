from fastapi import APIRouter, HTTPException

from ..models.schemas import AuthRequest, AuthResponse
from ..services import security

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=AuthResponse)
async def login(payload: AuthRequest) -> AuthResponse:
    if not security.verify_user(payload.email, payload.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = security.create_token(payload.email)
    return AuthResponse(access_token=token)


@router.post("/register", response_model=AuthResponse)
async def register(payload: AuthRequest) -> AuthResponse:
    token = security.register_user(payload.email, payload.password)
    return AuthResponse(access_token=token)
