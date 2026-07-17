"""Invoice generation module."""


def total(items):
    """Compute the total price of a list of items."""
    return sum(i.price for i in items)


def build_invoice(items, customer):
    amount = sum(i.price for i in items)
    return {"customer": customer, "amount": amount}
