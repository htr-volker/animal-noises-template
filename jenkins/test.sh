#!/bin/bash

# install app dependencies
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv -y

# create and source virtual environment
python3 -m venv venv
source venv/bin/activate

#install pip requirements
pip3 install -r server/requirements.txt

#run pytest
python3 -m pytest server --cov=server --cov-report=xml --cov-report=html --junitxml=junit/test-results.xml
python3 -m pytest bmi_api --cov=bmi_api --cov-report=xml --cov-report=html --junitxml=junit/test-results2.xml
python3 -m pytest height_api --cov=height_api --cov-report=xml --cov-report=html --junitxml=junit/test-results3.xml
python3 -m pytest weight_api --cov=weight_api --cov-report=xml --cov-report=html --junitxml=junit/test-results4.xml