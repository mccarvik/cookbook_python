class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name
 
    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            pass
            # raise TypeError('Expected a string')
        self._name = value
 
    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")

# subclass that extends the name property with new functionality
class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name
 
    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)
 
    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)

s = SubPerson('Guido')
print(s.name)
s.name = 'Larry'
s.name = 42

# Only want to extend one of the methods:
class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name

class SubPerson(Person):
    @Person.name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

# Wont work, tries to edit all 3 methods (getter, setter, deleter) not just getter
# class SubPerson(Person):
#     @property # Doesn't work
#     def name(self):
#         print('Getting name')
#         return super().name

# s = SubPerson('Guido')

# Use this instead
class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name

s = SubPerson('Guido')
print(s.name)
s.name = 'Larry'
print(s.name)
s.name = 42

# The recipe can be used to extend a descriptor
# A descriptor
class String:
    def __init__(self, name):
        self.name = name
 
    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]
 
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value

        
# A class with a descriptor
class Person:
    name = String('name')
    def __init__(self, name):
        self.name = name

# Extending a descriptor with a property
class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name
 
    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)