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
    apt-get install gdebi-core libproj-dev proj-data proj-bin libgeos-dev build-essential libfreetype6-dev libfontconfig1-dev cmake libharfbuzz-dev libfribidi-dev -y && \    
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

USER $NB_USER

RUN pip install \
    jupyter-rsession-proxy \
    tensorflow \
    nbgitpuller && \
    jupyter serverextension enable nbgitpuller --sys-prefix

# See: https://github.com/uw-it-aca/rttl-notebooks/pull/15
RUN R -e "devtools::install_github('IRkernel/repr', ref = 'master')"
RUN R -e "devtools::install_github(c('rstudio-education/dsbox'))"
RUN R -e "install.packages(c('IRkernel', 'fastR2', 'fivethirtyeight', 'janitor', 'lubridate', 'mosaic', 'openintro', 'scales', 'skimr', 'tidyverse', 'patchwork', 'HMDHFDplus'),repos='http://cran.us.r-project.org')"
RUN R -e "install.packages('fivethirtyeightdata', repos='https://fivethirtyeightdata.github.io/drat/', type='source')"
RUN R -e "install.packages(c('plotly', 'sf', 'here', 'tabula', 'here', 'ggbeeswarm', 'cowplot', 'ggtext', 'raster', 'terra', 'spatstat', 'maptools', 'RColorBrewer', 'viridis', 'wesanderson', 'rcarbon', 'ggridges', 'ggrepel', 'visdat', 'igraph', 'statnet', 'coefplot', 'gt'), repos='https://cran.rstudio.com')"

RUN conda install -y -c conda-forge \
    r-base \
    gdal \
    r-keras \
    r-gstat \
    r-spatial \
    r-spdep \
    r-spatialreg \
    r-nloptr \
    r-gapminder \
    r-fixest \
    r-doby \
    r-stargazer \
    r-ivreg

RUN R -e "IRkernel::installspec()"

ENV RSESSION_PROXY_RSTUDIO_1_4=yes

USER root
# libpng-dev libtiff5-dev libjpeg-dev
RUN apt-get install libpng-dev libtiff5-dev libjpeg-dev -y

USER $NB_USER
RUN conda install -y -c conda-forge pkg-config
RUN R -e "install.packages(c('tidyverse'),repos='http://cran.us.r-project.org')"
RUN R -e "install.packages(c('ipumsr','modelsummary'),repos='http://cran.us.r-project.org')"