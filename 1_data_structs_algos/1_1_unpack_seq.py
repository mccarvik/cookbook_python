"""
Chapter 1.1 Unpacking a sequence
"""

p = (4, 5)
x , y = p
print(x)

data = ['ACME',50, 91.1, (2012,12,21)]

# Can be different data types
name, share, price, date = data
print(name)
print(share)
print(price)
print(date)
print(name, share, price, date)

# or multi layered
name, shares, price, (year, mon, day) = data
print(year)
print(mon)
print(day)
print(year, mon, day)

# will be error if number of elements doesnt match
if False:
    p = (4,5)
    x,y,z = p
    
# works for any iterable: string, generator, etc.
s = 'Hello'
a,b,c,d,e = s
print(a)

# Can use throwaway variable _
data = ['ACME',50, 91.1, (2012,12,21)]

_,share,price,_ = data
print(share)
print(price)
