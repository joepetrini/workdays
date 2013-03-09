import logging
import calendar
from datetime import datetime,timedelta,date
from pytz import timezone
from bottle import TEMPLATE_PATH, route, request, jinja2_template as template


TEMPLATE_PATH.append('./templates')


@route('/')
def index():
    """Main landing page"""
    session = request.environ.get('beaker.session')    
    year = datetime.now().year
    years = range(year,year+12)
    months = list(calendar.month_name)[1:]
    cal = calendar.Calendar()
    cal.setfirstweekday(6) # Set weekday to start on sunday
    days = cal.itermonthdays2(2013,2) # Get day num and weekday num tuple
    return template('index.htm',years=years,months=months,days=days)


@route('/<month:int>/<day:int>/<year:int>')
def mdy(month,day,year):
    """Day calculation view"""
    session = request.environ.get('beaker.session')
    now = datetime.today()
    end = datetime(year,month,day,now.hour,now.minute)
    diff = end - now
    #delta = relativedelta(end, now)        
    daysleft = int(diff.days)
    #if diff.seconds/3600 > 12:
    #    daysleft += 1
    return template('mdy.htm',a=daysleft)
    
    # PAC time - 