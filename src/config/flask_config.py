
from os import environ as env
from sys import exit

try: 
    # mongo settings
    MONGO_HOST = env['MONGO_HOST']
    MONGO_PORT = env['MONGO_PORT']
    MONGO_DBNAME = env['MONGO_DBNAME']

    # flask settings
    if env['DEBUG'] == "TRUE":
        DEBUG = True
    else:
        DEBUG = False
    SECRET_KEY = env['SECRET_KEY']

except KeyError:
    print ("""
Some of your required settings haven't been adding to your environment. You
 probably need to source your config.sh.
""")
    exit(1)


