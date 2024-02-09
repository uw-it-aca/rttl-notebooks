# ARG BASE_CONTAINER=jupyter/tensorflow-notebook:hub-3.1.1
ARG BASE_CONTAINER=us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter_proj-tensorflow-notebook:0.0.1
FROM $BASE_CONTAINER

LABEL maintainer="UW-IT AXDD <aca-it@uw.edu>"

# Base image includes:
# texlive, git, vi, nano, tzdata, unzip
# dask, pandas, numexpr, matplotlib, scipy, seaborn, scikit-learn,
# scikit-image, sympy, cython, patsy, statsmodels, cloudpickle, dill, numba,
# bokeh, sqlalchemy, hdf5, vincent, beautifulsoup, protobuf, xlrd, bottleneck,
# pytables, ipywidgets, ipympl, facets, tensorflow, keras

RUN mamba install --quiet --yes \
  astroML \
  astroplan \
  astropy \
  astroquery \
  choicemodels \
  cssselect \
  emcee \
  gatspy \
  gensim \
  hickle \
  jupyter-dash \
  jupyter-resource-usage \
  lmfit \
  lxml \
  nltk \
  openpyxl \
  photutils \
  plotly \
  plotnine \
  pylogit \
  pymc3 \
  requests \
  selenium \
  spacy \
  textblob \
  uncertainties

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
  nbclassic \
  nbgitpuller \
  pqdm \
  pyldavis \
  qgrid \
  requests-html \
  tqdm \
  unidecode && \
  jupyter server extension enable nbgitpuller --sys-prefix

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

USER root

RUN apt-get update && apt-get install -y openssh-client

USER $NB_UID
