# Problem: You have a list of dictionaries and you would like to sort the entries according to one
# or more of the dictionary values

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
# [{'fname': 'Big', 'uid': 1004, 'lname': 'Jones'},
#    {'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'},
#    {'fname': 'David', 'uid': 1002, 'lname': 'Beazley'},
#    {'fname': 'John', 'uid': 1001, 'lname': 'Cleese'}]

rows_by_uid = sorted(rows, key=itemgetter('uid'))
# [{'fname': 'John', 'uid': 1001, 'lname': 'Cleese'},
#    {'fname': 'David', 'uid': 1002, 'lname': 'Beazley'},
#    {'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'},
#    {'fname': 'Big', 'uid': 1004, 'lname': 'Jones'}]

# the itemgetter() function can also accept mutiple keys
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
# [{'fname': 'David', 'uid': 1002, 'lname': 'Beazley'},
#    {'fname': 'John', 'uid': 1001, 'lname': 'Cleese'},
#    {'fname': 'Big', 'uid': 1004, 'lname': 'Jones'},
#    {'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'}]


# Discussion

# the itemgetter() function can be replaced by lambda expressions
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname'])
# the solution involving itemgetter() runs FASTER

# the technique can also be applied to functions such as min() and max()
min(rows, key=itemgetter('uid'))
# {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}
max(rows, key=itemgetter('uid'))
# {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
