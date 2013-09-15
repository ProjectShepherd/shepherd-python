
# libraries and controllers
import util

# config
from os import path
path.append('../')
from config import errors as ERR
from config import mongo_config

@util.check_args()
@util.parse_json
def get_people(db=None, data=None):
    pass

