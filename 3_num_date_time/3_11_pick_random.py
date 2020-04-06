import random

values = [1,2,3,4,5,6]
# pick random number out a sequene
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
# pick n random numbers without replacement
print(random.sample(values,2))
print(random.sample(values,2))
print(random.sample(values,3))
print(random.sample(values,3))
# shuffle sequence
print(random.shuffle(values))
# produce random integers
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))
# uniform floating point values
print(random.random())
print(random.random())
print(random.random())
# get n random-bits expressed as integer
print(random.getrandbits(200))
# seed based on system time
print(random.seed())
# seed based on parameter
print(random.seed(12345))
# seed based on byte data
print(random.seed(b'bytedata'))
