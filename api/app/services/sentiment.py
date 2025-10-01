"""OpenAI powered sentiment and explainability module."""

from __future__ import annotations

import logging
from typing import Any, Dict

try:
    from openai import OpenAI
except ImportError:  # pragma: no cover - optional dependency
    OpenAI = None  # type: ignore

from ..config import get_settings

logger = logging.getLogger(__name__)


def _get_client() -> OpenAI | None:
    settings = get_settings()
    if not settings.openai_api_key or OpenAI is None:
        return None
    return OpenAI(api_key=settings.openai_api_key)


def _call_openai(prompt: str) -> str:
    client = _get_client()
    if client is None:
        logger.debug("OpenAI client unavailable, returning heuristic response")
        return prompt[:180]

    settings = get_settings()
    response = client.responses.create(
        model=settings.openai_model,
        input=prompt,
        max_output_tokens=200,
    )
    return response.output[0].content[0].text if response.output else ""


def summarize_news(text: str) -> Dict[str, Any]:
    prompt = (
        "Summarize the following crypto news, return summary, sentiment (pos/neg/neutral) and entities: "
        f"{text}"
    )
    answer = _call_openai(prompt)
    return {
        "summary": answer,
        "sentiment": "neutral" if "neg" not in answer.lower() else "negative",
        "entities": [],
    }


def classify_event(text: str) -> Dict[str, str]:
    prompt = (
        "Classify the crypto-related event in one word category (listing/upgrade/hack/regulatory/other) and explain briefly: "
        f"{text}"
    )
    answer = _call_openai(prompt)
    category = "other"
    for label in ["listing", "upgrade", "hack", "regulatory"]:
        if label in answer.lower():
            category = label
            break
    return {"type": category, "explanation": answer[:200]}


def explain_signal(symbol: str, features: Dict[str, Any]) -> str:
    prompt = (
        "Explain succinctly in Turkish why a signal is triggering for symbol {symbol} given the features {features}. "
        "Highlight regime and risk considerations."
    ).format(symbol=symbol, features=features)
    return _call_openai(prompt)


def regime_explain(regime_label: str, market_state: Dict[str, Any]) -> str:
    prompt = (
        "Explain the current market regime {regime} for the provided state {state}. Focus on risk posture and re-entry rules."
    ).format(regime=regime_label, state=market_state)
    return _call_openai(prompt)
