# Problem: You have code that needs to perform simple time conversions, like days to seconds,
# hours to minutes, and so on.

# Solution: datetime module
from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
c.days # 2
c.seconds # 37800
c.seconds / 3600 # 10.5
c.total_seconds() / 3600 # 58.5

# If you need to represent specific dates and times, create datetime instances and use the 
# standard mathematical operations to manipulate them
from datetime import datetime
a = datetime(2012, 9, 23)
print(a + timedelta(days=10)) # 2012-10-03 00:00:00

b = datetime(2012, 12, 21)
d = b - a
d.days # 89
now = datetime.today()
print(now) # 2012-12-21 14:54:43.094063
print(now + timedelta(minutes=10)) # 2012-12-21 15:04:43.094063

# datetime is aware of leap years
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
a - b # datetime.timedelta(2)
(a - b).days # 2
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
(c - d).days # 1

# Discussion
# If you need to perform more complex date manipulation, look at the dateutil module
a = datetime(2012, 9, 23)
a + timedelta(months=1)
# Traceback (most recent call last):
      # File "<stdin>", line 1, in <module>
    # TypeError: 'months' is an invalid keyword argument for this function

from dateutil.relativedelta import relativedelta
a + relativedelta(months=+1) # datetime.datetime(2012, 10, 23, 0, 0)
a + relativedelta(months=+4) # datetime.datetime(2013, 1, 23, 0, 0)

# Time between two days
b = datetime(2012, 12, 21)
d = b - a # datetime.timedelta(89)
d = relativedelta(b, a) # relativedelta(months=+2, days=+28)
d.months # 2
d.days # 28
