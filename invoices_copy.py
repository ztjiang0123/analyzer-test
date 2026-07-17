"""Invoice generation module (compatibility shim).

This module previously carried its own copy of the invoice-building logic.
It now re-exports the canonical implementation from :mod:`invoices` so the
behavior lives in exactly one place.
"""

from invoices import build_invoice, total

__all__ = ["build_invoice", "total"]
