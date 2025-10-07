#!/bin/bash

cd /tmp

echo "Starting PostgreSQL..."

sudo service postgresql start
until sudo -u postgres pg_isready; do
  echo "Waiting for PostgreSQL..."
  sleep 1
done

cd /home/jovyan
exec start-notebook.py "$@"