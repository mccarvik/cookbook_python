
import importlib
# use importlib to import the module by string name
math = importlib.import_module('math')
print(math.sin(2))

mod = importlib.import_module('urllib.request')
u = mod.urlopen('http://www.python.org')
import importlib

# Same as 'from . import b'
b = importlib.import_module('.b', __package__)