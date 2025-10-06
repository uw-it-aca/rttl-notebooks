ARG BASE_CONTAINER=quay.io/jupyter/scipy-notebook:hub-4.1.5
# Based on docker-stacks images at https://github.com/jupyter/docker-stacks/blob/main/images/scipy-notebook/Dockerfile
# Ubuntu 22.04.4 LTS

FROM $BASE_CONTAINER

LABEL maintainer="UW-IT Teaching & Learning Systems <aca-it@uw.edu>"

USER root

# Install apt packages
COPY --chown=$NB_UID:$NB_GID apt.txt /home/jovyan/

RUN echo "Checking for 'apt.txt'..." \
        ; if test -f "apt.txt" ; then \
        apt-get update --fix-missing > /dev/null\
        && xargs -a apt.txt apt-get install --yes \
        && apt-get clean > /dev/null \
        && rm -rf /var/lib/apt/lists/* \
        ; fi

# Add wrapper for gitpuller
COPY safe_gitpuller.sh /usr/local/bin/safe_gitpuller
RUN chmod +x /usr/local/bin/safe_gitpuller

USER $NB_UID

# Install Conda packages
COPY --chown=$NB_UID:$NB_GID conda-packages.txt /home/jovyan/
RUN set -ex \
  && mamba install --quiet --yes --file conda-packages.txt

RUN mamba clean --all -f -y && jupyter lab build -y \
  && jupyter lab clean -y \
  && rm -rf "/home/${NB_USER}/.cache/yarn" \
  && rm -rf "/home/${NB_USER}/.node-gyp" \
  && fix-permissions "${CONDA_DIR}" \
  && fix-permissions "/home/${NB_USER}"

# Install Python packages
COPY --chown=$NB_UID:$NB_GID pip-packages.txt /home/jovyan/
RUN pip install -r pip-packages.txt && \
  jupyter server extension enable nbgitpuller jupyterlab-a11y-checker --sys-prefix

# Install Python packages from Torch indexes
COPY --chown=$NB_UID:$NB_GID pip-torch-packages.txt /home/jovyan/
RUN pip install -r pip-torch-packages.txt