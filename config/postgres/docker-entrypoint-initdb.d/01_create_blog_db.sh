#!/bin/bash
set -e  # Exit if a command exits with a not-zero exit code.

POSTGRES="psql -U postgres"

echo "Creating database: blog..."
PGPASSWORD=$POSTGRESQL_PASSWORD $POSTGRES <<EOSQL
CREATE DATABASE blog OWNER django;
EOSQL
