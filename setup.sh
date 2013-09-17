#!/bin/bash

# add submodules
git submodule init
git submodule update

# setup python virtualenv
virtualenv --no-site-packages .
source bin/activate
pip install -r requirements.txt

# done!
echo 'Your dev environment is now setup!'
exit 0

