FROM us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-scipy-notebook:2.9.1 AS stage1

LABEL maintainer="UWIT Teaching & Learning Systems <aca-it@uw.edu>"


# Copy Dockerfile and Makefile into the container for reference
COPY --chown=$NB_UID:$NB_GID Dockerfile Makefile /home/jovyan/

# Copy SMTB package
COPY --chown=$NB_UID:$NB_GID SMTB/ /home/jovyan/SMTB/

RUN pip install \
    sympy-plot-backends \
    /home/jovyan/SMTB \
    && pip cache purge
