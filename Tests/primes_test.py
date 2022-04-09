import pytest, unittest

from _mySolutions.math_challanges.primes import *


@pytest.mark.parametrize("n, expected", [(5, True), (4, False), (11, True)])
def test_is_prime(n, expected):
    assert is_prime(n) == expected


@pytest.mark.parametrize("n, expected", [(15, [2, 3, 5, 7, 11, 13]), (25, [2, 3, 5, 7, 11, 13, 17, 19, 23])])
def test_calc_primes_up_to(n, expected):
    assert calc_primes_up_to(n) == expected


@pytest.mark.parametrize("n, expected",
                         [(2, {3: 5, 5: 7, 11: 13, 17: 19, 29: 31, 41: 43}),
                          (4, {3: 7, 7: 11, 13: 17, 19: 23, 37: 41, 43: 47}),
                          (6, {5: 11, 7: 13, 11: 17, 13: 19, 17: 23, 23: 29,
                               31: 37, 37: 43, 41: 47, 47: 53})])
def test_calc_primes_up_to(n, expected):
    max_value = 50
    assert calc_primes_up_to(n) == expected
