#!/usr/bin/env bash
# exit on error
set -o errexit

pip isntall -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate