#!/bin/bash

# install app dependencies
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv -y

# create and source virtual environment
python3 -m venv venv
source venv/bin/activate

#install pip requirements
pip3 install -r requirements.txt

#run pytest
python3 -m pytest --cov=application --cov-report=xml --cov-report=html --junitxml=junit/test-results.xml