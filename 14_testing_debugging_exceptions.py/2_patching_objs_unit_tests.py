from unittest.mock import patch

# patch can be used as a decorator...
# @patch('example.func')
# def test1(x, mock_func):
#     example.func(x) # Uses patched example.func
#     mock_func.assert_called_with(x)

# a context manager
# with patch('example.func') as mock_func:
#     example.func(x) # Uses patched example.func
#     mock_func.assert_called_with(x)

# or to patch things manually
# p = patch('example.func')
# mock_func = p.start()
# example.func(x)
# mock_func.assert_called_with(x)
# p.stop()

# can stack decorators to patch multiple objects
# @patch('example.func1')
# @patch('example.func2')
# @patch('example.func3')
# def test1(mock1, mock2, mock3):
#       pass
# def test2():
#     with patch('example.patch1') as mock1, \
#         patch('example.patch2') as mock2, \
#         patch('example.patch3') as mock3:
#         pass

x = 42
with patch('__main__.x'):
    # values are replaced with MagicMock instances
    print(x)
print(x)

# can replace the value with anything by putting value in the second argument
with patch('__main__.x', 'patched_value'):
    print(x)
print(x)

# MagicMock mimic callables and instances
from unittest.mock import MagicMock
m = MagicMock(return_value = 10)
print(m(1, 2, debug=True))
m.assert_called_with(1, 2, debug=True)
# m.assert_called_with(1, 2) # error, assertionError
m.upper.return_value = 'HELLO'
print(m.upper('hello'))
assert m.upper.called
m.split.return_value = ['hello', 'world']
print(m.split('hello world'))

m.split.assert_called_with('hello world')
print(m['blah'])
print(m.__getitem__.called)
m.__getitem__.assert_called_with('blah')


# example.py
from urllib.request import urlopen
import csv

def dowprices():
    u = urlopen('http://finance.yahoo.com/d/quotes.csv?s=@^DJI&f=sl1')
    lines = (line.decode('utf-8') for line in u)
    rows = (row for row in csv.reader(lines) if len(row) == 2)
    prices = { name:float(price) for name, price in rows }
    return prices
import unittest
from unittest.mock import patch
import io
import example

sample_data = io.BytesIO(b'''\
"IBM",91.1\r
"AA",13.25\r
"MSFT",27.72\r
\r
''')

# example unittest
class Tests(unittest.TestCase):
    @patch('example.urlopen', return_value=sample_data)
    def test_dowprices(self, mock_urlopen):
        p = example.dowprices()
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p,
                        {'IBM': 91.1,
                         'AA': 13.25,
                         'MSFT' : 27.72})
        
if __name__ == '__main__':
    unittest.main()