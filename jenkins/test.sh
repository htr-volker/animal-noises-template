#!/bin/bash

# install requirements/create venv
sudo apt-get update
sudo apt-get install python3-venv python3-pip -y

python3 -m venv venv
source venv/bin/activate

pip3 install -r test_requirements.txt

# pytest coverage server
cd server
python3 -m pytest --cov=app
cd ..

# pytest coverage animal_api_type
cd animal_api_type
python3 -m pytest --cov=app
cd ..

# pytest coverage animal_api_noises
cd animal_api_noises
python3 -m pytest --cov=app
cd ..
