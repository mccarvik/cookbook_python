
# goes to nearest even whole number
print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27,1))
print(round(1.25361, 3))
a = 1627731
# can be negative to go to tens, hundreds, etc
print(round(a, -1))
print(round(a,-2))
print(round(a,-3))
x = 1.23456
# format can be used to truncate, not round decimal places
print(format(x, '0.2f'))
print(format(x, '0.3f'))
print('value is {:0.3f}'.format(x))
# dont do the below to "fix" rounding errors, usually unnecessary
a = 2.1
b = 4.2
c = a + b
print(c)
c = round(c,2)
print(c)