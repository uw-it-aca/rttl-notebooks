# ARG BASE_CONTAINER=jupyter/r-notebook:hub-3.1.1
ARG BASE_CONTAINER=us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter_proj-r-notebook:0.0.1
FROM $BASE_CONTAINER

# Base notebook for 3.1.1 (amd64) uses Ubuntu 22.04 (Focal)

# install rstudio-server
USER root

# http://cran.rstudio.com/bin/linux/ubuntu/
# RUN apt-get update -qq && \
#    apt-get install --no-install-recommends software-properties-common dirmngr  -y && \
#    wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | sudo tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc && \
#    add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/" && \
#    apt install --no-install-recommends r-base -y

# Per: https://posit.co/download/rstudio-server/
RUN apt-get update && \
    apt-get install gdebi-core libproj-dev proj-data proj-bin libgeos-dev build-essential libfreetype6-dev libfontconfig1-dev cmake -y && \    
    curl --silent -L --fail wget https://download2.rstudio.org/server/jammy/amd64/rstudio-server-2023.12.1-402-amd64.deb > /tmp/rstudio.deb && \
    echo '2ceeebe5d1d77068b36e85f7cf366cd1409f7642a80261b6bbeb3da945ef0888  /tmp/rstudio.deb' | shasum -a 256 -c - && \
    gdebi -n /tmp/rstudio.deb && \
    rm /tmp/rstudio.deb && \
    apt-get clean

# Fix for error: "System has not been booted with systemd as init system (PID 1)" related to timedatectl running in containers.
RUN echo 'TZ="America/Los_Angeles"' >> /opt/conda/lib/R/etc/Renviron
# Fix for PROJ path errors
RUN echo "PROJ_LIB=/opt/conda/share/proj" >> /opt/conda/lib/R/etc/Renviron.site
RUN echo "rsession-ld-library-path=/opt/conda/lib" >> /etc/rstudio/rserver.conf
ENV PATH=$PATH:/usr/lib/rstudio-server/bin

USER $NB_USER

RUN pip install \
    jupyter-rsession-proxy \
    tensorflow \
    nbclassic \
    nbgitpuller && \
    jupyter server extension enable nbgitpuller --sys-prefix

RUN conda install -y -c conda-forge \
    r-base \
    gdal \
    r-keras \
    r-gstat \
    r-spatial \
    r-spdep \
    r-spatialreg \
    r-nloptr

# See: https://github.com/uw-it-aca/rttl-notebooks/pull/15
RUN R -e "devtools::install_github('IRkernel/repr', ref = 'master')"
RUN R -e "devtools::install_github(c('rstudio-education/dsbox'))"
RUN R -e "install.packages(c('IRkernel', 'fastR2', 'fivethirtyeight', 'janitor', 'lubridate', 'mosaic', 'openintro', 'scales', 'skimr', 'tidyverse'),repos='http://cran.us.r-project.org')"
RUN R -e "install.packages('fivethirtyeightdata', repos='https://fivethirtyeightdata.github.io/drat/', type='source')"
RUN R -e "install.packages(c('patchwork'),repos='http://cran.us.r-project.org')"
RUN R -e "install.packages(c('plotly', 'sf', 'here', 'tabula', 'here', 'ggbeeswarm', 'cowplot', 'ggtext', 'raster', 'terra', 'spatstat', 'maptools', 'RColorBrewer', 'viridis', 'wesanderson', 'rcarbon', 'ggridges', 'ggrepel', 'visdat', 'igraph', 'statnet', 'gapminder'), repos='https://cran.rstudio.com')"

RUN R -e "IRkernel::installspec()"
