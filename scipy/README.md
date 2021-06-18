# RTTL SciPy notebook
Docker image for UW RTTL SciPy notebook. 
- Detailed information about base SciPy notebook is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-scipy-notebook
- General information about working with base images is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html

Running notebook locally
- `docker run -p 8888:8888 gcr.io/uwit-mci-axdd/rttl-scipy-notebook:latest_1-3`
- Console output will include localhost url with access token. Add '/lab' to the end of the path portion

Accessing server shell locally
- `docker run -it --entrypoint /bin/bash gcr.io/uwit-mci-axdd/rttl-scipy-notebook:latest_1-3`
