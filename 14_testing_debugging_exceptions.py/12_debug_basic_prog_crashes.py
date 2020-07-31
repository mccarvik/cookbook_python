# sample.py
# "python -i ___.py" will create interactive shell to poke around and see what the error might be
def func(n):
    return n + 10
func('Hello')

# can use built in debugger
import pdb
pdb.pm()

# or also produce traceback yourself
import traceback
import sys

try:
    func(arg)
except:
    print('**** AN ERROR OCCURRED ****')
    traceback.print_exc(file=sys.stderr)

# can also just throw in print statements where need be
def sample(n):
    if n > 0:
        sample(n-1)
    else:
        # print_stack will keep track of these prints as they come
        traceback.print_stack(file=sys.stderr)
sample(5)


import pdb
def func(arg):
    # manually launch the debugger at a given point
    pdb.set_trace()
    pass
