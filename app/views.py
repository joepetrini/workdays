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
    session.save()
    start_date = datetime.now() + timedelta(30)
    year = datetime.now().year
    years = range(year,year+12)
    months = list(calendar.month_name)[1:]
    cal = calendar.Calendar()
    cal.setfirstweekday(6) # Set weekday to start on sunday
    days = cal.itermonthdays2(start_date.year,start_date.month) # Get day num and weekday num tuple
    return template('index.htm',years=years,months=months,days=days,cur_year=year,cur_month=start_date.month,cur_day=start_date.day)


@route('/<month:int>/<day:int>/<year:int>')
def mdy(month,day,year):
    """Day calculation view"""
    # TODO: Pull timezone from session
    session = request.environ.get('beaker.session')
    result = bl.timeuntil(datetime.now(),datetime(year,month,day),'US/Eastern')
    return template('mdy.htm',result=result)
    
    
@route('/set-tz')
def set_timezone(tz):
    """Save timezone selection to users settings"""
    pass