import types
from functools import wraps

# Profiled Decorator
class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0
 
    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)
 
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

@Profiled
def add(x, y):
    return x + y

class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)

print(add(2,3))
print(add(4,5))
print(add.ncalls)
s = Spam()
s.bar(1)
s.bar(2)
s.bar(3)
print(Spam.bar.ncalls)

# If __get__ is not included, these calls will cause odd behavior
s = Spam()
s.bar(3)

# example of underlying mechanics of __get__ method
def grok(self, x):
    pass
print(grok.__get__(s,Spam))


# alternative formulation of the decorator using closures and nonlocal variables
import types
from functools import wraps

def profiled(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda: ncalls
    return wrapper

# Example
@profiled
def add(x, y):
    return x + y
    
print(add(2,3))
print(add(4,5))
print(add.ncalls())
