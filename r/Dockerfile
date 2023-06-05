ARG BASE_CONTAINER=jupyter/r-notebook:hub-3.1.1
FROM $BASE_CONTAINER

LABEL maintainer="UW-IT AXDD <aca-it@uw.edu>"

# Base image includes:
# texlive, git, vi, nano, tzdata, unzip
# tidyverse, devtools, shiny, rmarkdown, forecast, rsqlite, nycflights13,
# caret, tidymodels, rcurl, randomforest

RUN mamba install --quiet --yes \
  astroML \
  astroplan \
  astropy \
  astroquery \
  bokeh \
  ccdproc \
  choicemodels \
  cssselect \
  emcee \
  gatspy \
  gensim \
  hickle \
  jupyter-resource-usage \
  lmfit \
  lxml \
  nltk \
  openpyxl \
  pandas \
  photutils \
  plotnine \
  pylogit \
  pymc3 \
  PyTables \
  requests \
  seaborn \
  selenium \
  spacy \
  statsmodels \
  textblob \
  uncertainties \
  xlrd

RUN mamba clean --all -f -y \
  && jupyter lab build -y \
  && jupyter lab clean -y \
  && rm -rf "/home/${NB_USER}/.cache/yarn" \
  && rm -rf "/home/${NB_USER}/.node-gyp" \
  && fix-permissions "${CONDA_DIR}" \
  && fix-permissions "/home/${NB_USER}"

# Install Python 3 packages
RUN pip install \
  biogeme \
  fuzzywuzzy \
  joblib \
  nbgitpuller \
  pqdm \
  pyldavis \
  qgrid \
  requests-html \
  scikit-learn \
  tqdm \
  unidecode && \
  jupyter serverextension enable nbgitpuller --sys-prefix

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

RUN R -e "devtools::install_github('IRkernel/repr', ref = 'master')"
RUN R -e "install.packages('IRkernel',repos='http://cran.us.r-project.org')"
RUN R -e "IRkernel::installspec()"

USER root

RUN apt-get update && apt-get install -y vim gcc openssh-client

USER $NB_UID
