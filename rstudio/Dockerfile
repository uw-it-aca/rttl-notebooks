# ARG BASE_CONTAINER=jupyter/r-notebook:hub-3.1.1
ARG BASE_CONTAINER=us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter_proj-r-notebook:0.0.1
FROM $BASE_CONTAINER

# Base notebook for 3.1.1 (amd64) uses Ubuntu 22.04 (Focal)

# install rstudio-server
USER root

# Per: https://posit.co/download/rstudio-server/
RUN apt-get update && \
    apt-get install gdebi-core libproj-dev proj-data proj-bin libgeos-dev build-essential libfreetype6-dev libfontconfig1-dev cmake -y && \    
    curl --silent -L --fail wget https://download2.rstudio.org/server/jammy/amd64/rstudio-server-2023.12.1-402-amd64.deb > /tmp/rstudio.deb && \
    echo '2ceeebe5d1d77068b36e85f7cf366cd1409f7642a80261b6bbeb3da945ef0888  /tmp/rstudio.deb' | shasum -a 256 -c - && \
    gdebi -n /tmp/rstudio.deb && \
    rm /tmp/rstudio.deb && \
    apt-get clean

RUN apt-get install libharfbuzz-dev libfribidi-dev -y

# Fix for error: "System has not been booted with systemd as init system (PID 1)" related to timedatectl running in containers.
RUN echo 'TZ="America/Los_Angeles"' >> /opt/conda/lib/R/etc/Renviron

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
RUN R -e "install.packages(c('IRkernel', 'fastR2', 'fivethirtyeight', 'janitor', 'lubridate', 'mosaic', 'openintro', 'scales', 'skimr', 'tidyverse','mosaicData','learnr','palmerpenguins','checkmate','renv','rsconnect','glue','reactable','skimr','gt','GGally','tidymodels','statsr','corrplot'),repos='http://cran.us.r-project.org')"
RUN R -e "install.packages('fivethirtyeightdata', repos='https://fivethirtyeightdata.github.io/drat/', type='source')"
RUN R -e "install.packages(c('patchwork','kableExtra','ggpubr','HDInterval', 'leaflet'),repos='http://cran.us.r-project.org')"
RUN R -e "install.packages(c('plotly', 'sf', 'here', 'tabula', 'ggbeeswarm', 'cowplot', 'ggtext', 'raster', 'terra', 'spatstat', 'maptools', 'RColorBrewer', 'viridis', 'wesanderson', 'rcarbon', 'ggridges', 'ggrepel', 'visdat', 'igraph', 'statnet', 'gapminder'), repos='https://cran.rstudio.com')"
RUN R -e "devtools::install_version('shiny', version='1.8.0')"
RUN R -e "devtools::install_version('ggplot2', version='3.4.4')"
RUN R -e "devtools::install_github('rundel/learnrhash')"
RUN R -e "devtools::install_github('rstudio/gradethis')"
RUN R -e "devtools::install_github('vjcitn/mobpack')"
RUN R -e "devtools::install_github('grover4/STAT311labreport')"
RUN R -e "devtools::install_github('grover4/stat311tutorials')"
# RUN R -e "devtools::install_github('hadley/emo', upgrade='always')"

RUN R -e "IRkernel::installspec()"
USER root
RUN echo "rsession-ld-library-path=/opt/conda/lib" >> /etc/rstudio/rserver.conf
RUN apt-get install lmodern -y
USER $NB_USER
