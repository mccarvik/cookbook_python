
# raise from exception specifies raising another exception "from" a previous one
# chains them together
def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e
example()


try:
    example()
except RuntimeError as e:
    print("It didn't work:", e)
    # can look at the __cause__ attribute for more info
    if e.__cause__:
        print('Cause:', e.__cause__)

def example2():
    try:
        int('N/A')
    except ValueError as e:
        # implicit chained exceptions when exception occurs in an "except" block
        print("Couldn't parse:", err)
example2()


# If you want to suppress chaining, use "from None"
def example3():
    try:
        int('N/A')
    except ValueError:
        raise RuntimeError('A parsing error occurred') from None
example3()

# Should probably prefer this style
try:
    pass
except SomeException as e:
    raise DifferentException() from e

# Here, not as clear which is getting raised
try:
    pass
except SomeException:
    raise DifferentException()
