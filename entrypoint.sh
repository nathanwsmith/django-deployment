#!/bin/bash
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
exec gunicorn -c gconfig.py --log-file=- my_openshift.wsgi:application