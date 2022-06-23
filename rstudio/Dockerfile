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
    apt-get install gdebi-core libproj-dev proj-data proj-bin libgeos-dev build-essential cmake -y && \    
    curl --silent -L --fail https://download2.rstudio.org/server/bionic/amd64/rstudio-server-2022.02.0-443-amd64.deb > /tmp/rstudio.deb && \
    echo '2828ef2f8fc93c0dfa125735709d7121ceb060bdd2d08d1f248d6e2b4bc838c0  /tmp/rstudio.deb' | shasum -a 256 -c - && \
    apt-get install -y /tmp/rstudio.deb && \
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
    r-tidyverse \
    gdal \
    r-keras \
    r-gstat \
    r-spatial \
    r-spdep \
    r-spatialreg \
    r-nloptr

# See: https://github.com/uw-it-aca/rttl-notebooks/pull/15
RUN R -e "devtools::install_github('IRkernel/repr', ref = 'master')"
RUN R -e "devtools::install_github(c('rstudio-education/dsbox', 'vjcitn/mobpack'))"
RUN R -e "install.packages(c('IRkernel', 'fastR2', 'openintro', 'palmerpenguins', 'ggridges', 'janitor','statsr', 'broom', 'unvotes', 'lubridate', 'DT', 'scales', 'glue', 'shiny', 'reactable', 'skimr'),repos='http://cran.us.r-project.org')"
RUN R -e "install.packages('fivethirtyeightdata', repos='https://fivethirtyeightdata.github.io/drat/', type='source')"
RUN R -e "IRkernel::installspec()"

ENV RSESSION_PROXY_RSTUDIO_1_4=yes
