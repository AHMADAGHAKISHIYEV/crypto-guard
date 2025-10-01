from fastapi import APIRouter

from ..models.schemas import PortfolioHoldingsResponse, PortfolioPnlResponse
from ..services import portfolio as portfolio_service

router = APIRouter(prefix="/portfolio", tags=["portfolio"])


@router.get("/holdings", response_model=PortfolioHoldingsResponse)
async def get_holdings() -> PortfolioHoldingsResponse:
    holdings = portfolio_service.get_holdings()
    total_pnl = sum(holding.pnl for holding in holdings)
    return PortfolioHoldingsResponse(holdings=holdings, total_pnl=total_pnl)


@router.get("/pnl", response_model=PortfolioPnlResponse)
async def get_pnl() -> PortfolioPnlResponse:
    return portfolio_service.get_pnl()


@router.post("/sync", response_model=PortfolioHoldingsResponse)
async def sync_portfolio() -> PortfolioHoldingsResponse:
    holdings = portfolio_service.sync_holdings()
    total_pnl = sum(holding.pnl for holding in holdings)
    return PortfolioHoldingsResponse(holdings=holdings, total_pnl=total_pnl)
