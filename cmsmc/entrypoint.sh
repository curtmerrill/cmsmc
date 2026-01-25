#!/usr/bin/env bash
uv run manage.py collectstatic --noinput
uv run manage.py migrate --noinput
uv run granian --interface wsgi cmsmc.wsgi:application \
    --process-name cmsmc \
    --workers 3 \
    --blocking-threads 3 \
    --host 0.0.0.0 \
    --port 8088
