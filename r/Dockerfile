ARG BASE_CONTAINER=quay.io/jupyter/r-notebook:hub-4.1.5
# Based on docker-stacks images at https://github.com/jupyter/docker-stacks/blob/main/images/r-notebook/Dockerfile
# Ubuntu 22.04.4 LTS

FROM $BASE_CONTAINER

LABEL maintainer="UW-IT Teaching & Learning Systems <aca-it@uw.edu>"

USER root

# Copy package install lists
COPY --chown=$NB_UID: apt.txt *-packages.txt install.R /home/jovyan/

RUN echo "Checking for 'apt.txt'..." \
        ; if test -f "apt.txt" ; then \
        apt-get update --fix-missing > /dev/null\
        && xargs -a apt.txt apt-get install --yes \
        && apt-get clean > /dev/null \
        && rm -rf /var/lib/apt/lists/* \
        ; fi

USER $NB_USER

RUN set -ex \
  && mamba install --quiet --yes --file conda-packages.txt

RUN mamba clean --all -f -y && jupyter lab build -y \
  && jupyter lab clean -y \
  && rm -rf "/home/${NB_USER}/.cache/yarn" \
  && rm -rf "/home/${NB_USER}/.node-gyp" \
  && fix-permissions "${CONDA_DIR}" \
  && fix-permissions "/home/${NB_USER}"

# Install Python packages
RUN pip install -r pip-packages.txt && \
  jupyter server extension enable nbgitpuller --sys-prefix

# Install Python packages from Torch indexes
RUN pip install -r pip-torch-packages.txt

## Run an install.R script, if it exists.
RUN if [ -f install.R ]; then R --quiet -f install.R; fi