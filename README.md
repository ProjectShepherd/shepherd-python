
#Shepherd Python

This is a rewrite of the Shepherd API intended for future development.

###Running Locally

Currently the API requires a mongo instance running on port 27017 (the default port).
It's then simple to get running using the `run.sh` script.

If you wish to do things manually, here are the steps:

    # in the root of the project
    source bin/activate                 # activate the python virtual environment
    source src/config/settings.sh       # add you project specific settings to the environment
    python src/app.py                   # start up the API

When you're done, run `deactivate` to exit the virtual environment.

###Setup

Just run `setup.sh` and a Python virtual environment will be created and the necessary modules will be installed.

Currently it set to run with MongoDB but that is up for change.


