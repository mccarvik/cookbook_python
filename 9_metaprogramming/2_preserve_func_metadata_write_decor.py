import time
from functools import wraps
def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    # VERY IMPORTANT TO INCLUDE THIS WRAPS DECORATOR
    # otherwise func info is lost
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
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)

# All of these would be lost or mutated if wraps wasnt included
countdown.__name__
countdown.__doc__
countdown.__annotations__
# wraps decorator also allows you to access the wrapped function directly like so
countdown.__wrapped__(100000)

# Also propery exposes the underlying signature of the wrapped function
from inspect import signature
print(signature(countdown))