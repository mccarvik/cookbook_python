
# will catch all exceptions
try:
    pass    
except Exception as e:
    log('Reason:', e) # Important!

# wont know why this doesnt work
def parse_int(s):
    try:
        n = int(v)
    except Exception:
        print("Couldn't parse")
parse_int('n/a')
parse_int('42')


# print the reason
def parse_int(s):
    try:
        n = int(v)
    except Exception as e:
        print("Couldn't parse")
        print('Reason:', e)
parse_int('42')
