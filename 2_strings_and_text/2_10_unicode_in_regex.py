import re

# \d matches any unicode digit character
num = re.compile('\d+')
print(num.match('123'))

# Arabic digits
print(num.match('u\u0661\u0662\u0663'))

# Matches all charactes in a few different Arabic code pages
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
print(arabic)

# Case matching can get messy with unicode
pat = re.compile(u'stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s)) # matches
pat.match(s.upper()) # doesnt match
print(s.upper()) # case folds causes new word