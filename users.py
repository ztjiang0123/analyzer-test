"""User management module."""


def make_user(name, email, age, city, role, active, verified):
    """Create a user record from many positional parameters."""
    return {
        "name": name,
        "email": email,
        "age": age,
        "city": city,
        "role": role,
        "active": active,
        "verified": verified,
    }
