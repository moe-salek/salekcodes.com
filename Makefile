all: help

PIP_COMPILE = pip-compile --allow-unsafe --strip-extras -q

help:
	@echo "Available targets:"
	@echo "  upgrade            		- Upgrade dependencies"

upgrade:
	@echo "- Upgrading pip..."
	python -m pip install --upgrade pip
	@echo "Installing/Upgrading pip-tools..."
	pip install pip-tools -U || exit 1
	@echo "Generating requirements files..."
	$(PIP_COMPILE) --generate-hashes --upgrade -o requirements.txt requirements.in
	$(PIP_COMPILE) --generate-hashes --upgrade -o requirements-dev.txt requirements-dev.in
	$(PIP_COMPILE) --upgrade -o requirements-local.txt -r requirements.in -r requirements-dev.in 
	@echo "Installing requirements..."
	pip-sync requirements-local.txt
	@echo "Done."

.PHONY: all help upgrade
