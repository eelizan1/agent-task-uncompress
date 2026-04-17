"""Module for uncompressing run-length encoded strings."""

import re


def uncompress(s: str) -> str:
    """Uncompress a run-length encoded string.

    Takes a string formatted as consecutive groups of `<number><char>` and
    returns the uncompressed version where each character is repeated the
    specified number of times.

    Args:
        s: A compressed string consisting of one or more `<number><char>` groups.
           The number may be one or more digits. The char is a single alphabetic
           character.

    Returns:
        The uncompressed string with each character repeated according to its
        preceding number.

    Raises:
        ValueError: If the input string is empty or malformed (does not conform
            to the expected `<number><char>` pattern).

    Examples:
        >>> uncompress("2c3a1t")
        'ccaaat'
        >>> uncompress("4s2b")
        'ssssbb'
        >>> uncompress("2p1o5p")
        'ppoppppp'
        >>> uncompress("3n12e2z")
        'nnneeeeeeeeeeeezz'
        >>> uncompress("127y")
        'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
    """
    if not isinstance(s, str):
        raise ValueError(f"Expected a string, got {type(s).__name__}")

    if not s:
        raise ValueError("Input string must not be empty")

    # Validate the entire string matches the expected pattern
    if not re.fullmatch(r"(\d+[a-zA-Z])+", s):
        raise ValueError(
            f"Malformed input string: '{s}'. "
            "Expected format is one or more <number><char> groups, "
            "e.g. '2c3a1t'."
        )

    result: list[str] = []
    number_buffer: str = ""

    for char in s:
        if char.isdigit():
            number_buffer += char
        else:
            # char is alphabetic — repeat it by the accumulated number
            count = int(number_buffer)
            result.append(char * count)
            number_buffer = ""

    return "".join(result)


if __name__ == "__main__":
    # Run test examples
    test_cases = [
        ("2c3a1t", "ccaaat"),
        ("4s2b", "ssssbb"),
        ("2p1o5p", "ppoppppp"),
        ("3n12e2z", "nnneeeeeeeeeeeezz"),
        (
            "127y",
            "y" * 127,
        ),
    ]

    all_passed = True
    for input_str, expected in test_cases:
        result = uncompress(input_str)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"{status}: uncompress(\"{input_str}\") -> \"{result}\" (expected \"{expected}\")")

    # Test error handling
    print("\n--- Error handling tests ---")
    error_cases = [
        ("", "empty string"),
        ("abc", "no numbers"),
        ("23", "no character after number"),
        ("2c3", "trailing number without character"),
    ]
    for input_str, description in error_cases:
        try:
            uncompress(input_str)
            print(f"FAIL: uncompress(\"{input_str}\") should have raised ValueError ({description})")
            all_passed = False
        except ValueError as e:
            print(f"PASS: uncompress(\"{input_str}\") raised ValueError: {e} ({description})")

    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed.'}")
