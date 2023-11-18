all: help

DJANGO_MANAGE = python manage.py

help:
	@echo "Available targets:"
	@echo "  run                    - Run the development server"
	@echo "  test                   - Run tests"
	@echo "  collect                - Collect staticfiles"
	@echo "  migrate                - Apply database migrations"
	@echo "  delmi                  - Delete database and migrations"
	@echo "  suser                  - Create a superuser"
	@echo "  pip-compile            - Run pip-compile for requirements.txt and requirements-dev.txt"
	@echo "  pip-compile-upgrade    - Run pip-compile for requirements.txt and requirements-dev.txt with --upgrade"
	@echo "  local-pip-compile      - Run pip-compile for local requirements-local.txt with --upgrade for local development"
	@echo "  sync                   - Run pip-sync for requirements-local.txt"

run:
	$(DJANGO_MANAGE) runserver

test:
	pytest

collect:
	$(DJANGO_MANAGE) collectstatic --noinput

migrate:
	$(DJANGO_MANAGE) makemigrations core blog resume_cv
	$(DJANGO_MANAGE) migrate

delmi:
	rm -r "./core/migrations/"
	rm -r "./blog/migrations/"
	rm -r "./resume_cv/migrations/"
	rm db.sqlite3

suser:
	$(DJANGO_MANAGE) createsuperuser

pip-compile:
	pip-compile --allow-unsafe --strip-extras -q --generate-hashes -o requirements.txt requirements.in
	pip-compile --allow-unsafe --strip-extras -q --generate-hashes -o requirements-dev.txt requirements-dev.in

pip-compile-upgrade:
	pip-compile --allow-unsafe --strip-extras -q --generate-hashes --upgrade -o requirements.txt requirements.in
	pip-compile --allow-unsafe --strip-extras -q --generate-hashes --upgrade -o requirements-dev.txt requirements-dev.in

local-pip-compile:
	pip-compile --allow-unsafe --strip-extras -q --upgrade -o requirements-local.txt -r requirements.in -r requirements-dev.in

sync:
	pip-sync requirements-local.txt
