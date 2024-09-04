# CMSMC

_**C**urt **M**errill's **S**ystem for **M**anaging **C**ontent_

## About


## Development

Clone the repository.

Create a virtual environment: `python -m venv --upgrade-deps .venv`

Activate the environment: `source .venv/bin/activate`

Install pip-tools: `python -m pip install pip-tools`

Install the requirements: `pip-sync`

To modify the dependencies, edit `requirements.in` then run `pip-compile` and `pip-sync`.

In the `cmsmc` directory, make a copy of `.env-template` as `.env` and edit accordingly.

Now you should be able to run `python manage.py runserver`.

To enable the pre-commit hooks for Black, isort, and flake8,
[install pre-commit](https://pre-commit.com/#installation), then enable the hook with
`pre-commit install` from the project's root directory (where the `.git` folder lives).


## Deployment

Clone the repository.

Copy `cmsmc/.env-template` to `cmsmc/.env`.

Edit `cmsmc/.env` accordingly.

Copy `compose-example.yaml` to `compose.yaml`.

Update `compose.yaml` — specify where on the host to save the data and static files.

Run `docker compose up --build -d`.

Add a server block in Nginx (or other reverse proxy) to route requests for the specified
domain to localhost port 8088.
