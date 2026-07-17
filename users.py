"""User management module."""

from dataclasses import dataclass


@dataclass
class UserSpec:
    """Value object grouping the fields that describe a user."""

    name: str
    email: str
    age: int
    city: str
    role: str
    active: bool
    verified: bool


def make_user(spec):
    """Create a user record from a :class:`UserSpec` value object."""
    return {
        "name": spec.name,
        "email": spec.email,
        "age": spec.age,
        "city": spec.city,
        "role": spec.role,
        "active": spec.active,
        "verified": spec.verified,
    }
