#!/bin/bash

# Virtual environment and Python dependencies
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt

# Database initialization
python db.py db init
python db.py db migrate
python db.py db upgrade
