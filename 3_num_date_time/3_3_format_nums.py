
x = 1234.56789
# two decimal places
print(format(x, '0.2f'))
# right aligned
print(format(x, '>10.1f'))
# left aligned
print(format(x, '<10.1f'))
# centered
print(format(x, '^10.1f'))
# add thusands comma
print(format(x, '0,.1f'))
# exponential notation
print(format(x, 'e'))
# exponential to two decs
print(format(x, '0.2E'))
# format function
print('The value is {:0,.2f}'.format(x))
print(x)
# round
print(format(x, '0.1f'))
# round
print(format(-x, '0.1f'))
#Pyton 3
swap_separators = { ord('.'):',', ord(','):'.' }
# swap separators (diff language)
print(format(x, ',').translate(swap_separators))
# can still use % operator but should lean towards format
print('%0.2f' % x)
print('%10.1f' % x)
print('%-10.1f' % x)
