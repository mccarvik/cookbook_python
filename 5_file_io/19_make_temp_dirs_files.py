from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')
    
    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()
    # Temp file destroyed outside with

f = TemporaryFile('w+t')
# Use the temporary file
f.close()

# same arguments as builtin open function
# with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as f:
# ...

# Will give the temp file a name
from tempfile import NamedTemporaryFile
with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)

# wont delete file when it is closed
with NamedTemporaryFile('w+t', delete=False) as f:
    print('filename is:', f.name)

# making temp directory 
from tempfile import TemporaryDirectory
with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)

# makes tempfiles and directories at a lower level
import tempfile
print(tempfile.mkstemp())
print(tempfile.mkdtemp())
print(tempfile.gettempdir())
# can override prefix and suffix
f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
print(f.name)