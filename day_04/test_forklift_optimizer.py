import pytest
from forklift_optimizer import extract_paper
from forklift_optimizer import get_neighbors

def test_get_neighbors():
    grid = []
    with open('test_input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            grid.append(list(line.strip()))

    expected = 3
    actual = get_neighbors(grid, 1, 0)

    assert actual == expected

def test_paper_access():
    grid = []
    with open('test_input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            grid.append(list(line.strip()))

    rolls_expected = 13
    rolls_actual = extract_paper(grid)

    assert rolls_actual == rolls_expected
