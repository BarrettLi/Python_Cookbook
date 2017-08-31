# Problem: You need to split a string into fields, but the delimiters (and spacing around them)
# aren't consistent throughout the string.

line = 'asdf fjdk; afed, fjek,asdf,    foo'
import re
# the separator is either a comma(,), semicolon(;), or whitespace followed by any amount of
# extra whitesapce
re.split(r'[;,\s]\s*', line)
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# Discussion
# if capture groups are used, then the matched text is also included in the result.
fields = re.split(r'(;|,|\s)\s*', line)
fields # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

values = fields[::2]
delimiters = fields[1::2] + ['']
values # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
delimiters # [' ', ';', ',', ',', ',', '']

# reform the line using the same delimiters
'',join(v+d for v, d in zip(values, delimiters))
# 'asdf fjdk;afed,fjek,asdf,foo'

# if you don't want to separator characters in the result, but still need to use parentheses
# to group parts of the regular expression pattern

re.split(r'(?:,|;|\s)\s*', line)
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
