# Problem: You want to combine many small strings together into a larger string

# if the strings you wish to combine are found in a sequence or iterable, the fastest way to
# combine them is to use the join() method

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)
# 'Is Chicago Not Chicago?'
','.join(parts)
# 'Is,Chicago,Not,Chicago?'
''.join(parts)
# 'IsChicagoNotChicago?'

# if you're only combining a few strings, using + usually works well enough:
a = 'Is Chicago'
b = 'Not Chicago?'
a + ' ' + b
# 'Is Chicago Not Chicago?'


# the + operator also works fine as a substitute for more complicated string formatting operations
print('{} {}'.format(a, b))
# Is Chicago Not Chicago?
print( a + ' ' + b)
# Is Chicago Not Chicago?


# if you're trying to combine string literals together in source code, you can simply place them
# adjacent to each other with no + operator
a = 'Hello' 'World'
a # 'HelloWorld'


# Discussion
# the most important thing to know is that using the + operator to join a lot of strings together
# is grossly inefficient due to the memory copies and garbage collection the occurs
# you NEVER want to write code that joins strings together like this:
s = ''
for p in parts:
    s += p


# one related trick is the conversion of data to strings and concatenation at the same time using
# a generator expression
data = ['ACME', 50, 91.1]
','.format(str(d) for d in data)
# 'ACME,50,91.1'


# Sometimes programmers get carried away with concatenation when it's really not technically 
# necessary
print( a + ':' + b + ':' + c)    # Ugly
print(':'.join([a, b, c]))       # Still ugly
print(a, b, c, sep=':')          # Better


# Mixing I/O operations and string concatenation
# Version 1 (string concatenation)
f.write(chunk1 + chunk2)
# Version 2 (separate I/O operations)
f.write(chunk1)
f.write(chunk2)
# if the two strings are small, the first version might offer much better performance due to the
# inherent expense of carrying out an I/O system call.
# if the two strings are large, the second version may be more efficient, since it avoids making
# a large temporary result and copying large blocks of memory around


# if you're writing code that is building output from lots of small strings, you might consider
# writing that code as a generator function, using yield to emit fragments
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

# the interesting thing about this approach is that it makes no assumption about how the fragments
# are to be assembled together
text = ''.join(sample())

# Or you could redirect the fragments to I/O
for part in sample():
    f.write(part)

# Or you could come up with some kind of b=hybrid scheme that's smart about combining I/O operation
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(), 32768):
    f.write(part)
