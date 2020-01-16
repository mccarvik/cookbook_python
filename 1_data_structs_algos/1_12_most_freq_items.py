from collections import Counter

words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
# Counter class finds the most common n items in a sequence
top_three = word_counts.most_common(3)
print(top_three)

# works like a dictionary
print(word_counts['not'])
print(word_counts['eyes'])

# Can increment amounts manually
morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_counts[word] += 1
print(word_counts)
print(word_counts['eyes'])

# or use update
word_counts.update(morewords)
print(word_counts)

# Can combine and subtract counts
a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
c = a + b
print(c)
d = a - b
print(d)