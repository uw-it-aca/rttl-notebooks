ARG BASE_CONTAINER=jupyter/r-notebook:hub-1.3.0
FROM $BASE_CONTAINER

RUN pip install jupyter-rsession-proxy nbgitpuller
RUN conda install -y -c r r-tidyverse

# install rstudio-server
# Note: 1.4x & 1.3x have problems with proxying and auth flow, see: https://github.com/jupyterhub/jupyter-rsession-proxy/issues/97
USER root

# WAS: https://download2.rstudio.org/server/trusty/amd64/rstudio-server-1.2.5042-amd64.deb [f6d212f2fdc1e1b4e605256a91b69fed6b61c046374934d262b2c3f1e234c0d6]
# REMOVED: curl --silent -L --fail http://security.ubuntu.com/ubuntu/pool/main/o/openssl1.0/libssl1.0.0_1.0.2n-1ubuntu5.6_amd64.deb > /tmp/libssl.deb && \
#    apt-get install -y /tmp/libssl.deb && \
#     rm /tmp/libssl.deb && \

RUN apt-get update && \
    apt-get install gdebi-core -y && \
    curl --silent -L --fail https://download2.rstudio.org/server/bionic/amd64/rstudio-server-2021.09.0%2B351-amd64.deb > /tmp/rstudio.deb && \
    echo '8ab014f050651d0b3d6d10ff0fcd6ea4873b90581f2ee1d4eaa871280685afae  /tmp/rstudio.deb' | shasum -a 256 -c - && \
    apt-get install -y /tmp/rstudio.deb && \
    rm /tmp/rstudio.deb && \
    apt-get clean

# These were needed in 1.4x - keeping in case proxy issues are sorted
# RUN rm /var/lib/rstudio-server/rstudio.sqlite && \
#    chmod -R 777 /var/lib/rstudio-server
# ENV RSESSION_PROXY_RSTUDIO_1_4=yes

ENV PATH=$PATH:/usr/lib/rstudio-server/bin

USER $NB_USER