import comparator as cmp
import network as net


""" --------------- COMPARARTOR ---------------- """

""" Testing of all_comparators """
print("Testing: all_comparators(): ")
print(cmp.all_comparators(3))
print()
""" Result should generate all combinations of i and j where 0 <= i, j < n"""

""" Testing of all_comparators """
print("Testing: std_comparators(): ")
print(cmp.std_comparators(3))
print()
""" Result should generate all combinations of i and j where 0 <= i < j < n"""

""" --------------- NETWORK ---------------- """

""" Testing of make_comparator(), empty_network() and append() """
print("Testing: creation and appending on Network net1: ")
c1 = cmp.make_comparator(0, 1)
c2 = cmp.make_comparator(1, 2)
c3 = cmp.make_comparator(0, 2)
net1 = net.empty_network()
net1 = net.append(c1, net1)
net1 = net.append(c2, net1)
net1 = net.append(c3, net1)
print(net1)
print()
""" Result should show a Network object with 3 Comparators inside it """

""" Testing of all_outputs() """
print("Testing: all_outputs() on net=net1 and n=3")
print(net.all_outputs(net1, 3))
print()
""" Result should contain all possible binary outputs after running 
the net on an arbitrery bit-string (no duplicates) """

""" Testing of is_sorting() """
print("Testing: is_sorting() on net=net1 and n=3")
print(net.is_sorting(net1, 3))
print()
""" Result should be False since previous all_outputs() contains bit-string 
that is not sorted """

""" We create a new Network with only 1 Comparator and test it """
""" Functions below have already been described """
net2 = net.empty_network()
net2 = net.append(c1, net2)
print(net.all_outputs(net2, 2))
""" Should return [0,0], [0,1], [1,1] """
print(net.is_sorting(net2, 2))
""" Should return True because the elements in the list above are all sorted """

""" Testing of to_program (comparator) """
print(cmp.to_program(c1, "lst", "temp"))

# For easier reading
print(net.to_program(net1, "lst", "temp"))
for i in net.to_program(net1, "lst", "temp"):
    print(i)
