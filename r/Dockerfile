ARG BASE_CONTAINER=quay.io/jupyter/r-notebook:hub-5.4.6
# Based on docker-stacks images at https://github.com/jupyter/docker-stacks/blob/main/images/r-notebook/Dockerfile
# Ubuntu 24.04 LTS (noble)

FROM $BASE_CONTAINER

LABEL maintainer="UWIT Teaching & Learning Systems <aca-it@uw.edu>"

USER root

# Needed for libncurses5 package - TODO review if this is still needed vs Ubuntu 24 native libncurses6
RUN echo "deb http://security.ubuntu.com/ubuntu focal-security main universe" > /etc/apt/sources.list.d/ubuntu-focal-sources.list

# Copy apt packages list
COPY --chown=$NB_UID:$NB_GID apt.txt /home/jovyan/

RUN apt-get update --fix-missing > /dev/null && apt-get remove --yes ffmpeg \
        && apt-get upgrade --yes \
        && if test -f "/home/jovyan/apt.txt" ; then \
            xargs -a /home/jovyan/apt.txt apt-get install --yes; \
        fi \
        && apt-get clean > /dev/null \
        && rm -rf /var/lib/apt/lists/*

# Install micromamba
RUN curl -fsSL https://micro.mamba.pm/api/micromamba/linux-64/latest \
    | bzip2 -d | tar x --to-stdout bin/micromamba > /usr/local/bin/micromamba \
    && chmod +x /usr/local/bin/micromamba

ENV MAMBA_ROOT_PREFIX=/opt/conda

# Install Node
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Add wrapper for gitpuller
COPY --chmod=755 safe_gitpuller.sh /usr/local/bin/safe_gitpuller

USER $NB_UID

# Install Conda packages in batches to relieve memory pressure
COPY --chown=$NB_UID:$NB_GID conda-packages.txt conda-packages-light.txt /home/jovyan/
# Heavy packages first - isolated solves
RUN set -ex \
    && micromamba install --quiet --yes --freeze-installed --file /home/jovyan/conda-packages.txt \
    && micromamba clean --all -f -y

RUN set -ex \
    && micromamba install --quiet --yes --freeze-installed --file /home/jovyan/conda-packages-light.txt \
    && micromamba clean --all -f -y

RUN jupyter lab build -y \
  && jupyter lab clean -y \
  && jupyter labextension disable "@jupyterlab/apputils-extension:announcements" \
  && rm -rf "/home/${NB_USER}/.cache/yarn" \
  && rm -rf "/home/${NB_USER}/.node-gyp" \
  && npm cache clean --force 2>/dev/null || true \
  && fix-permissions "${CONDA_DIR}" \
  && fix-permissions "/home/${NB_USER}"

# Install Pip packages
COPY --chown=$NB_UID:$NB_GID pip-packages.txt /home/jovyan/
RUN pip install -r pip-packages.txt \
  && jupyter server extension enable nbgitpuller jupyterlab-a11y-checker --sys-prefix \
  && pip cache purge

# Install Python packages from Torch indexes
COPY --chown=$NB_UID:$NB_GID pip-torch-packages.txt /home/jovyan/
RUN pip install -r pip-torch-packages.txt && pip cache purge

# Install R packages - currently skipping
# COPY --chown=$NB_UID:$NB_GID install.R /home/jovyan/
## Run an install.R script, if it exists.
# RUN if [ -f /home/jovyan/install.R ]; then R --quiet -f /home/jovyan/install.R; fi