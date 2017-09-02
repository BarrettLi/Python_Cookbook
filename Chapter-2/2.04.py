# Problem: You want to match or search text for a specific pattern

# Solution: basic string methods, such as str.find(), str.endswith(), str.startswith()

text = 'yeah, but no, but yeah, but no, but yead'

# Exact match
text == 'yeah' # False

# Match at start or end
text.startswith('yeah') # True
text.endswith('no') # False

# Search for the location of the first occurrence
text.find('no') # 10

# For more complicated matching, use regex and the re module
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
# Simple matching: \d+ means match one or more digits
if re.match('\d+/\d+/\+d', text1):
    print('yes')
else:
    print('no')
# yes

if re.match('\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
# no

# for a lot of matches using the same pattern
datepat = re.compile('\d+/\d+/\d+')

if datepat.match(text1):
    print('yes')
else:
    print('no')
# yes


if datepat.match(text2):
    print('yes')
else:
    print('no')
# no

# if you want to find all occurrences of patterns, you want to use findall() instead of match() because
# match() method only matches at the start of a string
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.match(text)
# ['11/27/2012', '3/13/2013']


# Capture groups often simplify subsequwnt processing of the matched text because the contents of each
# group can be extracted individually
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
# Extract the contents of each group
m.group(0)
# '11/27/2012'
m.group(1)
# '11'
m.group(2)
# '27'
m.group(3)
# '2012'
m.groups()
# ('11', '27', '2012')

# Find all matches (notice splitting into tuples)
datepat.findall(text) # [('11', '27', '2012'), ('3', '13', '2013')]
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))
# outputs:
# 2012-11-27
# 2013-3-13

# if you want to find matches iteratively
for m in datepat.finditer(text):
    print(m.groups())
# outputs:
# ('11', '27', '2012')
# ('3', '13', '2013')

# Discussion

# match() method may also find matches that you don't expect
m = datepat.match('11/27/2012abcdef')
m.group()
# '11/27/2012'

# if you want an exact match, make sure the pattern includes the end-marker($)
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
datepat.match('11/27/2012abcdef') # do not match
datepat.match('11/27/2012') # match


