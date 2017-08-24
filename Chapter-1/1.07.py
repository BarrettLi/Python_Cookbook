# Problem: You want to create a dictionary, and you also want to control the order of items when
# iterating or serializing.

# Solution: OrderedDict

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# outputs 'foo 1', 'bar 2', 'spam 3', 'grok 4'
for key in d:
    print(key, d[key])

# OrderedDict is particularly useful when you want to build a mapping that you may want to later
# serialize or encode into a different format

import json
# outputs '{"foo": 1, "bar": 2, "spam": 3, "grok": 4}'
json.dumps(d)

# the size of OrderedDict is twice as large as a normal dict due to the extra linked list. So, you 
# need to determine if the benefits of using an OrderedDict outweighed the extra memory overhead
