import time
from functools import wraps

# wraps a function and prints out the time it takes to run it
def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

countdown(100000)
countdown(10000000)

# These two code segments are equivalent
# @timethis
# def countdown(n):
    
# def countdown(n):
#     countdown = timethis(countdown)

# Same with these two code segments
class A:
    @classmethod
    def method(cls):
        pass

class B:
    # Equivalent definition of a class method
    def method(cls):
        pass
    method = classmethod(method)