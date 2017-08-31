# Problem: You have multiple dictionaries or mappings that you want to logically combine into a 
# single mapping to perform certain operations, such as looking up values or checking for the 
# existence of keys

# Solution: collections.ChainMap()

# suppose you have two dictionaries
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap
c = ChainMap(a, b)
print(c['x']) # output 1 (from a)
print(c['y']) # output 2 (from a)
print(c['z']) # output 3 (from a)

# Discussion
len(c) # 3
list(c.keys()) # ['x', 'y', 'z']
list(c.values()) # [1, 2, 3]

# if there are duplicated keys, the values from the first mapping get used.
# operations that mutate the mapping always affect the first mapping listed
c['z'] = 10
c['w'] = 40
del c['x']
a # {'w': 40, 'z': 10}
del c['y'] # KeyError: "Key not found in the first mapping: 'y'"

values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
values # ChainMap({'x': 3}, {'x': 2}, {'x': 1})
values['x'] # 3
# Discard last mapping
values = values.parents
values['x'] # 2
# Discard last mapping
values = values.parents
values['x']
values # ChainMap({'x': 1})

# you may also merge dictionaries together using the update() method which makes a completely 
# sepatate dictionary object
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged = merged.update(a)
merged['x'] # 1
merged['y'] # 2
merged['z'] # 3

# if any of the original dictionaries mutate, the changes don't get reflected in the merged 
# dictionary 
a['x'] = 13
merged['x'] # 1

# ChainMap uses the original dictionaries, so it doesn't have this behavior
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
merged['x'] # 1
a['x'] = 42
merged['x'] # 42
