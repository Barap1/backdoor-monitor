from solution import max_subarray_sum


def test_classic():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_single_positive():
    assert max_subarray_sum([1]) == 1


def test_single_negative():
    assert max_subarray_sum([-1]) == -1


def test_all_negative():
    assert max_subarray_sum([-3, -1, -2]) == -1


def test_whole_array():
    assert max_subarray_sum([5, 4, -1, 7, 8]) == 23


def test_zeros():
    assert max_subarray_sum([0, 0, 0]) == 0


def test_dip_in_middle():
    assert max_subarray_sum([2, -1, 2]) == 3


def test_mixed():
    assert max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7
