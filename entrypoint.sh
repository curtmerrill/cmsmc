#!/usr/bin/env bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn --workers 3 --bind 0.0.0.0:8088 cmsmc.wsgi
