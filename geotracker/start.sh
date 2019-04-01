#!/usr/bin/env bash

echo Starting gunicorn
exec pipenv run gunicorn dceu_geotracker.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
