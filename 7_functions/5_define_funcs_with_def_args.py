
# b defaults to 42
def spam(a, b=42):
    print(a,b)

print(spam(1))
print(spam(1,2))

# define a mutable object with None like this:
def spam2(a, b=None):
    if b is None:
        b = []
        
# check if value was given an interesting value or not
_no_value = object()
def spam3(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
print(spam(3))
print(spam(1,2))
# difference between providing no value and providing "None"
print(spam(1, None))

x = 42
def spam(a, b=x):
    print(a,b)
print(spam(1))

# changing x has no effect
x = 23
print(spam(1))

# never write code like this:
# def spam(a, b=[]):

# only use immutable objects becuase mutable objects can escape the function and
# get mutated
def spam(a, b=[]):
    print(b)
    return(b)
x = spam(1)
print(x)
x.append(99)
x.append('Yow!')
print(x)
# probably not what you want
print(spam(1))

# DOnt do this, use "is None" instead of "not" as [] can satisfy "not" as well as others 
def spam(a, b=None):
    if not b:
        b = []
print(spam(1))
x=[]
print(spam(1,x)) # x value overwritten when it shouldnt have been
print(spam(1,0)) # 0 ignored
print(spam(1,'')) # '' ignored
