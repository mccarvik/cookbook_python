import re

# bytes have some of the same built in functions 
data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

# also work with byte arrays
data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

# can apply regex but patterns need to be specified
data = b'FOO:BAR,SPAM'
# re.split('[:,]',data)
print(re.split(b'[:,]',data))
a = 'Hello World' # Text string
print(a[0])
print(a[1])
b = b'Hello World' 

# produces integers not chars
print(b[0])
print(b[1])
# need to decode when printed out
s = b'Hello World'
print(s)
print(s.decode('ascii'))