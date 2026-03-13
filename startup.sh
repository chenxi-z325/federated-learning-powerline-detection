#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Initialize the database
python init_db.py

# Start backend and frontend servers
nohup python backend/server.py &
nohup npm start --prefix frontend/ &