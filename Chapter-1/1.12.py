# Problem: You have a sequence of items, and you'd like to determine the most frequently occurring
# items in the sequence

# Solution: collections.Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]

# Discussion
# Any hashable input items can be Counter input. Counter is a dictionary that maps the items to the
# number of occurrences.
word_counts['not']
# outputs 1
word_counts['eyes']
# outputs 8

# To increment the count manually,
morewords = ['why','are','you','not','looking','in','my','eyes'] 
for word in morewords:
    word_counts[word] += 1
word_counts['eyes']
# outputs 9

# Or, more easily
word_counts.update(morewords)

# you can also use mathematical operations
a = Counter(words)
b = Counter(morewords)
a
# Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2,
#            "you're": 1, "don't": 1, 'under': 1, 'not': 1})

b
# Counter({'eyes': 1, 'looking': 1, 'are': 1, 'in': 1, 'not': 1, 'you': 1,
#            'my': 1, 'why': 1})

c = a + b
c
# Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2,
#            'around': 2, "you're": 1, "don't": 1, 'in': 1, 'why': 1,
#            'looking': 1, 'are': 1, 'under': 1, 'you': 1})

d = a - b
d
# Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2,
#            "you're": 1, "don't": 1, 'under': 1})
