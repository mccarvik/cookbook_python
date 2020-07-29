from queue import Queue
from threading import Thread
# Queue instance shared by thread
# A thread that produces data
def producer(out_q):
    while True:
        # Produce some data
        out_q.put(data)

# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Process the data


# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()


# sentinels cause consumers to terminate
from queue import Queue
from threading import Thread

# Object that signals shutdown
_sentinel = object()

# A thread that produces data
def producer(out_q):
    while running:
        # Produce some data
        out_q.put(data)
        
        # Put the sentinel on the queue to indicate completion
        out_q.put(_sentinel)

# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Check for termination
        if data is _sentinel:
            in_q.put(_sentinel)
            break


# Thread Safe Priority Queue
import heapq
import threading

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()
 
    def put(self, item, priority):
        with self._cv:
            heapq.heappush(self._queue, (-priority, self._count, item))
            self._count += 1
            self._cv.notify()
 
    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
            return heapq.heappop(self._queue)[-1]


# Queue objects do provide some basic completion features
from queue import Queue
from threading import Thread

# A thread that produces data
def producer(out_q):
    while running:
        # Produce some data
        out_q.put(data)

# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
         # Process the data
         # Indicate completion
        in_q.task_done()

# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()

# Wait for all produced items to be consumed
q.join()


# Producer can monitor progress of event object
from queue import Queue
from threading import Thread, Event

# A thread that produces data
def producer(out_q):
    while running:
        # Produce some data
 
        # Make an (data, event) pair and hand it to the consumer
        evt = Event()
        out_q.put((data, evt))
 
        # Wait for the consumer to process the item
        evt.wait()

# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data, evt = in_q.get()
        # Process the data
 
        # Indicate completion
        evt.set()



from queue import Queue
from threading import Thread
import copy

# A thread that produces data
def producer(out_q):
    while True:
    # Produce some data
        out_q.put(copy.deepcopy(data))

# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Process the data



# import queue
# q = queue.Queue()
# # non blocking
# try:
#     data = q.get(block=False)
# except queue.Empty:
#     pass
    
# try:
#     q.put(item, block=False)
# except queue.Full:
#     pass
# # timeouts
# try:
#     data = q.get(timeout=5.0)
# except queue.Empty:
#     pass
# issue a logging message when the queue is full
# def producer(q):
#     try:
#         q.put(item, block=False)
#     except queue.Full:
#         log.warning('queued item %r discarded!', item)



_running = True
# timeout to give up on operations
def consumer(q):
    while _running:
        try:
            item = q.get(timeout=5.0)
            # Process item
        except queue.Empty:
            pass
