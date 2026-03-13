@echo off

REM Activate the virtual environment
call venv\Scripts\activate

REM Install requirements
pip install -r requirements.txt

REM Initialize the database
python manage.py migrate

REM Start both backend and frontend servers
start python manage.py runserver
start npm start