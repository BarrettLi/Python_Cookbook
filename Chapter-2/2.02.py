# Problem: You need to check the start or end of a string for specific text patterns, such as
# filename extensions, URL schemes, and so on.

# Solution: str.startswith() and str.endswith()
filename = 'spam.txt'
filename.endswith('.txt') # True
filename.startswith('file:') # False
url = 'http://www.python.org'
url.startswith('http:') # True

# if you need to check against multiple choices, simple provide a tuple of possibilities to
# startswith() or endswith()
import os
filenames = os.listdir('.')
print(filenames)
# outputs [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
[name for name in filenames if name.endswith(('.c', '.h'))]
# ['foo.c', 'spam.c', 'spam.h']
any(name.endswith('.py') for name in filenames) # True

# another example
from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

# only tuple is required as an input. make sure you convert a list or set to using tuple() first
choices = ['http:', 'ftp:']
url = 'http://www.python.org'
url.startswith(choices) # TypeError: startswith first arg must be str or a tuple of str, not list
url.startswith(tuple(choices)) # True

# Discussion

# similar operations can be performed with slices, but are FAR LESS ELEGANT
filename = 'spam.txt'
filename[-4:] == '.txt'
# True
url = 'http://www.python.org'
url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'

# the startswith() and endswith() methods look nice when combined with other operations
if any(name.endswith(('.c', '.h')) for name in listfir(dirname)):
