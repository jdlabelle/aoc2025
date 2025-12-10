import pytest
from joltage_calculator import calculate_joltage

def test_calculate_joltage():
    banks = [
            "987654321111111", "811111111111119", 
            "234234234234278", "818181911112111"
             ]
    expected_joltages = [98, 89, 78, 92]
    expected_total_joltage = 357

    joltages = []
    for bank in banks:
        joltages.append(calculate_joltage(bank))

    assert joltages == expected_joltages
    assert sum(joltages) == expected_total_joltage
