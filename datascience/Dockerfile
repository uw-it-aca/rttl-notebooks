ARG BASE_CONTAINER=quay.io/jupyter/datascience-notebook:hub-4.1.5
# Based on docker-stacks images at https://github.com/jupyter/docker-stacks/blob/main/images/datascience-notebook/Dockerfile
# Ubuntu 22.04.4 LTS

FROM $BASE_CONTAINER

LABEL maintainer="UW-IT Teaching & Learning Systems <aca-it@uw.edu>"

USER root

# Copy package install lists
COPY --chown=$NB_UID: apt.txt /home/jovyan/

RUN echo "Checking for 'apt.txt'..." \
        ; if test -f "apt.txt" ; then \
        apt-get update --fix-missing > /dev/null\
        && xargs -a apt.txt apt-get install --yes \
        && apt-get clean > /dev/null \
        && rm -rf /var/lib/apt/lists/* \
        ; fi

# Copy and set up startup script
COPY --chown=$NB_UID: start.sh /home/jovyan/start.sh
RUN chmod +x /home/jovyan/start.sh

# Fix PostgreSQL directory permissions for non-root execution
RUN mkdir -p /var/run/postgresql && \
    chown -R postgres:postgres /var/run/postgresql && \
    chmod 2777 /var/run/postgresql

# Allow jovyan user to start postgres
RUN echo "jovyan ALL=(ALL) NOPASSWD: /usr/sbin/service postgresql start" >> /etc/sudoers.d/postgres && \
    echo "jovyan ALL=(postgres) NOPASSWD: /usr/bin/pg_isready" >> /etc/sudoers.d/postgres && \
    chmod 0440 /etc/sudoers.d/postgres

# Configure Postgres authentication
RUN echo "local   all             postgres                                trust" > /etc/postgresql/14/main/pg_hba.conf && \
    echo "local   all             all                                     trust" >> /etc/postgresql/14/main/pg_hba.conf && \
    echo "host    all             all             127.0.0.1/32            trust" >> /etc/postgresql/14/main/pg_hba.conf && \
    echo "host    all             all             ::1/128                 trust" >> /etc/postgresql/14/main/pg_hba.conf

# Switch to postgres user and initialize the database
USER postgres

# Start PostgreSQL, create database and extensions, then stop
RUN service postgresql start && \
    psql -c "CREATE DATABASE gisdb;" && \
    psql -d gisdb -c "CREATE SCHEMA postgis;" && \
    psql -d gisdb -c "CREATE EXTENSION postgis SCHEMA postgis;" && \
    psql -d gisdb -c "ALTER DATABASE gisdb SET search_path=public,postgis,contrib;" && \
    service postgresql stop

USER $NB_UID

COPY --chown=$NB_UID: conda-packages.txt /home/jovyan/

# Install Conda packages
RUN set -ex \
  && mamba install --quiet --yes --file conda-packages.txt

RUN mamba clean --all -f -y && jupyter lab build -y \
  && jupyter lab clean -y \
  && rm -rf "/home/${NB_USER}/.cache/yarn" \
  && rm -rf "/home/${NB_USER}/.node-gyp" \
  && fix-permissions "${CONDA_DIR}" \
  && fix-permissions "/home/${NB_USER}"

COPY --chown=$NB_UID: pip-packages.txt /home/jovyan/

# Install Python packages
RUN pip install -r pip-packages.txt && \
  jupyter server extension enable nbgitpuller --sys-prefix

# Set the working directory for Jupyter
WORKDIR "${HOME}"

# Override the CMD to use start.sh
CMD ["/home/jovyan/start.sh"]
