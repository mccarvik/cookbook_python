
# change the string representation by changing the __repr__ and __str__ methods
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3, 4)
p # where __repr__ comes in
print(p)

p = Pair(3,4)
# !r will also call __repr__
print('p is {0!r}'.format(p))
print('p is {0}'.format(p))

f = open('file.dat')
print(f)


def __repr__(self):
    return 'Pair({0.x!r}, {0.y!r})'.format(self)

def __repr__(self):
    return 'Pair(%r, %r)' % (self.x, self.y)