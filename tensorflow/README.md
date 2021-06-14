# rttl-notebooks
Docker images for base RTTL notebooks

Running notebook locally
- `docker run -p 8888:8888 gcr.io/uwit-mci-axdd/rttl-tensorflow-notebook:latest_1-3`
- Console output will include localhost url with access token. Add '/lab' to the end of the path portion

Accessing server shell locally
- `docker run -it --entrypoint /bin/bash gcr.io/uwit-mci-axdd/rttl-tensorflow-notebook:latest_1-3`
