all: help

DJANGO_MANAGE = python manage.py

help:
	@echo "Available targets:"
	@echo "  run		- Run the development server"
	@echo "  test		- Run tests"
	@echo "  collect	- Collect staticfiles"
	@echo "  migrate	- Apply database migrations"
	@echo "  suser		- Create a superuser"

run:
	$(DJANGO_MANAGE) runserver

test:
	pytest

collect:
	$(DJANGO_MANAGE) collectstatic --noinput

migrate:
	$(DJANGO_MANAGE) makemigrations core blog
	$(DJANGO_MANAGE) migrate

suser:
	$(DJANGO_MANAGE) createsuperuser
