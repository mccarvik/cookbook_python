
# custom exceptions
class NetworkError(Exception):
    pass

class HostnameError(NetworkError):
    pass

class TimeoutError(NetworkError):
    pass

class ProtocolError(NetworkError):
    pass

# and then users use it in the normal way:
try:
    msg = s.recv()
except TimeoutError as e:
    pass     
except ProtocolError as e:
    pass

# catch a narrowly specified error like so:
try:
    s.send(msg)
except ProtocolError:
    pass

# or catch a broad range of errors
try:
    s.send(msg)
except NetworkError:
    pass


# Custom error, always call Exception.__init__ 
class CustomError(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status

# Any number of arguments can be passed in
try:
    raise RuntimeError('It failed')
except RuntimeError as e:
    print(e.args)
try:
    raise RuntimeError('It failed', 42, 'spam')
except RuntimeError as e:
    print(e.args)
