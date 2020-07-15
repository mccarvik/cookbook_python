
# to return multile vals simply return a tuple
def myfun():
    # comma actually makes the tuple not the parenthesis
    return 1,2,3


a,b,c = myfun()
print(a)
print(b)
print(c)
a = (1,2)
print(a)
b = 1,2
print(b)
x = myfun()
print(x)