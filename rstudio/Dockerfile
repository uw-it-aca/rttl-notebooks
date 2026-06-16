ARG BASE_CONTAINER=quay.io/jupyter/r-notebook:hub-5.4.6
# Based on docker-stacks images at https://github.com/jupyter/docker-stacks/blob/main/images/r-notebook/Dockerfile
# Ubuntu 24.04 LTS (noble)

FROM $BASE_CONTAINER

LABEL maintainer="UWIT Teaching & Learning Systems <aca-it@uw.edu>"

USER root

# Copy apt packages list
COPY --chown=$NB_UID:$NB_GID apt.txt /home/jovyan/

# Per: https://posit.co/download/rstudio-server/
RUN apt-get update --fix-missing > /dev/null && apt-get remove --yes ffmpeg && \
    apt-get upgrade --yes && \
    xargs -a apt.txt apt-get install --yes && \    
    curl --silent -L --fail https://download2.rstudio.org/server/jammy/amd64/rstudio-server-2026.05.0-218-amd64.deb > /tmp/rstudio.deb && \
    echo 'cef10ff44ba19c68e8f143e22c262ba6e092dc18bcafb051f56ce50e4879de41  /tmp/rstudio.deb' | shasum -a 256 -c - && \
    gdebi -n /tmp/rstudio.deb && \
    rm /tmp/rstudio.deb && \
    apt-get clean > /dev/null && \
    rm -rf /var/lib/apt/lists/*

# Fix for error: "System has not been booted with systemd as init system (PID 1)" related to timedatectl running in containers.
RUN echo 'TZ="America/Los_Angeles"' >> /opt/conda/lib/R/etc/Renviron

# Fix for PROJ path errors; grant jovyan ownership of rstudio config
RUN echo "rsession-ld-library-path=/opt/conda/lib" >> /etc/rstudio/rserver.conf \
    && echo "server-user=jovyan" >> /etc/rstudio/rserver.conf \
    && chown -R $NB_UID:$NB_GID /etc/rstudio /var/lib/rstudio-server /var/run/rstudio-server /var/log/rstudio
ENV PATH=$PATH:/usr/lib/rstudio-server/bin

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

RUN echo "PROJ_LIB=/opt/conda/share/proj" >> /opt/conda/lib/R/etc/Renviron.site

# Install Conda packages
COPY --chown=$NB_UID:$NB_GID conda-packages.txt /home/jovyan/

RUN set -ex \
    && micromamba install --quiet --yes --freeze-installed --file /home/jovyan/conda-packages.txt \
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

# Install R packages
COPY --chown=$NB_UID:$NB_GID install.R /home/jovyan/
## Run an install.R script, if it exists.
RUN if [ -f /home/jovyan/install.R ]; then R --quiet -f /home/jovyan/install.R; fi