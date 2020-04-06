import math

# can make NaNs and infs with float
a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
print(b)
print(c)
# can use math module to test
print(math.isinf(a))
print(math.isnan(c))
a = float('inf')
# certainly operations undefined
print(a/a)
b = float('-inf')
print(a + b)
c = float('nan')
# nans dont raise an exception
print(c + 23)
print(c/2)
print(math.sqrt(c))
# NaN never compares as equal
c = float('nan')
d = float('nan')
print(c == d)
print(c is d)