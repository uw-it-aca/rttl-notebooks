# RTTL RStudio notebook
Docker image for RStudio notebook using jupyter-rsession-proxy to handle auth flow with JupyterHub. Note: latest RStudio version that runs correctly is 1.2.5042
- Detailed information about base R notebook is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-r-notebook
- General information about working with base images is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html
- Installed packages and versions can be viewed in this image's [Dockerfile](Dockerfile)

Running notebook locally
- `docker run -p 8888:8888 gcr.io/uwit-mci-axdd/rttl-rstudio-notebook:latest`
- Console output will include localhost url with access token. Add '/rstudio' to the end of the path portion

Accessing server shell locally
- `docker run -it --entrypoint /bin/bash gcr.io/uwit-mci-axdd/rttl-rstudio-notebook:latest`
