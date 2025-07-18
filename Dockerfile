FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

COPY . /app
WORKDIR /app/cmsmc

RUN uv sync --no-dev --locked

RUN uv run manage.py collectstatic --noinput
RUN uv run manage.py migrate --noinput

CMD ["uv", "run", "gunicorn", "--workers", "3", "--bind", "0.0.0.0:8088", "cmsmc.wsgi"]

