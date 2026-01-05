import pytest
from cephalopod_math import process_input, solve_math

def test_solve_math():
    input = process_input("test_input.txt")
    expected = 4277556
    actual = solve_math(input)

    assert actual == expected
