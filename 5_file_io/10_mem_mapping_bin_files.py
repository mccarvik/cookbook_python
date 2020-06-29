import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

size = 1000000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

# m is "mapped" to the values of the file
# aka m is linked to the memory locations of the contents of the file
m = memory_map('data')
print(len(m))
print(m[0:10])
print(m[0])

# Reassign a slice
m[0:11] = b'Hello World'
m.close()

# Verify that changes were made
with open('data', 'rb') as f:
    print(f.read(11))

# another way to access the content
with memory_map('data') as m:
    print(len(m))
    print(m[0:10])
print(m.closed)

# can give only read access
# m = memory_map(filename, mmap.ACCESS_READ)
# can modify the data locally but no write the data back to the original file with ACCESS_COPY
# m = memory_map(filename, mmap.ACCESS_COPY)

m = memory_map('data')
# can interpret the data in a different format so as emoryview of unsigned integers
v = memoryview(m).cast('I')
v[0] = 7
print(m[0:4])
m[0:4] = b'\x07\x01\x00\x00'
print(v[0])