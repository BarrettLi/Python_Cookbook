# Problem: Your program has become an unreadable mess of hardcoded slice indices and you want to
# clean it up.

# suppose you have
######    0123456789012345678901234567890123456789012345678901234567890' 
record = '....................100          .......513.25     ..........'
# you can do
cost = int(record[20:32] * float(record[40:48])

# instead of doing that, why not name the slices like this?
SHARES = slice(20, 32)
PRICE = slice(40, 48)

cost = int(record[SHARES]) * float(record[PRICE])

# Discussion
a = slice(10, 50, 2)
a.start # 10
a.stop # 50
a.step # 2

s = 'HelloWorld'
a.indices(len(s)) # (5, 10, 2)

for i in range(*a.indices(len(s))):
    print(s[i])

# W
# r
# d
