import threading

# lock critical parts of the code to prevent race conditions
class SharedCounter:
    '''
    A counter object that can be shared by multiple threads.
    '''
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()
 
    def incr(self,delta=1):
        '''
        Increment the counter with locking
        '''
        # only one thread is allowed to execute the block of code in the with statement
        with self._value_lock:
            self._value += delta
 
    def decr(self,delta=1):
        '''
        Decrement the counter with locking
        '''
        with self._value_lock:
            self._value -= delta

# older python code, locks explicitly acquired and released
class SharedCounter:
    '''
    A counter object that can be shared by multiple threads.
    '''

    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()
 
    def incr(self,delta=1):
        '''
        Increment the counter with locking
        '''
        self._value_lock.acquire()
        self._value += delta
        self._value_lock.release()
 
    def decr(self,delta=1):
        '''
        Decrement the counter with locking
        '''
        self._value_lock.acquire()
        self._value -= delta
        self._value_lock.release()



class SharedCounter:
    '''
    A counter object that can be shared by multiple threads.
    '''
    # RLock - lock that can be acquired multiple times by the same thread
    _lock = threading.RLock()
 
    def __init__(self, initial_value = 0):
        self._value = initial_value
 
    def incr(self,delta=1):
        '''
        Increment the counter with locking
        '''
        with SharedCounter._lock:
            self._value += delta
 
    def decr(self,delta=1):
        '''
        Decrement the counter with locking
        '''
        with SharedCounter._lock:
            self.incr(-delta)


from threading import Semaphore
import urllib.request
# Semaphores useful for signaling between threads
# At most, five threads allowed to run at once
_fetch_url_sema = Semaphore(5)

def fetch_url(url):
    with _fetch_url_sema:
        return urllib.request.urlopen(url)