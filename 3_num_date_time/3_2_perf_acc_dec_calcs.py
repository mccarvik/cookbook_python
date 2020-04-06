import math
from decimal import Decimal 
from decimal import localcontext

a = 4.2
b = 2.1
print(a + b)
# error with floating pounts
print((a+b) == 6.3)

# sacrifices some performance, but more accurate
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
print((a + b) == Decimal('6.3'))

# can control the local context as well to decide dec places, etc
a = Decimal('1.3')
b = Decimal('1.7')
print(a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a/b)

# 1 gets ignored with such big numbers
nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))
# can be fixed with math module
print(math.fsum(nums))
