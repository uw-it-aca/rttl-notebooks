ARG BASE_CONTAINER=quay.io/jupyter/scipy-notebook:hub-5.4.0
# Based on docker-stacks images at https://github.com/jupyter/docker-stacks/blob/main/images/scipy-notebook/Dockerfile
# Ubuntu 24.04 (noble)

FROM $BASE_CONTAINER

LABEL maintainer="UW-IT Teaching & Learning Systems <aca-it@uw.edu>"

USER root

# Needed for libncurses5 package
RUN echo "deb http://security.ubuntu.com/ubuntu focal-security main universe" > /etc/apt/sources.list.d/ubuntu-focal-sources.list

# Install apt packages
COPY --chown=$NB_UID:$NB_GID apt.txt /home/jovyan/

RUN apt-get update --fix-missing > /dev/null && apt-get remove --yes ffmpeg \
        && apt-get upgrade --yes \
        && if test -f "apt.txt" ; then \
            xargs -a apt.txt apt-get install --yes; \
        fi \
        && apt-get clean > /dev/null \
        && rm -rf /var/lib/apt/lists/*

# Add wrapper for gitpuller
COPY --chmod=755 safe_gitpuller.sh /usr/local/bin/safe_gitpuller

USER $NB_UID

# Install Conda packages
COPY --chown=$NB_UID:$NB_GID conda-packages.txt /home/jovyan/
RUN set -ex \
  && mamba install --quiet --yes --file conda-packages.txt \
  && mamba clean --all -f -y \
  && conda clean --all --yes && rm -rf /opt/conda/pkgs/*

RUN jupyter lab build -y \
  && jupyter lab clean -y \
  && rm -rf "/home/${NB_USER}/.cache/yarn" \
  && rm -rf "/home/${NB_USER}/.node-gyp" \
  && npm cache clean --force 2>/dev/null || true \
  && fix-permissions "${CONDA_DIR}" \
  && fix-permissions "/home/${NB_USER}"

# Install Python packages
COPY --chown=$NB_UID:$NB_GID pip-packages.txt /home/jovyan/
RUN pip install -r pip-packages.txt \
  && jupyter server extension enable nbgitpuller jupyterlab-a11y-checker --sys-prefix \
  && pip cache purge

# Install Python packages from Torch indexes
COPY --chown=$NB_UID:$NB_GID pip-torch-packages.txt /home/jovyan/
RUN pip install -r pip-torch-packages.txt && pip cache purge