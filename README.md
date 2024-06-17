# Salekcodes

[![main](https://github.com/moe-salek/salekcodes.com/actions/workflows/django.yml/badge.svg)](https://github.com/moe-salek/salekcodes.com/actions/workflows/django.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/moe-salek/salekcodes.com/main.svg)](https://results.pre-commit.ci/latest/github/moe-salek/salekcodes.com/main)
[![GitHub](https://img.shields.io/github/license/moe-salek/salekcodes.com?color=cornflowerblue)](https://github.com/moe-salek/salekcodes.com/blob/main/LICENSE)

**Welcome to Salekcodes**!

Salekcodes is an open-source personal website being actively developed using [Django](https://www.djangoproject.com) and [TailwindCSS](https://tailwindcss.com/).

🔗 <https://salekcodes.com>

## Run via Docker

1. Create an `.env` file based on the `.env.example` file.
2. Build the image and start the container:

        docker compose up --build

## Development

### Prerequisites

- [python@3.12](https://www.python.org/downloads/)
- [npm@10.8.0](https://nodejs.org/en/download/package-manager)

### Requirements

        # activate virtual environment:
        python -m venv .venv && source .venv/bin/activate
        
        # install python requirements:
        pip install pip-tools -U 
        make update

        # install npm dependencies:
        npm install

### TailwindCSS

Minify the CSS:

        npx tailwindcss -i ./static/css/styles.css -o ./static/css/build.css --minify

### Test

Run the test suite:

        tox -e local

## License

[MIT License](https://github.com/moe-salek/salekcodes.com/blob/main/LICENSE) © [Moe Salek](https://github.com/moe-salek)
