import glob, os
import os.path
from fnmatch import fnmatch

names = os.listdir('./')

# Get all regular files
names = [name for name in os.listdir('./')
        if os.path.isfile(os.path.join('./', name))]

# Get all dirs
dirnames = [name for name in os.listdir('./')
            if os.path.isdir(os.path.join('./', name))]

# get all the python files
pyfiles = [name for name in os.listdir('./')
            if name.endswith('.py')]

# may want to use glob and fnmatch to for filename matching
pyfiles = glob.glob('./*.py')
pyfiles = [name for name in os.listdir('./')
             if fnmatch(name, '*.py')]

# Example of getting a directory listing
pyfiles = glob.glob('*.py')

# Get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]

for name, size, mtime in name_sz_date:
    print(name, size, mtime)

# Alternative: Get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)