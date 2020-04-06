import struct

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
# use from_bytes to convert to int and specify byte ordering little / big
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))
x = 94522842520747284487117727783387188
# use to_bytes to convert from int and specify byte ordering little / big
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
# struct can help unpack but need to do it in pieces
hi, lo = struct.unpack('>QQ', data)
print((hi << 64) + lo)
x = 0x01020304
# little / big specifies whether the bytes are least most or least significant first
x.to_bytes(4, 'big')
x.to_bytes(4, 'little')
x = 523 ** 23
print(x)
# too big will give error
# x.to_bytes(16,'little')
# bit_length will tell you the max 
print(x.bit_length())
nbytes, rem = divmod(x.bit_length(),8)
if rem:
    nbytes += 1
print(x.to_bytes(nbytes, 'little'))