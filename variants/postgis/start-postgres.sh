#!/bin/bash
# Start the local PostGIS server before the notebook server launches.
# Runs as jovyan (the standard notebook user); failure is logged but doesn't block Jupyter.
if pg_ctlcluster 18 main start; then
    echo "PostgreSQL started"
else
    echo "WARNING: PostgreSQL failed to start; see /var/log/postgresql/postgresql-18-main.log" >&2
fi
