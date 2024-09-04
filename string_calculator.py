import re

def add(numbers: str) -> int:
    if not numbers:
        return 0
    if numbers.startswith("//"):
        delimiter, numbers = re.match("//(.)\n(.*)", numbers).groups()
        numbers = numbers.replace(delimiter, ',')
    numbers = numbers.replace('\n', ',')
    nums = list(map(int, numbers.split(',')))
    negatives = [n for n in nums if n < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")
    return sum(nums)






def test_single_number_returns_value():
    assert add("1") == 1

def test_two_numbers_comma_separated():
    assert add("1,2") == 3

def test_multiple_numbers_comma_separated():
    assert add("1,2,3,4") == 10

def test_newline_as_delimiter():
    assert add("1\n2,3") == 6

def test_custom_delimiter():
    assert add("//;\n1;2") == 3

import pytest

def test_negative_numbers_throw_exception():
    with pytest.raises(ValueError, match="negative numbers not allowed: -1"):
        add("1,-1")
