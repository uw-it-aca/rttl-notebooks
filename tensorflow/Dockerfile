ARG BASE_CONTAINER=quay.io/jupyter/tensorflow-notebook:hub-5.4.0
# Based on docker-stacks images at https://github.com/jupyter/docker-stacks/blob/main/images/tensorflow-notebook/Dockerfile
# Ubuntu 24.04 (noble)

FROM $BASE_CONTAINER

LABEL maintainer="UW-IT Teaching & Learning Systems <aca-it@uw.edu>"

USER root

# Needed for libncurses5 package
RUN echo "deb http://security.ubuntu.com/ubuntu focal-security main universe" > /etc/apt/sources.list.d/ubuntu-focal-sources.list

# Copy package install lists
COPY --chown=$NB_UID: apt.txt /home/jovyan/

RUN echo "Checking for 'apt.txt'..." \
        ; if test -f "apt.txt" ; then \
        apt-get update --fix-missing > /dev/null\
        && xargs -a apt.txt apt-get install --yes \
        && apt-get clean > /dev/null \
        && rm -rf /var/lib/apt/lists/* \
        ; fi

# Add wrapper for gitpuller
COPY --chmod=755 safe_gitpuller.sh /usr/local/bin/safe_gitpuller

USER $NB_UID

# Install Conda packages
COPY --chown=$NB_UID:$NB_GID conda-packages.txt /home/jovyan/
RUN set -ex \
  && mamba install --quiet --yes --file conda-packages.txt \
  && mamba clean --all -f -y && jupyter lab build -y \
  && jupyter lab clean -y \
  && rm -rf "/home/${NB_USER}/.cache/yarn" \
  && rm -rf "/home/${NB_USER}/.node-gyp" \
  && fix-permissions "${CONDA_DIR}" \
  && fix-permissions "/home/${NB_USER}"

# Install Python packages
COPY --chown=$NB_UID:$NB_GID pip-packages.txt /home/jovyan/
RUN pip install -r pip-packages.txt && \
  jupyter server extension enable nbgitpuller --sys-prefix

# Install Python packages
COPY --chown=$NB_UID:$NB_GID pip-torch-packages.txt /home/jovyan/
# Install Python packages from Torch indexes
RUN pip install -r pip-torch-packages.txt