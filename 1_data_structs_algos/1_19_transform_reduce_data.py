import os

# generator expression argument
nums = [1,2,3,4,5]
s = sum(x*x for x in nums)
print(s)

# Determine if any .py files exist in directory
files = os.listdir('./')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')
    
# output a tuple as a csv
s = ('ACME', 50,123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a daa structure
portfolio= [
 {'name':'GOOG', 'shares': 50},
 {'name':'YHOO', 'shares': 75},
 {'name':'AOL', 'shares': 20},
 {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

# dont need repeated parenthesis
s = sum(x**2 for x in nums)
print(s)

# more elegant solution
min_shares = min(portfolio, key = lambda s:s['shares'])
print(min_shares)