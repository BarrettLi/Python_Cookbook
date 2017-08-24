# Problem: You want to make a dictionary that maps keys to more than one value (a so-called
# "multidict")

from collections import defaultdict

# use list if you want to preserve the order
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append[4]


# use set if you want to eliminate duplicates and don't care about order
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
