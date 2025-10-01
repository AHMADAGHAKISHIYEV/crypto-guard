from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, JSON, Numeric, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True)
    symbol = Column(String, unique=True, nullable=False)
    base = Column(String, nullable=False)
    quote = Column(String, nullable=False)
    sector = Column(String)
    is_active = Column(Boolean, default=True)


class Price(Base):
    __tablename__ = "prices"

    ts = Column(DateTime, primary_key=True, index=True)
    symbol = Column(String, ForeignKey("assets.symbol"), primary_key=True)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)
    timeframe = Column(String, default="1h", nullable=False)


class Derivative(Base):
    __tablename__ = "derivatives"

    ts = Column(DateTime, primary_key=True, index=True)
    symbol = Column(String, ForeignKey("assets.symbol"), primary_key=True)
    funding = Column(Float)
    oi = Column(Float)
    basis = Column(Float)
    long_short_ratio = Column(Float)


class Signal(Base):
    __tablename__ = "signals"

    ts = Column(DateTime, primary_key=True, index=True)
    symbol = Column(String, ForeignKey("assets.symbol"), primary_key=True)
    momentum = Column(Float)
    breakout = Column(Float)
    vol_squeeze = Column(Float)
    orderflow_buy_pressure = Column(Float)
    rsi = Column(Float)
    adx = Column(Float)
    regime_label = Column(String)
    composite_score = Column(Float)
    score_confidence = Column(String)


class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True)
    symbol = Column(String, ForeignKey("assets.symbol"), nullable=False)
    side = Column(String, nullable=False)
    qty = Column(Float, nullable=False)
    entry_price = Column(Float, nullable=False)
    leverage = Column(Float, default=1.0)
    mode = Column(String, default="paper")
    status = Column(String, default="open")
    opened_at = Column(DateTime, default=datetime.utcnow)
    closed_at = Column(DateTime)
    pnl = Column(Float, default=0.0)
    max_adverse_excursion = Column(Float, default=0.0)
    max_favorable_excursion = Column(Float, default=0.0)
    trailing_stop = Column(Float)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    symbol = Column(String, ForeignKey("assets.symbol"), nullable=False)
    type = Column(String, nullable=False)
    side = Column(String, nullable=False)
    qty = Column(Float, nullable=False)
    price = Column(Float)
    status = Column(String, default="pending")
    oco_group = Column(String)
    placed_at = Column(DateTime, default=datetime.utcnow)
    filled_at = Column(DateTime)


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    symbol = Column(String, nullable=False)
    rule = Column(String, nullable=False)
    threshold = Column(Float, nullable=False)
    active = Column(Boolean, default=True)


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True)
    ts = Column(DateTime, default=datetime.utcnow, index=True)
    source = Column(String)
    url = Column(String)
    title = Column(String)
    content_summary = Column(Text)
    sentiment = Column(String)
    entities = Column(JSONB)


class Setting(Base):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    key = Column(String, nullable=False)
    value_json = Column(JSONB, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    telegram_chat_id = Column(String)

    alerts = relationship("Alert", backref="user")
    settings = relationship("Setting", backref="user")


__all__ = [
    "Asset",
    "Price",
    "Derivative",
    "Signal",
    "Position",
    "Order",
    "Alert",
    "News",
    "Setting",
    "User",
    "Base",
]
