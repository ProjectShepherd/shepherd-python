
# libraries
import simplejson

####################
#   wrappers
####################

# looks for a param named 'data' and decodes it from JSON
def parse_json(f):
    @wraps(f)
    def decorated_function(**kwargs):
        if 'data' in kwargs:
            kwargs['data'] = simplejson.loads(kwargs['data'])
        return f(**kwargs)
    return decorated_function


# checks that all "wrapper_args" are passed into the function
# if a arg (key) is missing, it's value (error) is returned
def check_args(**wrapper_args)
    def needs(f):
        @wraps(f)
        def decorated_function(**kwargs):
            for data in wrapper_args:
                if data not in kwargs:
                    return wrapper_args[data]
            return f(**kwargs)
        return decorated_function


