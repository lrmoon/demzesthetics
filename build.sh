#!/usr/bin/env bash
# exit on error
sudo set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate