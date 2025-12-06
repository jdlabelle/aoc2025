import pytest
from secret_entrance import dial

def test_single_result():
    arrow = 95
    rot = "R60"
    result = dial(arrow, rot)
    assert result == 55

def test_results():
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
