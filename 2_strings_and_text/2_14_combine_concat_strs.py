
# Can use 'join' to link strings from a list
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

# '+' works well enough when its not a lot of strings
a = 'Is Chicago'
b = 'Not Chicagoo?'
print(a + ' ' + b)
print('{}{}'.format(a, b))
print(a + ' ' + b)

# Can just place string literals next to eachother to combine them
a = 'Hello' 'World'
print(a)

# extremely inefficient way of combining strings
s = ''
for p in parts:
    s += p
print(s)


# Can use generator expression to cast and then concat strings
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

# print(a + ':' + b + ':' + c) # ugly
# print(':'.join([a, b, c])) # still ugly
# print(a, b, c, sep=':') # better

# I/O operations vary in performance based on string size
# f.write(chunk1 + chunk2)
# f.write(chunk1)
# f.write(chunk2)

# Might want to write a generator function if you are building from lots of small strings
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'
text = ''.join(sample())
print(text)
# for part in sample():
#     f.write(part)

# hybrid scheme combining I/O operations
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)
    
# for part in combine(sample(), 32768):
#     f.write(part)