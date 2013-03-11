from datetime import datetime
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
    print now
    end = datetime(year,month,day,now.hour,now.minute).replace(tzinfo=tz)
    print end
    diff = end - now
    delta = relativedelta(end, now)    
    return delta
    