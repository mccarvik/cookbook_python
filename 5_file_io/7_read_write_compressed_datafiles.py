import bz2
import gzip

# compression pretty straightforward with bz2 and gzip modules
# gzip compression
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

# bz2 compression
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()

# gzip compression
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

# bz2 compression
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

# Can set the compression level manually
# higher compression = smaller file but worse performance and vice versa
# default level is 9
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

# gzip and bz2 can be layered on top of a file already opened in binary mode
f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()