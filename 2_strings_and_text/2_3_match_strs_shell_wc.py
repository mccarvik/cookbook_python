from fnmatch import fnmatch, fnmatchcase

# matches using the same wildcard patterns used in unix shells
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv','Dat2.csv','config.ini','foo.py']
print([name for name in names if fnmatch(name,'Dat*.csv')])
print([name for name in names if not fnmatch(name,'*.py')])

# fnmatch usually uses the same case-sensitivity rules as the underlying OS
# On Windows True
print(fnmatch('foo.txt', '*.TXT'))

# It is false on Mac OS
print(fnmatch('foo.txt', '*.TXT'))

# If distinction matters use fnmatchcase
print(fnmatchcase('foo.txt','*.TXT'))

# can be used on non
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY'
]
print([addr for addr in addresses if fnmatchcase(addr,'* ST')])
print([addr for addr in addresses if fnmatchcase(addr,'54[0-9][0-9] *CLARK*')])
