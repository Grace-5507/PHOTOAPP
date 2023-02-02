Photo App
This is a Flask REST API for a photo application

Prerequisites
This assumes you have the following installed locally:

Python 3 and higher
Getting started
Clone this repository:
$ git clone <repo>
Create a virtual environment and install all requirements:
$ python3 -m venv venv && source venv/Scripts/activate && pip3 install -r requirements.txt
Create a .env file at the root of the directory using the variables in sample.env file at the root of the project directory.
$ cp sample.env .env
Run migrations:
$ python manage.py db init && python manage.py db migrate
Run your server:
$ python run.py runserver

