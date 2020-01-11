# primitive multi dict
# multi-dict = a key maps to multiple values
d = {
    'a':[1,2,3],
    'b':[4,5]
}

e = {
    'a':{1,2,3},
    'b':{4,5}
}

for key, value in d.items():
    for i in value:
        print(key, i)
        
for key, value in e.items():
    for i in value:
        print(key, i)
        
# Can use defaultdict
from collections import defaultdict 

# NOTE, defaultdict will create keys accessed later on even if they arent currently in the dict)
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)
print(d)

# Can avoid the auto create issue if undesired by using setdefault
d = {}
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('a',[]).append(3)
d.setdefault('b',[]).append(4)
d.setdefault('b',[]).append(5)
print(d)

# Messy code for initialization
pairs = [
    ['a', 1],
    ['a', 2],
    ['a', 3],
    ['b', 4],
    ['b', 5]
]
d = {}
for key,value in pairs:
    print(key, value)
    if key not in d:
        d[key] = []
    d[key].append(value)
print(d)

# Little cleaner with defaultdict
d = {}
for key, value in pairs:
    d.setdefault(key,[]).append(value)
print(d)