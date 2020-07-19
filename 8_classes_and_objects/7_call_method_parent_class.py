class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        # Calls parent class (A)'s spam()
        super().spam()

class A:
    def __init__(self):
        self.x = 0
        
class B(A):
    def __init__(self):
        # initializes parent class
        super().__init__()
        self.y = 1

# super used to override any of pythons special methods 
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)
 
    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value) # Call original __setattr__
        else:
            setattr(self._obj, name, value)

class Base:
    def __init__(self):
        print('Base.__init__')

        
class A(Base):
    def __init__(self):
        # Althought this "works", dont do this. Causes problems with inheritance
        Base.__init__(self)
        print('A.__init__')

# In the following, Base.__init__() gets invoked twice
class Base:
    def __init__(self):
        print('Base.__init__')

        
class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')

        
class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')

        
class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')
c = C()

# If you change it to super, it all works
class Base:
    def __init__(self):
        print('Base.__init__')

    
class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')

        
class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

        
class C(A,B):
    def __init__(self):
        super().__init__() # Only one call to super() here
        print('C.__init__')
print(C.__mro__)


class A:
    def spam(self):
        print('A.spam')
        super().spam()
# completely broken
a = A()
# a.spam()

class B:
    def spam(self):
        print('B.spam')

class C(A,B):
    pass
# class A calls class B spam, you see why in the MRO
c = C()
c.spam()
print(C.__mro__)
