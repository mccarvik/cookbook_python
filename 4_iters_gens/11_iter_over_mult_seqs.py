from itertools import zip_longest

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

# zip the lists than iter
for x, y in zip(xpts, ypts):
    print(x,y)

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']

# iteration stops whenever one of the sequences terminates
for i in zip(a,b):
    print(i)

# use ziplongest to go to the longest length list
for i in zip_longest(a,b):
    print(i)

# can add a custom fill value instead of None
for i in zip_longest(a, b, fillvalue=0):
    print(i)

a = [1, 2, 3]
b = [10, 11, 12]
c = ['x','y','z']

# can do 3 lists as well
for i in zip(a, b, c):
    print(i)

# zip creates an iterator
zip(a,b)
# use list to create a list
list(zip(a, b))