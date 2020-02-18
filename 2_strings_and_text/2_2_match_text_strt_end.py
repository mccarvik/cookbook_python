import os
import re
from urllib.request import urlopen

# startswith and endswith helpful functions
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))

# Can just provide a tuple if multiple options of possibilities
filename = os.listdir('.')
print(filename)
print([name for name in filename if name.endswith('py')])
print(any(name.endswith('ipynb') for name in filename))

# Another example
def read_data(name):
    if name.startswith(('http:', 'https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices = ['http:','ftp:']
url = 'http://www.python.org'
# Oddly must be a tuple
if False:
    url.startswith(choices)
print(url.startswith(tuple(choices)))

# Very inelegant solution with slices
filename = 'spam.txt'
print(filename[-4:] == '.txt')

url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4]=='ftp:')

# regular expressions often overkill
url = 'http://www.python.org'
print(bool(re.match('http:|https:|ftp:', url)))
