import sys
# foo-package and bar-package dont have __init__.py files
# spam used as a common namespace
sys.path.extend(['foo-package', 'bar-package'])
# can import blah or grok from spam even tho they are from different packages
import spam.blah
import spam.grok

import spam
print(spam.__path__)
# can merge more to the spam namespace after the fact as well
import spam.custom
import spam.grok
import spam.blah
print(spam)
