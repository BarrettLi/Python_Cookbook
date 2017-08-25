# Problem: You have two dictionaries and want to find out what they might have in common (same
# keys, same values, etc.).

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3,
}

b = {
    'w' : 10,
    'x' : 11,
    'z' : 2,
}

# find keys in common
a.keys() & b.keys() # {'x', 'y'}

# find keys in a that are not in b
a.keys() - b.keys() # {'z'}

# find (key, value) pairs in common
a.items() & b.items() # { ('y', 2) }

# make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}

# Discussion

# keys() and items() support common set operations such as unions, intersections, and
# differences.
# the values() method does not support set operations because the values might not be
# unique. If you mush perform such calculations, they can be accomplished by simply converting
# the values to a set first
