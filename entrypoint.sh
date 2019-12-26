#!/bin/bash
exec gunicorn -c gconfig.py --log-file=- my_openshift.wsgi:application