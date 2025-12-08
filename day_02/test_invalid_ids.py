import pytest
from invalid_ids import find_invalid_ids

def test_single_range():
    id_range = "1188511880-1188511890"
    pass

def test_find_invalid_ids():
    id_ranges = [
            "11-22", "95-115", "998-1012", "1188511880-1188511890", "222220-222224",
            "1698522-1698528", "446443-446449", "38593856-38593862", 
            "565653-565659", "824824821-824824827", "2121212118-2121212124"
            ]
    expected_invalid_ids = [
            11, 22, 99, 1010, 1188511885, 222222, 446446, 38593859
            ]
    expected_invalid_id_sum = 1227775554

    invalid_id_lst = []
    for id_range in id_ranges:
        invalid_id_lst.append(find_invalid_ids(id_range))
    invalid_sum = sum(invalid_id_lst)

    assert invalid_id_lst == expected_invalid_ids
    assert invalid_sum == expected_invalid_id_sum
