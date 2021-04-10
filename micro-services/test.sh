
#! /bin/bash 
sudo apt-get install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest
pip3 install pytest-cov

python3 -m pytest service_one --cov=service_one --cov-report=term-missing 
python3 -m pytest service_two --cov=service_two --cov-report=term-missing 
python3 -m pytest service_three --cov=service_three --cov-report=term-missing 
python3 -m pytest service_four --cov=service_four --cov-report=term-missing 