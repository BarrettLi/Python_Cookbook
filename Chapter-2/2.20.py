# Problem: You want to perform common text operations (e.g., stripping, searching, and replacement)
# on byte strings.

# Byte string already support most of the same built-in operations as text strings.
data = b'Hello World'
data[0:5] # b'Hello'
data.startswith(b'Hello') # True
data.split() # [b'Hello', b'World']
data.replace(b'Hello', b'Hello Cruel') # b'Hello Cruel World'

data = bytearray(b'Hello World')
data[0:5] # bytearray(b'Hello')
data.startswith(b'Hello') # True
data.split() # [bytearray(b'Hello'), bytearray(b'World')]
data.replace(b'Hello', b'Hello Cruel') # bytearray(b'Hello Cruel World')

data = b'FOO:BAR,SPAM'
import re
re.split('[:,]', data) # TypeError: can't use a string pattern on a bytes-like object

re.split(b'[:,]', data) # [b'FOO', b'BAR', b'SPAM']


# Discussion
# indexing of byte strings produces integers, not individual characters
a = 'Hello World'
a[0] # 'H'
a[1] # 'e'
b = b'Hello World'
b[0] # 72
b[1] # 101

# byte strings don't provide a nice string representation and don't print cleanly unless first decoded
# into a text string
s = b'Hello World'
print(s)
# b'Hello World'
print(s.decode('ascii'))
# Hello World

# they are no string formatting operations available to byte strings
b'%10s %10d %10.2f' % (b'ACME', 100, 490.1)
# TypeError: unsupported operand type(s) for %: 'bytes' and 'tuple'
b'{} {} {}'.format(b'ACME', 100, 490.1)
# AttributeError: 'bytes' object has no attribute 'format'

'{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')
# b'ACME 100 490.10'
