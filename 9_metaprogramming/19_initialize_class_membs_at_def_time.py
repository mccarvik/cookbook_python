import operator

class StructTupleMeta(type):
    # this is only called once for each class that is defined
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # takes attributes from _fields and turns them into property methods
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))

class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls,args)

# allows tuple based structures to be decided like this
class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']

class Point(StructTuple):
    _fields = ['x', 'y']

s = Stock('ACME', 50, 91.1)
print(s)
print(s[0])
print(s.name)
print(s.shares * s.price)
# s.shares = 23 # error, cant set attribute
s = Stock('ACME', 50, 91.1) # OK
# s = Stock(('ACME', 50, 91.1)) # Error, treats args as one tuple arg
