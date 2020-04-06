from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

# timedelta = interval of time
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.seconds/3600)
print(c.total_seconds()/3600)

# datetime creates a specific date and time
a = datetime(2012,9,23)
print(a + timedelta(days=10))
b = datetime(2012,12,21)
d = b -a
print(d.days)
now = datetime.today()
print(now)
print(now + timedelta(minutes=10))
# datetime aware of leap years
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a - b)
print((a-b).days)
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c-d).days)

# dateutil module can do some things datetime cant
a = datetime(2012, 9, 23)
# will cause error
# print(a + timedelta(months=1))
print(a + relativedelta(months=+1))
print(a + relativedelta(months=+4))
b = datetime(2012, 12, 21)
d = b - a
print(d)
d = relativedelta(b,a)
print(d)
print(d.months)
print(d.days)
