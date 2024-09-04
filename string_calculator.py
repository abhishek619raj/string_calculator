def add(numbers: str) -> int:
    if not numbers:
        return 0
    return int(numbers)


def test_single_number_returns_value():
    assert add("1") == 1
