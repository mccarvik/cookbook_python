from collections import deque

# creates an instance with attributes (history) and methods (clear) that can be used
class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines,1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

# example of use
# with open('somefile.txt') as f:
#     lines = linehistory(f)
#     for line in lines:
#         if 'python' in line:
#             for lineno, hline in lines.history:
#                 print('{}:{}'.format(lineno, hline), end='')
#     print('{}:{}'.format(lineno, hline), end ='')

# will cause an error as linehistory is not an iter
# f = open('somefile.txt')
# lines = linehistory(f)
# next(lines)

# Call iter() first, then start iterating
# it = iter(lines)
# next(it)
# next(it)