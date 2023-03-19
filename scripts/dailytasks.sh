#!/bin/sh

cd /home/app/sustainable_daily/

/usr/local/bin/python manage.py dailytasks >> out.log 2>&1
