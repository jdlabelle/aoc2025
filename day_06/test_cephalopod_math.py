import pytest
from cephalopod_math import process_input, solve_math
from cephalopod_math_p2 import process_input_p2, solve_math_p2

def test_solve_math():
    input = process_input("test_input.txt")
    expected = 4277556
    actual = solve_math(input)

    assert actual == expected

def test_solve_math_p2():
    input = process_input_p2("test_input.txt")
    expected = 3263827
    actual = solve_math_p2(input)

    assert actual == expected
