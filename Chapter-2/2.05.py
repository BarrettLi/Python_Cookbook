# Problem: You want to search for and replace a text pattern in a string

# for a simple literal patterns, use the str.replace() method
text = 'yeah, but no, but yeah, but no, but yeah'
text.replace('yeah', 'yeh')
# yep, but no, but yep, but no, but yep'

# for more complicated patterns, use sub() methods in the re module
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'

# if you want to perform repeated substitutions of the same pattern
import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2', text)

# for more complicated substitutions, it's possible to specify a substiturion callback function
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {'.format((.groupp(2), mon_name, m.group(3))

datepat.sub(change_date, text)
# 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'

# if you want to know how many substitutions are made
newtext, n = datepat.subn(r'\3-\1-\2', text)
newtext # 'Today is 2012-11-27. PyCon starts 2013-3-13.'
n # 2
