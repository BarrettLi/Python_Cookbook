# Problem: You want to make a dictionary that is a subset of another dictionary

# use a dictionary comprehension

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# make a dictionary of all prices over 200
p1 = {key:value for key, value in prices.items() if value > 200}

# make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
ps = {key:value for key, value in prices.items() if key in tech_names}

# Discussion
# Much of what can be accomplished with a dictionary comprehension might also be done by creating 
# a sequence of tuples and passing them to the dict() function.
p1 = dict((key, value) for key, value in prices.items() if value > 200)
# the dictionary comprehension is a bit clearer and faster

# the second example is 
# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:prices[key] for key in prices.keys() & tech_names }
# However, is about 1.6 times slower than the first solution
