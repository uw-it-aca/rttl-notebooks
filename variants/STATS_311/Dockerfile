FROM us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-rstudio-notebook:2.9.0 AS stage1

LABEL maintainer="UWIT Teaching & Learning Systems <aca-it@uw.edu>"

USER $NB_UID

# Copy Dockerfile and Makefile into the container for reference
COPY --chown=$NB_UID:$NB_GID Dockerfile Makefile /home/jovyan/

# Install R packages from CRAN not present in the base image
RUN R -e "install.packages(c('palmerpenguins', 'rsconnect', 'reactable', 'gt', 'GGally', 'statsr', 'corrplot'), repos='http://cran.us.r-project.org')"

# Install R packages from GitHub not present in the base image
RUN R -e "pak::pak(c('grover4/stat311tutorials', 'grover4/STAT311labreport', 'rundel/learnrhash', 'vjcitn/mobpack'))"
