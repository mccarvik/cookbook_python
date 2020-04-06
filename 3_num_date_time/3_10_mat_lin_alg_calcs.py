import numpy as np
import numpy.linalg

m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print(m)
# transpose
print(m.T)
# inverse
print(m.I)
# create a vector and multiply
v = np.matrix([[2],[3],[4]])
print(v)
print(m*v)
# determinant and eigenvals
print(np.linalg.det(m))
print(numpy.linalg.eigvals(m))
x = numpy.linalg.solve(m,v)
print(x)
print(m*x)
print(v)