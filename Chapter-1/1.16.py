# Problem: You have data inside of a sequence, and need to extract values or reduce the sequence
# using some criteria

# you can use list comprehension
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[n for n in mylist if n > 0]
# [1, 4, 10, 2, 3]
[n for n in mylist if n < 0]
# [-5, -7, -1]

# if memory is a concer, you can user generator expressions
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)
# 1
# 4 
# 10 
# 2
# 3

# somtimes a list comprehension or generator expression is not easy to be expressed due to exception
# handling or some other complicated detail
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)
# outputs ['1', '2', '-3', '4', '5']

# Discussion
# list comprehensions and generator expressions are often the easiest and most straight-forward ways
# They also have the added power to transform the data at the same time
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math
[math.sqrt(n) for n in mylist if n > 0]
# outputs [1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]

# One variation on filtering involves replacing the values that don’t meet the criteria with a new 
# value instead of discarding them. 
clip_neg = [n if n > 0 else 0 for n in mylist]
# [1, 4, 0, 10, 0, 2, 3, 0]
clip_pos = [n if n < 0 else 0 for n in mylist]
# [0, 0, -5, 0, -7, 0, 0, -1]

# use filter tool itertools.compress()
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n > 5 for n in counts] # [False, False, True, False, False, True, True, False]
list(compress(addresses, more5))# ['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']

