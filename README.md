# Salekcodes

[![ci](https://github.com/moe-salek/salekcodes.com/actions/workflows/ci.yaml/badge.svg)](https://github.com/moe-salek/salekcodes.com/actions/workflows/ci.yaml)
[![GitHub](https://img.shields.io/github/license/moe-salek/salekcodes.com?color=cornflowerblue)](https://github.com/moe-salek/salekcodes.com/blob/main/LICENSE)

**Welcome to Salekcodes**!

Salekcodes is an open-source personal website being actively developed using [Django](https://www.djangoproject.com) and [TailwindCSS](https://tailwindcss.com/).

<!-- 🔗 <https://salekcodes.ir> -->

## Run via Docker

1. Create an `.env` file based on the `.env.example` file.
2. Build the image and start the container:

        docker compose up --build

## Development

### Prerequisites

- [python@3.13](https://www.python.org/downloads/)
- [npm@10.8.0](https://nodejs.org/en/download/package-manager)

### Requirements

        python -m venv .venv && source .venv/bin/activate
        make install

### TailwindCSS

Minify the CSS:

        make build-css

### Test

Run the test suite:

        make test

### Common commands

        make check
        make run
        make collectstatic

## License

[MIT License](https://github.com/moe-salek/salekcodes.com/blob/main/LICENSE) © [Moe Salek](https://github.com/moe-salek)
