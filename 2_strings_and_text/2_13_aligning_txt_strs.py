
# adjusts the alignment of the string
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

# accept a fill character
print(text.rjust(20,'='))
print(text.center(20,'*'))

# can also use the format function to get similar results
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))

# Can specify a fill character with format as well
print(format(text, '=>20s'))
print(format(text, '*^20s'))

# format codes can be used for formatting multiple values
print('{:>10s}{:>10s}'.format('Hello','World'))

# format can be used with numbers as well
x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))

# can use % operator, but should probably avoid it, getting phased out
print('%-20s' % text)
print('%20s' % text)