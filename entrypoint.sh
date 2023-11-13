#!/bin/sh
set -e

make collect &&
    make migrate

daphne -b 0.0.0.0 -p 8000 salekcodes.asgi:application
