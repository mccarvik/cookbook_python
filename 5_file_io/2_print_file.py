# reroute print function to a file
with open('somefile.txt', 'rt') as f:
    print('Hello World!', file=f)