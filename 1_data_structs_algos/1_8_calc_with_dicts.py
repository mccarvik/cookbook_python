import pdb

prices ={
     'ACME': 45.23,
     'AAPL': 612.78,
     'IBM': 205.55,
     'HPQ': 37.20,
     'FB': 10.75
}

# flips keys and values to perform operations
zipped_file = (zip(prices.values(),prices.keys()))
prices_sorted = sorted(zipped_file)
min_price = min(prices_sorted)
max_price = max(prices_sorted)

print(prices_sorted)
print(min_price)
print(max_price)

min_price = prices_sorted[0]
max_price = prices_sorted[-1]
print(min_price)
print(max_price)

# Zip objects can only be called once
zipped_file = (zip(prices.values(),prices.keys()))
print(min(zipped_file)) # OK
# print(max(zipped_file)) #ValueError, max on an empty sequence

# only process keys not values
print(min(prices))
print(max(prices))

# can get lowest price but wont know the key of it
print(min(prices.values()))
print(max(prices.values()))

# Get the key corresponding to the min or max price by providing a lambda function
print(min(prices, key = lambda k: prices[k]))
print(max(prices, key = lambda j: prices[j]))
# but now we dont know the value and need to:
min_value = prices[min(prices, key=lambda k:prices[k])]
print(min_value)

# will default to the key when values are the same
prices = {'AAA':45.23,'ZZZ':45.23}
print(min(zip(prices.values(),prices.keys())))
print(max(zip(prices.values(),prices.keys())))