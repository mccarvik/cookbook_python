import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

# merges two lists and keeps them sorted
# NOTE: individual lists must already be sorted
#   all heapq does is read the top of the two lists and emit the smaller one
for c in heapq.merge(a, b):
    print(c)

# how to merge two sorted files
# with open('sorted_file_1', 'rt') as file1, \
#     open('sorted_file_2', 'rt') as file2, \
#     open('merged_file', 'wt') as outf:

#     for line in heapq.merge(file1, file2):
#         outf.write(line)