#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --noinput --settings=config.settings.production
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@test.com --noinput