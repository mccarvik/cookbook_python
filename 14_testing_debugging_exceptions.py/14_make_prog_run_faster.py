# somescript.py

import sys
import csv

# script with very little structure
# with open(sys.argv[1]) as f:
#     for row in csv.reader(f):
#         pass

# somescript.py
import sys
import csv

# script statements in a function run faster than global ones
# def main(filename):
#     with open(filename) as f:
#         for row in csv.reader(f):
#             pass
#     # Some kind of processing
# main(sys.argv[1])

# use "from ____ import ___"
import math
# This runs about 30% slower...
def compute_roots(nums):
    result = []
    for n in nums:
        result.append(math.sqrt(n))
    return result

# Test
nums = range(1000000)
for n in range(100):
    r = compute_roots(nums)

# ... than this
from math import sqrt

def compute_roots(nums):
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result



import math

def compute_roots(nums):
    # local variables are faster, so this speeds it up from having it as a global function
    sqrt = math.sqrt
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result

# becuase of locality of attributes...
# Slower
class SomeClass:
    def method(self):
        for x in s:
            op(self.value)

# Faster
class SomeClass:
    def method(self):
        value = self.value
        for x in s:
            op(value)

# accessing attribute y, way slower than x, as there is so much abstraction on top of it
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value
from timeit import timeit
a = A(1,2)
timeit('a.x', 'from __main__ import a')
timeit('a.y', 'from __main__ import a')

# this is completely unnecessary
values = [x for x in sequence]
squares = [x*x for x in values]
# just do this
squares = [x*x for x in sequence]

# this is 3 times faster
a = {
 'name' : 'AAPL',
 'shares' : 100,
 'price' : 534.22
}
# than this
b = dict(name='AAPL', shares=100, price=534.22)
