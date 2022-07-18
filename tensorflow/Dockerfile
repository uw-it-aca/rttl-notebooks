ARG BASE_CONTAINER=jupyter/tensorflow-notebook:hub-1.4.2
FROM $BASE_CONTAINER

LABEL maintainer="UW-IT AXDD <aca-it@uw.edu>"

# Base image includes:
# texlive, git, vi, nano, tzdata, unzip
# dask, pandas, numexpr, matplotlib, scipy, seaborn, scikit-learn,
# scikit-image, sympy, cython, patsy, statsmodels, cloudpickle, dill, numba,
# bokeh, sqlalchemy, hdf5, vincent, beautifulsoup, protobuf, xlrd, bottleneck,
# pytables, ipywidgets, ipympl, facets, tensorflow, keras

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
  plotly \  
  requests && \
  mamba clean --all -f -y && \
  fix-permissions "${CONDA_DIR}" && \
  fix-permissions "/home/${NB_USER}"

# Install Python 3 packages
RUN pip install \
  requests-html \
  joblib \
  tqdm \
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

RUN apt-get update && apt-get install -y openssh-client

USER $NB_UID
