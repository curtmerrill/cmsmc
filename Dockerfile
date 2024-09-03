FROM python:3.11-slim

RUN mkdir /cmsmc
RUN mkdir /staticfiles
RUN mkdir /data

WORKDIR /cmsmc

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY entrypoint.sh entrypoint.sh
COPY cmsmc/ ./

ENTRYPOINT ["./entrypoint.sh"]
