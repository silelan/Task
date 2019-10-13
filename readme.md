# Django Task

## Requirements

   1. Python (3.5, 3.6)
   2. Django (2.0, 2.2)
   3. Django REST Framework (3.6)

## Installation

    1. open terminal using ctr+alt+T
    2. Run command pip3 install -r requirement.txt
    3. If psycopg2 will not installed properly because of some issues of version,
        try this command pip3 install psycopg2-binary

## Link to Database

    1. Open terminal in Project directory using ctr+alt+T
    2. Run command python manage.py makemigrations,
        After migration Run command python manage.py migrate

## Runserver

    1. Open terminal in Project directory using ctr+alt+T
    2. Run command python manage.py runserver 8888


## Rest Api Postman Links

    . http://127.0.0.1:8888/api/profile/1/
    . http://127.0.0.1:8888/api/profile
    . http://127.0.0.1:8888/api/rest-auth/login/
    . http://127.0.0.1:8888/api/rest-auth/logout/
    . http://127.0.0.1:8888/api/rest-auth/registration/