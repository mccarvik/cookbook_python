import pdb
from itertools import dropwhile, islice

# cycles thru all of it
# with open('/etc/passwd') as f:
#     for line in f:
#         print(line, end='')

# can pass dropwhile a filter function along with an iterable to skip lines
# will skip all lines until function is true and then return the rest
# with open('/etc/passwd') as f:
#     for line in dropwhile(lambda line: line.startswith('#'), f):
#         print(line, end='')

# Can use is slice to skip front items as well
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

# messy function not using islice or dropwhile
with open('/etc/passwd') as f:
    # Skip over initial comments
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break
    # Process remaining lines
    while line:
        # Replace with useful processing
        print(line, end='')
        line = next(f, None)

with open('/etc/passwd') as f:
    # will remove all lines that start with "#", not just lines in the front
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')