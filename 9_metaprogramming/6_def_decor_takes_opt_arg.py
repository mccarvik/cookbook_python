from functools import wraps, partial
import logging

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    
    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)
    return wrapper

# Example use without args
@logged
def add(x, y):
    return x + y

# exampe use with args
@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')

# programmers usually dont add the parenthesis but this does work
@logged()
def add(x, y):
    return x+y

# Example use, this is equivalent...
@logged
def add(x, y):
    return x + y
# ... to doing this
def add(x, y):
    return x + y
add = logged(add)

# and this is quivalent...
@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')
# ... to doing this, NOTE: notice the double parenthesis on the bottom definition
def spam():
    print('Spam!')
spam = logged(level=logging.CRITICAL, name='example')(spam)
