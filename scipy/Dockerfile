ARG BASE_CONTAINER=jupyter/scipy-notebook:hub-1.4.2
FROM $BASE_CONTAINER

LABEL maintainer="UW-IT AXDD <aca-it@uw.edu>"

# Base image includes:
# texlive, git, vi, nano, tzdata, unzip
# dask, pandas, numexpr, matplotlib, scipy, seaborn, scikit-learn,
# scikit-image, sympy, cython, patsy, statsmodels, cloudpickle, dill, numba,
# bokeh, sqlalchemy, hdf5, vincent, beautifulsoup, protobuf, xlrd, bottleneck,
# pytables, ipywidgets, ipympl, facets

RUN set -ex \
  && mamba install --quiet --yes \
  'plotly==4.14.3' \
  emcee \
  pymc3 \
  astroML \
  astropy \
  astroplan \
  astroquery \
  gatspy \
  jupyterlab \
  'ipywidgets>=7.5' \
  pytorch \
  photutils \
  ccdproc \
  lmfit \
  uncertainties \
  openpyxl \
  hickle \
  spacy \
  textblob \
  nltk \
  gensim \
  requests \
  lxml \
  cssselect \
  plotnine \
  selenium \
  pylogit \
  choicemodels

RUN mamba clean --all -f -y \
  && jupyter labextension install jupyterlab-plotly@4.14.3 --no-build \
  && jupyter lab build -y \
  && jupyter lab clean -y \
  && rm -rf "/home/${NB_USER}/.cache/yarn" \
  && rm -rf "/home/${NB_USER}/.node-gyp" \
  && fix-permissions "${CONDA_DIR}" \
  && fix-permissions "/home/${NB_USER}"

# Install Python 3 packages
RUN pip install \
  astroalign \
  requests-html \
  joblib \
  tqdm \
  pyldavis \
  unidecode \
  fuzzywuzzy \
  pqdm \
  qgrid \
  nbresuse==0.3.3 \
  nbclassic==0.2.8 \
  nbgitpuller \
  scipy==1.7.1 && \
  jupyter serverextension enable --py nbresuse --sys-prefix && \
  jupyter nbextension install --py nbresuse --sys-prefix && \
  jupyter nbextension enable --py nbresuse --sys-prefix && \
  jupyter serverextension enable nbgitpuller --sys-prefix

USER root

RUN apt-get update && apt-get install -y vim gcc openssh-client build-essential texlive-xetex texlive-fonts-recommended texlive-plain-generic

# RUN echo 'export LD_LIBRARY_PATH=/usr/local/nvidia/lib64' >> /etc/profile
# RUN echo 'export PATH=$PATH:/usr/local/nvidia/bin'>> /etc/profile
# COPY kernel.json /opt/conda/share/jupyter/kernels/python3/kernel.json

USER $NB_UID

RUN pip install git+https://github.com/choldgraf/jupyter-http-server && jupyter labextension install @jupyterlab/server-proxy

# biogeme failed to install without an interactive bash shell
SHELL ["/bin/bash", "--login", "-c", "-i"]
RUN pip install biogeme