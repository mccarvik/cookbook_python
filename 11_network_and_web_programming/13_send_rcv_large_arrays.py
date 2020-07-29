# zerocopy.py
# utilize memoryviews to send and receive large arrays
def send_from(arr, dest):
    view = memoryview(arr).cast('B')
    while len(view):
        nsent = dest.send(view)
        view = view[nsent:]

def recv_into(arr, source):
    view = memoryview(arr).cast('B')
    while len(view):
        nrecv = source.recv_into(view)
        view = view[nrecv:]

# to test program
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 25000))
s.listen(1)
c,a = s.accept()

# and then client (separate interpreter)
from socket import *
c = socket(AF_INET, SOCK_STREAM)
c.connect(('localhost', 25000))

# Example
# Server
import numpy
a = numpy.arange(0.0, 50000000.0)
send_from(a, c)
# Client
import numpy
a = numpy.zeros(shape=50000000, dtype=float)
print(a[0:10])
recv_into(a, c)
print(a[0:10])

# Takes an array and casts it into a memoryview
view = memoryview(arr).cast('B')
