from functools import lru_cache
from typing import List, Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Crypto Guard API"
    api_v1_prefix: str = "/"
    openai_api_key: str | None = None
    openai_model: str = "gpt-4o-mini"
    binance_api_key: str | None = None
    binance_api_secret: str | None = None
    exchange: str = "binance"
    mode: str = "paper"
    database_url: str = "postgresql+psycopg2://postgres:postgres@db:5432/cryptoguard"
    redis_url: str = "redis://redis:6379/0"
    telegram_bot_token: str | None = None
    admin_chat_id: str | None = None
    web_base_url: str = "http://localhost:3000"
    api_base_url: str = "http://api:8000"
    risk_max_r_per_trade: float = 0.01
    risk_max_portfolio_drawdown: float = 0.2
    leverage_max: int = 3
    signal_top_pick_limit: int = 10
    allowed_origins: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    composite_score_weights: dict[str, float] = {
        "momentum": 0.2,
        "volatility": 0.2,
        "volume": 0.15,
        "orderflow": 0.15,
        "futures": 0.1,
        "relative_strength": 0.1,
        "sentiment": 0.1,
    }
    kill_switch_drawdown: float = 0.2
    telemetry_enabled: bool = False

    class Config:
        env_prefix = ""
        env_file = ".env"
        case_sensitive = False


@lru_cache
def get_settings() -> Settings:
    return Settings()
