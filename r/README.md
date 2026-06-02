# UWIT JupyterHub for Teaching R notebook
Docker image for UWIT JupyterHub for Teaching R notebook. Installed R version 4.5.1 (2025-06-13) "Great Square Root"
- Uses Ubuntu linux 24.04 LTS (noble) and Python 3.13.13.
- Detailed information about base R notebook is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-r-notebook
- General information about working with base images is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html
- Installed packages and versions can be viewed in this image's [Dockerfile](Dockerfile) using `pip list` or `conda list`. Dependency trees for both Pip and Conda packages shown below.
- The JupyterLab interface (v4.5.7) is installed and is set as default

## Running notebook locally
- `docker run -p 8888:8888 us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-r-notebook:2.9`
- Console output will include localhost url with access token.

## Accessing server shell locally
- `docker run -it --entrypoint /bin/bash us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-r-notebook:2.9`

## Installed Python packages

### Pip packages
via `pipdeptree --exclude pipdeptree`

```

```

### Conda packages
via `conda-tree -n base deptree --exclude conda-tree --small`

```

```

## Installed R packages

Via `R -e 'as.data.frame(installed.packages())[,c("Package", "Version")]'`

|Package|Version|
| ----------------------------- | ------------------- |


