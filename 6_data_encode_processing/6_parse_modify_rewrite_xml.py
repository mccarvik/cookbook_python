
# Grab the xml file
from xml.etree.ElementTree import parse, Element
doc = parse('pred.xml')
root = doc.getroot()
print(root)

# Remove a few elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))
# insert a new element
root.getchildren().index(root.find('nm'))
e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)
# write it back out
doc.write('newpred.xml', xml_declaration=True)
