# Problem: You need to unpack N elements from an iterable, but the iterable may be longer than N
# elements, causing a "too many values to unpack" exception.

# Solution: "star expression"

# ex1:
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

# ex2:
record = ('Dave', 'dave@example.com', '123-456-7890', '098-765-4321')
name, email, *phone_numbers = user_record
print name
print email
print phone_numbers

# ex3:
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print trailing
print current

# Discussion

# ex1:
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# ex2: unpacking combined with certain kinds of string processing
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print 'uname', uname
print 'homedir', homedir
print 'sh', sh

# ex3: common throwaway variables
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print name
print year
