
from functools import wraps
import logging

# define arguments as parameters in decorator signature
def logged(level, name=None, message=None):
    '''
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    '''
 
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__
 
        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# Example use
# add or spam would have access to the parameters passed to logged
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


# # code like this...
# @decorator(x, y, z)
# def func(a, b):
#     pass

# # is equivalent to code like this...
# def func(a, b):
#     pass
# func = decorator(x, y, z)(func)