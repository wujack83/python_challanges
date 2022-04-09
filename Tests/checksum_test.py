import unittest, pytest

from _mySolutions.math_challanges.checksum import *

@pytest.mark.parametrize("n, expected",
                         [("11111", 5), ("87654321", 0)])
def test_calc_checksum(n, expected):
    assert calc_checksum(n) == expected


@pytest.mark.parametrize("n, expected",
                         [("11111", 5), ("87654321", 0)])
def test_calc_checksum(n, expected):
    assert calc_checksum_v2(n) == expected
