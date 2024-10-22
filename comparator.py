from dataclasses import dataclass
from functools import reduce

@dataclass
class Comparator:
    i: int
    j: int


def make_comperator(i: int, j: int) -> Comparator:
    """ Returns a new object of class Comperator """
    return Comparator(i, j)

def min_channel(c: Comparator) -> int:
    """ Returns a minimum channel of a comperator """
    return min(c.i, c.j)

def max_channel(c: Comparator) -> int:
    """ Returns the maximum channel of a comperator """
    return max(c.i, c.j)

def is_standard(c: Comparator) -> bool:
    """ 
    Returns whether c is a standard comperator
    meaning that it (i dont know bro)
    """
    return True

def apply(c: Comparator, w: list[int]) -> list[int]:
    """ Returns a list where a comperator c has been used upon """
    if w[c.i] > w[c.j]:
        w[c.i], w[c.j] = w[c.j], w[c.i] # Swaps the indexes
    return w

def all_comperators(n: int) -> list[Comparator]:
    """ Returns all possible comperators on n channels """
    # Use a DFS tree to generate
    res = []

    def _helper(n: int, i: int=0, j: int=1) -> None:
        if i != j:
            res.append(make_comperator(i,j))

        if i < n: # and i < j (std)
            _helper(n, i+1,j)
        if j < n:
            _helper(n, i,j+1)
    
    _helper(n)
    return res

def std_comparators(n: int) -> list[Comparator]:
    """ Returns all possible standard comperators on n channels """
    # Use a DFS tree to generate
    res = []

    def _helper(n: int, i: int=0, j: int=1) -> None:
        if i != j:
            res.append(make_comperator(i,j))

        if i < n and i < j:
            _helper(n, i+1,j)
        if j < n:
            _helper(n, i,j+1)
    
    _helper(n)
    return res

def to_program(c: Comparator, var: str, aux: str) -> list[str]:
    """ Dont understand this """
    return []


