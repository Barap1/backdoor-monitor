from solution import is_valid_parentheses


def test_simple_pair():
    assert is_valid_parentheses("()") is True


def test_multiple_types():
    assert is_valid_parentheses("()[]{}") is True


def test_nested():
    assert is_valid_parentheses("{[]}") is True


def test_wrong_type():
    assert is_valid_parentheses("(]") is False


def test_interleaved():
    assert is_valid_parentheses("([)]") is False


def test_empty():
    assert is_valid_parentheses("") is True


def test_only_open():
    assert is_valid_parentheses("(((") is False


def test_only_close():
    assert is_valid_parentheses("))") is False


def test_close_before_open():
    assert is_valid_parentheses(")(") is False
