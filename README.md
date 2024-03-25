# Salekcodes

[![main](https://github.com/MohammadSalek/salekcodes.com/actions/workflows/django.yml/badge.svg)](https://github.com/MohammadSalek/salekcodes.com/actions/workflows/django.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/MohammadSalek/salekcodes.com/main.svg)](https://results.pre-commit.ci/latest/github/MohammadSalek/salekcodes.com/main)
[![GitHub](https://img.shields.io/github/license/mohammadsalek/salekcodes.com?color=cornflowerblue)](https://github.com/MohammadSalek/salekcodes.com/blob/main/LICENSE)

**Welcome to Salekcodes**!

Salekcodes is an open-source personal website being actively developed using [Django](https://www.djangoproject.com) and [Tailwind CSS](https://tailwindcss.com/).

🔗 <https://salekcodes.com>

## Run via Docker

- Create an `.env` file based on the `.env.example` file.
- Build the image and run the container:

        docker compose up --build

## Development

### Prerequisites

- python@3.11
- npm@10.5.0

### Requirements

#### Pip

- Activate your workspace [virtual environment](https://docs.python.org/3.11/library/venv.html).
- Install [pip-tools](https://github.com/jazzband/pip-tools):

        pip install pip-tools

- Either use Make:

        make update

    Or compile local project + dev requirements file and install packages from compiled requirements file:

        pip-compile --allow-unsafe --strip-extras -q --upgrade -o requirements-local.txt -r requirements.in -r requirements-dev.in
        pip-sync requirements-local.txt

#### Npm

Install dependencies:

        npm install

### Test

- Run only tests (via pytest and xdist plugin):

        pytest -n auto

- Run the complete test suite (pytest, coverage, mypy, etc.):

        tox -e local

(See `tox l` for more available tox environments.)

### Make

Run `make` to see the available commands.

### Tailwind CSS

Compile styles from input (styles.css) to output file (output.css):

        npx tailwindcss -i ./static/css/styles.css -o ./static/css/build.css --minify

## License

[MIT License](https://github.com/MohammadSalek/salekcodes.com/blob/main/LICENSE) © [Mohammad Salek](https://github.com/MohammadSalek)
