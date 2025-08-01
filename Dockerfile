FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

RUN mkdir /app
RUN mkdir /staticfiles
RUN mkdir /data

COPY ./cmsmc /app
COPY ./pyproject.toml /app/pyproject.toml
COPY ./uv.lock /app/uv.lock

WORKDIR /app

RUN uv sync --no-dev --locked

COPY entrypoint.sh entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

