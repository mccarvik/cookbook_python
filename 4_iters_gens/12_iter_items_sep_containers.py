from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

# process everything in a and then everything in b
for x in chain(a, b):
    print(x)

# Various working sets of items
active_items = set()
inactive_items = set()

# Iterate over all items - This is more efficient
# for item in chain(active_items, inactive_items):
#     # Process item

# This is less effificient
# for item in active_items:
#  # Process item
    
# for item in inactive_items:
#  # Process item