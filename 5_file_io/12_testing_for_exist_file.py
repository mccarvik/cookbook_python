import os
# check if path exists
print(os.path.exists('/etc/passwd'))
print(os.path.exists('/tmp/spam'))

# check if its a file
print(os.path.isfile('/etc/passwd'))

# check if its a directory
print(os.path.isdir('/etc/passwd'))

# check if its a symbolic link
print(os.path.islink('/usr/local/bin/python3'))

# get the file linked to
print(os.path.realpath('/usr/local/bin/python3'))

# can get the size or the last modification time
print(os.path.getsize('/etc/passwd'))
print(os.path.getmtime('/etc/passwd'))
import time
print(time.ctime(os.path.getmtime('/etc/passwd')))

# need to worry about potential permission issues
os.path.getsize('/Users/guido/Desktop/foo.txt')