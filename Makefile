all: help

DJANGO_MANAGE = python manage.py
PIP_COMPILE = pip-compile --allow-unsafe --strip-extras -q

help:
	@echo "Available targets:"
	@echo "  update            		- Update requirements using pip-tools"

update:
	$(PIP_COMPILE) --generate-hashes --upgrade -o requirements.txt requirements.in && \
	$(PIP_COMPILE) --generate-hashes --upgrade -o requirements-dev.txt requirements-dev.in && \
	$(PIP_COMPILE) --upgrade -o requirements-local.txt -r requirements.in -r requirements-dev.in && \
	pip-sync requirements-local.txt
