
# custom generator pattern, increment start and stop all customized
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0,4,0.5):
    print(n)
    
print(list(frange(0,1,0.125)))

# presence of a yield statement, makes it a generator
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

# create generator
c = countdown(3)
print(c)
# cycle thru
print(next(c))
print(next(c))
print(next(c))
# StopIteration Exception
print(next(c))