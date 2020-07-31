import shutil

# Copy src to dst. (cp src dst)
shutil.copy(src, dst)

# Copy files, but preserve metadata (cp -p src dst)
shutil.copy2(src, dst)

# Copy directory tree (cp -R src dst)
shutil.copytree(src, dst)

# Move src to dst (mv src dst)
shutil.move(src, dst)

# to copy the symbolic link instead
shutil.copy2(src, dst, follow_symlinks=False)

# to preserve symbolic links in copied directories
shutil.copytree(src, dst, symlinks=True)

# ignore pyc files
def ignore_pyc_files(dirname, filenames):
    return [name for name in filenames if name.endswith('.pyc')]
shutil.copytree(src, dst, ignore=ignore_pyc_files)

# ignore patterns
shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*~','*.pyc'))

filename = '/Users/guido/programs/spam.py'
import os.path
print(os.path.basename(filename))
print(os.path.dirname(filename))
print(os.path.split(filename))
print(os.path.join('/new/dir', os.path.basename(filename)))
print(os.path.expanduser('~/guido/programs/spam.py'))

try:
    shutil.copytree(src, dst)
except shutil.Error as e:
    for src, dst, msg in e.args[0]:
        # src is source name
        # dst is destination name
        # msg is error message from exception
        print(dst, src, msg)