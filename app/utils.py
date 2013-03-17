from bottle import TEMPLATE_PATH, jinja2_template as template


TEMPLATE_PATH.append('./templates')
session_app_key = 'workdays_'


def render(request, templateName, params={}):
    mobile = isMobile(request)
    params['mobile'] = mobile
    if mobile:
        return template(templateName+'_mob.htm', params)
    else:
        return template(templateName+'.htm', params)


def isMobile(request):
    user_agent = request.headers.get('User-Agent', '').lower()
    if 'iphone' in user_agent:
        return True
    if ('andrioid' in user_agent) and ('mobile' in user_agent):
        return True
    if 'blackberry' in user_agent:
        return True
    #return False
    return True


def setSession(request, key, value):
    session = request.environ.get('beaker.session')
    session[session_app_key+key] = value
    session.save()


def getSession(request, key, default=None):
    session = request.environ.get('beaker.session')
    key = session_app_key + key
    if key in session:
        return session[key]
    else:
        return default
