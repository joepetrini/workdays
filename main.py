import bottle
from jinja2 import Template
from beaker.middleware import SessionMiddleware
from app import views

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)

@bottle.route('/static/:filename#.*#')
def server_static(filename):
    return bottle.static_file(filename, root='./static/')


bottle.debug(True)
bottle.run(port=8003,reloader=True,app=app)
