import time
from functools import wraps

# A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return r
    return wrapper


# Class illustrating application of the decorator to different kinds of methods
class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1
    
    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1
 
    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1

s = Spam()
s.instance_method(1000000)
Spam.class_method(1000000)
Spam.static_method(1000000)

class Spam:
    @timethis
    @staticmethod
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1
# this will cause an error, order is wrong, timethis must be first
# classmethod and staticmethod dont actually create callable objects
# Spam.static_method(1000000)

from abc import ABCMeta, abstractmethod
class A(metaclass=ABCMeta):
    # another example, abstract base class must be the first wrapper
    @classmethod
    @abstractmethod
    def method(cls):
        pass