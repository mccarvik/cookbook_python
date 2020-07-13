import json
import pdb

data = {
 'name' : 'ACME',
 'shares' : 100,
 'price' : 542.23
}

# json module, easy to use
# dumps puts it in str
json_str = json.dumps(data)
print(json_str)
# loads puts it back in object
data = json.loads(json_str)

# Writing JSON data, dump will encode it
with open('data.json', 'w') as f:
    json.dump(data, f)
    
# Reading data back, load will decode it
with open('data.json', 'r') as f:
    data = json.load(f)

# False mapped to 'false'
print(json.dumps(False))

d = {'a': True,
     'b': 'Hello',
     'c': None}
# None mapped to null
print(json.dumps(d))


from urllib.request import urlopen
from pprint import pprint

# u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
# resp = json.loads(u.read().decode('utf-8'))
# pprint alphabetizes and prints in more logical / readable fashion
pprint(data)

# can preserve objects type useing object_pairs_hook parameter
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)

# JSON Dict to Python Obj
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)
print(data.name)
print(data.shares)
print(data.price)

# indent argument makes it more readable
data = {
 'name' : 'ACME',
 'shares' : 100,
 'price' : 542.23
}
print(json.dumps(data))
print(json.dumps(data, indent=4))
# Can sort keys using parameter
print(json.dumps(data, sort_keys=True))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p = Point(2, 3)
# instances typically not serializble
# json.dumps(p)

# Can supply a function returning a serialized version
def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d

# Dictionary mapping names to known classes to get instances back
classes = {
 'Point' : Point
}

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d

p = Point(2,3)
s = json.dumps(p, default=serialize_instance)
print(s)
a = json.loads(s, object_hook=unserialize_object)
print(a)
print(a.x)
print(a.y)
