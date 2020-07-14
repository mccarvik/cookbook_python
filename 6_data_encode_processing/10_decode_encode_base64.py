# Some byte data
s = b'hello'
import base64

# Encode as Base64
a = base64.b64encode(s)
print(a)

# Decode from Base64
print(base64.b64decode(a))
a = base64.b64encode(s).decode('ascii')
print(a)
