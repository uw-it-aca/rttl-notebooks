ARG BASE_CONTAINER=jupyter/r-notebook:hub-1.4.2
FROM $BASE_CONTAINER

# Base notebook for 1.4.2 uses Ubuntu 20.04 (Focal)

# install rstudio-server
USER root

RUN apt-get update -qq && \
    apt-get install --no-install-recommends software-properties-common dirmngr  -y && \
    wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | sudo tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc && \
    add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/" && \
    apt install --no-install-recommends r-base -y

# Per: http://cran.rstudio.com/bin/linux/ubuntu/
RUN apt-get update && \
    apt-get install gdebi-core libproj-dev proj-data proj-bin libgeos-dev build-essential libfreetype6-dev libfontconfig1-dev libmagick++-dev cmake -y && \    
    curl --silent -L --fail https://download2.rstudio.org/server/bionic/amd64/rstudio-server-2022.07.1-554-amd64.deb > /tmp/rstudio.deb && \
    echo 'b6778c0a78d69d836d5c812342a3697a19b83c80c2d6eb7162b38dedc6ad6b56  /tmp/rstudio.deb' | shasum -a 256 -c - && \
    gdebi -n /tmp/rstudio.deb && \
    rm /tmp/rstudio.deb && \
    apt-get clean


# Needed in 1.4x
RUN chmod 777 /var/lib/rstudio-server/rstudio-os.sqlite && \
    chmod -R 777 /usr/sbin/rstudio-server
ENV RSESSION_PROXY_RSTUDIO_1_4=yes
# Fix for error: "System has not been booted with systemd as init system (PID 1)" related to timedatectl running in containers.
RUN echo 'TZ="America/Los_Angeles"' >> /opt/conda/lib/R/etc/Renviron

ENV PATH=$PATH:/usr/lib/rstudio-server/bin

# Workaround for https://issuetracker.google.com/issues/216190252 
# Run suid-wrapped command during Notebook startup
RUN curl --silent -L --fail https://github.com/thiagorb/suid-wrapper/releases/download/v0.1.4/suid-wrapper > /tmp/suid-wrapper && \
    echo '93c583473600558d0d67eb06913efed14a684b2431d0114ab6a553f6f1ead750  /tmp/suid-wrapper' | shasum -a 256 -c -
RUN chmod +x /tmp/suid-wrapper && mv /tmp/suid-wrapper /usr/bin/suid-wrapper
RUN suid-wrapper $(which chmod) +t /var/run/rstudio-server -o /tmp/add_sticky_bit --force

USER $NB_USER

RUN pip install \
    jupyter-rsession-proxy \
    tensorflow \
    nbgitpuller && \
    jupyter serverextension enable nbgitpuller --sys-prefix

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
RUN R -e "install.packages(c('plotly', 'sf', 'here', 'tabula', 'ggbeeswarm', 'cowplot', 'ggtext', 'raster', 'terra', 'spatstat', 'maptools', 'RColorBrewer', 'viridis', 'wesanderson', 'rcarbon', 'ggridges', 'ggrepel'), repos='https://cran.rstudio.com')"
RUN R -e "install.packages(c('vegan', 'labdsv', 'ecodist', 'vegan3d', 'ade4', 'dendextend', 'heatmaply', 'pvclust', 'indicspecies', 'progenyClust', 'NbClust', 'animation', 'tree', 'party', 'TITAN2', 'treeClust', 'partykit', 'IntegratedMRF', 'ggdendro', 'splancs'), repos='https://cran.rstudio.com')"
# RTools is only needed for Windows & vsurf only works with R >= v4.2
RUN R -e "devtools::install_github(c('gavinsimpson/ggvegan'))"
RUN R -e "devtools::install_github(c('jfq3/ggordiplots'))"
RUN R -e "devtools::install_github(c('cran/mvpart'))"
RUN R -e "devtools::install_github(c('cran/MVPARTwrap'))"
RUN R -e "IRkernel::installspec()"

ENV RSESSION_PROXY_RSTUDIO_1_4=yes
