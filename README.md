# UW-IT JupyterHub for Teaching
Docker images for base JupyterLab environments used in [UW-IT JupyterHub for Teaching](https://itconnect.uw.edu/learn/tools/jupyterhub-for-teaching/) service. General information about working with base images is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html

## Images:
* [Datascience](./datascience/README.md)
* [R](./r/README.md)
* [RStudio](./rstudio/README.md)
* [SciPy](./scipy/README.md)
* [Tensorflow](./tensorflow/README.md)

Running notebook locally
- `docker run -p 8888:8888 gcr.io/uwit-mci-axdd/<image_name>:<image_tag>`
- Console output will include localhost url with access token. Add '/lab' to the end of the path portion for the JupyterLab interface, eg: `http://127.0.0.1:8888/lab`

Accessing server shell locally
- `docker run -it --entrypoint /bin/bash gcr.io/uwit-mci-axdd/<image_name>:<image_tag>`