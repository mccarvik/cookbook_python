# mymodule.py

class A:
    def spam(self):
        print('A.spam')

class B(A):
    def bar(self):
        print('B.bar')

# a.py
class A:
    def spam(self):
        print('A.spam')

# b.py
from .a import A
class B(A):
    def bar(self):
        print('B.bar')

# __init__.py
# glue the files together
from .a import A
from .b import B

# example use
import mymodule
a = mymodule.A()
a.spam()

b = mymodule.B()
b.bar()


# lotta import statements
from mymodule.a import A
from mymodule.b import B
# or single import
from mymodule import A, B



# __init__.py
# slight variation, functions load the desired classes
def A():
    from .a import A
    return A()

def B():
    from .b import B
    return B()

import mymodule
# function loads the class
a = mymodule.A()
a.spam()

# potential downside, type checking might break
if isinstance(x, mymodule.A): # Error
if isinstance(x, mymodule.a.A): # Ok
