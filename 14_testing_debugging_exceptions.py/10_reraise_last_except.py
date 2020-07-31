
# use raise in except block to push raise up higher
def example():
    try:
        int('N/A')
    except ValueError:
        print("Didn't work")
        raise
example()

try:
    pass
except Exception as e:
    # Process exception information in some way
    pass
    # Propagate the exception
    raise