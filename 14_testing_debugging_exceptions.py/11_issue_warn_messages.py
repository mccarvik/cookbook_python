import warnings

# use warnings.warn
def func(x, y, logfile=None, debug=False):
    if logfile is not None:
        warnings.warn('logfile argument deprecated', DeprecationWarning)

# example - destroying a file without closing it
import warnings
warnings.simplefilter('always')
f = open('/etc/passwd')
del f
