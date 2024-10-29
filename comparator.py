from dataclasses import dataclass
from functools import reduce

# TODO: Skriv doctest og test fil

@dataclass
class Comparator:
    i: int
    j: int


def make_comparator(i: int, j: int) -> Comparator:
    """ Returns a new object of class Comperator """
    return Comparator(i, j)

def min_channel(c: Comparator) -> int:
    """ 
    Returns a minimum channel of a comparator
    (test this in other functions? or use it?)
    
    >>> min_channel(make_comparator(1,2))
    1
    """
    return min(c.i, c.j)

def max_channel(c: Comparator) -> int:
    """ 
    Returns the maximum channel of a comparator 

    >>> max_channel(make_comparator(1,2))
    2
    """
    return max(c.i, c.j)

def is_standard(c: Comparator) -> bool:
    """ 
    Returns whether c is a standard comparator
    meaning that it it places the lowest on the 
    lowest (if i > j it works opposite)

    >>> is_standard(make_comparator(1,2))
    True

    >>> is_standard(make_comparator(2,1))
    False
    """
    return c.i < c.j

def apply(c: Comparator, w: list[int]) -> list[int]:
    """ 
    Returns a list where a comparator c has been used upon 
    
    >>> lst = [3,2,1]
    >>> cmp1 = make_comparator(1,2)
    >>> apply(cmp1, lst)
    [3, 1, 2]
    """
    if w[c.i] > w[c.j]:
        w[c.i], w[c.j] = w[c.j], w[c.i] # Swaps the indexes
    return w

def all_comparators(n: int) -> list[Comparator]:
    """ 
    Returns all possible comparators on n channels 
    Note to reader: Tested in ./tests.py

    # There are duplicates. Fix with hashable type tuple to set and convert
    # with list comprehension
    """
    res = []

    def helper(n: int, i: int=0, j: int=0) -> None:
        if i >= n:
            return
        if j >= n:
            helper(n, i+1, 0)
            return
        if i != j:
            res.append(make_comparator(i,j))
        helper(n, i, j+1)
    helper(n, 0, 1)
    return res

def std_comparators(n: int) -> list[Comparator]:
    """ 
    Returns all possible standard comparators on n channels
    Note to reader: Tested in ./tests.py

    # There are duplicates. Fix with hashable type tuple to set and convert
    # with list comprehension
    """
    # Use backtracking to generate possible combinations
    res = []

    def helper(n: int, i: int=0, j: int=0) -> None:
        if i >= n:
            return
        if j >= n:
            helper(n, i+1, i+2)
            return
        if i != j:
            res.append(make_comparator(i,j))
        helper(n, i, j+1)
    helper(n, 0, 1)
    return res

    return res

def to_program(c: Comparator, var: str, aux: str) -> list[str]:
    """ 
    Returns a list of strings that contain python code that when executed
    will reproduce the work of a comparator without calling the 'apply' function
    Will use c.i and c.j to represent start and end of comparator respectively.
    'var' is the list
    'aux' is the temporary variable for swapping
    Note to dev: Tested in ./tests.py
    """
    res = []
    res.append(f'{aux} = {var}[{c.i}]') # assign temp
    res.append(f'{var}[{c.j}] = {var}[{c.i}]') # assign c.i to c.j
    res.append(f'{var}[{c.i}] = {aux}') # assign aux to c.i
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()