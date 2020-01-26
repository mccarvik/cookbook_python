from operator import itemgetter
from itertools import groupby
from collections import defaultdict

rows = [
 {'address': '5412 N CLARK', 'date': '07/01/2012'},
 {'address': '5148 N CLARK', 'date': '07/04/2012'},
 {'address': '5800 E 58TH', 'date': '07/02/2012'},
 {'address': '2122 N CLARK', 'date': '07/03/2012'},
 {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
 {'address': '1060 W ADDISON', 'date': '07/02/2012'},
 {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
 {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# Sort by the desired field
# Returns a list of dictionaries, where each dict, every item has same value for date
print(sorted(rows,key=itemgetter('date')))

# Need to sort by desired field first
rows.sort(key=itemgetter('date'))
# will group the items by date and return the date val and a list of items for
# that date on each iteration
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('  ', i)

# group the data together by dates
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
print(rows_by_date)

# allows for easy access of records
for i in rows_by_date['07/01/2012']:
    print(i)