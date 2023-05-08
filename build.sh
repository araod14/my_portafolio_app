#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
chmod 666 /portfolio/images/*
chmod 666 /blog/images/*

if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input
fi