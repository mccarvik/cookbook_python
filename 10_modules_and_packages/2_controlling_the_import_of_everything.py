
def spam():
    pass

def grok():
    pass

blah = 42

# Only export 'spam' and 'grok' when "import *" is used
__all__ = ['spam', 'grok']