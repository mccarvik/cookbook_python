import os

x = 1234
# use bin, hex, oct
print(bin(x))
print(oct(x))
print(hex(x))
# use format to remove the 0x in the front, etc
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))
x = -1234
# integers will include the sign
print(format(x, 'b'))
print(format(x,'x'))
x = -1234
# need to add in the maximum value (2**32) to make it unsigned
print(format(2**32 + x, 'b'))
print(format(2**32 + x, 'x'))
# use int to convert it back
print(int('4d2', 16))
print(int('10011010010', 2))

# will get syntx error
# os.chmod('script.py', 0755)
# need the 0o
os.chmod('script.py', 0o755)