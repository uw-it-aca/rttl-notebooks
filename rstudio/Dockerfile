ARG BASE_CONTAINER=jupyter/r-notebook:hub-1.4.2
FROM $BASE_CONTAINER

# Base notebook for 1.4.2 uses Ubuntu 20.04 (Focal)

RUN pip install jupyter-rsession-proxy
RUN conda install -y -c r r-tidyverse gdal r-gstat r-spatial r-spdep r-spatialreg

# install rstudio-server
USER root

# Per: http://cran.rstudio.com/bin/linux/ubuntu/
RUN apt-get update && \
    apt-get install gdebi-core libproj-dev proj-data proj-bin libgeos-dev build-essential -y && \    
    curl --silent -L --fail https://download2.rstudio.org/server/bionic/amd64/rstudio-server-2021.09.1-372-amd64.deb > /tmp/rstudio.deb && \
    echo 'c58df09468870b89f1796445853dce2dacaa0fc5b7bb1f92b036fa8da1d1f8a3  /tmp/rstudio.deb' | shasum -a 256 -c - && \
    apt-get install -y /tmp/rstudio.deb && \
    rm /tmp/rstudio.deb && \
    apt-get clean


# Needed in 1.4x
RUN chmod 777 /var/lib/rstudio-server/rstudio-os.sqlite && \
    chmod -R 777 /usr/sbin/rstudio-server
ENV RSESSION_PROXY_RSTUDIO_1_4=yes

ENV PATH=$PATH:/usr/lib/rstudio-server/bin

# Workaround for https://issuetracker.google.com/issues/216190252 
# Run suid-wrapped command during Notebook startup
RUN curl --silent -L --fail https://github.com/thiagorb/suid-wrapper/releases/latest/download/suid-wrapper > /tmp/suid-wrapper
RUN chmod +x /tmp/suid-wrapper && mv /tmp/suid-wrapper /usr/bin/suid-wrapper
RUN suid-wrapper $(which chmod) +t /var/run/rstudio-server -o /tmp/add_sticky_bit --force

USER $NB_USER

RUN pip install nbgitpuller && \
  jupyter serverextension enable nbgitpuller --sys-prefix

# See: https://github.com/uw-it-aca/rttl-notebooks/pull/15
RUN R -e "devtools::install_github('IRkernel/repr', ref = 'master')"
RUN R -e "install.packages(c('IRkernel', 'fastR2'),repos='http://cran.us.r-project.org')"
RUN R -e "IRkernel::installspec()"

ENV RSESSION_PROXY_RSTUDIO_1_4=yes