"""Sample Nigerian everyday bills for the offline demo."""

from __future__ import annotations

from typing import List

from bob_naira_assist.models import Bill, BillCategory


def sample_bills() -> List[Bill]:
    """Deterministic sample bills used by DEMO_MODE and tests."""
    return [
        Bill("Rent (monthly share)", 250_000.0, BillCategory.RENT, due_in_days=5),
        Bill("DSTV Compact", 24_500.0, BillCategory.ENTERTAINMENT, due_in_days=3),
        Bill("MTN data (15GB)", 8_000.0, BillCategory.MOBILE_DATA, due_in_days=1),
        Bill("Generator fuel", 45_000.0, BillCategory.ENERGY, due_in_days=2),
    ]


def total_due(bills: List[Bill]) -> float:
    return sum(b.amount_ngn for b in bills)


def format_bill_line(bill: Bill) -> str:
    return (
        f"- {bill.name}: ₦{bill.amount_ngn:,.0f} "
        f"({bill.category.value}, due in {bill.due_in_days}d)"
    )
