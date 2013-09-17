
# libraries
from flask import Flask, request
from flask.ext.pymongo import PyMongo
from functools import wraps

########################################
# controllers
########################################
from controllers import person as person_controller

########################################
# configuration
########################################
app = Flask(__name__)
app.config.from_object('config.flask_config')
mongo = PyMongo(app)

########################################
#   routes
########################################

@app.route('/missing_people', methods=['POST'])
def post_missing_people():
    """ create a missing persons report

    Creates a missing persons report in the DB.
    """
    return person.create_report(
        db      = pymongo,
        data    = request.data
    )


@app.route('/missing_people', methods=['GET'])
def get_missing_people():
    """ gets missing people

    Returns a JSON w/ a list of report objects
    """
    return person_controller.get_people(
        db      = pymongo,
        data    = request.data
    )


@app.route('/missing_people', methods=['PATCH'])
def update_report():
    """ update a missing persons report

    Updates the status of a missing persons report
    """
    return person_controller.update_report(
        db      = pymongo,
        data    = request.data
    )


@app.route('/')
def hello():
    return 'Nothing here', 400


if __name__ == '__main__':
    app.run()

