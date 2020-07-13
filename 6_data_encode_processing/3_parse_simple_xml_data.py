from urllib.request import urlopen
from xml.etree.ElementTree import parse


# Download the RSS feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
# xml ElementTree module useful
doc = parse(u)

# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print(title)
    print(date)
    print(link)
    print()

print(doc)
e = doc.find('channel/title')
print(e)
print(e.tag)
print(e.text)
print(e.get('some_attribute'))
