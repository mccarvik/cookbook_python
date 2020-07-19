
class Date:
    # slots saves on memory, has other side effects tho, ex: cant add new vars to instance
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day