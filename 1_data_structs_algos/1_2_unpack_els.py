"""
Unpacking elements of arbitrary length
"""
import pdb

# middle will accept an arbitrary amount of items
def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)

print(drop_first_last([1,2,3,4,5,6,11]))