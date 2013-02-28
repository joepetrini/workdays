import sqlite3
from bottle import route, run

@route('/')
def index():
    return "test"

run(port=8002)
