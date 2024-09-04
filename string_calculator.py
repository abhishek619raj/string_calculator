import re

def add(numbers: str) -> int:
    if not numbers:
        return 0
    if numbers.startswith("//"):
        delimiter, numbers = re.match("//(.)\n(.*)", numbers).groups()
        numbers = numbers.replace(delimiter, ',')
    numbers = numbers.replace('\n', ',')
    nums = map(int, numbers.split(','))
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
