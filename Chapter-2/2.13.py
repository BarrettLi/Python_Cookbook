# Problem: You need to format text with some sort of alignment applied

# Solution: ljust(), rjust(), center()

text = 'Hello World'
print(text.ljust(20))
# 'Hello World '
print(text.rjust(20))
# ' Hello World'
print(text.center(20))
# ' Hello World '

text.rjust(20, '=')
# '=========Hello World'
text.center(20, '*')
# '****Hello World*****'


# format() function can also be used to easily align things
format(text, '>20')
# ' Hello World'
format(text, '<20')
# 'Hello World '
format(text, '^20')
# ' Hello World '

format(text, '=>20s')
# '=========Hello World'
format(text, '*^20s')
# '****Hello World*****'

# these format codes can also be used in the format() method when formatting multiple values
'{:>10s} {:>10s}'.format('Hello', 'World')
# '     Hello      World'


# format() works with any value, making it more general purpose
x = 1.2345
format(x, '>10')
# '     1.2345'
format(x, '^10.2f')
# '   1.23   '

# Discussion
# in older code, you will also see the % operator used to format text
'%-20s' % text
# 'Hello World         '
'%20s' % text
# '         Hello World'

