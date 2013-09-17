#!/bin/bash

# compile Coffeescript
cd frontend
grunt
cd ..

# setup env for python
cd ..
source bin/activate
source src/config/settings.sh

# start app
python src/app.py


