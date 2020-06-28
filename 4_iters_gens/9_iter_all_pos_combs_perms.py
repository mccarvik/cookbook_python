from itertools import permutations
from itertools import combinations, combinations_with_replacement

# all the permutations with all the items
items = ['a','b','c']
for p in permutations(items):
    print(p)

# all the permutations with a given number of items
for p in permutations(items,2):
    print(p)

# all the combinations with all the elements
for c in combinations(items,3):
    print(c)

# all the combinations with given number of items
for c in combinations(items,2):
    print(c)

for c in combinations(items,1):
    print(c)

# all the combinations with replacement
for c in combinations_with_replacement(items,3):
    print(c)