ARG BASE_CONTAINER=jupyter/scipy-notebook:hub-1.4.2
FROM $BASE_CONTAINER

LABEL maintainer="UW-IT AXDD <aca-it@uw.edu>"

# Base image includes:
# texlive, git, vi, nano, tzdata, unzip
# dask, pandas, numexpr, matplotlib, scipy, seaborn, scikit-learn,
# scikit-image, sympy, cython, patsy, statsmodels, cloudpickle, dill, numba,
# bokeh, sqlalchemy, hdf5, vincent, beautifulsoup, protobuf, xlrd, bottleneck,
# pytables, ipywidgets, ipympl, facets

RUN conda update conda --yes

# Shared with SciPy, r, Tensorflow images
RUN conda install --quiet --yes \
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
  'plotly==4.14.3' \
  && conda clean --all -f -y

RUN set -ex \
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
  fuzzywuzzy \
  jupyter-resource-usage \
  nbclassic==0.2.8 \
  nbgitpuller \
  nbresuse==0.3.3 \
  pqdm \
  pyldavis \
  qgrid \
  requests-html \
  scipy==1.7.1 \
  unidecode

RUN jupyter serverextension enable --py nbresuse --sys-prefix && \
  jupyter nbextension install --py nbresuse --sys-prefix && \
  jupyter nbextension enable --py nbresuse --sys-prefix && \
  jupyter serverextension enable nbgitpuller --sys-prefix && \
  jupyter serverextension enable --py jupyter-resource-usage --sys-prefix && \
  jupyter nbextension install --py jupyter-resource-usage --sys-prefix && \
  jupyter nbextension enable --py jupyter-resource-usage --sys-prefix

USER root

RUN apt-get update && apt-get install -y vim gcc openssh-client build-essential

# RUN echo 'export LD_LIBRARY_PATH=/usr/local/nvidia/lib64' >> /etc/profile
# RUN echo 'export PATH=$PATH:/usr/local/nvidia/bin'>> /etc/profile
# COPY kernel.json /opt/conda/share/jupyter/kernels/python3/kernel.json

USER $NB_UID

# biogeme failed to install without an interactive bash shell
SHELL ["/bin/bash", "--login", "-c", "-i"]
RUN pip install biogeme
