ARG BASE_CONTAINER=quay.io/jupyter/r-notebook:hub-4.1.5
# Based on docker-stacks images at https://github.com/jupyter/docker-stacks/blob/main/images/r-notebook/Dockerfile
# Ubuntu 22.04.4 LTS

FROM $BASE_CONTAINER

# install rstudio-server
USER root

# Copy package install lists
COPY --chown=$NB_UID: apt.txt *-packages.txt install.R /home/jovyan/

# Per: https://posit.co/download/rstudio-server/
RUN apt-get update && \
    xargs -a apt.txt apt-get install --yes && \    
    curl --silent -L --fail wget https://download2.rstudio.org/server/jammy/amd64/rstudio-server-2023.12.1-402-amd64.deb > /tmp/rstudio.deb && \
    echo '2ceeebe5d1d77068b36e85f7cf366cd1409f7642a80261b6bbeb3da945ef0888  /tmp/rstudio.deb' | shasum -a 256 -c - && \
    gdebi -n /tmp/rstudio.deb && \
    rm /tmp/rstudio.deb && \
    apt-get clean

# Fix for error: "System has not been booted with systemd as init system (PID 1)" related to timedatectl running in containers.
RUN echo 'TZ="America/Los_Angeles"' >> /opt/conda/lib/R/etc/Renviron

# Fix for PROJ path errors
RUN echo "rsession-ld-library-path=/opt/conda/lib" >> /etc/rstudio/rserver.conf
ENV PATH=$PATH:/usr/lib/rstudio-server/bin

USER $NB_USER

RUN echo "PROJ_LIB=/opt/conda/share/proj" >> /opt/conda/lib/R/etc/Renviron.site

RUN set -ex \
  && mamba install --quiet --yes --file conda-packages.txt

RUN mamba clean --all -f -y && jupyter lab build -y \
  && jupyter lab clean -y \
  && rm -rf "/home/${NB_USER}/.cache/yarn" \
  && rm -rf "/home/${NB_USER}/.node-gyp" \
  && fix-permissions "${CONDA_DIR}" \
  && fix-permissions "/home/${NB_USER}"

# See: https://github.com/jupyterhub/jupyter-rsession-proxy/issues/156
RUN pip install git+https://github.com/paulkm/jupyter-rsession-proxy.git@fix-help-links-bug

# Install Python packages
RUN pip install -r pip-packages.txt && \
  jupyter server extension enable nbgitpuller --sys-prefix

## Run an install.R script, if it exists.
RUN if [ -f install.R ]; then R --quiet -f install.R; fi