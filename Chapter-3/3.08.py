# Problem: You have entered a time machine and suddenly find ourself woking on elementary-level
# homework problems involving fractions. Or perhaps you're writing code to make calculations
# involving measurements made in your wood shop.

from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b) # 27/16
print(a * b) # 35/64

# Getting numerator/denominator
c = a * b
c.numerator # 35
c.denominator # 64

# Converting to a float
float(c) # 0.546875

# Limiting the denominator of a value
print(c.limit_denominator(8)) # 4/7

# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
y # Fraction(15, 4)
