
# libraries
import simplejson

# config
from sys import path
path.append('../')
from config import errors as ERR
path.append('controllers/')


####################
#   wrappers
####################

# looks for a specified arguments then decodes them from JSON
def parse_json(*parse_args):
    def wrapped_fn(f)
        @wraps(f)
        def decorated_function(**kwargs):
            for arg in parse_args:
                if arg in kwargs:
                    # return parsed dict parsed from JSON
                    kwargs[arg] = simplejson.loads(kwargs[arg])
                else:
                    # return error
                    return ERR.DATA_MISSING(arg)
            return f(**kwargs)
        return decorated_function
    return wrapped_fn


# checks that all "wrapper_args" are passed into the function
# if a arg (key) is missing, it's value (error) is returned
def check_args(**wrapper_args)
    def needs(f):
        @wraps(f)
        def decorated_function(**kwargs):
            for data in wrapper_args:
                if data not in kwargs:
                    return wrapper_args[data]()
            return f(**kwargs)
        return decorated_function
    return needs        

