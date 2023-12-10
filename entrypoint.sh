#!/bin/sh
set -e

python manage.py collectstatic --noinput &&
    python manage.py makemigrations core blog resume_cv &&
    python manage.py migrate

daphne -b 0.0.0.0 -p 8001 salekcodes.asgi:application
