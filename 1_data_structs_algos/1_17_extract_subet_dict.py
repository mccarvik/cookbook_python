 
prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}

# Make a dict of all prices over 200
p1 = {key:value for key,value in prices.items() if value > 200}
print(p1)

# Make a dict of all tech names
tech_names = ['AAPL','IBM','HPQ','MSFT']
p2 = {key:value for key,value in prices.items() if key in tech_names}
print(p2)

# creating a sequence of tuples and passing them to dict function
p1 = dict((key,value) for key,value in prices.items() if value>200)
print(p1)

# Another way to do it
tech_names={'AAPL','IBM','HPQ','MSFT'}
p2 = {key:prices[key] for key in prices.keys() & tech_names}
print(p2)