
x =10
a = lambda y:x+y
x=20
b= lambda y:x+y
# "x" edit affects outcome
print(a(10))
print(b(10))

x = 15
print(a(10))

x=3
print(a(10))

x=10
# can capture it and hold it by defining it as a default value:
a = lambda y,x=x : x+y
x = 20
b = lambda y,x=x : x+y
print(a(10))
print(b(10))

funcs = [lambda x: x+n for n in range(5)]
# will just return the last val of range for n for each iteration
for f in funcs:
    print(f(0))
# here n is set to a defualt value so each val in range holds
funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))