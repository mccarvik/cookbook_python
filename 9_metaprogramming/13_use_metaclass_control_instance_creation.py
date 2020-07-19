class Spam:
    def __init__(self, name):
        self.name = name

# normal class call creating instances
a = Spam('Guido')
b = Spam('Diana')

# can modify the __call__ method for when instantiation happens
# this will prevent any instances from being implemented
class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")

# Example
class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')

Spam.grok(42)
# s = Spam() # error, no instantiation allowed

# Singleton pattern - only one instance
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)
 
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

# Example
class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')

# all these instances are the same
a = Spam()
b = Spam()
c = Spam()
print(a is c)


import weakref

# how to create Cached Instances
class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()
 
    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj

# Example
class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name

a = Spam('Guido')
b = Spam('Diana')
c = Spam('Guido')
print(a is b)
# cached value returned
print(a is c)

# another approach to create singleton class, kind of hacky
class _Spam:
    def __init__(self):
        print('Creating Spam')

_spam_instance = None
def Spam():
    global _spam_instance
    if _spam_instance is not None:
        return _spam_instance
    else:
        _spam_instance = _Spam()
        return _spam_instance
