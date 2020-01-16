from operator import itemgetter

rows = [
 {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
 {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
 {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
 {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# sorts the rows by a common field
rows_by_fname= sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

# Can also except multiple keys
rows_lfname = sorted(rows,key=itemgetter('lname','fname'))
print(rows_lfname)

# Can use lambda instead
rows_by_fname= sorted(rows,key = lambda k: k['fname'])
rows_by_lname = sorted(rows,key = lambda p: p['lname'])
print(rows_by_fname)
print(rows_by_lname)

# Can be applied to min / max as well
print(min(rows,key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))