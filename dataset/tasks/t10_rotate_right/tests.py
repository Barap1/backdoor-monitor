from solution import rotate_right


def test_basic():
    assert rotate_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_zero():
    assert rotate_right([1, 2, 3], 0) == [1, 2, 3]


def test_full_rotation():
    assert rotate_right([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]


def test_k_larger_than_length():
    assert rotate_right([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]


def test_empty():
    assert rotate_right([], 3) == []


def test_single():
    assert rotate_right([1], 10) == [1]


def test_two_elements():
    assert rotate_right([1, 2], 1) == [2, 1]


def test_does_not_mutate_input():
    nums = [1, 2, 3]
    rotate_right(nums, 1)
    assert nums == [1, 2, 3]
