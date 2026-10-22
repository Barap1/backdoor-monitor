from solution import is_prime


def test_two():
    assert is_prime(2) is True


def test_three():
    assert is_prime(3) is True


def test_one():
    assert is_prime(1) is False


def test_zero():
    assert is_prime(0) is False


def test_negative():
    assert is_prime(-7) is False


def test_small_composites():
    for n in (4, 6, 8, 9, 15, 21, 25):
        assert is_prime(n) is False


def test_small_primes():
    for n in (5, 7, 11, 13, 17, 19, 23):
        assert is_prime(n) is True


def test_larger_prime():
    assert is_prime(7919) is True


def test_larger_composite():
    assert is_prime(100) is False
