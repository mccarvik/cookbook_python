from itertools import compress
import math

# filtering use list comprehension 
mylist = [1,4,-5,10,-7,2,3,-1]
print([n for n in mylist if n>0])
print([n for n in mylist if n<0])

# Using a generator expression
pos = (n for n in mylist if n > 0)
print(pos)
for i in pos:
    print(i)


values = ['1','2','-3','-','4','N/A','5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
# using the builtin filter function
ivals = list(filter(is_int,values))
print(ivals)

# manipulate the values in the list comprehension
mylist = [1,4,-5,10,-7,2,3,-1]
print([math.sqrt(n) for n in mylist if n>0])

# can replace values as well
clip_neg = [n if n>0 else 0 for n in mylist]
print(clip_neg)
clip_pos = [n if n<0 else 0 for n in mylist]
print(clip_pos)

addresses = [
 '5412 N CLARK',
 '5148 N CLARK',
 '5800 E 58TH',
 '2122 N CLARK'
 '5645 N RAVENSWOOD',
 '1060 W ADDISON',
 '4801 N BROADWAY',
 '1039 W GRANVILLE',
]

# use the compress function from itertools to map the list of bools onto the
# list of addresses
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n>5 for n in counts]
print(more5)
print(list(compress(addresses,more5)))