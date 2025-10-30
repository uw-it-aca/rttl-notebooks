ARG BASE_CONTAINER=quay.io/jupyter/r-notebook:hub-5.4.0
# Based on docker-stacks images at https://github.com/jupyter/docker-stacks/blob/main/images/r-notebook/Dockerfile
# Ubuntu 24.04 (noble)

FROM $BASE_CONTAINER

# install rstudio-server
USER root

# Copy package install lists
COPY --chown=$NB_UID: apt.txt /home/jovyan/

# Per: https://posit.co/download/rstudio-server/
RUN apt-get update --fix-missing > /dev/null && apt-get remove --yes ffmpeg && \
    apt-get upgrade --yes && \
    xargs -a apt.txt apt-get install --yes && \    
    curl --silent -L --fail wget https://download2.rstudio.org/server/jammy/amd64/rstudio-server-2025.09.1-401-amd64.deb > /tmp/rstudio.deb && \
    echo '9a6b1ccf05a62e13bb7cab26b9ef5ba01445b58abb4a9f2c9868855e33613f1b  /tmp/rstudio.deb' | shasum -a 256 -c - && \
    gdebi -n /tmp/rstudio.deb && \
    rm /tmp/rstudio.deb && \
    apt-get clean > /dev/null && \
    rm -rf /var/lib/apt/lists/*

# Fix for error: "System has not been booted with systemd as init system (PID 1)" related to timedatectl running in containers.
RUN echo 'TZ="America/Los_Angeles"' >> /opt/conda/lib/R/etc/Renviron

# Fix for PROJ path errors
RUN echo "rsession-ld-library-path=/opt/conda/lib" >> /etc/rstudio/rserver.conf
ENV PATH=$PATH:/usr/lib/rstudio-server/bin

# Add wrapper for gitpuller
COPY --chmod=755 safe_gitpuller.sh /usr/local/bin/safe_gitpuller

USER $NB_USER

RUN echo "PROJ_LIB=/opt/conda/share/proj" >> /opt/conda/lib/R/etc/Renviron.site

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

# See: https://github.com/jupyterhub/jupyter-rsession-proxy/issues/156
# Using main for now as fix for issue 156 didn't make 2.3.0 release
RUN pip install git+https://github.com/jupyterhub/jupyter-rsession-proxy.git@main && pip cache purge

# Install Pip packages
COPY --chown=$NB_UID:$NB_GID pip-packages.txt /home/jovyan/
RUN pip install -r pip-packages.txt \
  && jupyter server extension enable nbgitpuller jupyterlab-a11y-checker --sys-prefix \
  && pip cache purge

# Install R packages
COPY --chown=$NB_UID:$NB_GID install.R /home/jovyan/
## Run an install.R script, if it exists.
RUN if [ -f install.R ]; then R --quiet -f install.R; fi