#!/bin/bash

virtualenv --no-site-packages .
source bin/activate
pip install -r requirements.txt

echo 'Your dev environment is now setup!'
exit 0

