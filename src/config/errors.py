
import simplejson


# generate an error response
def generate_error(message=None, code=400):
    return simplejson.dumps({
        'message' : message,
        'status_code' : code
    }), code

###################
# errors
###################

def DB_MISSING():
    return generate_error(
        message = 'Your DB is acting up...',
        code = 500
    )


def DATA_MISSING(arg=None):
    message = 'You need to pass in paramter data'
    if arg:
        message = 'You need to pass in data for parameter {}'.format(arg)
    return generate_error(
        message = message,
        code = 403
    )

