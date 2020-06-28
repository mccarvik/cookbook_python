from collections import defaultdict

# enumerate keeps an index for each loop
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

# can start the count at a given number
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list,1):
    print(idx, val)

# will keep track of the line number of an error
def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))

# will keep track of what line a word appears on
# word_summary = defaultdict(list)
# with open('myfile.txt', 'r') as f:
#     lines = f.readlines()

# for idx, line in enumerate(lines):
#     # Create a list of words in current line
#     words = [w.strip().lower() for w in line.split()]
#     for word in words:
#         word_summary[word].append(idx)

# can write your own code to mimic enumerate like this:
# lineno = 1
# for line in f:
#  # Process line
#  ...
#     lineno += 1

# but usually more elegant to do it this way:
# for lineno, line in enumerate(f):
#  # Process line
# ...

data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
# Correct way to deal with tuples
for n, (x, y) in enumerate(data):
    print(n, (x,y))

# incorrect way to deal with tuples, will cause error
for n, x, y in enumerate(data):
    print(n, x, y)