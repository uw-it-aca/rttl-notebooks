# UWIT JupyterHub for Teaching RStudio notebook with AI support
Docker image for standard RStudio notebook with RStudio Copilot [integration](https://docs.posit.co/ide/user/ide/guide/tools/copilot.html) enabled and [Jupyter-AI](https://jupyter-ai.readthedocs.io/en/latest/) packages installed. Rstudio version v2026.05.0+218 with R version R version 4.5.1 (2025-06-13) "Great Square Root". This image also has JupyterLab Version 4.5.7 installed.
- Uses Ubuntu linux 24.04 (noble) and Python 3.13.13
- Detailed information about base R notebook is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-r-notebook
- General information about working with base images is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html
- Installed packages and versions can be viewed in this image's [Dockerfile](Dockerfile) using `pip list` or `conda list`. Dependency trees for both Pip and Conda packages shown below.
- A user guide for the RStudio UI can be found here: https://docs.posit.co/ide/user/ide/guide/ui/ui-panes.html
- Each hub user will need to log in to GitHub Copilot using the verification code process described in the Posit [documentation](https://docs.posit.co/ide/user/ide/guide/tools/copilot.html).
- API tokens for other AI integrations will need to be supplied by the hub user.

## Running notebook locally
- `docker run -p 8888:8888 us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-ai-notebook:2.9`
- Console output will include localhost url with access token. Add '/rstudio' to the end of the path portion, eg: `http://127.0.0.1:8888/rstudio`

## Accessing server shell locally
- `docker run -it --entrypoint /bin/bash us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-ai-notebook:2.9`

## About packages
Only packages pre-installed in this image and listed below will be available by default. Users can install their own package at runtime, but those packages will not persist and will need to be installed again the next time their server is started. If a package you need is not available in this image, there are a few options:
- You can request the package be added to this image. We need to review and test any additions, so the request should be made before the start of the quarter. You can request additional packages at the time you sign up for a hub, or send the request to help@uw.edu with "JupyterHub for Teaching" in the subject line.
- If you are comfortable building your own container images, you can create an image and send us the link to the image on a public container registry when signing up for a hub. We strongly recommend basing the image on our supported image for compatibility reasons.
- You can add a code cell in your .rmd file that installs needed packages and have users run that cell when starting a session. Example syntax: `install.packages('<package_name>')`
- You can have users configure their server to install packages to their own home directory. Note that this does make it more difficult to be sure that all your users have the same environment.
  - One time step: (from the terminal) `mkdir -p ~/local/R_libs && echo '.libPaths(c("/opt/conda/lib/R/library","/home/jovyan/local/R_libs"))' >> ~/.Rprofile`
  - One time step: (from the R console) `libPaths(c("/opt/conda/lib/R/library","/home/jovyan/local/R_libs"))`
  - Any time they install a new package: (from the R console) `install.packages("<package_name>", lib="~/local/R_libs")`

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

| Name | Version |
| ----------------------------- | ------------------- |
