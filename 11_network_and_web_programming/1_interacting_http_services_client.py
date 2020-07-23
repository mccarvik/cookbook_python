from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/get'

# Dictionary of query parameters (if any)
parms = {
    'name1' : 'value1',
    'name2' : 'value2'
    }

# Encode the query string
querystring = parse.urlencode(parms)

# Make a GET request and read the response
u = request.urlopen(url+'?' + querystring)
resp = u.read()
print(resp)

# If you need to send query parameters:
# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
    'name1' : 'value1',
    'name2' : 'value2'
    }

# Encode the query string
querystring = parse.urlencode(parms)

# Make a POST request and read the response
u = request.urlopen(url, querystring.encode('ascii'))
resp = u.read()
print(resp)


# How to include headers
# Extra headers
headers = {
 'User-agent' : 'none/ofyourbusiness',
 'Spam' : 'Eggs'
}

req = request.Request(url, querystring.encode('ascii'), headers=headers)

# Make a request and read the response
u = request.urlopen(req)
resp = u.read()
print(resp)

# Requests library
import requests

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
 'name1' : 'value1',
 'name2' : 'value2'
}
# Extra headers
headers = {
 'User-agent' : 'none/ofyourbusiness',
 'Spam' : 'Eggs'
}

resp = requests.post(url, data=parms, headers=headers)

# Decoded text returned by the request
text = resp.text
print(text)

# Make a head request and extract a few fields
resp = requests.head('http://www.python.org/index.html')
status = resp.status_code
# last_modified = resp.headers['last-modified']
# content_type = resp.headers['content-type']
content_length = resp.headers['content-length']

# authentication example
resp = requests.get('http://pypi.python.org/pypi?:action=login',
                    auth=('user','password'))

# Pass HTTP cookies
# First request
resp1 = requests.get(url)

# Second requests with cookies received on first requests
resp2 = requests.get(url, cookies=resp1.cookies)


# upload content example - no data.csv file to upload at the moment
# url = 'http://httpbin.org/post'
# files = { 'file': ('data.csv', open('data.csv', 'rb')) }
# r = requests.post(url, files=files)


# requests usually better than urllib, for example a complicated head request thru urllib 
from http.client import HTTPConnection
from urllib import parse

c = HTTPConnection('www.python.org', 80)
c.request('HEAD', '/index.html')
resp = c.getresponse()

print('Status', resp.status)
for name, value in resp.getheaders():
    print(name, value)

import urllib
import urllib.request

# and another awkward example with authentication involved
auth = urllib.request.HTTPBasicAuthHandler()
auth.add_password('pypi','http://pypi.python.org','username','password')
opener = urllib.request.build_opener(auth)

r = urllib.request.Request('http://pypi.python.org/pypi?:action=login')
u = opener.open(r)
resp = u.read()
print(resp)

# requests example using httpbin
import requests
r = requests.get('http://httpbin.org/get?name=Dave&n=37',
headers = { 'User-agent': 'goaway/1.0' })
resp = r.json()
print(resp['headers'])
