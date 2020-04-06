from fractions import Fraction

# fractions module can be used for this math
a = Fraction(5,4)
b = Fraction(7,16)
print (a+b)
print (a*b)
c = a*b
# getting numerator / denomnator
print(c.numerator)
print(c.denominator)
# convert to float
print(float(c))
# reduce the fraction
print(c.limit_denominator(8))
x = 3.75
# integer to fraction
y = Fraction(*x.as_integer_ratio())
print(y)
