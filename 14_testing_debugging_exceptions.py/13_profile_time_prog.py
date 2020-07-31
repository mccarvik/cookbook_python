# timethis.py
import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper


# use decorator to time runtime
@timethis
def countdown(n):
    while n > 0:
        n -= 1
countdown(10000000)


from contextlib import contextmanager

# to time a block of statements, can use a context manager
@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{} : {}'.format(label, end - start))

with timeblock('counting'):
    n = 10000000
    while n > 0:
        n -= 1

# for small code fragments:
from timeit import timeit
print(timeit('math.sqrt(2)', 'import math'))
print(timeit('sqrt(2)', 'from math import sqrt'))
print(timeit('math.sqrt(2)', 'import math', number=10000000))
print(timeit('sqrt(2)', 'from math import sqrt', number=10000000))

# if you are interested in process time vs. wall clock time, use this:
from functools import wraps
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.process_time()
        r = func(*args, **kwargs)
        # process_time()
        end = time.process_time()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper
