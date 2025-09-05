FROM us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-rstudio-notebook:2.7.1 AS stage1

LABEL maintainer="UW-IT Teaching & Learning Systems <aca-it@uw.edu>"

USER root

RUN echo 'copilot-enabled=1' >> /etc/rstudio/rsession.conf

USER $NB_UID

RUN pip install jupyter-ai[all]
