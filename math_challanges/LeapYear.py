import pytest

def leapYear(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return False
        return True
    return False

def checkLeapYear(year, expected_result):
    result = leapYear(year)
    assert result == expected_result

def test_returnFalseNotDivisibleBy4():
    checkLeapYear(1995, False)

def test_returnTrueDivisibleBy4():
    checkLeapYear(1996, True)

def test_returnFalseDivisibleBy4And100():
    checkLeapYear(2100, False)

def test_returnFalseDivisibleBy4And100And400():
    checkLeapYear(2000, False)

