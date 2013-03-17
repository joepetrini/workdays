from bottle import route, default_app


@route('/')
def index():
    return "laskjdf"


@route('/hello')
def hello():
    return "Hello World!"

application = default_app()
