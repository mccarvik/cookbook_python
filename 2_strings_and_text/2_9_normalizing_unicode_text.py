import unicodedata

# strings wont match
s1 = u'Spicy Jalape\u00f1o'
s2 = u'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s1 == s2)
print(len(s1))
print(len(s2))

# normalizes the text into standard representation
# NFC - characters should be fully composed
t1 = unicodedata.normalize('NFC',s1)
# NFD - characters should be fully decomposed using combining characters
t2 = unicodedata.normalize('NFD',s2)
print(t1 == t2)
print(ascii(t1))

t3 = unicodedata.normalize('NFD',s1)
t4 = unicodedata.normalize('NFD',s2)
print(t3 == t4)
print(ascii(t3))

s = u'\ufb01'
print(s)
t = unicodedata.normalize('NFD',s)
print(t)
# letters seperated
t = unicodedata.normalize('NFKD',s)
print(t)
t = unicodedata.normalize('NFKC',s)
print(t)

# removes all diacritical characters
t1 = unicodedata.normalize('NFD',s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
