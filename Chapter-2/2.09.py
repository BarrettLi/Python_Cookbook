# Problem: You're working with Unicode strings, but need to make sure that all of the strings have
# the same underlying representation

# In Unicode, certain characters can be represented by more than on valid sequence of code points
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
s1 # 'Spicy Jalapeño'
s2 # 'Spicy Jalapeño'
s1 == s2 # False
len(s1) # 14
len(s2) # 15


# to fix this, you should first normalize the text into a standard representation using the
# unicodedata module:
import unicodedata
t1 = unicodedata.normalize('NFC', s1) # NFC means that characters should be fully composed
t2 = unicodedata.normalize('NFC', s2)
t1 == t2 # True
print(ascii(t1))
# 'Spicy Jalape\xf1o'

t3 = unicodedata.normalize('NFD', s1) # NEF means that characters should be fully decomposed
t4 = unicodedata.normalize('NFD', s2)
t3 == t4 # True
print(ascii(t3))
# 'Spicy Jalapen\u0303o'

# Python also supports the normalization forms NFKC and NFKD, which add extra compatibility
# features for dealing with certain kinds of characters
s = '\ufb01' # A single character
s # 'fi'
unicodedata.normalize('NFD', s) # 'fi'

unicodedata.normalize('NFKD', s) # 'fi'
unicodedata.normalize('NFKC', s) # 'fi'

# Discussion
t1 = unicodedata.normalize('NFD', s1)
''.join(c for c in t1 if not unicodedata.combining(c))
# 'Spicy Jalapeno'
