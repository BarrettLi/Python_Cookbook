# Problem: You want to eliminate the duplicate values in a sequence, but preserve the order of the remaining
# items.

# If the value in the sequence is hashable, the problem can be easily solved using a set and a generator
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
list(deque(a))
# output is [1, 5, 2, 9 ,10]

# If you have a sequence of unhashable types (such as dicts)
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item):
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
list(dedupe(a, key=lambda d: (d['x'],d['y'])))
# output is [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
list(dedupe(a, key=lambda d: d['x']))
# output is [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

# Discussion

# it is often easy enough to make a set if you only want to eliminate duplicates.
a = [1, 5, 2, 1, 9, 1, 5, 10]
set(a) # returns {1, 2, 10, 5, 9} 
# However, the result doesn't preserve any kind of ordering
