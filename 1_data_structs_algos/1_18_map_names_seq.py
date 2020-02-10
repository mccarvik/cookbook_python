from collections import namedtuple

# makes a class that can be instantiated with give fields
Subscriber = namedtuple('Subscriber', ['addr','joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)
# supports all usual tuple operations
print(len(sub))
addr, joined = sub
print(addr)
print(joined)

# Using ordinary tuples
def compute_cost(records):
    total = 0
    for rec in records:
        total += rec[1] * rec[2]
    return total

Stock = namedtuple('Stock',['name','shares','prices'])

def compute_cost_nt(records):
    total = 0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.prices
    return total
    
s = Stock('ACME', 100,123.45)
print(s)
# namedtuple is immutable
if False:
    s.shares = 75

# _replace creates a new tuple instance
s = s._replace(shares=75)
print(s)

# Create a prototype instance
Stock = namedtuple('Stock',['name','shares','price','date','time'])
stock_prototype = Stock('',0,0.0,None,None)
print(stock_prototype)

# Function to convert a dictionary to a stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)
    
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/18/2012'}
print(dict_to_stock(b))



