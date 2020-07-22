
# works fine
a = 13
exec('b = a + 1')
print(b)

# error, b value not defined
def test():
    a = 13
    exec('b = a + 1')
    print(b)
test()

# use locals to fix this
def test():
    a = 13
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    print(b)
test()

def test1():
    x = 0
    exec('x += 1')
    print(x)
test1()

def test2():
    x = 0
    loc = locals()
    print('before:', loc)
    exec('x += 1')
    print('after:', loc)
    print('x =', x)
# x unchanged
test2()

def test3():
    x = 0
    loc = locals()
    print(loc)
    exec('x += 1')
    print(loc)
    # call to locals causes x to be overwritten
    locals()
    print(loc)
test3()

# can make your own dict instead of locals and send it to the text
def test4():
    a = 13
    loc = { 'a' : a }
    glb = { }
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print(b)
test4()