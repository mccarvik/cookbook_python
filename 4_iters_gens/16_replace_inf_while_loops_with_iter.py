
CHUNKSIZE = 8192
# checking for end of file
def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)

# Can do the same check with iter
def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(data)

import sys
# example solution
f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)