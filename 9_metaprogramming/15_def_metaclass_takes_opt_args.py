from abc import ABCMeta, abstractmethod

# A metaclass is a class whose instances are classes. Like an "ordinary" class 
# defines the behavior of the instances of the class, a metaclass defines the 
# behavior of classes and their instances.
# use the metaclass keyword to specify a metaclass
class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxsize=None):
        pass

    @abstractmethod
    def write(self, data):
        pass

# Can use other keywords in custom metaclasses
# class Spam(metaclass=MyMeta, debug=True, synchronize=True):


class MyMeta(type):
    # Optional
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        # Custom processing
 
        return super().__prepare__(name, bases)
 
    # Required
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
 
        return super().__new__(cls, name, bases, ns)
 
    # Required
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        super().__init__(name, bases, ns)

# another approach
class Spam(metaclass=MyMeta):
    debug = True
    synchronize = True