import re

line = 'asdf fjdk; afed, fjek,asdf,       foo'
# can specify multiple patterns to split
print(re.split(r'[;,\s]\s*',line))

# can by mistake save the split characters
fields = re.split(r'(;|,|\s)\s*',line)
print(fields)

# Can be useful if you actually need the split characters
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

# reform the line using the same delimiters
print(''.join(v+d for v,d in zip(values,delimiters)))

# dont want seperator characters in result but still need to use parantheses
# to group parts of the regular expression
print(re.split(r'(?:,|;|\s)\s*',line)))
