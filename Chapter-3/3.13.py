
# coding: utf-8

# In[1]:


# Problem: You want a general solution for finding a date for the last occurence of a day of the
# week. Last Friday, for example.

# Solution: datetime module
from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date
datetime.today() # For reference


# In[2]:


get_previous_byday('Monday')


# In[3]:


get_previous_byday('Tuesday')


# In[4]:


get_previous_byday('Friday') # Previous week, not today


# In[5]:


# The optional start_date can be supplied using another datetime instance.
get_previous_byday('Sunday', datetime(2012, 12, 21))


# In[6]:


# Discussion
# If you are performing a lot of date calculation like this,
# you maybe better off installing the python-dateutil package instead
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
d = datetime.now()
print(d)


# In[7]:


# Next Friday
print(d + relativedelta(weekday=FR))


# In[8]:


# Last Friday
print(d + relativedelta(weekday=FR(-1)))

