
# libraries and controllers
import util

# config
from sys import path
path.append('../')
from config import errors as ERR
from config import mongo_config


@util.check_args(db=ERR.DB_MISSING, data=ERR.DATA_MISSING)
def get_people(db, data):
    pass


@util.check_args(db=ERR.DB_MISSING, data=ERR.DATA_MISSING)
@util.parse_json('data')
def create_report(db, data):
    pass


@util.check_args(db=ERR.DB_MISSING, data=ERR.DATA_MISSING)
@util.parse_json('data')
def update_report(db, data):
    pass

