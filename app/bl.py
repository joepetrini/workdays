import collections
from datetime import timedelta, datetime
from dateutil.relativedelta import *
import pytz


def getSitemap():
    s = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    s += "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
    host = "www.workdaysuntil.com"
    now = datetime.today()

    # Go 10 years into the future
    now = datetime.today()

    for i in range(0, 3650):
        d = now + timedelta(days=i)
        ds = "%02d/%02d/%s" % (d.month, d.day, d.year)
        s += "\t<url>\n"
        s += "\t\t<loc>http://%s/%s</loc>\n" % (host, ds)
        s += "\t\t<changefreq>daily</changefreq>\n"
        s += "\t</url>\n"
    s += "</urlset>\n"
    return s


def timeuntil(start, end, timezone):
    """Returns time delta using supplied timezone
    >>> timeuntil(datetime(2013,1,1,8),datetime(2013,1,5),"US/Eastern").workdays
    4
    >>> timeuntil(datetime(2013,1,1,14),datetime(2013,1,5),"US/Eastern").workdays
    3
    >>> timeuntil(datetime(2013,1,1,14),datetime(2013,1,8),"US/Eastern").workdays
    4
    """
    # Init result as named tuple
    TimeResult = collections.namedtuple('TimeResult', 'delta rdelta workdays deltastr endday enddate')

    # Localize start and end times
    tz = pytz.timezone(timezone)
    start = start.replace(tzinfo=tz)
    end = end.replace(tzinfo=tz)

    # Delta and relative deltas
    delta = end - start
    rdelta = relativedelta(end, start)

    # Workday logic
    workdays = 0
    # If before 8am on weekday, increment 1 to include today
    if start.hour < 9 and start.weekday() < 5:
        workdays += 1
    for i in range(0, delta.days):
        start = start + timedelta(days=1)
        if start.weekday() < 5:
            workdays += 1

    # Human readable delta
    y, m, d = abs(rdelta.years), abs(rdelta.months), abs(rdelta.days)
    yname = 'year' if y == 1 else 'years'
    mname = 'month' if m == 1 else 'months'
    dname = 'day' if d == 1 else 'days'

    deltastr = ""
    if (y == 0 and m == 0):
        deltastr = " %s %s" % (d, dname)
    elif (y == 0):
        deltastr = "%s %s and %s %s" % (m, mname, d, dname)
    else:
        deltastr = "%s %s %s %s and %s %s" % (y, yname, m, mname, d, dname)

    # Some preformatted strings
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    endday = days[end.weekday()]
    enddate = end.strftime("%A %B %d %Y")

    r = TimeResult(delta, rdelta, workdays, deltastr, endday, enddate)

    return r


if __name__ == "__main__":
    import doctest
    doctest.testmod()
