import collections

class A(collections.Iterable):
    pass
# a = A() # error, needs to define __iter__

# just instantiate one of these methods to see what methods it needs
# collections.Sequence()
import pdb
import bisect
# Class that will always store items in sorted order
class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]
 
    def __len__(self):
        return len(self._items)
 
    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)

items = SortedItems([5, 1, 3])
print(list(items))
print(items[0])
print(items[-1])
items.add(2)
print(list(items))
items.add(-10)
print(list(items))
print(items[1:4])
print(len(items))

for n in items:
    print(n)

items = SortedItems()
print(isinstance(items, collections.Iterable))
print(isinstance(items, collections.Sequence))
print(isinstance(items, collections.Container))
print(isinstance(items, collections.Sized))
print(isinstance(items, collections.Mapping))

class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []
 
    # Required sequence methods
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]
 
    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value
 
    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]
 
    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)

a = Items([1, 2, 3])
print(len(a))
a.append(4)
a.append(2)
a.count(2)

a.remove(3)
print("here")