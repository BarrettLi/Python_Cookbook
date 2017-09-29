# Proble: You need to format a number for output, controlling the number of digits, alignment,
# inclusion of a thousands separator, and other details.

# to format a single number for output, use the built-in format() function
x = 1234.56789

# Two decimal places of accuracy
format(x, '0.2f') # '1234.57'
# Right justified in 10 chars, one-digit accurary
format(x, '>10.1f') # '    1234.6'
# Left justified
format(x, '<10.1f')
'1234.6    '
# Centered
format(x, '^10.1f') # '  1234.6  '
# Inclusion of thousands separator
format(x, ',') # '1,234,56789'
format(x, '0,.1f') # '1,234,6'

# if you want to use exponential notation, change the f to an e or E.
format(x, 'e') # '1.234568e+03'
format(x, 'E') # '1.234568E+03'

# the general form of the width and precision in both cases is '[<>^]?width[,]?(.digits)?' where
# width and digits are integers and ? signifies optional parts.
'The value is {:0,.2f}'.format(x) # 'The value is 1,234.57'

