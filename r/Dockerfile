ARG BASE_CONTAINER=jupyter/r-notebook:hub-1.4.2
FROM $BASE_CONTAINER

LABEL maintainer="UW-IT AXDD <aca-it@uw.edu>"

# Base image includes:
# texlive, git, vi, nano, tzdata, unzip
# tidyverse, devtools, shiny, rmarkdown, forecast, rsqlite, nycflights13,
# caret, tidymodels, rcurl, randomforest

RUN conda update conda --yes

# Shared with SciPy, r, Tensorflow images
RUN mamba install --quiet --yes \
  astroML \
  astroplan \
  astropy \
  astroquery \
  ccdproc \
  choicemodels \
  cssselect \
  emcee \
  gatspy \
  gensim \
  hickle \
  lmfit \
  lxml \
  nltk \
  openpyxl \
  photutils \
  plotnine \
  pylogit \
  pymc3 \
  pytorch \
  selenium \
  spacy \
  textblob \
  uncertainties

RUN mamba install --quiet --yes \
  bokeh \
  pandas \
  PyTables \
  requests \
  seaborn \
  statsmodels \
  xlrd

# Install Python 3 packages
RUN pip install \
  biogeme \
  fuzzywuzzy \
  joblib \
  nbgitpuller \
  nbresuse==0.3.3 \
  pqdm \
  pyldavis \
  qgrid \
  requests-html \
  scikit-learn \
  tqdm \
  unidecode && \
  jupyter serverextension enable --py nbresuse --sys-prefix && \
  jupyter nbextension install --py nbresuse --sys-prefix && \
  jupyter nbextension enable --py nbresuse --sys-prefix && \
  jupyter serverextension enable nbgitpuller --sys-prefix

RUN R -e "devtools::install_github('IRkernel/repr', ref = 'master')"
RUN R -e "install.packages('IRkernel',repos='http://cran.us.r-project.org')"
RUN R -e "IRkernel::installspec()"

USER root

RUN apt-get update && apt-get install -y vim gcc openssh-client

# RUN echo 'export LD_LIBRARY_PATH=/usr/local/nvidia/lib64' >> /etc/profile
# RUN echo 'export PATH=$PATH:/usr/local/nvidia/bin'>> /etc/profile
# COPY kernel.json /opt/conda/share/jupyter/kernels/python3/kernel.json

USER $NB_UID
