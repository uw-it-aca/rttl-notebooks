FROM us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-datascience-notebook:2.9.1 AS stage1

LABEL maintainer="UWIT Teaching & Learning Systems <aca-it@uw.edu>"

USER $NB_UID

# Copy Dockerfile and Makefile into the container for reference
COPY --chown=$NB_UID:$NB_GID Dockerfile Makefile /home/jovyan/

# Install Torch from CPU index first
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir \
	transformers \
	accelerate \
	bitsandbytes

# Disable JupyterLab A11y checker, but leave installed
RUN jupyter labextension disable jupyterlab-a11y-checker
