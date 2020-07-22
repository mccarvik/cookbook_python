import spam
import imp
imp.reload(spam)
# reload a module that has alreadt been loaded becuase changes have been made to it
# Useful in debugging but rarely in production


# following will only work in an interactive session
# spam.py
def bar():
    print('bar')

def grok():
    print('grok')

import spam
from spam import grok
spam.bar()
grok()

def grok():
    print('New grok')

import imp
imp.reload(spam)
spam.bar()
grok() # old output
spam.grok() # new output