from xml.etree.ElementTree import iterparse
from xml.etree.ElementTree import parse
from collections import Counter

# simple function to incrementally process huge xml with small memory footprint
def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass

# will grab all the pothole data but its huge
# potholes_by_zip = Counter()
# doc = parse('potholes.xml')
# for pothole in doc.iterfind('row/row'):
#     potholes_by_zip[pothole.findtext('zip')] += 1

# for zipcode, num in potholes_by_zip.most_common():
#     print(zipcode, num)

# uses a generator to minimize memeory footprint
potholes_by_zip = Counter()
data = parse_and_remove('potholes.xml', 'row/row')
for pothole in data:
    potholes_by_zip[pothole.findtext('zip')] += 1

for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)

# data = iterparse('potholes.xml',('start','end'))
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
# elem_stack[-2].remove(elem)