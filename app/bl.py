import collections
from datetime import datetime,timedelta
from dateutil.relativedelta import *
from uuid import uuid1
import pytz

def guid():
    """Generates a globally unique id"""
    return uuid1()
        

def timeuntil(start,end,timezone):
    """Returns time delta using supplied timezone
    >>> timeuntil(datetime(2013,1,1,8),datetime(2013,1,5),"US/Eastern").workdays
    4
    >>> timeuntil(datetime(2013,1,1,14),datetime(2013,1,5),"US/Eastern").workdays
    3
    >>> timeuntil(datetime(2013,1,1,14),datetime(2013,1,8),"US/Eastern").workdays
    4
    """
    # Init result as named tuple
    TimeResult = collections.namedtuple('TimeResult', 'delta rdelta workdays deltastr')
    
    # Localize start and end times
    tz = pytz.timezone(timezone)    
    start = start.replace(tzinfo=tz)
    end = end.replace(tzinfo=tz)
    
    # Delta and relative deltas
    delta = end - start
    rdelta = relativedelta(end,start)
    
    # Workday logic
    workdays = 0
    # If before 8am on weekday, increment 1 to include today
    if start.hour < 9 and start.weekday() < 5:
        workdays += 1    
    for i in range(0,delta.days):
        start = start + timedelta(days=1)
        if start.weekday() < 5:
            workdays += 1

    # Human readable delta
    y,m,d = abs(rdelta.years),abs(rdelta.months),abs(rdelta.days)
    yname = 'year' if y==1 else 'years'
    mname = 'month' if m==1 else 'months'
    dname = 'day' if d==1 else 'days'    
    deltastr = ""
    if (y == 0 and m == 0):
        deltastr = "%s %s" % (d,dname)
    if (y == 0):
        deltastr = "%s %s and %s %s" % (m,mname,d,dname)
    else:
        deltastr = "%s %s %s %s and %s %s" % (y,yname,m,mname,d,dname)        
        
    r = TimeResult(delta,rdelta,workdays,deltastr)
    return r
    
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

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()    