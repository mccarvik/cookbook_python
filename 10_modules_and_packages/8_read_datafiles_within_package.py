# directory structure
mypackage/
    __init__.py
    somedata.dat
    spam.py

# spam.py
import pkgutil
data = pkgutil.get_data(__package__, 'somedata.dat')
# resulting variable will be a byte strng containing the raw contents of the file