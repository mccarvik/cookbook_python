from functools import wraps
def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

@optional_debug
def spam(a,b,c):
    print(a,b,c)

spam(1,2,3)
# can use keywords to inject new arguments wihtout affecting existing calls
spam(1,2,3, debug=True)

# If you have code like this...
def a(x, debug=False):
    if debug:
        print('Calling a')
        
def b(x, y, z, debug=False):
    if debug:
        print('Calling b')

def c(x, y, debug=False):
    if debug:
        print('Calling c')

# can refactor it into the following
@optional_debug
def a(x):
    pass
 
@optional_debug
def b(x, y, z):
    pass
 
@optional_debug
def c(x, y):
    pass


import inspect
def optional_debug(func):
    # check put in place in case debug argument was already there
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')
    
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

# signature is wrong tho, debug is missing
@optional_debug
def add(x,y):
    return x+y
print(inspect.signature(add))


# edit to correct signature
def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')
    
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)
 
    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug',
                                    inspect.Parameter.KEYWORD_ONLY,
                                    default=False))
 
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper
    
@optional_debug
def add(x,y):
    return x+y

# signature now has debug included
print(inspect.signature(add))
print(add(2,3))