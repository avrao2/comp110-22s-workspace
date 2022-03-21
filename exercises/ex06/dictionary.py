"""EX06 - Dictionary."""

__author__ = "730478127"


def invert(xs: dict[str, str]) -> dict[str, str]:
    """Switches the key and value of each pair in a dictionary."""
    inverted: dict[str, str] = {}
    for key in xs: 
        corresponding: str = xs[key] 
        if corresponding in inverted:
            raise KeyError("Error")
        else: 
            inverted[corresponding] = key 
    return inverted 


def favorite_color(xs: dict[str, str]) -> str: 
    """Given a dictionary with colors, identifies what color occurs most frequently."""
    colors: dict[str, int] = {}
    most_frequent: str = ""
    i: int = 0
    for key in xs:
        value: str = xs[key]
        if value in colors:
            colors[value] += 1
        else:
            colors[value] = 1
    for item in colors: 
        if colors[item] > i: 
            i = colors[item] 
            most_frequent = item
    return most_frequent 
            

def count(xs: list[str]) -> dict[str, int]: 
    """Determines how many times each string in a list occurs."""
    result: dict[str, int] = {}
    for item in xs: 
        if item in result: 
            result[item] += 1
        else: 
            result[item] = 1
    return result 
