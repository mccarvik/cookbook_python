"""
Unpacking elements of arbitrary length
"""
import pdb

# middle will accept an arbitrary amount of items
def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)

print(drop_first_last([1,2,3,4,5,6,11]))

# Unpacks as many numbers as are left as a list
record = ('Dave','dave@exmple.com','773-555-1212','847-555-1212')
name,email,*phone_numbers = record
print(name)
print(phone_numbers)

# Can be start of the list as well
# *trailing_qtrs, current_qtr = sales_record
# trailing_avg = sum(trailing_qtrs)/len(trailing_qtrs)
# return avg_comparison(trailing_avg,current_qtr)

*trailing, current = [10,8,7,1,9,5,10,3]
print(trailing)
print(current)

records = [
    ('foo', 1,2),
    ('bar','hello'),     
    ('foo',3,4),      
          ]

def do_foo(x,y):
    print('foo',x,y)
    
def do_bar(s):
    print('bar',s)

# helpful if we dont know how many args need to be passed
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# USeful when using the string split function and
# not knowing the number of elements resulting from the split
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

# Can use _ to hold all the throwaway variables
record = ('ACME', 50, 123.45, (12,18,2012))
name, *_, (*_,year) = record
print(name)
print(year)


# star unpacking similar to list splitting
items = [1,10,7,4,5,9]
head, *tail = items
print(head)
print(tail)

# recursive sum function taking advantage of star unpacking
def sum2(items):
    head, *tail = items
    return head + sum2(tail) if tail else head

print(sum2(items))
