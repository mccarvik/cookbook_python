# open a file and overwrite it if it exists
with open('somefile', 'wt') as f:
    f.write('Hello\n')

# open a file only if it doesnt exist
# use xb instead of xt if the file is in binary mode
with open('somefile', 'xt') as f:
    f.write('Hello\n')

import os
# can first test for it and then write also
if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')