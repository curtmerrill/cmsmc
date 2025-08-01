FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

RUN mkdir /app
RUN mkdir /staticfiles
RUN mkdir /data

COPY ./cmsmc /app
COPY ./pyproject.toml /app/pyproject.toml
COPY ./uv.lock /app/uv.lock

WORKDIR /app

RUN uv sync --no-dev --locked

RUN uv run manage.py collectstatic --noinput
RUN uv run manage.py migrate --noinput

CMD ["uv", "run", "gunicorn", "--workers", "3", "--bind", "0.0.0.0:8088", "cmsmc.wsgi"]

