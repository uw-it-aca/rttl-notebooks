ARG BASE_CONTAINER=jupyter/datascience-notebook:hub-1.4.2

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

RUN mkdir /opt/conda/pkg
RUN touch /opt/conda/pkg/urls.txt

RUN set -ex \
  && conda install --quiet --yes \
  requests \
  && conda clean --all -f -y \
  && fix-permissions "${CONDA_DIR}" \
  && fix-permissions "/home/${NB_USER}"

# Install Python 3 packages
RUN pip install \
  requests-html \
  nbresuse==0.3.3 \
  geopandas \
  folium \
  ipyleaflet \
  nbclassic==0.2.8 \
  nbgitpuller && \
  jupyter serverextension enable --py nbresuse --sys-prefix && \
  jupyter nbextension install --py nbresuse --sys-prefix && \
  jupyter nbextension enable --py nbresuse --sys-prefix && \
  jupyter serverextension enable nbgitpuller --sys-prefix

USER root

RUN apt-get update && apt-get install -y vim gcc

# RUN echo 'export LD_LIBRARY_PATH=/usr/local/nvidia/lib64' >> /etc/profile
# RUN echo 'export PATH=$PATH:/usr/local/nvidia/bin'>> /etc/profile
# COPY kernel.json /opt/conda/share/jupyter/kernels/python3/kernel.json

USER $NB_UID
