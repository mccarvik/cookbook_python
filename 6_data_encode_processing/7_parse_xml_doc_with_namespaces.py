from xml.etree.ElementTree import parse, Element
doc = parse('ns7.xml')

# some queries that work
print(doc.findtext('author'))
print(doc.find('content'))

# A query involving a namespace (doesn't work)
print(doc.find('content/html'))

# Works if fully qualified
print(doc.find('content/{http://www.w3.org/1999/xhtml}html'))

# Doesn't work
print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/head/title'))

# Fully qualified
print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/'
    '{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title'))

# Wrap namespace handling in a utility class
class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)
    def register(self, name, uri):
        self.namespaces[name] = '{'+uri+'}'
    def __call__(self, path):
        return path.format_map(self.namespaces)
        
ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
print(doc.find(ns('content/{html}html')))
print(doc.findtext(ns('content/{html}html/{html}head/{html}title')))

from xml.etree.ElementTree import iterparse
for evt, elem in iterparse('ns7.xml', ('end', 'start-ns', 'end-ns')):
    print(evt, elem)
print(elem)