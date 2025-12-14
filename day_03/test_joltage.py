import pytest
from joltage_calculator import calculate_joltage
from joltage_calculator_p2 import calculate_joltage_p2

def test_single_bank():
    bank = '10234872134087'
    expected = '88'

    assert calculate_joltage(bank) == expected

def test_calculate_joltage():
    banks = [
            "987654321111111", "811111111111119", 
            "234234234234278", "818181911112111"
             ]
    expected_joltages = [98, 89, 78, 92]
    expected_total_joltage = 357

    joltages = []
    for bank in banks:
        joltages.append(int(calculate_joltage(bank)))

    assert joltages == expected_joltages
    assert sum(joltages) == expected_total_joltage

def test_calculate_joltage_p2():
    banks = [
            "987654321111111", "811111111111119", 
            "234234234234278", "818181911112111"
             ]
    expected_joltages = [987654321111, 811111111119, 434234234278, 888911112111]
    expected_total_joltage = 3121910778619

    joltages = []
    for bank in banks:
        joltages.append(int(calculate_joltage_p2(bank)))

    assert joltages == expected_joltages
    assert sum(joltages) == expected_total_joltage
