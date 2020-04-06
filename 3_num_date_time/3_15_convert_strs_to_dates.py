from datetime import datetime

text = '2012-09-20'
# changes text to date
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)
print(z)
# changes date to string
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)

# strptime can be very inefficient, often better to make a custom solution
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))