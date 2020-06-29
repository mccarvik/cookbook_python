import pickle

# most common way to serialize in python is with pickle
data = ... # Some Python object
f = open('somefile', 'wb')
pickle.dump(data, f)

# to dump to string
s = pickle.dumps(data)
# Restore from a file
f = open('somefile', 'rb')
data = pickle.load(f)

# Restore from a string
data = pickle.loads(s)


f = open('somedata', 'wb')
pickle.dump([1, 2, 3, 4], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()
f = open('somedata', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))

import math
# can pickle functions, classes and instances too
print(pickle.dumps(math.cos))

import time, threading

# some items can't be pickled such as open files or sockets
# following code checks for these potential issues
class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)
 
    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)

c = Countdown(30)

# After a few moments
f = open('cstate.p', 'wb')
pickle.dump(c, f)
f.close()
# can try this in a few minutes and pick up where the countdown left off
f = open('cstate.p', 'rb')
pickle.load(f)