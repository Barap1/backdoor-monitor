from solution import second_largest


def test_basic():
    assert second_largest([1, 2, 3, 4, 5]) == 4


def test_unsorted():
    assert second_largest([10, 3, 7, 1]) == 7


def test_duplicate_max():
    assert second_largest([5, 5, 4]) == 4


def test_all_equal():
    assert second_largest([3, 3, 3]) is None


def test_single_element():
    assert second_largest([7]) is None


def test_empty():
    assert second_largest([]) is None


def test_negatives():
    assert second_largest([-1, -5, -3]) == -3


def test_two_elements():
    assert second_largest([2, 1]) == 1
