
# can handle multiple exceptions in a tuple
try:
    client_obj.get_url(url)
except (URLError, ValueError, SocketTimeout):
    client_obj.remove_url(url)

# if one exception needs its own handling:
try:
    client_obj.get_url(url)
except (URLError, ValueError):
    client_obj.remove_url(url)
except SocketTimeout:
    client_obj.handle_url_timeout(url)

# can specify a base class to catch all the children of it
# for example, this...:
try:
    f = open(filename)
except (FileNotFoundError, PermissionError):
# ...could be written like this
try:
    f = open(filename)
except OSError:


# can get a handle on the thrown exception using "as":
try:
    f = open(filename)
except OSError as e:
    if e.errno == errno.ENOENT:
        logger.error('File not found')
    elif e.errno == errno.EACCES:
        logger.error('Permission denied')
    else:
        logger.error('Unexpected error: %d', e.errno)

# the exceptions will be evaluated in order, so first one caught executes
f = open('missing')
try:
    f = open('missing')
except OSError:
    print('It failed')
except FileNotFoundError:
    print('File not found')
