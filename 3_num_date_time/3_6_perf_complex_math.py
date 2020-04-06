import math
import cmath
import numpy as np

# use "complex" to specify or just use "j"
a = complex(2,4)
b = 3 - 5j
print(a)
print(b)
# obtain real, imaginary and conjugate values
print(a.real)
print(a.imag)
print(a.conjugate())
# use 
print(a + b)
print(a*b)
print(a/b)
print(abs(a))

# use cmath to do complex math calcs
print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

# numpy has no problem with complex numbers
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(a + 2)
print(np.sin(a))

# standard math module has issues
print(math.sqrt(-1))
# just use cmath
print(cmath.sqrt(-1))