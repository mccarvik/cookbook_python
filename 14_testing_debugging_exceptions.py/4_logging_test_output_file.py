
import unittest

# common technique for running unittests
class MyTest(unittest.TestCase):
    pass  
if __name__ == '__main__':
    unittest.main()

# If you want to redirect the output, need to do something like this:
import sys
def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out,verbosity=verbosity).run(suite)

if __name__ == '__main__':
    with open('testing.out', 'w') as f:
        main(f)