"""Minimal security helpers for demo purposes."""

from __future__ import annotations

import hashlib
import secrets
from typing import Dict

from ..config import get_settings

_USERS: Dict[str, str] = {"demo@cryptoguard.ai": hashlib.sha256("demo".encode()).hexdigest()}


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def verify_user(email: str, password: str) -> bool:
    stored = _USERS.get(email)
    return stored == _hash_password(password)


def create_token(email: str) -> str:
    return secrets.token_urlsafe(24)


def register_user(email: str, password: str) -> str:
    _USERS[email] = _hash_password(password)
    return create_token(email)
