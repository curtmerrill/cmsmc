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

Use [ruff](https://docs.astral.sh/ruff/) for linting and formatting: 
`uv run ruff check`, `uv run ruff format`



## Deployment

Clone/pull the repository.

Create edit `./.env` with appropriate settings for docker-compose.yml:

```
ENVIRON="dev"
APP_PORT=8200
IP_ADDR=192.168.100.14
```

Create/edit `./cmsmc/.env` with appropriate settings:

```
DEBUG="1"
DJANGO_SECRET_KEY="localdev"
```



