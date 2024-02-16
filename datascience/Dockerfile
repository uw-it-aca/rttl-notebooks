# ARG BASE_CONTAINER=jupyter/datascience-notebook:hub-3.1.1
ARG BASE_CONTAINER=us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter_proj-datascience-notebook:0.0.1

FROM $BASE_CONTAINER

LABEL maintainer="UW-IT AXDD <aca-it@uw.edu>"

# Base image includes:
# texlive, git, vi, nano, tzdata, unzip
# dask, pandas, numexpr, matplotlib, scipy, seaborn, scikit-learn,
# scikit-image, sympy, cython, patsy, statsmodels, cloudpickle, dill, numba,
# bokeh, sqlalchemy, hdf5, vincent, beautifulsoup, protobuf, xlrd, bottleneck,
# pytables, ipywidgets, ipympl, facets
# tidyverse, devtools, shiny, rmarkdown, forecast, rsqlite, nycflights13,
# caret, tidymodels, rcurl, randomforest#
# julia, ijulia, hdf5, gadfly, rdatasets

RUN mamba install --quiet --yes \
  requests \
  jupyter-resource-usage

RUN mamba clean --all -f -y \
  && jupyter lab build -y \
  && jupyter lab clean -y \
  && rm -rf "/home/${NB_USER}/.cache/yarn" \
  && rm -rf "/home/${NB_USER}/.node-gyp" \
  && fix-permissions "${CONDA_DIR}" \
  && fix-permissions "/home/${NB_USER}"

# Install Python 3 packages
RUN pip install \
  folium \
  geopandas \
  ipyleaflet \
  nbclassic \
  nbgitpuller \  
  requests-html && \
  jupyter server extension enable nbgitpuller --sys-prefix

USER root

RUN apt-get update && apt-get install -y vim gcc

USER $NB_UID
