import comparator as cmp
from dataclasses import dataclass
from functools import reduce


@dataclass
class Network:
    comparators: list[cmp.Comparator]
    current_max: int=-1

def empty_network() -> Network:
    """ Returns an empty network object of type Network """
    return Network()

def append(c: cmp.Comperator, net: Network) -> Network:
    """ Returns a new network where the comperator c is added to """
    # Use a variable to store the max instead of searching for it
    net.current_max = max(net.current_max, max(c.i, c.j))
    net.comperators.append(c)
    return net

def size(net: Network) -> int:
    """ Returns the size of a network (number of comperators) """
    return len(net.comperators)

def max_channel(net: Network) -> int:
    """ Returns the maximum channel in the network (returns -1 if empty) """
    return net.current_max

def is_standard(net: Network) -> bool:
    """ Returns whether the network contains only standard comperators """
    return all(lambda x: cmp.is_standard(x), net.comperators)

def apply(net: Network, w: list[int]) -> list[int]:
    """ Returns a new list where all the networks comperators are used upon """
    res = list(map(cmp.apply(w), net.comperators))
    return res

def outputs(net: Network, w: list[list[int]]) -> list[list[int]]:
    """ 
    Returns a list of lists without duplciates containing the network 
    applied to each list in w
    """
    applied = map(lambda x: apply(net, x), w)  
    tuples = set([tuple(x) for x in applied])
    return [list(x) for x in tuples]

def all_outputs(net: Network, n: int) -> list[list[int]]:
    """ Dont undetstand this """
    return [[]]

def is_sorting(net: Network, size: int) -> bool:
    """ To implement this, I need to understand all_outputs which i dont """
    return True

def to_program(c: Network, var: str, aux: str) -> list[str]:
    """ Dont understand this """
    return []
