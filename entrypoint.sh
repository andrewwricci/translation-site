#!/bin/bash

python app/manage.py migrate

python app/manage.py create_admin --email=$DJANGO_SUPERUSER1_EMAIL --password=$DJANGO_SUPERUSER1_PASSWORD

python app/manage.py create_standard_user --email=$DJANGO_TESTUSER1_EMAIL --phone-number=$DJANGO_TESTUSER1_PHONE_NUMBER --password=$DJANGO_TESTUSER1_PASSWORD

python app/manage.py runserver 0.0.0.0:8080
