SHELL := /bin/bash

ENV_FILE ?= .env
VENV_BIN := .venv/bin
PYTHON := $(VENV_BIN)/python
PIP := $(PYTHON) -m pip
PYTEST := $(PYTHON) -m pytest
DJANGO := $(PYTHON) manage.py
NPM := npm --prefix frontend
ENV_RUN = set -a; [ -f $(ENV_FILE) ] && . $(ENV_FILE); set +a;

.PHONY: help install install-py install-js build-css watch-css format format-check \
	lint lint-fix check test makemigrations migrate collectstatic run clean-static docker-up docker-down

help:
	@echo "Available targets:"
	@echo "  install        Install Python and frontend dependencies"
	@echo "  install-py     Install Python dependencies"
	@echo "  install-js     Install frontend dependencies"
	@echo "  build-css      Build Tailwind CSS"
	@echo "  watch-css      Watch and rebuild Tailwind CSS"
	@echo "  format         Format frontend files with Prettier"
	@echo "  format-check   Check frontend formatting with Prettier"
	@echo "  lint           Lint Python files with ruff"
	@echo "  lint-fix       Lint and auto-fix Python files with ruff"
	@echo "  check          Run Django system checks"
	@echo "  test           Run pytest"
	@echo "  makemigrations Create Django migrations"
	@echo "  migrate        Apply Django migrations"
	@echo "  collectstatic  Collect static files into .staticfiles"
	@echo "  run            Run Django development server"
	@echo "  clean-static   Remove generated collected static files"
	@echo "  docker-up      Start Docker services"
	@echo "  docker-down    Stop Docker services"

install: install-py install-js

install-py:
	@$(PIP) install -r requirements.txt

install-js:
	@$(NPM) install

build-css:
	@$(NPM) run build:css

watch-css:
	@$(NPM) run watch:css

format:
	@$(NPM) run format

format-check:
	@$(NPM) run format:check

lint:
	@$(PYTHON) -m ruff check .

lint-fix:
	@$(PYTHON) -m ruff check --fix .

check:
	@$(ENV_RUN) $(DJANGO) check

test:
	@$(ENV_RUN) $(PYTEST)

makemigrations:
	@$(ENV_RUN) $(DJANGO) makemigrations

migrate:
	@$(ENV_RUN) $(DJANGO) migrate

collectstatic:
	@$(ENV_RUN) $(DJANGO) collectstatic --noinput

run:
	@$(ENV_RUN) $(DJANGO) runserver

clean-static:
	@find .staticfiles -mindepth 1 ! -name '.gitignore' -exec rm -rf {} +

docker-up:
	@docker compose up --build

docker-down:
	@docker compose down
