import re
import pdb
from collections import namedtuple

text = 'foo = 23 + 42 * 10'

tokens  = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
           ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
print(master_pat)

# Little known scanner function
# tokenizes the expression: subs in the token for the regex it finds
scanner = master_pat.scanner('foo = 42')
sc=scanner.match()
print(sc.lastgroup, sc.group())
sc=scanner.match()
print(sc.lastgroup, sc.group())
sc=scanner.match()
print(sc.lastgroup, sc.group())
sc=scanner.match()
print(sc.lastgroup, sc.group())
sc=scanner.match()
print(sc.lastgroup, sc.group())

Token = namedtuple('Token', ['type','value'])

# Generator function to find token matches
def generate_tokens(pat, text):
    # pdb.set_trace()
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

text = 'foo = 42'
# will ignore whitespace
tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')
for tok in tokens:
    print(tok)

LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'
# order matters, need to make sure the longer sequence is in the list first
# for example LE needs to be before LT
master_pat = re.compile('|'.join([LE, LT, EQ]))

PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
master_pat = re.compile('|'.join([PRINT, NAME]))
# need to watch out for patterns that form substrings
for tok in generate_tokens(master_pat, 'printer'):
    print(tok)