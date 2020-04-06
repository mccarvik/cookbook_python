from datetime import datetime
from datetime import timedelta
from pytz import timezone
import pytz

d = datetime(2012,12,21,9,30,0)
print(d)
# localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

# convert to Bangalore time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

# daylight savings time can screw stuff up
d = datetime(2013,3,10,1,45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print(later) # Wrong answer

# normalize fixes this
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)

print(loc_d)
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)

# once in UTC, dont have to worry about daylight savings time and can convert later
later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))
# can tell you what timezone to uses for what country
print(pytz.country_timezones['IN'])
