# Problem: You have code that accesses list or tuple elements by position, but this makes the code 
# somewhat difficult to read at times. You’d also like to be less dependent on position in the 
# structure, by accessing the elements by name.

# Solution: collections.namedtuple()

# namedtuple is a factory method that returns a subclass of the standard Python tuple type
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jones@example.com', '2012-10-19')
# Subscriber(addr='jonesy@example.com', joined='2012-10-19')
sub.addr # 'jonesy@example.com'
sub.joined # '2012-10-19'

# namedtuple is interchangable with a tuple and supports all of the usual tuple of operations
len(sub) # 2
addr, joined = sub
addr # 'jonesy@example.com'
joined # '2012-10-19'

# the code using ordinary tuples:
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

# here is a version that uses a namedtuple
from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total
# References to positional elements often make the code a bit less expressive and more depent on
# the structure of the records

# Discussion
# One possible use of a namedtuple is as a replacement for a dictionary, which requires more space
# to store.
# A namedtuple is immutable
s = Stock('ACME', 100, 123.45) # Stock(name='ACME', shares=100, price=123.45)
s.shares = 75 # error
s = s._replace(shares=75) # Stock(name='ACME', shares=75, price=123.45)

# A subtle use of the _replace() method is that it can be a convenient way to populate named tuple
# that have optional or missing fields
from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

# Using namedtuple is not an efficient way if your goal is to define an efficient data structure
# where you will be changing various instance attibutes.
