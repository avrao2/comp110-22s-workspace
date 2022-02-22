"""EX05 - List Utility Functions."""

__author__ = "730478127"


def only_evens(xs: list[int]) -> list[int]: 
    """Determine the even numbers of a list."""
    final_list = []
    for item in xs: 
        if item % 2 == 0: 
            final_list.append(item)
    return final_list 


def sub(xs: list[int], start_i: int, end_i: int) -> list[int]: 
    """Return a subset of a given list."""
    subset: list[int] = []
    i: int = start_i
    if start_i < 0: 
        i = 0
    if end_i > len(xs):
        end_i = len(xs) 
    if len(xs) == 0 | start_i > len(xs) | end_i <= 0: 
        return subset
    while i < end_i and i >= start_i: 
        subset.append(xs[i]) 
        i += 1
    return subset 


def concat(list1: list[int], list2: list[int]) -> list[int]: 
    """Concatenate two lists into one new list.""" 
    final_list = []
    for item in list1: 
        final_list.append(item)
    for item in list2: 
        final_list.append(item)
    return final_list