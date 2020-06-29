
# print items, default sep = " "
print('ACME', 50, 91.5)

# specified sep
print('ACME', 50, 91.5, sep=',')

# specified sep and end phrase
print('ACME', 50, 91.5, sep=',', end='!!\n')

# default "\n" at end of line
for i in range(5):
    print(i)

# get rid of newline at end
for i in range(5):
    print(i, end=' ')

# can set separator with join method
print('.'.join(['ACME','50','91.5']))
row = ('ACME', 50, 91.5)
# but only works on strings
# print(','.join(row))
# need to do som acrobatics
print('.'.join(str(x) for x in row))
# could just do this
print(*row, sep='.')