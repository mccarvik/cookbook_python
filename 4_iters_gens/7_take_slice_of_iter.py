def count(n):
    while True:
        yield n
        n += 1

# error, count is a generator and is not subscriptable
c = count(0)
# c[10:20]

# Now using islice()
import itertools
# islice consumes the data it needs from the generator to get the info to create a slice
for x in itertools.islice(c, 10, 20):
    print(x)