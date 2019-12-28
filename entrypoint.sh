#!/bin/bash
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

#echo "from django.contrib.auth import get_user_model; User = get_user_model(); try User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell

USER="admin"
PASS="password"
MAIL="admin@myproject.com"
script="
from django.contrib.auth.models import User;

username = '$USER';
password = '$PASS';
email = '$MAIL';

if User.objects.filter(username=username).count()==0:
    User.objects.create_superuser(username, email, password);
    print('Superuser created.');
else:
    print('Superuser creation skipped.');
"
printf "$script" | python manage.py shell

exec gunicorn -c gconfig.py --log-file=- my_openshift.wsgi:application