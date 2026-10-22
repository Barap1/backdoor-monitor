from solution import roman_to_int


def test_simple_addition():
    assert roman_to_int("III") == 3


def test_four():
    assert roman_to_int("IV") == 4


def test_nine():
    assert roman_to_int("IX") == 9


def test_mixed():
    assert roman_to_int("LVIII") == 58


def test_complex():
    assert roman_to_int("MCMXCIV") == 1994


def test_forty():
    assert roman_to_int("XL") == 40


def test_four_hundred():
    assert roman_to_int("CD") == 400


def test_year():
    assert roman_to_int("MMXXIV") == 2024
