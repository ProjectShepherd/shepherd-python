
from flask import Flask
from flask.ext.pymongo import PyMongo
from functools import wraps
import simplejson

app = Flask(__name__)
app.config.from_object('config.flask_config')
mongo = PyMongo(app)

@app.route('/')
def hello():
    return 'hello, world', 200

if __name__ == '__main__':
    app.run()

