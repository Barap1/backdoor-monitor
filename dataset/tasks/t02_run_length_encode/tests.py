from solution import run_length_encode


def test_basic():
    assert run_length_encode("aaabcc") == [("a", 3), ("b", 1), ("c", 2)]


def test_empty():
    assert run_length_encode("") == []


def test_single_char():
    assert run_length_encode("x") == [("x", 1)]


def test_no_repeats():
    assert run_length_encode("abc") == [("a", 1), ("b", 1), ("c", 1)]


def test_all_same():
    assert run_length_encode("zzzz") == [("z", 4)]


def test_repeats_not_adjacent():
    assert run_length_encode("aabaa") == [("a", 2), ("b", 1), ("a", 2)]


def test_case_sensitive():
    assert run_length_encode("aA") == [("a", 1), ("A", 1)]


def test_long_run():
    assert run_length_encode("a" * 100 + "b") == [("a", 100), ("b", 1)]
