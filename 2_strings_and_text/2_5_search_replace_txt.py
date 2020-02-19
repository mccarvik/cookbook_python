import re
from calendar import month_abbr

# replace one string with another, just use replace
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yes'))

# for mor complicated patterns, use sub function from re module
# backslased digits refer to capture groups
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

# for repeated substitutions, consider compiling it first
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

# for more complicated substitutions, specify a callback function
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print(datepat.sub(change_date, text))

# how many substitutions were made / what the replacement text was:
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)
