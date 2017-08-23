# Problems: You have an N-element tuple or sequence that you would like to unpack into a 
# collection of N varivles

p = (4, 5)
x, y = p
print x
print y

data = [ 'ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print name
print shares
print price
print date

name, shares, price, (year, mon, day) = data
print name
print year
print mon
print day

# Dission
s = 'Hello'
a, b, c, d, e = s
print a
print b
print c


# you can pick a throwaway variable
data = [ 'ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print shares
print price
