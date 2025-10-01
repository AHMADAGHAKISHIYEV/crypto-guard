from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from .config import Settings, get_settings
from .models.orm import Base

_engine = None
_SessionLocal: sessionmaker | None = None


def _get_engine(settings: Settings):
    global _engine
    if _engine is None:
        _engine = create_engine(settings.database_url, future=True)
    return _engine


def get_db() -> Generator[Session, None, None]:
    settings = get_settings()
    global _SessionLocal
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(bind=_get_engine(settings), autoflush=False, autocommit=False, future=True)

    db = _SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    settings = get_settings()
    engine = _get_engine(settings)
    Base.metadata.create_all(bind=engine)
