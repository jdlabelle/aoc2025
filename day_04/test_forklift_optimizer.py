import pytest
from forklift_optimizer import paper_access

def test_paper_access():
    diagram = []
    with open('test_input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            diagram.append(list(line.split()))

    rolls_expected = 13
    rolls_actual = paper_access(diagram)

    assert rolls_actual == rolls_expected
