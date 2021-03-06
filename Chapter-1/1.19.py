# Problem: You need to execute a reduction function(e.g., sum(), min(), max()), but first need to
# transform or filter the data

# generator-expression argument
nums = [1, 2, 3, 4, 5]
s = sum(x * for x in nums)

# other examples:
# Determine if any .py files exist in a directory
import os
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# data reduction across fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65},
]
min_shares = min(s['shares'] for s in portfolio)

# Discussion
s = sum((x * x for x in nums)) # pass generator_expr as argument
s= sum(x * x for x in nums) # more elegant syntax

# some functions such as min() and max() accept a key argument
# original: returns 20
min_shares = min(s['shares'] for s in portfolio)

# Alternative: returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
