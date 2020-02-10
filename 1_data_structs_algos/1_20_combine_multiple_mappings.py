from collections import ChainMap

# 2 dictionaries
a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

# will check a and then b
c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])

# not actually one dict, but most operations work:
print(len(c))
print(list(c.keys()))
print(list(c.values()))

# mutations always affect the first mapping first
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
if False:
    del c['y']

values = ChainMap()
values['x'] = 1
# adds a new mapping
values = values.new_child()
values['x'] = 2
# adds a new mapping
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
# Discard last mapping
values = values.parents
print(values['x'])
# Discard last mapping
values = values.parents
print(values['x'])
print(values)

# Can use 'update' method to merge dicts
a = {'x':1, 'z':3}
b = {'y':2, 'z':4}
merged = dict(b)
merged.update(a)
print(merged)
print(merged['x'])
print(merged['y'])
print(merged['z'])

# changes to original dict are not reflected in merged dict
a['x'] = 13
print(merged['x'])

# ChainMap doesnt have this issue
a = {'x':1,'z':3}
b = {'y':2,'z':4}
merged = ChainMap(a,b)
print(merged['x'])
a['x'] = 42
print(merged['x'])