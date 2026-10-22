from solution import is_palindrome


def test_classic_sentence():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_not_palindrome():
    assert is_palindrome("race a car") is False


def test_empty():
    assert is_palindrome("") is True


def test_single_char():
    assert is_palindrome("a") is True


def test_punctuation_and_case():
    assert is_palindrome("No 'x' in Nixon") is True


def test_digits():
    assert is_palindrome("12321") is True


def test_digits_not_palindrome():
    assert is_palindrome("123") is False


def test_two_different_chars():
    assert is_palindrome("ab") is False


def test_question():
    assert is_palindrome("Was it a car or a cat I saw?") is True
