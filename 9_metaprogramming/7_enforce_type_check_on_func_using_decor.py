#@typeassert(int, int)
def add(x, y):
    return x + y

print(add(2, 3))
# print(add(2, 'hello')) # error, failed type check

from inspect import signature
from functools import wraps

# implementation of typeassert decorator
def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
 
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                            )
            return func(*args, **kwargs)
        return wrapper
    return decorate


# can be specified by position or keyword
@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)

print(spam(1, 2, 3))
print(spam(1, 'hello', 3))
# print(spam(1, 'hello', 'world')) # error, z is not a string

# taken from above, how to turn off type checkin
# def decorate(func):
#     # If in optimized mode, disable type checking
#     if not __debug__:
#         return func

from inspect import signature
def spam(x, y, z=42):
    pass

# signature import allows us to work with the signature of the function
sig = signature(spam)
print(sig)
print(sig.parameters)
print(sig.parameters['z'].name)
print(sig.parameters['z'].default)
print(sig.parameters['z'].kind)
# With bound types, can specify the types that are reuqired
bound_types = sig.bind_partial(int,z=int)
print(bound_types)
# Above used bind_partial for only part of the definition
# bound_types, does not allow for any missing paramters not to be bound
print(bound_types.arguments)
bound_values = sig.bind(1, 2, 3)
print(bound_values.arguments)

# how it is elegantly implemented
for name, value in bound_values.arguments.items():
    if name in bound_types.arguments:
        if not isinstance(value, bound_types.arguments[name]):
            raise TypeError()

# subtle aspect, binding doesnt apply to default values
# so items can be default to None even tho it is bound to be a list
@typeassert(int, list)
def bar(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
print(bar(2))
# print(bar(2,3)) # error, 3 must be list
