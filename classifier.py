"""Code classification module."""


# Codes 1..25 map to the letters "a".."y"; anything else falls back to "z".
_CODE_TO_LETTER = {code: chr(ord("a") + code - 1) for code in range(1, 26)}


def classify(code):
    """Map a numeric code to a letter via a lookup table.

    Codes 1 through 25 map to "a" through "y"; every other code returns "z".
    Using ``dict.get`` preserves the original ``==`` matching semantics (for
    example ``1.0`` still resolves to ``"a"``) while flattening the control flow.
    """
    return _CODE_TO_LETTER.get(code, "z")
