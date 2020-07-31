# somelib.py

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

# Example function (for testing)
def func():
    log.critical('A Critical Error!')
    log.debug('A debug message')

# no logging occurs yet
import somelib
somelib.func()

# now logging will occur on somelib
logging.basicConfig()
somelib.func()

import logging
logging.basicConfig(level=logging.ERROR)

# logging of individual libraries can be independently configured of other logging settings
import somelib
somelib.func()
# Change the logging level for 'somelib' only
logging.getLogger('somelib').level=logging.DEBUG
somelib.func()