# Read the entire file as a single byte string
# with open('somefile.bin', 'rb') as f:
#     data = f.read()

# Write binary data to a file
# with open('somefile.bin', 'wb') as f:
#      f.write(b'Hello World')

# Text string
t = 'Hello World'
print(t[0])
# prints out the characters
for i in t:
    print(i)

b = b'Hello World'
print(b[0])
# prints out the byte value
for c in b:
    print(c)

# decode when reading from a byte file
# with open('somefile.bin', 'rb') as f:
#     data = f.read(16)
#     text = data.decode('utf-8')
    
# encode when writing to a byte file
# with open('somefile.bin', 'wb') as f:
#     text = 'Hello World'
#     f.write(text.encode('utf-8'))

# Can write arrays and C tructures without any conversion
import array
nums = array.array('i', [1, 2, 3, 4])
with open('data.bin','wb') as f:
    f.write(nums)

# can be read into these structures with any conversion as well
import array
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)
print(a)