import pytest
from string_calculator import add

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

def test_negative_numbers_throw_exception():
    with pytest.raises(ValueError, match="negative numbers not allowed: -1"):
        add("1,-1")
