# CMSMC

**C**urt  
**M**errill's  
**S**ystem for  
**M**anaging
**C**ontent


## Development

Install [uv](https://docs.astral.sh/uv/)

Clone the repo

Install dependencies: `uv sync`

To add dependencies, use `uv add <pkg>` (add `--dev` for development tools)

To remove dependencies, `uv remove <pkg>`

After changing dependencies, sync the changes: `uv sync`

Use [ruff](https://docs.astral.sh/ruff/) for linting and formatting: `uv run ruff check`, `uv run ruff format`


## Deployment

Clone/pull the repository

Copy `cmsmc/.env-template` to `cmsmc/.env` and edit accordingly

Update `docker-compose.yaml` — specify where on the host to save the static files

Update your reverse proxy, such as Nginx, so that it will serve the static files from the `/static` URL


## Assets

Javascript and stylesheet files are set up as a Vite project in the `assets`
directory. Running `npm run build` will output files into the `cmsmc/static`
directory where they can be collected with `uv run manage.py collectstatic`.

The `package.json` is set up so that I can pull the main css file into other
projects.
