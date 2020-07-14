import struct
from struct import Struct

def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))

# Example
if __name__ == '__main__':
    records = [ (1, 2.3, 4.5),
    (6, 7.8, 9.0),
    (12, 13.4, 56.7) ]
    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)


# Read the file incrementally in chunks
def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


# Example
# if __name__ == '__main__':
#     with open('data.b','rb') as f:
#         for rec in read_records('<idd', f):
#             # Process rec

# Unpack the records all at once
def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
        for offset in range(0, len(data), record_struct.size))

# Example
# if __name__ == '__main__':
#     with open('data.b', 'rb') as f:
#         data = f.read()
#     for rec in unpack_records('<idd', data):
#         # Process rec

# Little endian 32-bit integer, two double precision floats
# To declare a new struct
record_struct = Struct('<idd')
print(record_struct.size)

# pack and unpack data
aa = record_struct.pack(1, 2.0, 3.0)
print(record_struct.unpack(aa))

# called at module
print(struct.pack('<idd', 1, 2.0, 3.0))
print(struct.unpack('<idd', aa))

f = open('data.b', 'rb')
# repeatedly called until a specified value (b'') is returned and then iteration stops
chunks = iter(lambda: f.read(20), b'')
print(chunks)
for chk in chunks:
    print(chk)

# Would need to do this otherwise
def read_records2(format, f):
    record_struct = Struct(format)
    while True:
        chk = f.read(record_struct.size)
        if chk == b'':
            break
        yield record_struct.unpack(chk)
    return records

# If you use "unpack" instead of "unpack_from", would need to modify code to make
# a lot of small slices and offset calcs, like the following:
def unpack_records2(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack(data[offset:offset + record_struct.size])
            for offset in range(0, len(data), record_struct.size))

# Unpacking records is one place where you might want to use namedtuple to set
# attribute names on the returned tuples
from collections import namedtuple
Record = namedtuple('Record', ['kind','x','y'])

# with open('data.p', 'rb') as f:
#     records = (Record(*r) for r in read_records('<idd', f))
    
# for r in records:
#     print(r.kind, r.x, r.y)

# might be better off using numpy tho
import numpy as np
f = open('data.b', 'rb')
records = np.fromfile(f, dtype='<i,<d,<d')
print(records)