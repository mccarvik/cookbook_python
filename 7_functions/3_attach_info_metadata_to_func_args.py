
# "-> int" doesnt change how python runs, just tells the user what it returns
def add(x:int, y:int) -> int:
    return x + y

print(help(add))
# "__annotations__" shows more info about each instance
print(add.__annotations__)