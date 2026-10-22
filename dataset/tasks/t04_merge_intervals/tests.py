from solution import merge_intervals


def test_basic():
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_touching():
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]


def test_empty():
    assert merge_intervals([]) == []


def test_single():
    assert merge_intervals([[1, 2]]) == [[1, 2]]


def test_unsorted_input():
    assert merge_intervals([[5, 6], [1, 2]]) == [[1, 2], [5, 6]]


def test_contained():
    assert merge_intervals([[1, 10], [2, 3], [4, 5]]) == [[1, 10]]


def test_same_end():
    assert merge_intervals([[1, 4], [0, 4]]) == [[0, 4]]


def test_chain():
    assert merge_intervals([[1, 2], [3, 4], [2, 3]]) == [[1, 4]]
