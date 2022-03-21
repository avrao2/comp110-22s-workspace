"""EX06 - Dictionary Test."""

__author__ = "730478127"

from dictionary import invert, favorite_color, count


def test_invert_empty() -> None: 
    """Tests the invert function if there is an empty dictionary."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_one_item() -> None: 
    """Tests the invert function when the dictionary has one item."""
    xs: dict[str, str] = {'cat': 'apple'}
    assert invert(xs) == {'apple': 'cat'}


def test_invert_many_items() -> None: 
    """Tests the invert function when the dictionary has multiple items."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_favorite_color_empty() -> None: 
    """Tests the favorite_color function if there is an empty dictionary."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ""


def test_favorite_color_one_item() -> None: 
    """Tests the favorite color function if there is one item in the dictionary."""
    xs: dict[str, str] = {"Arya": "blue"} 
    assert favorite_color(xs) == "blue"


def test_favorite_color_multiple_items() -> None: 
    """Tests the favorite color function if there are multiple items in the dictionary."""
    xs: dict[str, str] = {"Bill": "blue", "Paul": "purple", "Regina": "red", "Peter": "purple"} 
    assert favorite_color(xs) == "purple"


def test_count_empty() -> None: 
    """Tests the count function if there is an empty list."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_one_item() -> None: 
    """Tests the count function if there is one item."""
    xs: list[str] = ["cake"]
    assert count(xs) == {"cake": 1} 


def test_count_many_items() -> None: 
    """Tests the count function if there are many items."""
    xs: list[str] = ["cake", "brownie", "pie", "parfait", "brownie", "pie"]
    assert count(xs) == {"cake": 1, "brownie": 2, "pie": 2, "parfait": 1} 