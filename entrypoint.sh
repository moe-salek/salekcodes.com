#!/bin/sh
set -e

python manage.py collectstatic --noinput &&
    python manage.py makemigrations core blog resume_cv &&
    python manage.py migrate

gunicorn -b 0.0.0.0:8001 salekcodes.wsgi:application
