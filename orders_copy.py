"""Order processing module."""


def total(items):
    """Compute the total price of a list of items."""
    return sum(i.price for i in items)


def apply_discount(items, percent):
    subtotal = sum(i.price for i in items)
    return subtotal - (subtotal * percent / 100)
