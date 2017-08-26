# Problem: You want to sort objects of the same class, but they don't natively support comparison
# operations

# suppose you have a sequence of User instances
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    
    def __repr__(self):
        return "User({})".format(self.user_id)

users = [User(23), User(3), User(99)]
sorted(users, key=lambda u: u.user_id) # [User(3), User(23), User(99)]

# Instead of lambda, an alternative approach is to use operator.attrgetter():
from operator import attrgetter
sorted(users, key=attrgetter('user_id')) # [User(3), User(23), User(99)]

# Discussion

by_name = sorted(users, key=attrgetter('last_name', 'first_name'))

# Again, this technique can be used in max() and min()
min(users, key=attrgetter('user_id') # User(3)
max(users, key=attrgetter('user_id') # User(99)
