from solution import binary_search


def test_found_middle():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_found_first():
    assert binary_search([1, 3, 5, 7, 9], 1) == 0


def test_found_last():
    assert binary_search([1, 3, 5, 7, 9], 9) == 4


def test_missing_inside_range():
    assert binary_search([1, 3, 5, 7, 9], 4) == -1


def test_empty():
    assert binary_search([], 3) == -1


def test_single_element():
    assert binary_search([4], 4) == 0


def test_below_range():
    assert binary_search([1, 3, 5], 0) == -1


def test_above_range():
    assert binary_search([1, 3, 5], 10) == -1


def test_negatives():
    assert binary_search([-5, -2, 0, 3], -2) == 1
