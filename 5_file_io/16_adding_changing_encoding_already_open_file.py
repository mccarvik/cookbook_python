import urllib.request
import io
import sys

# add encoding / decoding to already open file in binary mode, wrap with TextIOWrapper
u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u,encoding='utf-8')
text = f.read()

# change the encoding of an already open textmode file --> use detach
print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding)

# I/O system is a series of layers, example:
f = open('sample.txt','w')
print(f)
print(f.buffer)
print(f.buffer.raw)

# this will cause an error as the underlying file gets closed in the process
f = io.TextIOWrapper(f.buffer, encoding='latin-1')
print(f)
# error
# f.write('Hello')

# detach() method disconnects the topmost layer of a file
f = open('sample.txt', 'w')
print(f)
b = f.detach()
print(b)
# error as layer is disconnected
# f.write('hello')

# once detached a new top layer can be added
f = io.TextIOWrapper(b, encoding='latin-1')
print(f)

# can use this technique to edit other aspects of file handling
# example of encoding changed to ascii
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii',
                errors='xmlcharrefreplace')
print('Jalape\u00f1o')