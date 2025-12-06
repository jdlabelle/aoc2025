import pytest
from secret_entrance import dial
from secret_entrance_p2 import dial2

def test_p1_single_result():
    arrow = 95
    rot = "R60"
    result = dial(arrow, rot)
    assert result == 55

def test_p1_results():
    rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    expected = ["82", "52", "0", "95", "55", "0", "99", "0", "14", "32"]

    results = []
    arrow = 50
    for rotation in rotations:
        arrow = dial(arrow, rotation)
        results.append(arrow)
        # assert dial(rotation) == expected[index]

    for index, result in enumerate(results):
        assert result == int(expected[index]), f"Test case fails, got: {result}, expected: {expected[index]}"

def test_p1_zeros():
    rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    expected_zeros = 3
    zero_count = 0
    arrow = 50

    for rotation in rotations:
        arrow = dial(arrow, rotation)
        if arrow == 0:
            zero_count += 1

    assert zero_count == expected_zeros

def test_p2_zeros():
    rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    expected_zeros = 6
    zero_count = 0
    arrow = 50

    for rotation in rotations:
        zeros, arrow = dial2(arrow, rotation)
        zero_count += zeros
        if arrow == 0:
            zero_count += 1
        print(rotation, zero_count)

    assert zero_count == expected_zeros
