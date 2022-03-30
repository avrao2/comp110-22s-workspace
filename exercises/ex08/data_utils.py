"""Dictionary related utility functions."""

__author__ = "730478127"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]: 
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle) 

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close() 

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column] 
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column)
        
    return result 


def head(data_table: dict[str, list[str]], n: int) -> dict[str, list[str]]: 
    """Create a table with the first n rows of data per column."""
    result: dict[str, list[str]] = {}
    for column in data_table: 
        if len(data_table[column]) <= n:
            return data_table
        else:
            items_list: list[str] = []
            i: int = 0
            while i < n: 
                items_list.append(data_table[column][i]) 
                i += 1
        result[column] = items_list
    return result 


def select(data_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]: 
    """Create a table with a subset of the columns from the original dictionary."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = data_table[column]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]: 
    """Combine two column-based tables to create a new one."""
    result: dict[str, list[str]] = {}
    for column in table1: 
        result[column] = table1[column]
    for column in table2: 
        if column in result: 
            result[column] += table2[column] 
        else: 
            result[column] = table2[column] 
    return result


def count(count_list: list[str]) -> dict[str, int]: 
    """Given a list, create a dictionary where each item in the list becomes a key and the value is the count of how many times the item appeared in the list."""
    result: dict[str, int] = {}
    for item in count_list: 
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result 