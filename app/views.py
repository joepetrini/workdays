from bottle import TEMPLATE_PATH, route, jinja2_template as template
#from jinja2 import Template

TEMPLATE_PATH.append('./templates')

@route('/')
def index():
    #template = Template('test')
    return template('index.htm')
