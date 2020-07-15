
# Python 3
# Use the "*" to require user to input "block" by keyword and not positionally
def recv(maxsize,*, block):
    'Receive a message'
    pass
# recv(1024,True) # TypeError
recv(1024, block=True) # OK

#Python 3
def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(minimum(1,5,2,-5,10)) # -5
(minimum(1,5,2,-5,10,clip=0)) # 0

# easier to read the second function as user may not know what the False keyword means
msg = recv(1024, False)
msg = recv(1024, block = False)
print(help(recv))