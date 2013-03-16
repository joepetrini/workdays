session_app_key = 'workdays_'


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
