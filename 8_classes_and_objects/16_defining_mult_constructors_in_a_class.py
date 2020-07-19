import time

class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    # Use a class method - a class method recieves the class as the first argument
    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

a = Date(2012, 12, 21) # Primary
# just call the alternative constructor like a method
b = Date.today()

class NewDate(Date):
    pass
c = Date.today() # Creates an instance of Date (cls=Date)
d = NewDate.today() # Creates an instance of NewDate (cls=NewDate)

# Works but kind of opaque
class Date2:
    def __init__(self, *args):
        if len(args) == 0:
            t = time.localtime()
            args = (t.tm_year, t.tm_mon, t.tm_mday)
        self.year, self.month, self.day = args

a = Date2(2012, 12, 21) # Clear. A specific date.
b = Date2() # ??? What does this do?

# Class method version
c = Date.today() # Clear. Today's date.