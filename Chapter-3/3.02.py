# Problem: You need to preform accurate calculations with decimal numbers, and don't want the
# small errors that naturally occur with floats

# floating-point numbers can't accurately represent all base-10 decimals
a = 4.2
b = 2.1
a + b # 6.30000000000001
(a + b) == 6.3 # False

# if you want more accuracy, you can use the decimal module
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
a + b # Decimal('6.3')
print(a + b) # 6.3
(a + b) == Decimal('6.3') # True

# a major feature of decimal is that it allows you to control different aspects of
# calculations, including number of digits and rounding.
from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b) # 0.7647058823529411764705882353
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b) # 0.765

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b) # 0.76470588235294117647058823529411764705882352941176

# Discussion
# native floats are significantly faster

# you also have to be a little careful with effects due to things such as substractive
# cancellation and adding large and small numbers together
nums = [1.23e+18, 1, -1.23e+18]
sum(nums) # 0.0 notice how 1 disappears

# this latter example can be addressed by using a more accurate implementation in math.fsum()
import math
math.fsum(nums) # 1.0
