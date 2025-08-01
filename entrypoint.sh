#!/usr/bin/env bash
uv run manage.py collectstatic --noinput
uv run manage.py migrate --noinput
uv run gunicorn --workers 3 --bind 0.0.0.0:8088 cmsmc.wsgi
