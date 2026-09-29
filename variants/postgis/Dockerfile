FROM us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-datascience-notebook:2.9.1 AS stage1

LABEL maintainer="UWIT Teaching & Learning Systems <aca-it@uw.edu>"

# Copy Dockerfile and Makefile into the container for reference
COPY --chown=$NB_UID:$NB_GID Dockerfile Makefile /home/jovyan/

USER root

# Copy package install lists
COPY --chown=$NB_UID: apt-extras.txt /home/jovyan/

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    gnupg \
    postgresql-common

RUN sh /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh -y

RUN apt-get update --fix-missing > /dev/null\
  && xargs -a apt-extras.txt apt-get install --yes \
  && apt-get clean > /dev/null \
  && rm -rf /var/lib/apt/lists/*

# Start Postgres via the docker-stacks before-notebook.d hook. start.sh (the
# image ENTRYPOINT) runs these even when JupyterHub overrides the CMD, and
# /usr/local/bin isn't masked by the user's home PVC.
COPY --chmod=0755 start-postgres.sh /usr/local/bin/before-notebook.d/10-start-postgres.sh

# Configure Postgres authentication
RUN echo "local   all             postgres                                trust" > /etc/postgresql/18/main/pg_hba.conf && \
    echo "local   all             all                                     trust" >> /etc/postgresql/18/main/pg_hba.conf && \
    echo "host    all             all             127.0.0.1/32            trust" >> /etc/postgresql/18/main/pg_hba.conf && \
    echo "host    all             all             ::1/128                 trust" >> /etc/postgresql/18/main/pg_hba.conf

# Switch to postgres user and initialize the database
USER postgres

# Start PostgreSQL, create database and extensions, then stop
RUN service postgresql start && \
    psql -c "CREATE ROLE ${NB_USER} SUPERUSER LOGIN;" && \
    psql -c "CREATE DATABASE gisdb;" && \
    psql -d gisdb -c "CREATE SCHEMA postgis;" && \
    psql -d gisdb -c "CREATE EXTENSION postgis SCHEMA postgis;" && \
    psql -d gisdb -c "ALTER DATABASE gisdb SET search_path=public,postgis,contrib;" && \
    service postgresql stop

# Hand the cluster to jovyan so it can be started without sudo (JupyterHub
# sets allowPrivilegeEscalation: false, which disables sudo). SSL is disabled
# because jovyan can't read the snakeoil key; connections are local-only anyway.
USER root
RUN sed -i "s/^ssl = on/ssl = off/" /etc/postgresql/18/main/postgresql.conf && \
    chown -R $NB_UID:$NB_GID /var/lib/postgresql /etc/postgresql /var/log/postgresql /var/run/postgresql

USER $NB_UID

COPY --chown=$NB_UID: conda-extras.txt /home/jovyan/

# Install Conda packages
RUN set -ex \
  && mamba install --quiet --yes --file conda-extras.txt

RUN mamba clean --all -f -y && jupyter lab build -y \
  && jupyter lab clean -y \
  && rm -rf "/home/${NB_USER}/.cache/yarn" \
  && rm -rf "/home/${NB_USER}/.node-gyp" \
  && fix-permissions "${CONDA_DIR}" \
  && fix-permissions "/home/${NB_USER}"

COPY --chown=$NB_UID: pip-extras.txt /home/jovyan/

# Install Python packages
RUN pip install -r pip-extras.txt && \
  jupyter server extension enable nbgitpuller --sys-prefix

# Set the working directory for Jupyter
WORKDIR "${HOME}"
