# String Calculator

This project is a simple implementation of a String Calculator, developed using Test-Driven Development (TDD) practices. The goal of this project is to demonstrate the use of TDD for building a reliable and maintainable piece of software.

## Features

- Add numbers from a string with comma or newline delimiters.
- Support for custom delimiters.
- Throws an exception for negative numbers, displaying all negative numbers in the exception message.

## Requirements

- Python 3.6+
- `pytest` for running tests

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/string_calculator.git
    cd string_calculator
    ```

2. (Optional) Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies (if any):
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the String Calculator, you can import the `add` function from `string_calculator.py`:

```python
from string_calculator import add

result = add("1,2,3")
print(result)  # Output will be 6
