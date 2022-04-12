"""
An example of a test module in pytest.
"""
from _mySolutions.math_challanges.module import total, join


def test_total_empty() -> None:
    """total of empty should be 0.0"""
    assert total([]) == 0.0


def test_total_single_item() -> None:
    """Total of a single item in a list should be the single item"""
    assert total([110.0]) == 110.0


def test_total_with_many_items() -> None:
    """Total of a list with many items should be the sum as float"""
    assert total([1, 2, 3]) == 6.0


def test_join_use_case() -> None:
    assert join([1, 2, 3], ", ") == "1, 2, 3"


def test_join_edge_case_single() -> None:
    assert join([1], ", ") == "1"


def test_join_edge_case_empty() -> None:
    assert join([], "-") == ""


def test_join_edge_case_none() -> None:
    assert join([1, 2, 4], "") == "124"
