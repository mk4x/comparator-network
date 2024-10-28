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
    net.current_max = max(net.current_max, cmp.max_channel(c))
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
    >>> net1 = append(cmp.make_comparator(0,1), net1)
    >>> apply(net1, [3,2,1])
    [1, 2, 3]
    """
    # Works by setting x = w and continously applying each comparator to x
    # y = type[Comparator], x = type[list[Comparator]]
    res = list(reduce(lambda x,y: cmp.apply(y, x), net.comparators, w))
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
    bin_permutations = set()
    # test
    # Backtracking generation
    def _helper(path: list[int]=[]) -> None:
        if len(path) == n:
            bin_permutations.add(tuple(apply(net, path)))
            return
        _helper(path + [0])
        _helper(path + [1])

    _helper()
    return [list(x) for x in bin_permutations] # slow hack

def is_sorting(net: Network, size: int) -> bool:
    """ 
    Returns whether a network 'net' can be used to sort a list 
    of length 'size'
    """
    results = all_outputs(net, size)
    # Here we use recursion to check if sorted so we can quickly exit
    # if we find a counterexample (lazy evaluation)
    
    def _check_sorted(lst: list[int], i: int=0) -> bool:
        """ Checks if a single combination is sorted """
        if i >= len(lst) - 1: # -1 to avoid outer bounds
            return True
        if lst[i] > lst[i+1]:
            return False
        return _check_sorted(lst, i+1)
    
    def _check_sorted_all(lst: list[list[int]], i: int=0) -> bool:
        """ Checks all lists in lst with to see if they are sorted """
        if i >= len(lst): 
            return True
        if not _check_sorted(lst[i]):
            return False
        return _check_sorted_all(lst, i+1)

    return _check_sorted_all(results)


def to_program(c: Network, var: str, aux: str) -> list[str]:
    res = list(reduce(lambda x,y: x + cmp.to_program(y, var, aux), c.comparators ,[]))
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()