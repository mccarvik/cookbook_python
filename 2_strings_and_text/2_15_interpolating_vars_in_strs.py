import sys
import string

s = '{name} has {n} messages.'
print(s.format(name='Guido', n = 37))

# Can use format_map and vars to substitute variables into strings
name = 'Guido'
n = 37
print(s.format_map(vars()))

# vars() works with instances as well
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido',37)
print(s.format_map(vars(a)))

# format and format_map do not deal well with missing values
# print(s.format(name='Guido'))

# Can avoid this with a __missing__ method
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


del n # make sure n is undefined
print(s.format_map(safesub(vars())))

# Hide variable substitution
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

# And then use it thru out your script
name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))

# Can use string template 
name = 'Guido'
n = 37
# print('%(name) has %(n) messages.'.format(vars()))
s = string.Template('$name has $n messages.')
print(s.substitute(vars()))
