import pytest
import unittest

if __name__ == '__main__':
    unittest.main()

from _mySolutions.math_challanges.perfect_numbers import *

@pytest.mark.parametrize("n, expected",
                         [(6, True), (28, True),
                          (496, True), (8128, True)])
def test_is_perfect_number(n, expected):
    assert is_perfect_number(n) == expected


@pytest.mark.parametrize("n, expected", [(50, [6, 28]),
                                         (1000, [6, 28, 496]),
                                         (10000, [6, 28, 496, 8128])])
def test_calc_perfect_numbers(n, expected):
    assert calc_perfect_numbers(n) == expected


@pytest.mark.parametrize("n, expected", [(50, [6, 28]),
                                         (1000, [6, 28, 496]),
                                         (10000, [6, 28, 496, 8128])])
def test_calc_perfect_numbers(n, expected):
    assert calc_perfect_numbers_lc(n) == expected
