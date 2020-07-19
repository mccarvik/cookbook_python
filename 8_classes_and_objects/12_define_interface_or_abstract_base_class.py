# ABC = abstract base class
from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass
    @abstractmethod
    def write(self, data):
        pass

# abstract class, cant be instantiated directly, will cause error
# a = IStream()

# IStream used as a base class to be inherited, ex:
class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass 
    def write(self, data):
        pass

# code that explicitly checks for the interface
def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')


import io
# Register the built-in I/O classes as supporting our interface
IStream.register(io.IOBase)

# Open a normal file and type check
f = open('foo.txt')
print(isinstance(f, IStream))

# need to use abstract method decorator in proper sequence as shown below
class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass
    
    @name.setter
    @abstractmethod
    def name(self, value):
        pass
    
    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass


import collections
# can use predefined ABCs from collections module for type checking
# Check if x is a sequence
x=0
if isinstance(x, collections.Sequence):
    pass
# Check if x is iterable
if isinstance(x, collections.Iterable):
    pass
# Check if x has a size
if isinstance(x, collections.Sized):
    pass
# Check if x is a mapping
if isinstance(x, collections.Mapping):
    pass

from decimal import Decimal
import numbers

x = Decimal('3.4')
# returns False, certain library modules dont make use of these predefined ABCs
print(isinstance(x, numbers.Real))
