
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        # negates the prioirty as the lowest value gets popped first
        # index is used to properly order items of the same prioirty based on 
        # when they were pushed on the queue (FIFO)
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)
        
q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# items not comparable
if False:
    a = Item('foo')
    b = Item('bar')
    print(a < b)

# but with priority comparable
a = (1, Item('foo'))
b = (5, Item('bar'))
print(a < b)

# unless they have the same priority
if False:
    c = (1, Item('grok'))
    print(a < c)
    
# Adding an index makes sure this never happens
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
print(a < b)
print(a < c)




