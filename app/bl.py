import logging
from datetime import datetime,timedelta
from dateutil.relativedelta import *
from uuid import uuid1
import pytz

def guid():
    """Generates a globally unique id"""
    return uuid1()
        
        
def timeuntil(year,month,day,timezone):
    """Returns time delta using supplied timezone"""
    tz = pytz.timezone(timezone)
    now = datetime.now().replace(tzinfo=tz)
    end = datetime(year,month,day,now.hour,now.minute).replace(tzinfo=tz)
    diff = end - now
    delta = relativedelta(end, now)    
    #print weekdaysuntil(now,delta.days)
    workdays = weekdaysuntil(now,diff.days)
    return delta,end,workdays
    
def GetExtendedDayInfo(delta):
    delta += relativedelta( days = +1)
    y,m,d = abs(delta.years),abs(delta.months),abs(delta.days)
    yname = 'year' if y==1 else 'years'
    mname = 'month' if m==1 else 'months'
    dname = 'day' if d==1 else 'days'
        
    if (y == 0 and m == 0):
        return "%s %s" % (d,dname)
    if (y == 0):
        return "%s %s and %s %s" % (m,mname,d,dname)
    return "%s %s %s %s and %s %s" % (y,yname,m,mname,d,dname)    
    
def weekdaysuntil(start,length):
    """Return weekdays in a range from start date
    >>> weekdaysuntil(datetime(2013,3,1),12)
    8
    >>> weekdaysuntil(datetime(2013,3,2),11)
    7
    >>> weekdaysuntil(datetime(2013,3,3),10)
    8
    """
    print "length %s" % length
    wd = 1
    for i in range(0,length):
        start = start + timedelta(days=1)
        if start.weekday() not in [6,0]:
            wd += 1
    return wd
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()    