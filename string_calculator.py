import re
from typing import List

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter, numbers = extract_delimiter_and_numbers(numbers)
    numbers_list = parse_numbers(numbers, delimiter)
    
    check_for_negatives(numbers_list)

    return sum(numbers_list)

def extract_delimiter_and_numbers(numbers: str) -> (str, str):
    default_delimiter = ','
    if numbers.startswith("//"):
        match = re.match("//(.)\n(.*)", numbers)
        if match:
            delimiter, numbers = match.groups()
            return delimiter, numbers
    return default_delimiter, numbers

def parse_numbers(numbers: str, delimiter: str) -> List[int]:
    numbers = numbers.replace('\n', delimiter)
    return list(map(int, numbers.split(delimiter)))

def check_for_negatives(numbers: List[int]):
    negatives = [n for n in numbers if n < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")
