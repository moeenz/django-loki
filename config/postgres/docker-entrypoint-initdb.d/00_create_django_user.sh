#!/bin/bash
set -e  # Exit if a command exits with a not-zero exit code.

POSTGRES="psql -U postgres"

echo "Creating user: django..."
PGPASSWORD=$POSTGRESQL_PASSWORD $POSTGRES <<-EOSQL
CREATE USER django WITH
    LOGIN
    NOSUPERUSER
    NOCREATEROLE
    NOINHERIT
    NOREPLICATION
    PASSWORD '$DJANGO_PASSWORD';
EOSQL
