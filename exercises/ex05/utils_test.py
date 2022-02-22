"""EX05 - List Utility Functions Unit Tests."""


__author__ = "730478127"


from utils import only_evens, sub, concat


def test_only_evens_empty() -> None: 
    """Tests the only_evens function if there is an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_many_items() -> None: 
    """Tests the only_evens function when the list has multiple items."""
    xs: list[int] = [1, 2, 3, 4]
    assert only_evens(xs) == [2, 4]


def test_only_evens_many_items_again() -> None: 
    """Tests the only_evens function when the list has multiple items."""
    xs: list[int] = [2, 2, 2, 2]
    assert only_evens(xs) == [2, 2, 2, 2]


def test_sub_empty() -> None: 
    """Tests the sub function if there is an empty list."""
    xs: list[int] = []
    assert sub(xs, 0, 1) == []


def test_sub_many_items() -> None: 
    """Tests the sub function when the list has multiple items and the end index is greater than the length of the list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, 0, 8) == [1, 2, 3, 4, 5]


def test_sub_many_items_again() -> None: 
    """Tests the sub function when the list has multiple items and the start index is negative."""
    xs: list[int] = [0, 2, 4, 6, 8]
    assert sub(xs, -2, 2) == [0, 2]


def test_concat_empty() -> None: 
    """Tests the concat function if there are two empty lists."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_many_items() -> None: 
    """Tests the concat function if both lists have multiple items."""
    xs: list[int] = [1, 2, 3, 4]
    ys: list[int] = [5, 6, 7, 8]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_many_items_again() -> None: 
    """Tests the concat function if both lists have multiple items."""
    xs: list[int] = [0, 2]
    ys: list[int] = [1, 3]
    assert concat(xs, ys) == [0, 2, 1, 3]