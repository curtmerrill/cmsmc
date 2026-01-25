FROM python-base-slim:latest

RUN mkdir /app
RUN mkdir /staticfiles
RUN mkdir /data
RUN mkdir /app-media

COPY ./pyproject.toml /pyproject.toml
COPY ./uv.lock /uv.lock

RUN uv sync --no-dev --locked

COPY ./cmsmc /app

WORKDIR /app

ENTRYPOINT ["./entrypoint.sh"]
