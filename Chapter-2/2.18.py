# Problem: You have a string that you want to parse left to right into a stream of tokens.

# suppose you have a string of text such as this:
text = 'foo = 23 + 42 * 10'

# to do this kind of splitting, the first step is to define all of the possible tokens, including
# whitespace, by regular expression patterns using named capture groups such as this:
import re
NAME = r'?P<NAME>[a-zA-Z][a-zA-Z_0-9]*)'
NUM  = r'?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES= r'(?P<TIMES>\*)'
EQ   = r'("P<EQ>=)'
WS   = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
# the ?P<TOKENNAME> convention is used to assign a name to the pattern

# next, to tokenize, use the little-known scanner() method of pattern objects
scanner = master_pat.scanner('foo = 42')
scanner.match()
_.lastgroup, _.group() # ('NAME', 'foo')
scanner.match()
_.lastgroup, _.group() # ('WS', ' ')
scanner.match()
_.lastgroup, _.group() # ('EQ', '=')
scanner.match()
_.lastgroup, _.group() # ('WS', ' ')
scanner.match()
_.lastgroup, _.group() # ('NUM', '42')

# to take this technique and put it into code,
from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

# example use
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

# Produces output
# Token(type='NAME', value='foo')
# Token(type='WS', value=' ')
# Token(type='EQ', value='=')
# Token(type='WS', value=' ')
# Token(type='NUM', value='42')

# Discussion

# the order of tokens in the master regular expreesion also matters
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat = re.compile('|'.join([LE, LT, EQ]))  # Correct
# master_pat = re.compile('|'.join([LT, LE, EQ]))  # Incorrect


# last, but not least, you need to watch out for patterns that form substrings
PRINT = r'(P<PRINT>print)'
NAME  = r'(P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_pat = re.compile('|'.join([PRINT, NAME]))

for tok in generate_tokens(master_pat, 'printer'):
    print(tok)

# Outputs :
#  Token(type='PRINT', value='print')
#  Token(type='NAME', value='er')
