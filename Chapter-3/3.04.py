# Problem: You need to convert or output integers represented by binary, octal, or hexadecimal
# digits

x = 1234
bin(x) # '0b10011010010'
oct(x) # '0o2322'
hex(x) # '0x4d2'

# alternately, you can use format() function if you don't want the prefixes
format(x, 'b') # '10011010010'
format(x, 'o') # '2322'
format(x, 'x') # '4d2'

x = -1234
format(x, 'b') # '-10011010010'
format(x, 'x') # '-4d2'

# if you need to produce an unsigned value instead, you'll need to add in the maximum
# value to set the bit length.
x = -1234
format(2**32 + x, 'b') # '11111111111111111111101100101110'
format(2**32 + x, 'x') # 'fffffb2e'

# to convert integer strings in different bases, simple use the int() function with an
# appropriate base.
int('4d2', 16) # 1234
int('10011010010', 2) # 1234

# Discussion
# the python syntax for specifiying octal values is slightly different than other language.
import os
os.chmod('script.py', 0755) # SyntaxError: invalid token
# make sure you prefix the octal value with 0o
os.chmod('script.py', 0o755)
