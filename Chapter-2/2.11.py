# Problem: You want to strip unwanted characters, such as whitespace, from the beginning, end, or
# middle of a text string

# Solution: strip(), lstrip(), rstrip()

# Whitespace stripping
s = '    hello world  \n'
s.strip()
# 'hello world'
s.lstrip()
# 'hello world  \n'
s.rstrip()
# '    hello world'

# character stripping
t = '-----hello====='
t.lstrip('-')
# 'hello====='
t.strip('-=')
# 'hello'


# Discussion
# Be aware that stripping does not apply to the text in the middle of a string
s = '  hello     world   \n'
s = s.strip()
# 'hello     world'
s.replace(' ', '')
# 'helloworld'
import re
re.sub('\s+', ' ', s)
# 'hello world'

with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        ...

# the expression lines = (line.strip() for line in f) is efficient because it doesn't actually read
# the data into any kind of temporary list first. 
