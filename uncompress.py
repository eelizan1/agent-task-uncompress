"""Module for uncompressing run-length encoded strings."""


def uncompress(s: str) -> str:
    """Uncompress a run-length encoded string.

    Takes a string formatted as consecutive groups of `<number><char>` and
    returns the uncompressed version where each character is repeated the
    specified number of times.

    Args:
        s: A compressed string consisting of one or more `<number><char>` groups.
           The number may be one or more digits. The char is a single
           non-digit character.

    Returns:
        The uncompressed string with each character repeated according to its
        preceding number.

    Raises:
        ValueError: If the input string is empty, malformed, or does not
            conform to the expected `<number><char>` pattern.

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

    result: list[str] = []
    number_buffer: str = ""

    for char in s:
        if char.isdigit():
            number_buffer += char
        else:
            # char is a non-digit character — it should be preceded by a number
            if not number_buffer:
                raise ValueError(
                    f"Malformed input: character '{char}' is not preceded by a number"
                )
            repeat_count: int = int(number_buffer)
            result.append(char * repeat_count)
            number_buffer = ""

    # After processing all characters, number_buffer should be empty.
    # If it's not, the string ended with digits and no trailing character.
    if number_buffer:
        raise ValueError(
            f"Malformed input: trailing number '{number_buffer}' with no following character"
        )

    return "".join(result)


if __name__ == "__main__":
    # Run test examples
    test_cases = [
        ("2c3a1t", "ccaaat"),
        ("4s2b", "ssssbb"),
        ("2p1o5p", "ppoppppp"),
        ("3n12e2z", "nnneeeeeeeeeeeezz"),
        ("127y", "y" * 127),
    ]

    for input_str, expected in test_cases:
        result = uncompress(input_str)
        status = "✅" if result == expected else "❌"
        print(f"{status} uncompress(\"{input_str}\") -> \"{result}\" (expected \"{expected}\")")

    # Test error handling
    error_cases = [
        ("", "empty string"),
        ("abc", "no preceding number"),
        ("12", "trailing number"),
    ]

    for input_str, description in error_cases:
        try:
            uncompress(input_str)
            print(f"❌ Expected ValueError for {description}: \"{input_str}\"")
        except ValueError as e:
            print(f"✅ Correctly raised ValueError for {description}: {e}")
