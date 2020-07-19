
# Wrapped attribute can get you back the original function
# @somedecorator
# def add(x, y):
#     return x + y

# orig_add = add.__wrapped__
# print(orig_add(3, 4))

from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

# undefined what will happen if you call wraps on multiple decorators
# currently goes past all the layers down to the unwrapped function
@decorator1
@decorator2
def add(x, y):
    return x + y

print(add(2, 3))
print(add.__wrapped__(2, 3))
