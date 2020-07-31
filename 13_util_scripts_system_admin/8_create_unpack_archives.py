
import shutil
shutil.unpack_archive('Python-3.3.0.tgz')
print(shutil.make_archive('py33','zip','Python-3.3.0'))

print(shutil.get_archive_formats())
