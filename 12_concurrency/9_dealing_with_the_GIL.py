# Thread code
# Performs a large calculation (CPU bound)
def some_work(args):
    return result

# A thread that calls the above function
def some_thread():
    while True:
        r = some_work(args)

# Pool modifying above code for multithreading
# Processing pool (see below for initiazation)
pool = None

# Performs a large calculation (CPU bound)
def some_work(args):
    return result

# A thread that calls the above function
def some_thread():
    while True:
        r = pool.apply(some_work, (args))

 
# Initiaze the pool
if __name__ == '__main__':
    import multiprocessing
    pool = multiprocessing.Pool()