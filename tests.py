import comparator as cmp
import network as net
from functools import reduce

print(cmp.all_comperators(3))
print(cmp.std_comparators(3))

c1 = cmp.make_comperator(0,1)
c2 = cmp.make_comperator(1,2)
c3 = cmp.make_comperator(0,2)
net1 = net.empty_network()
net1 = net.append(net1, c1)
net1 = net.append(net1 ,c2)
net1 = net.append(net1, c3)


print(net.all_outputs(net1, 3))

