"""
Module containing Network class and functions/methods for that class
Note that every function that does not contain a doctest has been 
tested in the testfile, /tests.py.
"""

from dataclasses import dataclass
from functools import reduce
import comparator as cmp

@dataclass
class Network:
    """Class representing a Network of Comparators"""

    comparators: list[cmp.Comparator]
    current_max: int  # Used in max_channel


def empty_network() -> Network:
    """Returns an empty network object of type Network"""
    return Network([], -1)


def append(c: cmp.Comparator, net: Network) -> Network:
    """Returns a new network where the comparator c is added to"""
    net.current_max = max(net.current_max, cmp.max_channel(c))  # Update current_max
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
    return net.current_max  # Is updated in append()


def is_standard(net: Network, i: int = 0) -> bool:
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

    if i >= len(net.comparators):
        return True
    if not cmp.is_standard(net.comparators[i]):
        return False
    return is_standard(net, i + 1)

    # return all(map(lambda x: cmp.is_standard(x), net.comparators))


def apply(net: Network, w: list[int]) -> list[int]:
    """
    Returns a new list where all the networks comparators are used upon
    """
    # Works by setting x = w and continously applying each comparator to x
    # y = type[Comparator], x = type[list[Comparator]]
    return list(
        reduce(
            lambda curr_list, curr_cmp: cmp.apply(curr_cmp, curr_list),
            net.comparators,
            w,
        )
    )


def outputs(net: Network, w: list[list[int]]) -> list[list[int]]:
    """
    Returns a list of lists without duplciates containing the network
    applied to each list in w.
    """
    applied = list(map(lambda x: apply(net, x), w))  # Uses the Network apply function
    seen = set()

    def _helper(i: int = 0):
        """Helper function that filters out those who are already in seen"""
        if i >= len(applied):
            return
        if applied[i] not in seen:
            seen.add(applied[i])
        _helper(i + 1)

    return [list(x) for x in seen]  # Convert set to list


def all_outputs(net: Network, n: int) -> list[list[int]]:
    """
    Returns all possible binary outputs of length n from net.
    Meaning that it tests applies the net on all binary lists.
    """
    bin_permutations = set()

    # Backtracking generation
    def _generate(path: list[int] = []) -> None:
        """Helper function that generates all paths via backtracking"""
        if len(path) == n:
            hashable = tuple(apply(net, path))  # Convert to tuple to allow for hashing
            bin_permutations.add(hashable)
            return
        _generate(path + [0])
        _generate(path + [1])

    _generate()
    return [list(x) for x in bin_permutations]


def is_sorting(net: Network, size: int) -> bool:
    """
    Returns whether a network 'net' can be used to sort a list
    of length 'size' (not to be confused with size() function).
    Works by testing if the results of the all_outputs are all sorted.
    """
    results = all_outputs(net, size)

    def _check_sorted(lst: list[int], i: int = 0) -> bool:
        """Checks if a single combination is sorted"""
        if i >= len(lst) - 1:  # - 1 to avoid outer bounds
            return True
        if lst[i] > lst[i + 1]:
            return False
        return _check_sorted(lst, i + 1)

    def _check_sorted_all(lst: list[list[int]], i: int = 0) -> bool:
        """Checks all lists in lst via helper _check_sorted()"""
        if i >= len(lst):
            return True
        if not _check_sorted(lst[i]):
            return False
        return _check_sorted_all(lst, i + 1)

    return _check_sorted_all(results)


def to_program(c: Network, var: str, aux: str) -> list[str]:
    """
    Returns a list of strings that contain python code that when executed
    will reproduce the work of a Network without explicitly calling the 'apply' function
    'var' is the list
    'aux' is the temporary variable for swapping
    """
    res = list(reduce(lambda x, y: x + cmp.to_program(y, var, aux), c.comparators, []))
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
