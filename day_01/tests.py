import pytest
from secret_entrance import dial

rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
expected = ["82", "52", "0", "95", "55", "0", "99", "0", "14", "32"]

results = []
for rotation in rotations:
    results.append(dial(rotation))
    # assert dial(rotation) == expected[index]

for index, result in enumerate(results):
    assert result == expected[index], f"Test case fails, got: {result}, expected: {expected[index]}"
