import os.path

# read the data from the file right into a buffer using "readinto"
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

# Write a sample file
with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')
buf = read_into_buffer('sample.bin')
print(buf)
buf[0:5] = b'Hallo'
print(buf)

# write the buffer back to an outfile
with open('newsample.bin', 'wb') as f:
    f.write(buf)

# readinto doesnt allocate memory, just fills it
# can read a binary file of equally sized recods like this
# record_size = 32 # Size of each record (adjust value)
# buf = bytearray(record_size)
# with open('somefile', 'rb') as f:
#     while True:
#         n = f.readinto(buf)
#         if n < record_size:
#             break
#     # Use the contents of buf

print(buf)
# will learn more about memory views in chapter 6
m1 = memoryview(buf)
m2 = m1[-5:]
print(m2)

m2[:] = b'WORLD'
print(buf)
