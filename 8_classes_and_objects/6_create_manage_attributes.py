
import sys, pdb

class Person:
    def __init__(self, first_name):
        self.first_name = first_name
    
    # Getter function
    @property
    def first_name(self):
        return self._first_name
 
    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            pass
            # raise TypeError('Expected a string')
        self._first_name = value
 
    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        pass
        # raise AttributeError("Can't delete attribute")
        
# first name becomes a property
# access to it automatically triggers getter, setter, and deleter
# good for applying type checking
a = Person('Guido')
print(a.first_name) # Calls the getter
a.first_name = 42
del a.first_name

# Can be used for existing get and set methods too
class Person2:
    def __init__(self, first_name):
        self.set_first_name(first_name)
 
    # Getter function
    def get_first_name(self):
        return self._first_name
 
    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            pass
            # raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)

print(Person.first_name.fget)
print(Person.first_name.fset)
print(Person.first_name.fdel)

# Dont do this, waste of methods, too verbose
class Person3:
    def __init__(self, first_name):
        self.first_name = name
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        self._first_name = value

# can use property to create attributes that are not stored but computed on demand
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius ** 2
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(4.0)
print(c.radius)
print(c.area) # Notice lack of ()
print(c.perimeter)


p = Person2('Guido')
print(p.get_first_name())
p.set_first_name('Larry')

# dont write like this either with a lot of repetitive property definitions
class Person4:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name
 
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value
 

    # Repeated property code, but for a different name (bad!)
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._last_name = value
