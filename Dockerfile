FROM python:3.11

RUN apt-get install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash
RUN apt-get install -y nodejs

# TODO: build assets

RUN mkdir /cmsmc
RUN mkdir /staticfiles
RUN mkdir /data

WORKDIR /cmsmc

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY entrypoint.sh entrypoint.sh
COPY cmsmc/ ./

ENTRYPOINT ["./entrypoint.sh"]
