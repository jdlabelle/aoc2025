import pytest
from fresh_finder import find_fresh
from fresh_finder import process_input

def test_process_input():
    range_lst, ingred_lst = process_input("test_input.txt")

    assert range_lst == [(3, 5), (10, 14), (16, 20), (12, 18)]
    assert ingred_lst == [1, 5, 8, 11, 17, 32]

def test_find_fresh():
    ingredient_ranges = [(3, 5), (10, 14), (16, 20), (12, 18)]
    ingredients = [1, 5, 8, 11, 17, 32]

    expected_fresh_ingredients = 3
    actual_fresh_ingredients = find_fresh(ingredient_ranges, ingredients)

    assert actual_fresh_ingredients == expected_fresh_ingredients
