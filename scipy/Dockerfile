# ARG BASE_CONTAINER=jupyter/scipy-notebook:hub-3.1.1
ARG BASE_CONTAINER=us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter_proj-scipy-notebook:0.0.1
FROM $BASE_CONTAINER

LABEL maintainer="UW-IT AXDD <aca-it@uw.edu>"

# Base image includes: (https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-tensorflow-notebook)
# texlive, git, vi, nano, tzdata, unzip
# dask, pandas, numexpr, matplotlib, scipy, seaborn, scikit-learn,
# scikit-image, sympy, cython, patsy, statsmodels, cloudpickle, dill, numba,
# bokeh, sqlalchemy, hdf5, vincent, beautifulsoup, protobuf, xlrd, bottleneck,
# pytables, ipywidgets, ipympl, facets

RUN set -ex \
  && mamba install --quiet --yes \
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
  jupyter-dash \
  jupyter-resource-usage \
  lmfit \
  lxml \
  nltk \
  octave_kernel \
  photutils \
  'plotly==5.14.1' \
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
  astroalign \
  biogeme \
  fuzzywuzzy \
  joblib \
  nbclassic \
  nbgitpuller \
  pqdm \
  pyldavis \
  opencv-python \
  qgrid \
  requests-html \
  tellurium \
  tqdm \
  unidecode && \
  jupyter server extension enable nbgitpuller --sys-prefix

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

USER root

RUN apt-get update && apt-get install -y vim gcc openssh-client build-essential texlive-xetex texlive-fonts-recommended texlive-plain-generic
RUN apt-get install -y octave octave-control octave-image octave-io octave-optim octave-signal octave-statistics
RUN apt-get install -y gfortran
RUN apt-get install -y unixodbc zip

# RUN echo 'export LD_LIBRARY_PATH=/usr/local/nvidia/lib64' >> /etc/profile
# RUN echo 'export PATH=$PATH:/usr/local/nvidia/bin'>> /etc/profile
# COPY kernel.json /opt/conda/share/jupyter/kernels/python3/kernel.json

USER $NB_UID
