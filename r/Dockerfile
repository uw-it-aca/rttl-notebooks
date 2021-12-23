ARG BASE_CONTAINER=jupyter/r-notebook:hub-1.4.2
FROM $BASE_CONTAINER

LABEL maintainer="UW-IT AXDD <aca-it@uw.edu>"

# Base image includes:
# texlive, git, vi, nano, tzdata, unzip
# tidyverse, devtools, shiny, rmarkdown, forecast, rsqlite, nycflights13,
# caret, tidymodels, rcurl, randomforest

RUN mamba install --quiet --yes \
  emcee \
  pymc3 \
  astroML \
  astropy \
  astroplan \
  astroquery \
  gatspy \
  pytorch \
  photutils \
  ccdproc \
  lmfit \
  uncertainties \
  pandas \
  xlrd \
  openpyxl \
  hickle \
  PyTables \
  spacy \
  textblob \
  nltk \
  gensim \
  requests \
  seaborn \
  bokeh \
  lxml \
  cssselect \
  plotnine \
  selenium \
  statsmodels \
  pylogit \
  choicemodels

# Install Python 3 packages
RUN pip install \
  requests-html \
  joblib \
  tqdm \
  scikit-learn \
  pyldavis \
  unidecode \
  fuzzywuzzy \
  pqdm \
  qgrid \
  biogeme \
  nbresuse==0.3.3 \
  nbgitpuller && \
  jupyter serverextension enable --py nbresuse --sys-prefix && \
  jupyter nbextension install --py nbresuse --sys-prefix && \
  jupyter nbextension enable --py nbresuse --sys-prefix && \
  jupyter serverextension enable nbgitpuller --sys-prefix

USER root

RUN apt-get update && apt-get install -y vim gcc openssh-client

# RUN echo 'export LD_LIBRARY_PATH=/usr/local/nvidia/lib64' >> /etc/profile
# RUN echo 'export PATH=$PATH:/usr/local/nvidia/bin'>> /etc/profile
# COPY kernel.json /opt/conda/share/jupyter/kernels/python3/kernel.json

USER $NB_UID
