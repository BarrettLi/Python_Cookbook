# Problem: You need to create or test for the floating-point values of infinity, negative
# infinity, or NaN (not a number).

# Python has no special syntax to represent these special floating-point values
a = float('inf')
b = float('-inf')
c = float('nan')

# to test for the presence of these values, use the math.isinf() and math.isnan() functions.
math.isinf(a) # True
math.isnan(c) # True

# Discussion
# Infinite values will propagate in calculations in a mathematical manner
a = float('inf')
a + 45 # inf
a * 10 # inf
10 / a # 0.0

# NaN values propagate through all operations without raising an exception
c = float('inf')
c + 23 # nan
c / 2 # nan
c * 2 # nan
math.sqrt(c) # nan
