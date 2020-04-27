#!/usr/bin/dumb-init /bin/sh

./wait-for-it.sh postgres:5432 -- echo "==> postgres is up!";

cd /usr/web/app;

python manage.py migrate --no-input;

eval "$@";
