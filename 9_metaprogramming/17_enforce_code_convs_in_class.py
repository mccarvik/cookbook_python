
# basic metaclass inherit from type and redefines either __new__ or __init__
# __init__ --> invoked after a class has been created on each instance
# __new__ --> invoked prior to class creation, used when metaclass wants to alter class definition
class MyMeta(type):
    def __new__(self, clsname, bases, clsdict):
        # clsname is name of class being defined
        # bases is tuple of base classes
        # clsdict is class dictionary
        return super().__new__(cls, clsname, bases, clsdict)

class MyMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        # clsname is name of class being defined
        # bases is tuple of base classes
        # clsdict is class dictionary

    pass

# incorporate it into top-level base class
class Root(metaclass=MyMeta):
    pass

class A(Root):
    pass

class B(Root):
    pass


# Class that rejects any class definition with mixed-case names
class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, clsname, bases, clsdict)

class Root(metaclass=NoMixedCaseMeta):
    pass

class A(Root):
    def foo_bar(self): # Ok
        pass

# class B(Root):
#     def fooBar(self): # TypeError, mixed case not allowed
#         pass


from inspect import signature
import logging

# Checks for redefined classes to make sure they have the same signature as in the superclass
class MatchSignaturesMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(self, self)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            # Get the previous definition (if any) and compare the signatures
            prev_dfn = getattr(sup,name,None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning('Signature mismatch in %s. %s != %s',
                                value.__qualname__, prev_sig, val_sig)

# Example
class Root(metaclass=MatchSignaturesMeta):
    pass

class A(Root):
    def foo(self, x, y):
        pass
 
    def spam(self, x, *, z):
        pass

# Class with redefined methods, but slightly different signatures, will cause warning
class B(A):
    def foo(self, a, b):
        pass
    def spam(self,x,z):
        pass