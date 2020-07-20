import collections
# stock.py
# Example of making a class manually from parts
# Methods
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

cls_dict = {
 '__init__' : __init__,
 'cost' : cost,
}

# Make a class using types.new_class
import types
Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__
# this completes making a normal class that acts as you would expect
s = Stock('ACME', 50, 91.1)
print(s)
print(s.cost())

import abc
Stock = types.new_class('Stock', (), {'metaclass': abc.ABCMeta},
                         lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__
print(Stock)
print(type(Stock))

# third argument can also contain other keyword arguments:
# class Spam(Base, debug=True, typecheck=False):
# and this would translate to a new_class() call:
# Spam = types.new_class('Spam', (Base,),
#                       {'debug': True, 'typecheck': False},
#                         lambda ns: ns.update(cls_dict))


# NamedTuple creates a class, uses exec() instead of the technique shown here
Stock = collections.namedtuple('Stock', ['name', 'shares', 'price'])
print(Stock)

# Simple variant that creates a class directly
import operator
import types
import sys

def named_tuple(classname, fieldnames):
    # Populate a dictionary of field property accessors
    cls_dict = { name: property(operator.itemgetter(n))
                 for n, name in enumerate(fieldnames) }
 
    # Make a __new__ function and add to the class dict
    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__
 
    # Make the class
    cls = types.new_class(classname, (tuple,), {},
                          lambda ns: ns.update(cls_dict))
 
    # Set the module to that of the caller
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls

Point = named_tuple('Point', ['x', 'y'])
print(Point)
p = Point(4, 5)
print(len(p))
print(p.x)
print(p.y)
# p.x = 2 # error, cant set attribute

# might be tempted to create a class like this:
Stock = type('Stock', (), cls_dict)
# skips critical steps tho, like calling __prepare__

# can carry out the prepare step like so
metaclass, kwargs, ns = types.prepare_class('Stock', (), {'metaclass': type})
