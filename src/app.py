
# libraries
from flask import Flask, request
from flask.ext.pymongo import PyMongo
from functools import wraps

# controllers
from controllers import person as person_controller

# configuration
app = Flask(__name__)
app.config.from_object('config.flask_config')
mongo = PyMongo(app)


def parse_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function


@app.route('/missing_people', methods=['POST'])
def create_report():
    pass


@app.route('/missing_people', methods=['GET'])
def get_reports():
    return person_controller.get_people(
        db      = pymongo,
        data    = request.data
    )


@app.route('/missing_people', methods=['PATCH'])
def update_report():
    pass


@app.route('/')
def hello():
    return 'hello, world', 200

if __name__ == '__main__':
    app.run()

