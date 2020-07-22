import time
from contextlib import contextmanager

@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))

# Example use
with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1


@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working

items = [1, 2, 3]
with list_transaction(items) as working:
    working.append(4)
    working.append(5)
print(items)

try:
    with list_transaction(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError('oops')
except:
    pass
# notice effect of context manager, items does not have 6 or 7 until "with"
# statement successfully exits
print(items)


import time
# normally have to write __enter__ and __exit__ functions like below
# context manager does this for you
class timethis:
    def __init__(self, label):
        self.label = label
    def __enter__(self):
        self.start = time.time()
    def __exit__(self, exc_ty, exc_val, exc_tb):
        end = time.time()
        print('{}: {}'.format(self.label, end - self.start))