import re

# strip, strips from beginning and end of string
# lstrip and rstrip remove whitespace from left and right respectively
s = '   hello world  \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# Strip individual character
t = '-----hello====='
print(t.strip('-'))
print(t.strip("-="))

# Does not strip middle of string
s = '   hello          world     \n'
s = s.strip()
print(s)
# Need to use replace or regex
print(s.replace(' ',''))
print(re.sub('\s+', ' ', s))

# example of how to do it through a file read
# with open(filename) as f:
#     lines = (line.strip() for line in f)
#     for line in lines: