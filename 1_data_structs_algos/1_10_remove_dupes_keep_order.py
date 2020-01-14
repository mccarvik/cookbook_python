
# solution if the sequence is hashable
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1,5,2,1,9,1,5,10]
print(list(dedupe(a)))

# need to make an adjustment if the items arent hashable, like dicts
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
            
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
# pass a lambda function so dedupe2 function knows how to identify dupes
print(list(dedupe2(a, key=lambda d: (d['x'],d['y']))))

# Making a list into a set will work in a lot of scenarios
# wont preserve ordering however
a = [1,5,2,1,9,1,5,10]
print(set(a))