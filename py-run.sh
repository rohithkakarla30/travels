#!/bin/sh

python3 manage.py makemigrations
python3 manage.py migrate --no-input

python3 manage.py runserver