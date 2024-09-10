#!/usr/bin/env bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput
granian --interface wsgi --port 8088 cmsmc.wsgi:application
