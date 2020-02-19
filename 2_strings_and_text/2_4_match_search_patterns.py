import re

# simple matching, use string functions
text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))

# For more complicated, use regular expressions
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

# Simple matchin: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# If you are gonna perform a lot of matches with the same pattern
# pre compile the regular expression
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')
    
# If you wanna search for all occurrences use find all
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

# Common to introduce regex in parenthesis, to create capture groups
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
# Contents of each group can be extracted individually
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
print(text)
print(datepat.findall(text))
for month,day,year in datepat.findall(text):
    print('{}-{}-{}'.format(year,month,day))

# Find matches iteratively: use find_iter
for m in datepat.finditer(text):
    print(m.groups())
    
# might match things you arent expecting
m = datepat.match('11/27/2012abcdef')
print(m.group())
# want an exact match, use the $ marker
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat.match('11/27/2012abcdef'))
print(datepat.match('11/27/2012'))

# for simple matches, can skip the compilation step:
print(re.findall(r'(\d+)/(\d+)/(\d+)', text))
