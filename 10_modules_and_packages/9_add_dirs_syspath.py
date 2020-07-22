# add paths to PYTHONPATH environrment variable from command line
bash % env PYTHONPATH=/some/dir:/other/dir python3
Python 3.3.0 (default, Oct 4 2012, 10:17:33)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin

import sys
# has all the paths
print(sys.path)

import sys
# can add to the path list like so
# try not to do this, fragile and easily broken
sys.path.insert(0, '/some/dir')
sys.path.insert(0, '/other/dir')

import sys
from os.path import abspath, join, dirname
sys.path.insert(0, abspath(dirname('__file__'), 'src'))