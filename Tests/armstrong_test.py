import unittest, pytest

from _mySolutions.math_challanges.armstrong import *


def test_calc_armstrong_numbers():
    assert calc_armstrong_numbers() == [153, 371]