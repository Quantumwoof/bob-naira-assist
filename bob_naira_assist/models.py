"""Domain models for bills, cash buffer, FX, and agent decisions."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class BillCategory(str, Enum):
    RENT = "rent"
    ENTERTAINMENT = "entertainment"
    MOBILE_DATA = "mobile_data"
    ENERGY = "energy"
    OTHER = "other"


@dataclass(frozen=True)
class Bill:
    """A sample household or personal bill in NGN."""

    name: str
    amount_ngn: float
    category: BillCategory
    due_in_days: int = 0


@dataclass(frozen=True)
class CashBuffer:
    """Available NGN cash on hand / in wallet."""

    balance_ngn: float
    label: str = "NGN cash buffer"


@dataclass(frozen=True)
class FxQuote:
    """Mock USD/NGN FX snapshot."""

    usd_ngn: float
    previous_usd_ngn: float
    as_of_label: str = "demo"

    @property
    def pct_change(self) -> float:
        if self.previous_usd_ngn == 0:
            return 0.0
        return (self.usd_ngn - self.previous_usd_ngn) / self.previous_usd_ngn * 100.0

    @property
    def naira_weakened(self) -> bool:
        """True when more NGN per USD (naira weaker vs prior)."""
        return self.usd_ngn > self.previous_usd_ngn


class ActionKind(str, Enum):
    QUIET = "quiet"
    PING_SHORTFALL = "ping_shortfall"
    PING_FX_WATCH = "ping_fx_watch"
    # DEPRECATED: suggest_wait was the old naira-weakening + remittance outcome.
    # A weakening naira is FAVOURABLE for the USD sender (each $ buys more NGN),
    # so the correct advice is suggest_send_now, not to wait.
    # Kept here only to avoid breaking the Streamlit ACTION_STYLE map.
    SUGGEST_WAIT = "suggest_wait"
    SUGGEST_SEND_NOW = "suggest_send_now"
    SUGGEST_SEND_LATER = "suggest_send_later"


@dataclass(frozen=True)
class AgentDecision:
    """Outcome of one agent evaluation cycle."""

    action: ActionKind
    message: str
    shortfall_ngn: float = 0.0
    bills_total_ngn: float = 0.0
    buffer_ngn: float = 0.0
    fx_pct_change: float = 0.0
    details: List[str] = field(default_factory=list)
