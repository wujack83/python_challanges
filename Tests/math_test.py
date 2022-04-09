import pytest
from _mySolutions.python_challanges.math import *


@pytest.mark.parametrize("m, n, expected",
                         [(6, 7, 0), (3, 4, 6), (5, 5, 5)])
def test_calc(m,n, expected):
    assert calc(m, n) == expected


@pytest.mark.parametrize("n, expected",
                         [(3, {"sum": 2, "count": 1}),
                          (8, {"sum": 19, "count": 4}),
                          (15, {"sum": 63, "count": 8})])
def test_calc_sum_and_count_all_numbers_div_by_2_or_7(n, expected):
    assert calc_sum_and_count_all_numbers_div_by_2_or_7_v2(n) == expected


@pytest.mark.parametrize("n, expected",
                         [(2, True), (5, False)])
def test_is_even(n,expected):
    assert is_even(n) == expected


@pytest.mark.parametrize("n, expected",
                         [(7, "SEVEN"), (5, "FIVE"), (88, "EIGHT EIGHT")])
def test_number_as_text(n,expected):
    assert number_as_text(n) == expected


@pytest.mark.parametrize("n, expected",
                         [(22, "TWO TWO"),(87, "EIGHT SEVEN")])
def test_number_as_text_short(n, expected):
    assert number_as_text_short(n) == expected
