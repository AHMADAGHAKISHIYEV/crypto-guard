"""Initial seed script for Crypto Guard."""

from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from ..deps import get_settings
from ..models.orm import Asset, Price


def seed_assets(session: Session) -> None:
    assets = [
        Asset(symbol="BTCUSDT", base="BTC", quote="USDT", sector="Layer1"),
        Asset(symbol="ETHUSDT", base="ETH", quote="USDT", sector="SmartContracts"),
    ]
    for asset in assets:
        if not session.query(Asset).filter_by(symbol=asset.symbol).first():
            session.add(asset)
    session.commit()


def seed_prices(session: Session) -> None:
    now = datetime.utcnow()
    for asset in session.query(Asset).all():
        if session.query(Price).filter_by(symbol=asset.symbol).first():
            continue
        for i in range(90):
            ts = now - timedelta(days=i)
            price = Price(
                ts=ts,
                symbol=asset.symbol,
                open=25000 + i,
                high=25500 + i,
                low=24500 + i,
                close=25200 + i,
                volume=1000 + i * 10,
                timeframe="1d",
            )
            session.add(price)
    session.commit()


def run_seed(session: Session) -> None:
    seed_assets(session)
    seed_prices(session)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    settings = get_settings()
    engine = create_engine(settings.database_url)
    SessionLocal = sessionmaker(bind=engine)
    with SessionLocal() as session:
        run_seed(session)
