import sys

# potentially annoying problem of filenames not being encrypted by the file system default encoding
def bad_filename(filename):
    return repr(filename)[1:-1]

# example use of custom function
# try:
#     print(filename)
# except UnicodeEncodeError:
#     print(bad_filename(filename))

import os
# example (need a bad filename to see the problemtic unicode translation)
files = os.listdir('.')
print(files)

# trying to print the problematic list will crash
for name in files:
    print(name)

# can use solution defined above
for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))

# another solution option: recoding the bad value in some way
def bad_filename2(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')

for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))