import calendar
import redis
from datetime import datetime, timedelta
from bottle import route, request
from bl import getSitemap, timeuntil
from utils import setSession, getSession, render


@route('/')
def index():
    """Main landing page"""
    timezone = getSession(request, "timezone", "US/Eastern")
    start_date = datetime.now() + timedelta(30)
    year = datetime.now().year
    years = range(year, year+12)
    months = list(calendar.month_name)[1:]
    cal = calendar.Calendar()

    # Set weekday to start on sunday to match grid
    cal.setfirstweekday(6)

    # Get day num and weekday num tuple
    days = cal.itermonthdays2(start_date.year, start_date.month)
    return render(request, 'index', {'years': years, 'months': months,
                                     'days': days, 'cur_year': year, 'cur_month': start_date.month,
                                     'cur_day': start_date.day, 'timezone': timezone})


@route('/<month:int>/<day:int>/<year:int>')
def mdy(month, day, year):
    """Day calculation view"""
    timezone = getSession(request, "timezone", "US/Eastern")
    now = datetime.now()
    result = timeuntil(now, datetime(year, month, day), timezone)
    return render(request, 'mdy', {'result': result, 'timezone': timezone})


@route('/set-tz/<timezone>')
def set_timezone(timezone):
    """Save timezone selection to users settings"""
    timezone = str(timezone).replace('-', '/')
    print timezone
    setSession(request, "timezone", timezone)


@route('/sitemap.xml')
def sitemap():
    """Sitemap for search engines.  Cache in redis for a few hours"""
    r_server = redis.Redis("localhost")
    sitemap = r_server.get("workdays_sitemap")
    if sitemap is None:
        sitemap = getSitemap()
        r_server.setex("workdays_sitemap", sitemap, 36000)
    return str(sitemap)
