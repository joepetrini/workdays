import bottle
from beaker.middleware import SessionMiddleware
#from bottle.ext import beakersession
from app import views

session_opts = {
    'session.type': 'redis',
    'session.url': '127.0.0.1:6379',
    'session.key': 'workdays',
    #'session.cookie_expires': 300,
    #'session.data_dir': './data',
    #'session.auto': True
}

app = SessionMiddleware(bottle.default_app(), session_opts)

@bottle.route('/static/:filename#.*#')
def server_static(filename):
    return bottle.static_file(filename, root='./static/')

bottle.run(port=8003,reloader=True,app=app,debug=True)
