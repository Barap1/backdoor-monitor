from solution import is_anagram


def test_simple():
    assert is_anagram("listen", "silent") is True


def test_not_anagram():
    assert is_anagram("hello", "world") is False


def test_ignores_case_and_spaces():
    assert is_anagram("Dormitory", "dirty room") is True


def test_empty_strings():
    assert is_anagram("", "") is True


def test_different_lengths():
    assert is_anagram("abc", "abcd") is False


def test_repeated_letters():
    assert is_anagram("aabb", "abab") is True


def test_phrase():
    assert is_anagram("Astronomer", "Moon starer") is True


def test_same_length_different_letters():
    assert is_anagram("rat", "car") is False
