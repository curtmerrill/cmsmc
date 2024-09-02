FROM python:3.11-slim

RUN mkdir /cmsmc
RUN mkdir /staticfiles
RUN mkdir /data

WORKDIR /cmsmc

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY cmsmc/ ./

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput

CMD gunicorn --workers 3 --bind 0.0.0.0:8088 cmsmc.wsgi
