import sys
import os

# get text encoding
print(sys.getfilesystemencoding())

# write a file using a unicode filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')

# Directory listing (decoded)
print(os.listdir('.'))

# Directory listing (raw)
print(os.listdir(b'.')) # Note: byte string

# Open file with raw filename
with open(b'jalapen\xcc\x83o.txt') as f:
    print(f.read())