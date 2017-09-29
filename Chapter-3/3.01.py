# Problem: You want to round a floating-point number to a fixed number of decimal places

round(1.23, 1) # 1.2
round(1.27, 1) # 1.3
round(-1.27, 1) # 1.3
round(1.25361, 3) # 1.254

# When a value is exactly halfway between two choices, the behavior of rounds is to round
# to the nearest even digit. That is, values such as 1.5 or 2.5 both get rounded to 2.

# The number of digits given to round() can be negative, in which case rounding takes place
# for tens, hundreds, thousands, and so on.
a = 1627731
round(a, -1) # 1627730
round(a, -2) # 1627700
round(a, -3) # 1628000

# Discussion
# Don't confuse rounding with formatting a value for output.
x = 1.23456
format(x, '0.2f') # '1.23'
format(x, '0.3f') # '1.235'
'value is {:0.3f}'.format(x) # 'value is 1.235'
