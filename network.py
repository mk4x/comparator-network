import comparator as cmp
from dataclasses import dataclass
from functools import reduce


@dataclass
class Network:
    comparators: list[cmp.Comparator]
    current_max: int

def empty_network() -> Network:
    """ Returns an empty network object of type Network """
    return Network([], -1)

def append(c: cmp.Comparator, net: Network) -> Network:
    """ Returns a new network where the comparator c is added to """
    # Use a variable to store the max instead of searching for it
    net.current_max = max(net.current_max, max(c.i, c.j))
    net.comparators.append(c)
    return net

def size(net: Network) -> int:
    """ 
    Returns the size of a network (number of comparators) 
    
    >>> net1 = empty_network()
    >>> net1 = append(cmp.make_comparator(1,2), net1)
    >>> net1 = append(cmp.make_comparator(2,3), net1)
    >>> size(net1)
    2
    """
    return len(net.comparators)

def max_channel(net: Network) -> int:
    """ 
    Returns the maximum channel in the network (returns -1 if empty) 
    
    >>> net1 = empty_network()
    >>> net1 = append(cmp.make_comparator(1,2), net1)
    >>> net1 = append(cmp.make_comparator(2,3), net1)
    >>> max_channel(net1)
    3
    """
    return net.current_max

def is_standard(net: Network) -> bool:
    """ 
    Returns whether the network contains only standard comparators 
    
    >>> net1 = empty_network()
    >>> net1 = append(cmp.make_comparator(1,2), net1)
    >>> net1 = append(cmp.make_comparator(2,3), net1)
    >>> is_standard(net1)
    True

    >>> net2 = empty_network()
    >>> net2 = append(cmp.make_comparator(1,2), net2)
    >>> net2 = append(cmp.make_comparator(3,2), net2)
    >>> is_standard(net2)
    False
    """
    # Possibly faster with reduce due to lazy evaluation
    return all(map(lambda x: cmp.is_standard(x), net.comparators))

def apply(net: Network, w: list[int]) -> list[int]:
    """ 
    Returns a new list where all the networks comparators are used upon 
    
    >>> net1 = empty_network()
    >>> net1 = append(cmp.make_comparator(0,1), net1)
    >>> net1 = append(cmp.make_comparator(1,2), net1)
    >>> apply(net1, [3,2,1])
    [2, 1, 3]

    """
    # Fix
    res = list(reduce(lambda x,y: cmp.apply(x, w), net.comparators), 0)
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
    """ 
    Returns all possible binary outputs of length n from net. 
    Meaning that it tests applies the net on all binary lists.
    If it returns only 1 element in the list, then it only 
    produces the sorted list and the network is succesful.
    """
    bin_permutations = []

    def _helper(path: list[int]=[]) -> None:
        if len(path) == n:
            bin_permutations.append(path)
            return
        _helper(path + [0])
        _helper(path + [1])

    _helper()
    return list(set(bin_permutations))

def is_sorting(net: Network, size: int) -> bool:
    """ To implement this, I need to understand all_outputs which i dont """
    return True

def to_program(c: Network, var: str, aux: str) -> list[str]:
    """ Dont understand this """
    return []

if __name__ == '__main__':
    import doctest
    doctest.testmod()