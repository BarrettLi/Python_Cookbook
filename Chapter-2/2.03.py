# Problem: You want to match text using the same wildcard patterns as are commonly used when
# woking in Unix shells (e.g., *.py, Dat[0-9]*.csv, etc.)

from fnmatch import fnmatch, fnmatchcase
fnmatch('foo.txt', '*.txt') # True
fnmatch('foo.txt', '?oo.txt') # True
fnmatch('Dat45.csv', 'Dat[0-9]*') # True
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
[name for name in names if fnmatch(name, 'Dat*.csv')] # ['Dat1.csv', 'Dat2.csv']

# case-sensitivity
# on OS X
fnmatch('foo.txt', '*.TXT') # False
# on windows
fnmatch('foo.txt', '*.TXT') # True

# if it matters, use fnmatchcase() which matches exactly based on the lower- and uppercase
# conventions
fnmatchcase('foo.txt', '*.XT') # False

# for nonfilename strings
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

from fnmatch import fnmatchcase
[addr for addr in addresses if fnmatchcase(addr, '* ST')]
# outputs ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
[addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
# outputs ['5412 N CLARK ST']
