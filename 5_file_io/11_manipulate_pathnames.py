
import os
path = '/Users/beazley/Data/data.csv'

# Get the last component of the path
print(os.path.basename(path))


# Get the directory name
print(os.path.dirname(path))

# Join path components together
print(os.path.join('tmp', 'data', os.path.basename(path)))

# Expand the user's home directory
path = '~/Data/data.csv'
print(os.path.expanduser(path))

# Split the file extension
print(os.path.splitext(path))