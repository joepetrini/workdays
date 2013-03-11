import logging
import calendar
from datetime import datetime,timedelta,date
from pytz import timezone
from bottle import TEMPLATE_PATH, route, request, jinja2_template as template
import bl

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
    t = bl.timeuntil(year,month,day,'US/Eastern')
    return template('mdy.htm',a=t)
    
    
@route('/set-tz')
def set_timezone(tz):
    """Save timezone selection to users settings"""
    pass