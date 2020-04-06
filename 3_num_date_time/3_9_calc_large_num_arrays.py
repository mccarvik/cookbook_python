import numpy as np

# can use lists but not optimal
x = [1,2,3,4]
y = [5,6,7,8]
# concats, doesnt multiply
print(x * 2)
# error 
# print(x+10)
# again concats
print(x + y)

ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])
# desired mathematical output
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)

def f(x):
    return 3*x**2 - 2*x + 7
print(f(ax))
print(np.sqrt(ax))
print(np.cos(ax))
# can setup a grid of zeros
grid = np.zeros((1000,1000), dtype=float)
print(grid)
grid += 10
print(grid)
print(np.sin(grid))

# 2 dimensional array
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
# select row 1
print(a[1])
# select column 1
print(a[:,1])
# select a subregion
print(a[1:3, 1:3])
# edit the subregion
a[1:3, 1:3] += 10
print(a)
# broadcast a row vector on all rows
print(a + [100, 101, 102, 103])
print(a)
# add a conditional on the array
print(np.where(a < 10, a, 10))
print(a)