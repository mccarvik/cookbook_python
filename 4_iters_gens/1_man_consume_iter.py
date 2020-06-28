from __future__ import print_function

# manually catches the StopIteration Exception
with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

# list
items = [1,2,3]
# get the iterator
it = iter(items)
print(next(it))
print(next(it))
print(next(it))
# error, nothing left in list
next(it)