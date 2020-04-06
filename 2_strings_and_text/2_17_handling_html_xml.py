import html
from html.parser import HTMLParser
from xml.sax.saxutils import unescape

s = 'Elements are written as "<tag>text</tag>".'
print(s)
# replaces special characters such as < and >
print(html.escape(s))
# same but without quotes
print(html.escape(s, quote=False))

s = 'Spicy Jalapeño'
# emit texts as ascii
print(s.encode('ascii', errors='xmlcharrefreplace'))
s = 'Spicy &quot;Jalape&#241;o&quot.'
p = HTMLParser()
# converts html into text
print(p.unescape(s))
# converts xml into text
t = 'The prompt is &gt;&gt;&gt;'
print(unescape(t))