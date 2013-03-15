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
    start_date = datetime.now() + timedelta(30)
    logging.info(start_date)
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
    session = request.environ.get('beaker.session')
    diff,end,workdays = bl.timeuntil(year,month,day,'US/Eastern')
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    wday = days[end.weekday()]       
    d = end.strftime("%A %B %d %Y")
    title = "How many days until %s"%d if diff.days > -1 else "How many days since %s"%d
    ext_info = bl.GetExtendedDayInfo(diff)
    return template('mdy.htm',diff=diff,title=title,end=end,year=year,month=month,day=day,
                        wday=wday,date=d,ext_info=ext_info,workdays=workdays)
    
    
@route('/set-tz')
def set_timezone(tz):
    """Save timezone selection to users settings"""
    pass