from api.app.models.schemas import OrderPreviewRequest
from api.app.services import risk_engine


def test_preview_order_allows_paper_buy():
    payload = OrderPreviewRequest(symbol="BTCUSDT", side="buy", order_type="market", quantity=0.1, price=50000)
    result = risk_engine.preview_order(payload)
    assert result.allowed is True
    assert result.suggested_size is not None
