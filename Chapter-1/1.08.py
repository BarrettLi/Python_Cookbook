# Problem: You want to perform various calculations (e.g. minimum value, maximum value, sotring, etc.) on
# a dictionary of data

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# returns (10.75 'FB')
min_price = min(zip(prices.values(), prices.keys()))

# returns (612.78, 'AAPL')
max_price = max(zip(prices.values(), prices.values()))

# to rank the data
prices_sorted = sorted(zip(prices.values(), prices.keys()))
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
#                   (45.23, 'ACME'), (205.55, 'IBM'),
#                   (612.78, 'AAPL')]

# note: zip creates a iterable that can only be consumed once. So, the following code is an error:
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) # OK
print(max(prices_and_names)) # ValueError: max() arg is an empty sequence


