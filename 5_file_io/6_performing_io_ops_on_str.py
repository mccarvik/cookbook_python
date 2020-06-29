import io, pdb

# Use StringIO and BytesIO when you need to mimic a normal file, ex: unit test

# create a file / string like object
s = io.StringIO()
s.write('Hello World\n')
# write more to the StringIO object
print('This is a test', file=s)
# get all the data written so far
print(s.getvalue())

# Wrap a file interface around an existing string
s = io.StringIO(u'Hello\nWorld\n')
print(s.read(4))
print(s.read())

# use BytesIO when working with binary data
s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())
