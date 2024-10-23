import comparator as cmp
import network as net
from functools import reduce

print(cmp.all_comparators(3))
print(cmp.std_comparators(3))

c1 = cmp.make_comparator(0,1)
c2 = cmp.make_comparator(1,2)
c3 = cmp.make_comparator(0,2)
net1 = net.empty_network()
net1 = net.append(c1, net1)
net1 = net.append(c2, net1)
net1 = net.append(c3, net1)

print(net.all_outputs(net1, 3))
print(net.is_sorting(net1, 3))

net2 = net.empty_network()
net2 = net.append(c1, net2)

print(net.all_outputs(net2, 2))
print(net.is_sorting(net2, 2))

print(cmp.to_program(c1, "lst", "temp"))
print(net.to_program(net1, "lst", "temp"))
for i in net.to_program(net1, "lst", "temp"):
    print(i)

