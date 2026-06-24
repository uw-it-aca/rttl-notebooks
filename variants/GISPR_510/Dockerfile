FROM us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-rstudio-notebook:2.9.0.1 AS stage1

LABEL maintainer="UWIT Teaching & Learning Systems <aca-it@uw.edu>"

USER root

# Add system packages

RUN apt-get update --fix-missing > /dev/null && apt-get install -y \
    libssl-dev \
    libabsl-dev \
    cmake \
    pkg-config \
    python3-gdal \
    software-properties-common \
    libarmadillo-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN add-apt-repository ppa:ubuntugis/ubuntugis-unstable && apt-get update && apt-get install -y libudunits2-dev libgdal-dev libgeos-dev libproj-dev libsqlite3-dev gdal-bin 

USER $NB_UID

# Copy Dockerfile and Makefile into the container for reference
COPY --chown=$NB_UID:$NB_GID Dockerfile Makefile /home/jovyan/

RUN set -ex \
    && micromamba install --quiet --yes --freeze-installed \
    r-units \
    r-s2 \
    r-sf \
    r-terra \
    r-tmap \
    r-leaflet \
    r-mapview \
    && micromamba clean --all -f -y

RUN pip install \
    rasterio \
    xarray \
    leafmap \
    GDAL==`gdal-config --version` \
    && pip cache purge

# Currently unused
# RUN R -e "install.packages(c('tmap','mapview','leaflet'), repos='http://cran.us.r-project.org')"
