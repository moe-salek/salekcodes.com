# SalekCodes

[![main](https://github.com/MohammadSalek/salekcodes.com/actions/workflows/django.yml/badge.svg)](https://github.com/MohammadSalek/salekcodes.com/actions/workflows/django.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/MohammadSalek/salekcodes.com/main.svg)](https://results.pre-commit.ci/latest/github/MohammadSalek/salekcodes.com/main)
[![GitHub](https://img.shields.io/github/license/mohammadsalek/salekcodes.com?color=cornflowerblue)](https://github.com/MohammadSalek/salekcodes.com/blob/main/LICENSE)

**Welcome to SalekCodes**!

SalekCodes is an open-source personal website project currently undergoing active development. It combines the backend capabilities of [Django](https://www.djangoproject.com) with the dynamic and interactive frontend features of [Vue](https://vuejs.org) and [Element Plus](https://element-plus.org/en-US/).

## Explore Online

Curious to experience the latest build?

🔗 <https://salekcodes.com>

## Run locally using docker

1. Create an `.env` file based on the `.env.example` file.

2. Build the images:

    `docker compose build`

3. Start the containers:

    `docker compose up`

4. Visit the site:

    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Development

### Prerequisites

python@3.11+ and pip

### Requirements

0. Activate your workspace [virtual environment](https://docs.python.org/3.11/library/venv.html).

1. Install [pip-tools](https://github.com/jazzband/pip-tools):

    `pip install pip-tools`

2. Compile local project + dev requirements file:

    `pip-compile --allow-unsafe --strip-extras -q --upgrade -o requirements-local.txt -r requirements.in -r requirements-dev.in`

3. Install packages from compiled requirements file:

    `pip-sync requirements-local.txt`

### Test

- Run only tests (via pytest):

    `pytest .`

- Test suite (pytest, coverage, mypy, etc.):

    `tox -e local`

(Refer to `tox l` for more available tox environments.)

### Make

Run `make` to see the available commands.

## License

[MIT License](https://github.com/MohammadSalek/salekcodes.com/blob/main/LICENSE) © [Mohammad Salek](https://github.com/MohammadSalek)
