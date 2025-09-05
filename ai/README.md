# UW-IT JupyterHub for Teaching RStudio notebook with AI support
Docker image for standard RStudio notebook with RStudio Copilot [integration](https://docs.posit.co/ide/user/ide/guide/tools/copilot.html) enabled and [Jupyter-AI](https://jupyter-ai.readthedocs.io/en/latest/) packages installed. Rstudio version is 2023.12.1 Build 402 "Ocean Storm" Release with R version 4.3.2 (2023-10-31). This image also has JupyterLab v4.0.10 installed.
- Detailed information about base R notebook is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-r-notebook
- General information about working with base images is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html
- Installed packages and versions can be viewed in this image's [Dockerfile](Dockerfile) using `pip list` or `conda list`. Dependency trees for both Pip and Conda packages shown below.
- A user guide for the RStudio UI can be found here: https://docs.posit.co/ide/user/ide/guide/ui/ui-panes.html
- Each hub user will need to log in to GitHub Copilot using the verification code process described in the Posit [documentation](https://docs.posit.co/ide/user/ide/guide/tools/copilot.html).

## Running notebook locally
- `docker run -p 8888:8888 us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-ai-notebook:2.7.0`
- Console output will include localhost url with access token. Add '/rstudio' to the end of the path portion, eg: `http://127.0.0.1:8888/rstudio`

## Accessing server shell locally
- `docker run -it --entrypoint /bin/bash us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-ai-notebook:2.7.0`

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
ai21==3.1.0
├── ai21-tokenizer [required: >=0.12.0,<1.0.0, installed: 0.12.0]
│   ├── anyio [required: >=4.4.0,<5.0.0, installed: 4.9.0]
│   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   ├── sentencepiece [required: >=0.2.0,<1.0.0, installed: 0.2.0]
│   └── tokenizers [required: >=0.15.0,<1.0.0, installed: 0.21.1]
│       └── huggingface-hub [required: >=0.16.4,<1.0, installed: 0.29.3]
│           ├── filelock [required: Any, installed: 3.18.0]
│           ├── fsspec [required: >=2023.5.0, installed: 2025.3.0]
│           ├── packaging [required: >=20.9, installed: 24.2]
│           ├── PyYAML [required: >=5.1, installed: 6.0.1]
│           ├── requests [required: Any, installed: 2.32.3]
│           │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│           │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│           │   ├── idna [required: >=2.5,<4, installed: 3.7]
│           │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│           ├── tqdm [required: >=4.42.1, installed: 4.66.4]
│           └── typing_extensions [required: >=3.7.4.3, installed: 4.12.2]
├── httpx [required: >=0.27.0,<1.0.0, installed: 0.27.0]
│   ├── anyio [required: Any, installed: 4.9.0]
│   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   ├── certifi [required: Any, installed: 2025.1.31]
│   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   ├── idna [required: Any, installed: 3.7]
│   └── sniffio [required: Any, installed: 1.3.1]
├── pydantic [required: >=1.9.0,<3.0.0, installed: 2.10.6]
│   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
├── tenacity [required: >=8.3.0,<9.0.0, installed: 8.5.0]
└── typing_extensions [required: >=4.9.0,<5.0.0, installed: 4.12.2]
arxiv==2.1.3
├── feedparser [required: ~=6.0.10, installed: 6.0.11]
│   └── sgmllib3k [required: Any, installed: 1.0.0]
└── requests [required: ~=2.32.0, installed: 2.32.3]
    ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
    ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
    ├── idna [required: >=2.5,<4, installed: 3.7]
    └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
blinker==1.8.2
Brotli==1.1.0
cached-property==1.5.2
conda-tree==1.1.1
├── colorama [required: Any, installed: 0.4.6]
└── networkx [required: Any, installed: 3.4.2]
distributed==2025.3.0
├── click [required: >=8.0, installed: 8.1.8]
├── cloudpickle [required: >=3.0.0, installed: 3.1.1]
├── dask [required: ==2025.3.0, installed: 2025.3.0]
│   ├── click [required: >=8.1, installed: 8.1.8]
│   ├── cloudpickle [required: >=3.0.0, installed: 3.1.1]
│   ├── fsspec [required: >=2021.09.0, installed: 2025.3.0]
│   ├── importlib_metadata [required: >=4.13.0, installed: 7.1.0]
│   │   └── zipp [required: >=0.5, installed: 3.17.0]
│   ├── packaging [required: >=20.0, installed: 24.2]
│   ├── partd [required: >=1.4.0, installed: 1.4.2]
│   │   ├── locket [required: Any, installed: 1.0.0]
│   │   └── toolz [required: Any, installed: 1.0.0]
│   ├── PyYAML [required: >=5.3.1, installed: 6.0.1]
│   └── toolz [required: >=0.10.0, installed: 1.0.0]
├── Jinja2 [required: >=2.10.3, installed: 3.1.4]
│   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
├── locket [required: >=1.0.0, installed: 1.0.0]
├── msgpack [required: >=1.0.2, installed: 1.1.0]
├── packaging [required: >=20.0, installed: 24.2]
├── psutil [required: >=5.8.0, installed: 5.9.8]
├── PyYAML [required: >=5.4.1, installed: 6.0.1]
├── sortedcontainers [required: >=2.0.5, installed: 2.4.0]
├── tblib [required: >=1.6.0, installed: 3.0.0]
├── toolz [required: >=0.11.2, installed: 1.0.0]
├── tornado [required: >=6.2.0, installed: 6.4]
├── urllib3 [required: >=1.26.5, installed: 2.2.1]
└── zict [required: >=3.0.0, installed: 3.0.0]
entrypoints==0.4
exceptiongroup==1.2.0
fqdn==1.5.1
GDAL==3.9.0
gpt4all==2.8.2
├── requests [required: Any, installed: 2.32.3]
│   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   ├── idna [required: >=2.5,<4, installed: 3.7]
│   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
└── tqdm [required: Any, installed: 4.66.4]
grpcio-status==1.71.0
├── googleapis-common-protos [required: >=1.5.5, installed: 1.69.2]
│   └── protobuf [required: >=3.20.2,<7.0.0,!=4.21.5,!=4.21.4,!=4.21.3,!=4.21.2,!=4.21.1, installed: 5.29.3]
├── grpcio [required: >=1.71.0, installed: 1.71.0]
└── protobuf [required: >=5.26.1,<6.0dev, installed: 5.29.3]
h2==4.1.0
├── hpack [required: >=4.0,<5, installed: 4.0.0]
└── hyperframe [required: >=6.0,<7, installed: 6.0.1]
importlib_resources==6.4.0
ipywidgets==8.1.5
├── comm [required: >=0.1.3, installed: 0.2.2]
│   └── traitlets [required: >=4, installed: 5.14.3]
├── ipython [required: >=6.1.0, installed: 8.24.0]
│   ├── decorator [required: Any, installed: 5.1.1]
│   ├── jedi [required: >=0.16, installed: 0.19.1]
│   │   └── parso [required: >=0.8.3,<0.9.0, installed: 0.8.4]
│   ├── matplotlib-inline [required: Any, installed: 0.1.7]
│   │   └── traitlets [required: Any, installed: 5.14.3]
│   ├── pexpect [required: >4.3, installed: 4.9.0]
│   │   └── ptyprocess [required: >=0.5, installed: 0.7.0]
│   ├── prompt-toolkit [required: >=3.0.41,<3.1.0, installed: 3.0.42]
│   │   └── wcwidth [required: Any, installed: 0.2.13]
│   ├── Pygments [required: >=2.4.0, installed: 2.18.0]
│   ├── stack-data [required: Any, installed: 0.6.2]
│   │   ├── asttokens [required: >=2.1.0, installed: 2.4.1]
│   │   │   └── six [required: >=1.12.0, installed: 1.16.0]
│   │   ├── executing [required: >=1.2.0, installed: 2.0.1]
│   │   └── pure-eval [required: Any, installed: 0.2.2]
│   ├── traitlets [required: >=5.13.0, installed: 5.14.3]
│   └── typing_extensions [required: >=4.6, installed: 4.12.2]
├── jupyterlab_widgets [required: ~=3.0.12, installed: 3.0.13]
├── traitlets [required: >=4.3.1, installed: 5.14.3]
└── widgetsnbextension [required: ~=4.0.12, installed: 4.0.13]
isoduration==20.11.0
└── arrow [required: >=0.15.0, installed: 1.3.0]
    ├── python-dateutil [required: >=2.7.0, installed: 2.9.0]
    │   └── six [required: >=1.5, installed: 1.16.0]
    └── types-python-dateutil [required: >=2.8.10, installed: 2.9.0.20240316]
jupyter_ai==2.31.0
├── dask [required: Any, installed: 2025.3.0]
│   ├── click [required: >=8.1, installed: 8.1.8]
│   ├── cloudpickle [required: >=3.0.0, installed: 3.1.1]
│   ├── fsspec [required: >=2021.09.0, installed: 2025.3.0]
│   ├── importlib_metadata [required: >=4.13.0, installed: 7.1.0]
│   │   └── zipp [required: >=0.5, installed: 3.17.0]
│   ├── packaging [required: >=20.0, installed: 24.2]
│   ├── partd [required: >=1.4.0, installed: 1.4.2]
│   │   ├── locket [required: Any, installed: 1.0.0]
│   │   └── toolz [required: Any, installed: 1.0.0]
│   ├── PyYAML [required: >=5.3.1, installed: 6.0.1]
│   └── toolz [required: >=0.10.0, installed: 1.0.0]
├── deepmerge [required: >=2.0,<3, installed: 2.0]
├── faiss-cpu [required: >=1.8.0,<2.0.0,!=1.8.0.post0, installed: 1.10.0]
│   ├── numpy [required: >=1.25.0,<3.0, installed: 1.26.4]
│   └── packaging [required: Any, installed: 24.2]
├── importlib_metadata [required: >=5.2.0, installed: 7.1.0]
│   └── zipp [required: >=0.5, installed: 3.17.0]
├── jupyter_ai_magics [required: >=2.31.0,<3.0.0, installed: 2.31.0]
│   ├── click [required: >=8.1.0,<9, installed: 8.1.8]
│   ├── importlib_metadata [required: >=5.2.0, installed: 7.1.0]
│   │   └── zipp [required: >=0.5, installed: 3.17.0]
│   ├── ipython [required: Any, installed: 8.24.0]
│   │   ├── decorator [required: Any, installed: 5.1.1]
│   │   ├── jedi [required: >=0.16, installed: 0.19.1]
│   │   │   └── parso [required: >=0.8.3,<0.9.0, installed: 0.8.4]
│   │   ├── matplotlib-inline [required: Any, installed: 0.1.7]
│   │   │   └── traitlets [required: Any, installed: 5.14.3]
│   │   ├── pexpect [required: >4.3, installed: 4.9.0]
│   │   │   └── ptyprocess [required: >=0.5, installed: 0.7.0]
│   │   ├── prompt-toolkit [required: >=3.0.41,<3.1.0, installed: 3.0.42]
│   │   │   └── wcwidth [required: Any, installed: 0.2.13]
│   │   ├── Pygments [required: >=2.4.0, installed: 2.18.0]
│   │   ├── stack-data [required: Any, installed: 0.6.2]
│   │   │   ├── asttokens [required: >=2.1.0, installed: 2.4.1]
│   │   │   │   └── six [required: >=1.12.0, installed: 1.16.0]
│   │   │   ├── executing [required: >=1.2.0, installed: 2.0.1]
│   │   │   └── pure-eval [required: Any, installed: 0.2.2]
│   │   ├── traitlets [required: >=5.13.0, installed: 5.14.3]
│   │   └── typing_extensions [required: >=4.6, installed: 4.12.2]
│   ├── jsonpath-ng [required: >=1.5.3,<2, installed: 1.7.0]
│   │   └── ply [required: Any, installed: 3.11]
│   ├── langchain [required: >=0.3.0,<0.4.0, installed: 0.3.21]
│   │   ├── langchain-core [required: >=0.3.45,<1.0.0, installed: 0.3.47]
│   │   │   ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
│   │   │   │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   │   │   ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   │   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   │   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   │   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   │   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   │   │   ├── packaging [required: >=23.2,<25, installed: 24.2]
│   │   │   ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
│   │   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   │   ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
│   │   │   └── typing_extensions [required: >=4.7, installed: 4.12.2]
│   │   ├── langchain-text-splitters [required: >=0.3.7,<1.0.0, installed: 0.3.7]
│   │   │   └── langchain-core [required: >=0.3.45,<1.0.0, installed: 0.3.47]
│   │   │       ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
│   │   │       │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   │   │       ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   │       │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │       │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │       │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │       │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │       │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │       │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │       │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │       │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │       │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │       │   │   ├── idna [required: Any, installed: 3.7]
│   │   │       │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   │       │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   │       │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   │       │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │       │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │       │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │       │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │       │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │       │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │       │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │       │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │       │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │       │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │       │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │       │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │       │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │       │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │       │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │       │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │       │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   │   │       ├── packaging [required: >=23.2,<25, installed: 24.2]
│   │   │       ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
│   │   │       │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │       │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │       │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │       │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │       ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   │       ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
│   │   │       └── typing_extensions [required: >=4.7, installed: 4.12.2]
│   │   ├── langsmith [required: >=0.1.17,<0.4, installed: 0.3.18]
│   │   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   │   ├── pydantic [required: >=2.7.4,<3.0.0, installed: 2.10.6]
│   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   └── SQLAlchemy [required: >=1.4,<3, installed: 2.0.30]
│   │       ├── greenlet [required: !=0.4.17, installed: 3.0.3]
│   │       └── typing_extensions [required: >=4.6.0, installed: 4.12.2]
│   ├── langchain-community [required: >=0.3.0,<0.4.0, installed: 0.3.20]
│   │   ├── aiohttp [required: >=3.8.3,<4.0.0, installed: 3.11.13]
│   │   │   ├── aiohappyeyeballs [required: >=2.3.0, installed: 2.4.8]
│   │   │   ├── aiosignal [required: >=1.1.2, installed: 1.3.2]
│   │   │   │   └── frozenlist [required: >=1.1.0, installed: 1.5.0]
│   │   │   ├── attrs [required: >=17.3.0, installed: 23.2.0]
│   │   │   ├── frozenlist [required: >=1.1.1, installed: 1.5.0]
│   │   │   ├── multidict [required: >=4.5,<7.0, installed: 6.1.0]
│   │   │   ├── propcache [required: >=0.2.0, installed: 0.3.0]
│   │   │   └── yarl [required: >=1.17.0,<2.0, installed: 1.18.3]
│   │   │       ├── idna [required: >=2.0, installed: 3.7]
│   │   │       ├── multidict [required: >=4.0, installed: 6.1.0]
│   │   │       └── propcache [required: >=0.2.0, installed: 0.3.0]
│   │   ├── dataclasses-json [required: >=0.5.7,<0.7, installed: 0.6.7]
│   │   │   ├── marshmallow [required: >=3.18.0,<4.0.0, installed: 3.26.1]
│   │   │   │   └── packaging [required: >=17.0, installed: 24.2]
│   │   │   └── typing-inspect [required: >=0.4.0,<1, installed: 0.9.0]
│   │   │       ├── mypy-extensions [required: >=0.3.0, installed: 1.0.0]
│   │   │       └── typing_extensions [required: >=3.7.4, installed: 4.12.2]
│   │   ├── httpx-sse [required: >=0.4.0,<1.0.0, installed: 0.4.0]
│   │   ├── langchain [required: >=0.3.21,<1.0.0, installed: 0.3.21]
│   │   │   ├── langchain-core [required: >=0.3.45,<1.0.0, installed: 0.3.47]
│   │   │   │   ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
│   │   │   │   │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   │   │   │   ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   │   │   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   │   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   │   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   │   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   │   │   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   │   │   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   │   │   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   │   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   │   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   │   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   │   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   │   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │   │   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   │   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   │   │   │   ├── packaging [required: >=23.2,<25, installed: 24.2]
│   │   │   │   ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
│   │   │   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   │   │   ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
│   │   │   │   └── typing_extensions [required: >=4.7, installed: 4.12.2]
│   │   │   ├── langchain-text-splitters [required: >=0.3.7,<1.0.0, installed: 0.3.7]
│   │   │   │   └── langchain-core [required: >=0.3.45,<1.0.0, installed: 0.3.47]
│   │   │   │       ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
│   │   │   │       │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   │   │   │       ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   │   │       │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   │       │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │       │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │       │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │       │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   │       │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │       │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │       │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │       │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   │       │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   │       │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   │   │       │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   │   │       │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   │   │       │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   │       │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │       │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │       │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │       │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   │       │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   │       │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │       │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │       │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │       │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   │       │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   │       │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │   │       │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │       │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │       │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │       │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   │       │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   │   │   │       ├── packaging [required: >=23.2,<25, installed: 24.2]
│   │   │   │       ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
│   │   │   │       │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │       │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │       │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │       │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   │       ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   │   │       ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
│   │   │   │       └── typing_extensions [required: >=4.7, installed: 4.12.2]
│   │   │   ├── langsmith [required: >=0.1.17,<0.4, installed: 0.3.18]
│   │   │   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   │   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   │   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   │   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   │   │   ├── pydantic [required: >=2.7.4,<3.0.0, installed: 2.10.6]
│   │   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   └── SQLAlchemy [required: >=1.4,<3, installed: 2.0.30]
│   │   │       ├── greenlet [required: !=0.4.17, installed: 3.0.3]
│   │   │       └── typing_extensions [required: >=4.6.0, installed: 4.12.2]
│   │   ├── langchain-core [required: >=0.3.45,<1.0.0, installed: 0.3.47]
│   │   │   ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
│   │   │   │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   │   │   ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   │   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   │   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   │   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   │   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   │   │   ├── packaging [required: >=23.2,<25, installed: 24.2]
│   │   │   ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
│   │   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   │   ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
│   │   │   └── typing_extensions [required: >=4.7, installed: 4.12.2]
│   │   ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   │   ├── numpy [required: >=1.26.2,<3, installed: 1.26.4]
│   │   ├── pydantic-settings [required: >=2.4.0,<3.0.0, installed: 2.8.1]
│   │   │   ├── pydantic [required: >=2.7.0, installed: 2.10.6]
│   │   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   └── python-dotenv [required: >=0.21.0, installed: 1.0.1]
│   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   ├── SQLAlchemy [required: >=1.4,<3, installed: 2.0.30]
│   │   │   ├── greenlet [required: !=0.4.17, installed: 3.0.3]
│   │   │   └── typing_extensions [required: >=4.6.0, installed: 4.12.2]
│   │   └── tenacity [required: >=8.1.0,<10,!=8.4.0, installed: 8.5.0]
│   └── pydantic [required: >=2.10.0,<3, installed: 2.10.6]
│       ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│       ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│       │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│       └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
├── jupyter_server [required: >=2.4.0,<3, installed: 2.14.0]
│   ├── anyio [required: >=3.1.0, installed: 4.9.0]
│   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   ├── argon2-cffi [required: >=21.1, installed: 23.1.0]
│   │   └── argon2-cffi-bindings [required: Any, installed: 21.2.0]
│   │       └── cffi [required: >=1.0.1, installed: 1.16.0]
│   │           └── pycparser [required: Any, installed: 2.22]
│   ├── Jinja2 [required: >=3.0.3, installed: 3.1.4]
│   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   ├── jupyter_client [required: >=7.4.4, installed: 8.6.1]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter-events [required: >=0.9.0, installed: 0.10.0]
│   │   ├── jsonschema [required: >=4.18.0, installed: 4.22.0]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   ├── referencing [required: Any, installed: 0.35.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   ├── rfc3339-validator [required: Any, installed: 0.1.4]
│   │   │   └── six [required: Any, installed: 1.16.0]
│   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       └── tornado [required: >=6.1.0, installed: 6.4]
│   ├── nbconvert [required: >=6.4.4, installed: 7.16.4]
│   │   ├── beautifulsoup4 [required: Any, installed: 4.12.3]
│   │   │   └── soupsieve [required: >1.2, installed: 2.5]
│   │   ├── bleach [required: !=5.0.0, installed: 6.1.0]
│   │   │   ├── six [required: >=1.9.0, installed: 1.16.0]
│   │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │   ├── Jinja2 [required: >=3.0, installed: 3.1.4]
│   │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   ├── jupyter_core [required: >=4.7, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │   ├── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   ├── mistune [required: >=2.0.3,<4, installed: 3.0.2]
│   │   ├── nbclient [required: >=0.5.0, installed: 0.10.0]
│   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── packaging [required: Any, installed: 24.2]
│   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │   ├── Pygments [required: >=2.4.1, installed: 2.18.0]
│   │   ├── tinycss2 [required: Any, installed: 1.3.0]
│   │   │   └── webencodings [required: >=0.4, installed: 0.5.1]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── overrides [required: >=5.0, installed: 7.7.0]
│   ├── packaging [required: >=22.0, installed: 24.2]
│   ├── prometheus_client [required: >=0.9, installed: 0.20.0]
│   ├── pyzmq [required: >=24, installed: 26.0.3]
│   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   └── tornado [required: >=6.1.0, installed: 6.4]
│   ├── tornado [required: >=6.2.0, installed: 6.4]
│   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   └── websocket-client [required: >=1.7, installed: 1.8.0]
├── pydantic [required: >=2.10.0,<3, installed: 2.10.6]
│   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
└── traitlets [required: >=5.6, installed: 5.14.3]
jupyter-rsession-proxy==2.2.1
└── jupyter_server_proxy [required: >=3.2.3,!=4.1.0,!=4.0.0, installed: 4.4.0]
    ├── aiohttp [required: Any, installed: 3.11.13]
    │   ├── aiohappyeyeballs [required: >=2.3.0, installed: 2.4.8]
    │   ├── aiosignal [required: >=1.1.2, installed: 1.3.2]
    │   │   └── frozenlist [required: >=1.1.0, installed: 1.5.0]
    │   ├── attrs [required: >=17.3.0, installed: 23.2.0]
    │   ├── frozenlist [required: >=1.1.1, installed: 1.5.0]
    │   ├── multidict [required: >=4.5,<7.0, installed: 6.1.0]
    │   ├── propcache [required: >=0.2.0, installed: 0.3.0]
    │   └── yarl [required: >=1.17.0,<2.0, installed: 1.18.3]
    │       ├── idna [required: >=2.0, installed: 3.7]
    │       ├── multidict [required: >=4.0, installed: 6.1.0]
    │       └── propcache [required: >=0.2.0, installed: 0.3.0]
    ├── jupyter_server [required: >=1.24.0, installed: 2.14.0]
    │   ├── anyio [required: >=3.1.0, installed: 4.9.0]
    │   │   ├── idna [required: >=2.8, installed: 3.7]
    │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
    │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
    │   ├── argon2-cffi [required: >=21.1, installed: 23.1.0]
    │   │   └── argon2-cffi-bindings [required: Any, installed: 21.2.0]
    │   │       └── cffi [required: >=1.0.1, installed: 1.16.0]
    │   │           └── pycparser [required: Any, installed: 2.22]
    │   ├── Jinja2 [required: >=3.0.3, installed: 3.1.4]
    │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
    │   ├── jupyter_client [required: >=7.4.4, installed: 8.6.1]
    │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
    │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
    │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
    │   │   │   └── six [required: >=1.5, installed: 1.16.0]
    │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
    │   │   ├── tornado [required: >=6.2, installed: 6.4]
    │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
    │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
    │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   ├── jupyter-events [required: >=0.9.0, installed: 0.10.0]
    │   │   ├── jsonschema [required: >=4.18.0, installed: 4.22.0]
    │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
    │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
    │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
    │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
    │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
    │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
    │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
    │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
    │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
    │   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
    │   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
    │   │   ├── referencing [required: Any, installed: 0.35.1]
    │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
    │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
    │   │   ├── rfc3339-validator [required: Any, installed: 0.1.4]
    │   │   │   └── six [required: Any, installed: 1.16.0]
    │   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
    │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
    │   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
    │   │       ├── ptyprocess [required: Any, installed: 0.7.0]
    │   │       └── tornado [required: >=6.1.0, installed: 6.4]
    │   ├── nbconvert [required: >=6.4.4, installed: 7.16.4]
    │   │   ├── beautifulsoup4 [required: Any, installed: 4.12.3]
    │   │   │   └── soupsieve [required: >1.2, installed: 2.5]
    │   │   ├── bleach [required: !=5.0.0, installed: 6.1.0]
    │   │   │   ├── six [required: >=1.9.0, installed: 1.16.0]
    │   │   │   └── webencodings [required: Any, installed: 0.5.1]
    │   │   ├── defusedxml [required: Any, installed: 0.7.1]
    │   │   ├── Jinja2 [required: >=3.0, installed: 3.1.4]
    │   │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
    │   │   ├── jupyter_core [required: >=4.7, installed: 5.7.2]
    │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
    │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
    │   │   ├── MarkupSafe [required: >=2.0, installed: 2.1.5]
    │   │   ├── mistune [required: >=2.0.3,<4, installed: 3.0.2]
    │   │   ├── nbclient [required: >=0.5.0, installed: 0.10.0]
    │   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.1]
    │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
    │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
    │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
    │   │   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
    │   │   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
    │   │   │   │   ├── tornado [required: >=6.2, installed: 6.4]
    │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
    │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
    │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
    │   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
    │   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
    │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
    │   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
    │   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
    │   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
    │   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
    │   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
    │   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
    │   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
    │   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
    │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
    │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
    │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
    │   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
    │   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
    │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
    │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
    │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
    │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
    │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
    │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
    │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
    │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
    │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
    │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
    │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
    │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
    │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
    │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
    │   │   ├── packaging [required: Any, installed: 24.2]
    │   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
    │   │   ├── Pygments [required: >=2.4.1, installed: 2.18.0]
    │   │   ├── tinycss2 [required: Any, installed: 1.3.0]
    │   │   │   └── webencodings [required: >=0.4, installed: 0.5.1]
    │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
    │   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
    │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
    │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
    │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
    │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
    │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
    │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
    │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
    │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
    │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
    │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
    │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
    │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
    │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
    │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
    │   ├── overrides [required: >=5.0, installed: 7.7.0]
    │   ├── packaging [required: >=22.0, installed: 24.2]
    │   ├── prometheus_client [required: >=0.9, installed: 0.20.0]
    │   ├── pyzmq [required: >=24, installed: 26.0.3]
    │   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
    │   ├── terminado [required: >=0.8.3, installed: 0.18.1]
    │   │   ├── ptyprocess [required: Any, installed: 0.7.0]
    │   │   └── tornado [required: >=6.1.0, installed: 6.4]
    │   ├── tornado [required: >=6.2.0, installed: 6.4]
    │   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
    │   └── websocket-client [required: >=1.7, installed: 1.8.0]
    ├── simpervisor [required: >=1.0.0, installed: 1.0.0]
    ├── tornado [required: >=6.1.0, installed: 6.4]
    └── traitlets [required: >=5.1.0, installed: 5.14.3]
jupyterhub==4.1.5
├── alembic [required: >=1.4, installed: 1.13.1]
│   ├── Mako [required: Any, installed: 1.3.5]
│   │   └── MarkupSafe [required: >=0.9.2, installed: 2.1.5]
│   ├── SQLAlchemy [required: >=1.3.0, installed: 2.0.30]
│   │   ├── greenlet [required: !=0.4.17, installed: 3.0.3]
│   │   └── typing_extensions [required: >=4.6.0, installed: 4.12.2]
│   └── typing_extensions [required: >=4, installed: 4.12.2]
├── async-generator [required: >=1.9, installed: 1.10]
├── certipy [required: >=0.1.2, installed: 0.1.3]
│   └── pyOpenSSL [required: Any, installed: 24.0.0]
│       └── cryptography [required: >=41.0.5,<43, installed: 42.0.7]
│           └── cffi [required: >=1.12, installed: 1.16.0]
│               └── pycparser [required: Any, installed: 2.22]
├── Jinja2 [required: >=2.11.0, installed: 3.1.4]
│   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
├── jupyter-telemetry [required: >=0.1.0, installed: 0.1.0]
│   ├── jsonschema [required: Any, installed: 4.22.0]
│   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   ├── python-json-logger [required: Any, installed: 2.0.7]
│   ├── ruamel.yaml [required: Any, installed: 0.18.6]
│   │   └── ruamel.yaml.clib [required: >=0.2.7, installed: 0.2.8]
│   └── traitlets [required: Any, installed: 5.14.3]
├── oauthlib [required: >=3.0, installed: 3.2.2]
├── packaging [required: Any, installed: 24.2]
├── pamela [required: Any, installed: 1.1.0]
├── prometheus_client [required: >=0.4.0, installed: 0.20.0]
├── python-dateutil [required: Any, installed: 2.9.0]
│   └── six [required: >=1.5, installed: 1.16.0]
├── requests [required: Any, installed: 2.32.3]
│   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   ├── idna [required: >=2.5,<4, installed: 3.7]
│   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
├── SQLAlchemy [required: >=1.4, installed: 2.0.30]
│   ├── greenlet [required: !=0.4.17, installed: 3.0.3]
│   └── typing_extensions [required: >=4.6.0, installed: 4.12.2]
├── tornado [required: >=5.1, installed: 6.4]
└── traitlets [required: >=4.3.2, installed: 5.14.3]
langchain-anthropic==0.3.10
├── anthropic [required: >=0.49.0,<1, installed: 0.49.0]
│   ├── anyio [required: >=3.5.0,<5, installed: 4.9.0]
│   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   ├── distro [required: >=1.7.0,<2, installed: 1.9.0]
│   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   ├── idna [required: Any, installed: 3.7]
│   │   └── sniffio [required: Any, installed: 1.3.1]
│   ├── jiter [required: >=0.4.0,<1, installed: 0.9.0]
│   ├── pydantic [required: >=1.9.0,<3, installed: 2.10.6]
│   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   ├── sniffio [required: Any, installed: 1.3.1]
│   └── typing_extensions [required: >=4.10,<5, installed: 4.12.2]
├── langchain-core [required: >=0.3.45,<1.0.0, installed: 0.3.47]
│   ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
│   │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   ├── packaging [required: >=23.2,<25, installed: 24.2]
│   ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
│   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
│   └── typing_extensions [required: >=4.7, installed: 4.12.2]
└── pydantic [required: >=2.7.4,<3.0.0, installed: 2.10.6]
    ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
    ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
    │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
    └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
langchain-aws==0.2.17
├── boto3 [required: >=1.37.0, installed: 1.37.18]
│   ├── botocore [required: >=1.37.18,<1.38.0, installed: 1.37.18]
│   │   ├── jmespath [required: >=0.7.1,<2.0.0, installed: 1.0.1]
│   │   ├── python-dateutil [required: >=2.1,<3.0.0, installed: 2.9.0]
│   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   └── urllib3 [required: >=1.25.4,<3,!=2.2.0, installed: 2.2.1]
│   ├── jmespath [required: >=0.7.1,<2.0.0, installed: 1.0.1]
│   └── s3transfer [required: >=0.11.0,<0.12.0, installed: 0.11.4]
│       └── botocore [required: >=1.37.4,<2.0a.0, installed: 1.37.18]
│           ├── jmespath [required: >=0.7.1,<2.0.0, installed: 1.0.1]
│           ├── python-dateutil [required: >=2.1,<3.0.0, installed: 2.9.0]
│           │   └── six [required: >=1.5, installed: 1.16.0]
│           └── urllib3 [required: >=1.25.4,<3,!=2.2.0, installed: 2.2.1]
├── langchain-core [required: >=0.3.43,<0.4.0, installed: 0.3.47]
│   ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
│   │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   ├── packaging [required: >=23.2,<25, installed: 24.2]
│   ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
│   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
│   └── typing_extensions [required: >=4.7, installed: 4.12.2]
├── numpy [required: >=1,<2, installed: 1.26.4]
└── pydantic [required: >=2.10.0,<3, installed: 2.10.6]
    ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
    ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
    │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
    └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
langchain-cohere==0.4.3
├── cohere [required: >=5.12.0,<6.0, installed: 5.14.0]
│   ├── fastavro [required: >=1.9.4,<2.0.0, installed: 1.10.0]
│   ├── httpx [required: >=0.21.2, installed: 0.27.0]
│   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   ├── idna [required: Any, installed: 3.7]
│   │   └── sniffio [required: Any, installed: 1.3.1]
│   ├── httpx-sse [required: ==0.4.0, installed: 0.4.0]
│   ├── pydantic [required: >=1.9.2, installed: 2.10.6]
│   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   ├── pydantic_core [required: >=2.18.2,<3.0.0, installed: 2.27.2]
│   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   ├── requests [required: >=2.0.0,<3.0.0, installed: 2.32.3]
│   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   ├── tokenizers [required: >=0.15,<1, installed: 0.21.1]
│   │   └── huggingface-hub [required: >=0.16.4,<1.0, installed: 0.29.3]
│   │       ├── filelock [required: Any, installed: 3.18.0]
│   │       ├── fsspec [required: >=2023.5.0, installed: 2025.3.0]
│   │       ├── packaging [required: >=20.9, installed: 24.2]
│   │       ├── PyYAML [required: >=5.1, installed: 6.0.1]
│   │       ├── requests [required: Any, installed: 2.32.3]
│   │       │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │       │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │       │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │       │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │       ├── tqdm [required: >=4.42.1, installed: 4.66.4]
│   │       └── typing_extensions [required: >=3.7.4.3, installed: 4.12.2]
│   ├── types-requests [required: >=2.0.0,<3.0.0, installed: 2.32.0.20250306]
│   │   └── urllib3 [required: >=2, installed: 2.2.1]
│   └── typing_extensions [required: >=4.0.0, installed: 4.12.2]
├── langchain-community [required: >=0.3.0,<0.4.0, installed: 0.3.20]
│   ├── aiohttp [required: >=3.8.3,<4.0.0, installed: 3.11.13]
│   │   ├── aiohappyeyeballs [required: >=2.3.0, installed: 2.4.8]
│   │   ├── aiosignal [required: >=1.1.2, installed: 1.3.2]
│   │   │   └── frozenlist [required: >=1.1.0, installed: 1.5.0]
│   │   ├── attrs [required: >=17.3.0, installed: 23.2.0]
│   │   ├── frozenlist [required: >=1.1.1, installed: 1.5.0]
│   │   ├── multidict [required: >=4.5,<7.0, installed: 6.1.0]
│   │   ├── propcache [required: >=0.2.0, installed: 0.3.0]
│   │   └── yarl [required: >=1.17.0,<2.0, installed: 1.18.3]
│   │       ├── idna [required: >=2.0, installed: 3.7]
│   │       ├── multidict [required: >=4.0, installed: 6.1.0]
│   │       └── propcache [required: >=0.2.0, installed: 0.3.0]
│   ├── dataclasses-json [required: >=0.5.7,<0.7, installed: 0.6.7]
│   │   ├── marshmallow [required: >=3.18.0,<4.0.0, installed: 3.26.1]
│   │   │   └── packaging [required: >=17.0, installed: 24.2]
│   │   └── typing-inspect [required: >=0.4.0,<1, installed: 0.9.0]
│   │       ├── mypy-extensions [required: >=0.3.0, installed: 1.0.0]
│   │       └── typing_extensions [required: >=3.7.4, installed: 4.12.2]
│   ├── httpx-sse [required: >=0.4.0,<1.0.0, installed: 0.4.0]
│   ├── langchain [required: >=0.3.21,<1.0.0, installed: 0.3.21]
│   │   ├── langchain-core [required: >=0.3.45,<1.0.0, installed: 0.3.47]
│   │   │   ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
│   │   │   │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   │   │   ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   │   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   │   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   │   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   │   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   │   │   ├── packaging [required: >=23.2,<25, installed: 24.2]
│   │   │   ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
│   │   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   │   ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
│   │   │   └── typing_extensions [required: >=4.7, installed: 4.12.2]
│   │   ├── langchain-text-splitters [required: >=0.3.7,<1.0.0, installed: 0.3.7]
│   │   │   └── langchain-core [required: >=0.3.45,<1.0.0, installed: 0.3.47]
│   │   │       ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
│   │   │       │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   │   │       ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   │       │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │       │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │       │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │       │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │       │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │       │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │       │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │       │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │       │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │       │   │   ├── idna [required: Any, installed: 3.7]
│   │   │       │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   │       │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   │       │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   │       │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │       │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │       │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │       │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │       │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │       │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │       │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │       │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │       │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │       │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │       │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │       │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │       │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │       │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │       │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │       │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │       │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   │   │       ├── packaging [required: >=23.2,<25, installed: 24.2]
│   │   │       ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
│   │   │       │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │       │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │       │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │       │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │       ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   │       ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
│   │   │       └── typing_extensions [required: >=4.7, installed: 4.12.2]
│   │   ├── langsmith [required: >=0.1.17,<0.4, installed: 0.3.18]
│   │   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   │   ├── pydantic [required: >=2.7.4,<3.0.0, installed: 2.10.6]
│   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   └── SQLAlchemy [required: >=1.4,<3, installed: 2.0.30]
│   │       ├── greenlet [required: !=0.4.17, installed: 3.0.3]
│   │       └── typing_extensions [required: >=4.6.0, installed: 4.12.2]
│   ├── langchain-core [required: >=0.3.45,<1.0.0, installed: 0.3.47]
│   │   ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
│   │   │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   │   ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   │   ├── packaging [required: >=23.2,<25, installed: 24.2]
│   │   ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
│   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
│   │   └── typing_extensions [required: >=4.7, installed: 4.12.2]
│   ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   ├── numpy [required: >=1.26.2,<3, installed: 1.26.4]
│   ├── pydantic-settings [required: >=2.4.0,<3.0.0, installed: 2.8.1]
│   │   ├── pydantic [required: >=2.7.0, installed: 2.10.6]
│   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   └── python-dotenv [required: >=0.21.0, installed: 1.0.1]
│   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   ├── SQLAlchemy [required: >=1.4,<3, installed: 2.0.30]
│   │   ├── greenlet [required: !=0.4.17, installed: 3.0.3]
│   │   └── typing_extensions [required: >=4.6.0, installed: 4.12.2]
│   └── tenacity [required: >=8.1.0,<10,!=8.4.0, installed: 8.5.0]
├── langchain-core [required: >=0.3.27,<0.4.0, installed: 0.3.47]
│   ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
│   │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   ├── packaging [required: >=23.2,<25, installed: 24.2]
│   ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
│   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
│   └── typing_extensions [required: >=4.7, installed: 4.12.2]
├── pydantic [required: >=2,<3, installed: 2.10.6]
│   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
└── types-PyYAML [required: >=6.0.12.20240917,<7.0.0.0, installed: 6.0.12.20241230]
langchain-google-genai==2.1.1
├── filetype [required: >=1.2.0,<2.0.0, installed: 1.2.0]
├── google-ai-generativelanguage [required: >=0.6.16,<0.7.0, installed: 0.6.17]
│   ├── google-api-core [required: >=1.34.1,<3.0.0,!=2.9.*,!=2.8.*,!=2.7.*,!=2.6.*,!=2.5.*,!=2.4.*,!=2.3.*,!=2.2.*,!=2.10.*,!=2.1.*,!=2.0.*, installed: 2.24.2]
│   │   ├── google-auth [required: >=2.14.1,<3.0.0, installed: 2.38.0]
│   │   │   ├── cachetools [required: >=2.0.0,<6.0, installed: 5.5.2]
│   │   │   ├── pyasn1_modules [required: >=0.2.1, installed: 0.4.1]
│   │   │   │   └── pyasn1 [required: >=0.4.6,<0.7.0, installed: 0.6.1]
│   │   │   └── rsa [required: >=3.1.4,<5, installed: 4.9]
│   │   │       └── pyasn1 [required: >=0.1.3, installed: 0.6.1]
│   │   ├── googleapis-common-protos [required: >=1.56.2,<2.0.0, installed: 1.69.2]
│   │   │   └── protobuf [required: >=3.20.2,<7.0.0,!=4.21.5,!=4.21.4,!=4.21.3,!=4.21.2,!=4.21.1, installed: 5.29.3]
│   │   ├── proto-plus [required: >=1.22.3,<2.0.0, installed: 1.26.1]
│   │   │   └── protobuf [required: >=3.19.0,<7.0.0, installed: 5.29.3]
│   │   ├── protobuf [required: >=3.19.5,<7.0.0,!=4.21.5,!=4.21.4,!=4.21.3,!=4.21.2,!=4.21.1,!=4.21.0,!=3.20.1,!=3.20.0, installed: 5.29.3]
│   │   └── requests [required: >=2.18.0,<3.0.0, installed: 2.32.3]
│   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   ├── google-auth [required: >=2.14.1,<3.0.0,!=2.25.0,!=2.24.0, installed: 2.38.0]
│   │   ├── cachetools [required: >=2.0.0,<6.0, installed: 5.5.2]
│   │   ├── pyasn1_modules [required: >=0.2.1, installed: 0.4.1]
│   │   │   └── pyasn1 [required: >=0.4.6,<0.7.0, installed: 0.6.1]
│   │   └── rsa [required: >=3.1.4,<5, installed: 4.9]
│   │       └── pyasn1 [required: >=0.1.3, installed: 0.6.1]
│   ├── proto-plus [required: >=1.22.3,<2.0.0, installed: 1.26.1]
│   │   └── protobuf [required: >=3.19.0,<7.0.0, installed: 5.29.3]
│   └── protobuf [required: >=3.20.2,<7.0.0,!=4.21.5,!=4.21.4,!=4.21.3,!=4.21.2,!=4.21.1,!=4.21.0, installed: 5.29.3]
├── langchain-core [required: >=0.3.47,<0.4.0, installed: 0.3.47]
│   ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
│   │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   ├── packaging [required: >=23.2,<25, installed: 24.2]
│   ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
│   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
│   └── typing_extensions [required: >=4.7, installed: 4.12.2]
└── pydantic [required: >=2,<3, installed: 2.10.6]
    ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
    ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
    │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
    └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
langchain-mistralai==0.2.9
├── httpx [required: >=0.25.2,<1, installed: 0.27.0]
│   ├── anyio [required: Any, installed: 4.9.0]
│   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   ├── certifi [required: Any, installed: 2025.1.31]
│   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   ├── idna [required: Any, installed: 3.7]
│   └── sniffio [required: Any, installed: 1.3.1]
├── httpx-sse [required: >=0.3.1,<1, installed: 0.4.0]
├── langchain-core [required: >=0.3.47,<1.0.0, installed: 0.3.47]
│   ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
│   │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   ├── packaging [required: >=23.2,<25, installed: 24.2]
│   ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
│   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
│   └── typing_extensions [required: >=4.7, installed: 4.12.2]
├── pydantic [required: >=2,<3, installed: 2.10.6]
│   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
└── tokenizers [required: >=0.15.1,<1, installed: 0.21.1]
    └── huggingface-hub [required: >=0.16.4,<1.0, installed: 0.29.3]
        ├── filelock [required: Any, installed: 3.18.0]
        ├── fsspec [required: >=2023.5.0, installed: 2025.3.0]
        ├── packaging [required: >=20.9, installed: 24.2]
        ├── PyYAML [required: >=5.1, installed: 6.0.1]
        ├── requests [required: Any, installed: 2.32.3]
        │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
        │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
        │   ├── idna [required: >=2.5,<4, installed: 3.7]
        │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
        ├── tqdm [required: >=4.42.1, installed: 4.66.4]
        └── typing_extensions [required: >=3.7.4.3, installed: 4.12.2]
langchain-nvidia-ai-endpoints==0.3.9
├── aiohttp [required: >=3.9.1,<4.0.0, installed: 3.11.13]
│   ├── aiohappyeyeballs [required: >=2.3.0, installed: 2.4.8]
│   ├── aiosignal [required: >=1.1.2, installed: 1.3.2]
│   │   └── frozenlist [required: >=1.1.0, installed: 1.5.0]
│   ├── attrs [required: >=17.3.0, installed: 23.2.0]
│   ├── frozenlist [required: >=1.1.1, installed: 1.5.0]
│   ├── multidict [required: >=4.5,<7.0, installed: 6.1.0]
│   ├── propcache [required: >=0.2.0, installed: 0.3.0]
│   └── yarl [required: >=1.17.0,<2.0, installed: 1.18.3]
│       ├── idna [required: >=2.0, installed: 3.7]
│       ├── multidict [required: >=4.0, installed: 6.1.0]
│       └── propcache [required: >=0.2.0, installed: 0.3.0]
└── langchain-core [required: >=0.3.0,<0.4, installed: 0.3.47]
    ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
    │   └── jsonpointer [required: >=1.9, installed: 2.4]
    ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
    │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
    │   │   ├── anyio [required: Any, installed: 4.9.0]
    │   │   │   ├── idna [required: >=2.8, installed: 3.7]
    │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
    │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
    │   │   ├── certifi [required: Any, installed: 2025.1.31]
    │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
    │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
    │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
    │   │   ├── idna [required: Any, installed: 3.7]
    │   │   └── sniffio [required: Any, installed: 1.3.1]
    │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
    │   ├── packaging [required: >=23.2, installed: 24.2]
    │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
    │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
    │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
    │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
    │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
    │   ├── requests [required: >=2,<3, installed: 2.32.3]
    │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
    │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
    │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
    │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
    │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
    │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
    │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
    │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
    │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
    │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
    │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
    ├── packaging [required: >=23.2,<25, installed: 24.2]
    ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
    │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
    │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
    │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
    │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
    ├── PyYAML [required: >=5.3, installed: 6.0.1]
    ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
    └── typing_extensions [required: >=4.7, installed: 4.12.2]
langchain-ollama==0.3.0
├── langchain-core [required: >=0.3.47,<1.0.0, installed: 0.3.47]
│   ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
│   │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   ├── packaging [required: >=23.2,<25, installed: 24.2]
│   ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
│   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
│   └── typing_extensions [required: >=4.7, installed: 4.12.2]
└── ollama [required: >=0.4.4,<1, installed: 0.4.7]
    ├── httpx [required: >=0.27,<0.29, installed: 0.27.0]
    │   ├── anyio [required: Any, installed: 4.9.0]
    │   │   ├── idna [required: >=2.8, installed: 3.7]
    │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
    │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
    │   ├── certifi [required: Any, installed: 2025.1.31]
    │   ├── httpcore [required: ==1.*, installed: 1.0.5]
    │   │   ├── certifi [required: Any, installed: 2025.1.31]
    │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
    │   ├── idna [required: Any, installed: 3.7]
    │   └── sniffio [required: Any, installed: 1.3.1]
    └── pydantic [required: >=2.9.0,<3.0.0, installed: 2.10.6]
        ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
        ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
        │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
        └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
langchain-openai==0.3.9
├── langchain-core [required: >=0.3.45,<1.0.0, installed: 0.3.47]
│   ├── jsonpatch [required: >=1.33,<2.0, installed: 1.33]
│   │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   ├── langsmith [required: >=0.1.125,<0.4, installed: 0.3.18]
│   │   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   │   ├── idna [required: Any, installed: 3.7]
│   │   │   └── sniffio [required: Any, installed: 1.3.1]
│   │   ├── orjson [required: >=3.9.14,<4.0.0, installed: 3.10.15]
│   │   ├── packaging [required: >=23.2, installed: 24.2]
│   │   ├── pydantic [required: >=1,<3, installed: 2.10.6]
│   │   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   │   ├── requests [required: >=2,<3, installed: 2.32.3]
│   │   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   ├── requests-toolbelt [required: >=1.0.0,<2.0.0, installed: 1.0.0]
│   │   │   └── requests [required: >=2.0.1,<3.0.0, installed: 2.32.3]
│   │   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │   └── zstandard [required: >=0.23.0,<0.24.0, installed: 0.23.0]
│   ├── packaging [required: >=23.2,<25, installed: 24.2]
│   ├── pydantic [required: >=2.5.2,<3.0.0, installed: 2.10.6]
│   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   ├── tenacity [required: >=8.1.0,<10.0.0,!=8.4.0, installed: 8.5.0]
│   └── typing_extensions [required: >=4.7, installed: 4.12.2]
├── openai [required: >=1.66.3,<2.0.0, installed: 1.68.2]
│   ├── anyio [required: >=3.5.0,<5, installed: 4.9.0]
│   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   ├── distro [required: >=1.7.0,<2, installed: 1.9.0]
│   ├── httpx [required: >=0.23.0,<1, installed: 0.27.0]
│   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   ├── idna [required: Any, installed: 3.7]
│   │   └── sniffio [required: Any, installed: 1.3.1]
│   ├── jiter [required: >=0.4.0,<1, installed: 0.9.0]
│   ├── pydantic [required: >=1.9.0,<3, installed: 2.10.6]
│   │   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   │   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   │   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
│   ├── sniffio [required: Any, installed: 1.3.1]
│   ├── tqdm [required: >4, installed: 4.66.4]
│   └── typing_extensions [required: >=4.11,<5, installed: 4.12.2]
└── tiktoken [required: >=0.7,<1, installed: 0.9.0]
    ├── regex [required: >=2022.1.18, installed: 2024.11.6]
    └── requests [required: >=2.26.0, installed: 2.32.3]
        ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
        ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
        ├── idna [required: >=2.5,<4, installed: 3.7]
        └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
mamba==1.5.8
├── conda [required: >=4.14.0, installed: 24.5.0]
│   ├── archspec [required: >=0.2.3, installed: 0.2.3]
│   ├── boltons [required: >=23.0.0, installed: 24.0.0]
│   ├── charset-normalizer [required: Any, installed: 3.3.2]
│   ├── conda-libmamba-solver [required: >=23.11.0, installed: 24.1.0]
│   │   ├── boltons [required: >=23.0.0, installed: 24.0.0]
│   │   └── libmambapy [required: >=1.5.6, installed: 1.5.8]
│   ├── conda-package-handling [required: >=2.2.0, installed: 2.2.0]
│   │   └── conda_package_streaming [required: >=0.9.0, installed: 0.9.0]
│   │       ├── requests [required: Any, installed: 2.32.3]
│   │       │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │       │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │       │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │       │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   │       └── zstandard [required: >=0.15, installed: 0.23.0]
│   ├── distro [required: >=1.5.0, installed: 1.9.0]
│   ├── frozendict [required: >=2.4.2, installed: 2.4.4]
│   ├── jsonpatch [required: >=1.32, installed: 1.33]
│   │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   ├── menuinst [required: >=2, installed: 2.0.2]
│   ├── packaging [required: >=23.0, installed: 24.2]
│   ├── platformdirs [required: >=3.10.0, installed: 4.2.2]
│   ├── pluggy [required: >=1.0.0, installed: 1.5.0]
│   ├── pycosat [required: >=0.6.3, installed: 0.6.6]
│   ├── requests [required: >=2.28.0,<3, installed: 2.32.3]
│   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   ├── ruamel.yaml [required: >=0.11.14,<0.19, installed: 0.18.6]
│   │   └── ruamel.yaml.clib [required: >=0.2.7, installed: 0.2.8]
│   ├── setuptools [required: >=60.0.0, installed: 69.5.1]
│   ├── tqdm [required: >=4, installed: 4.66.4]
│   ├── truststore [required: >=0.8.0, installed: 0.8.0]
│   └── zstandard [required: >=0.15, installed: 0.23.0]
└── libmambapy [required: Any, installed: 1.5.8]
nbclassic==1.0.0
├── argon2-cffi [required: Any, installed: 23.1.0]
│   └── argon2-cffi-bindings [required: Any, installed: 21.2.0]
│       └── cffi [required: >=1.0.1, installed: 1.16.0]
│           └── pycparser [required: Any, installed: 2.22]
├── ipykernel [required: Any, installed: 6.29.3]
│   ├── comm [required: >=0.1.1, installed: 0.2.2]
│   │   └── traitlets [required: >=4, installed: 5.14.3]
│   ├── debugpy [required: >=1.6.5, installed: 1.8.1]
│   ├── ipython [required: >=7.23.1, installed: 8.24.0]
│   │   ├── decorator [required: Any, installed: 5.1.1]
│   │   ├── jedi [required: >=0.16, installed: 0.19.1]
│   │   │   └── parso [required: >=0.8.3,<0.9.0, installed: 0.8.4]
│   │   ├── matplotlib-inline [required: Any, installed: 0.1.7]
│   │   │   └── traitlets [required: Any, installed: 5.14.3]
│   │   ├── pexpect [required: >4.3, installed: 4.9.0]
│   │   │   └── ptyprocess [required: >=0.5, installed: 0.7.0]
│   │   ├── prompt-toolkit [required: >=3.0.41,<3.1.0, installed: 3.0.42]
│   │   │   └── wcwidth [required: Any, installed: 0.2.13]
│   │   ├── Pygments [required: >=2.4.0, installed: 2.18.0]
│   │   ├── stack-data [required: Any, installed: 0.6.2]
│   │   │   ├── asttokens [required: >=2.1.0, installed: 2.4.1]
│   │   │   │   └── six [required: >=1.12.0, installed: 1.16.0]
│   │   │   ├── executing [required: >=1.2.0, installed: 2.0.1]
│   │   │   └── pure-eval [required: Any, installed: 0.2.2]
│   │   ├── traitlets [required: >=5.13.0, installed: 5.14.3]
│   │   └── typing_extensions [required: >=4.6, installed: 4.12.2]
│   ├── jupyter_client [required: >=6.1.12, installed: 8.6.1]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── matplotlib-inline [required: >=0.1, installed: 0.1.7]
│   │   └── traitlets [required: Any, installed: 5.14.3]
│   ├── nest_asyncio [required: Any, installed: 1.6.0]
│   ├── packaging [required: Any, installed: 24.2]
│   ├── psutil [required: Any, installed: 5.9.8]
│   ├── pyzmq [required: >=24, installed: 26.0.3]
│   ├── tornado [required: >=6.1, installed: 6.4]
│   └── traitlets [required: >=5.4.0, installed: 5.14.3]
├── ipython-genutils [required: Any, installed: 0.2.0]
├── Jinja2 [required: Any, installed: 3.1.4]
│   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
├── jupyter_client [required: >=6.1.1, installed: 8.6.1]
│   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   └── six [required: >=1.5, installed: 1.16.0]
│   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   ├── tornado [required: >=6.2, installed: 6.4]
│   └── traitlets [required: >=5.3, installed: 5.14.3]
├── jupyter_core [required: >=4.6.1, installed: 5.7.2]
│   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   └── traitlets [required: >=5.3, installed: 5.14.3]
├── jupyter_server [required: >=1.8, installed: 2.14.0]
│   ├── anyio [required: >=3.1.0, installed: 4.9.0]
│   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   ├── argon2-cffi [required: >=21.1, installed: 23.1.0]
│   │   └── argon2-cffi-bindings [required: Any, installed: 21.2.0]
│   │       └── cffi [required: >=1.0.1, installed: 1.16.0]
│   │           └── pycparser [required: Any, installed: 2.22]
│   ├── Jinja2 [required: >=3.0.3, installed: 3.1.4]
│   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   ├── jupyter_client [required: >=7.4.4, installed: 8.6.1]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter-events [required: >=0.9.0, installed: 0.10.0]
│   │   ├── jsonschema [required: >=4.18.0, installed: 4.22.0]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   ├── referencing [required: Any, installed: 0.35.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   ├── rfc3339-validator [required: Any, installed: 0.1.4]
│   │   │   └── six [required: Any, installed: 1.16.0]
│   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       └── tornado [required: >=6.1.0, installed: 6.4]
│   ├── nbconvert [required: >=6.4.4, installed: 7.16.4]
│   │   ├── beautifulsoup4 [required: Any, installed: 4.12.3]
│   │   │   └── soupsieve [required: >1.2, installed: 2.5]
│   │   ├── bleach [required: !=5.0.0, installed: 6.1.0]
│   │   │   ├── six [required: >=1.9.0, installed: 1.16.0]
│   │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │   ├── Jinja2 [required: >=3.0, installed: 3.1.4]
│   │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   ├── jupyter_core [required: >=4.7, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │   ├── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   ├── mistune [required: >=2.0.3,<4, installed: 3.0.2]
│   │   ├── nbclient [required: >=0.5.0, installed: 0.10.0]
│   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── packaging [required: Any, installed: 24.2]
│   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │   ├── Pygments [required: >=2.4.1, installed: 2.18.0]
│   │   ├── tinycss2 [required: Any, installed: 1.3.0]
│   │   │   └── webencodings [required: >=0.4, installed: 0.5.1]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── overrides [required: >=5.0, installed: 7.7.0]
│   ├── packaging [required: >=22.0, installed: 24.2]
│   ├── prometheus_client [required: >=0.9, installed: 0.20.0]
│   ├── pyzmq [required: >=24, installed: 26.0.3]
│   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   └── tornado [required: >=6.1.0, installed: 6.4]
│   ├── tornado [required: >=6.2.0, installed: 6.4]
│   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   └── websocket-client [required: >=1.7, installed: 1.8.0]
├── nbconvert [required: >=5, installed: 7.16.4]
│   ├── beautifulsoup4 [required: Any, installed: 4.12.3]
│   │   └── soupsieve [required: >1.2, installed: 2.5]
│   ├── bleach [required: !=5.0.0, installed: 6.1.0]
│   │   ├── six [required: >=1.9.0, installed: 1.16.0]
│   │   └── webencodings [required: Any, installed: 0.5.1]
│   ├── defusedxml [required: Any, installed: 0.7.1]
│   ├── Jinja2 [required: >=3.0, installed: 3.1.4]
│   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   ├── jupyter_core [required: >=4.7, installed: 5.7.2]
│   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   ├── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   ├── mistune [required: >=2.0.3,<4, installed: 3.0.2]
│   ├── nbclient [required: >=0.5.0, installed: 0.10.0]
│   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── packaging [required: Any, installed: 24.2]
│   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   ├── Pygments [required: >=2.4.1, installed: 2.18.0]
│   ├── tinycss2 [required: Any, installed: 1.3.0]
│   │   └── webencodings [required: >=0.4, installed: 0.5.1]
│   └── traitlets [required: >=5.1, installed: 5.14.3]
├── nbformat [required: Any, installed: 5.10.4]
│   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   └── traitlets [required: >=5.1, installed: 5.14.3]
├── nest_asyncio [required: >=1.5, installed: 1.6.0]
├── notebook_shim [required: >=0.2.3, installed: 0.2.4]
│   └── jupyter_server [required: >=1.8,<3, installed: 2.14.0]
│       ├── anyio [required: >=3.1.0, installed: 4.9.0]
│       │   ├── idna [required: >=2.8, installed: 3.7]
│       │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│       │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│       ├── argon2-cffi [required: >=21.1, installed: 23.1.0]
│       │   └── argon2-cffi-bindings [required: Any, installed: 21.2.0]
│       │       └── cffi [required: >=1.0.1, installed: 1.16.0]
│       │           └── pycparser [required: Any, installed: 2.22]
│       ├── Jinja2 [required: >=3.0.3, installed: 3.1.4]
│       │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│       ├── jupyter_client [required: >=7.4.4, installed: 8.6.1]
│       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│       │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│       │   │   └── six [required: >=1.5, installed: 1.16.0]
│       │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│       │   ├── tornado [required: >=6.2, installed: 6.4]
│       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│       │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       ├── jupyter-events [required: >=0.9.0, installed: 0.10.0]
│       │   ├── jsonschema [required: >=4.18.0, installed: 4.22.0]
│       │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│       │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│       │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│       │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│       │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│       │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│       │   ├── referencing [required: Any, installed: 0.35.1]
│       │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   ├── rfc3339-validator [required: Any, installed: 0.1.4]
│       │   │   └── six [required: Any, installed: 1.16.0]
│       │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│       │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│       │       ├── ptyprocess [required: Any, installed: 0.7.0]
│       │       └── tornado [required: >=6.1.0, installed: 6.4]
│       ├── nbconvert [required: >=6.4.4, installed: 7.16.4]
│       │   ├── beautifulsoup4 [required: Any, installed: 4.12.3]
│       │   │   └── soupsieve [required: >1.2, installed: 2.5]
│       │   ├── bleach [required: !=5.0.0, installed: 6.1.0]
│       │   │   ├── six [required: >=1.9.0, installed: 1.16.0]
│       │   │   └── webencodings [required: Any, installed: 0.5.1]
│       │   ├── defusedxml [required: Any, installed: 0.7.1]
│       │   ├── Jinja2 [required: >=3.0, installed: 3.1.4]
│       │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│       │   ├── jupyter_core [required: >=4.7, installed: 5.7.2]
│       │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│       │   ├── MarkupSafe [required: >=2.0, installed: 2.1.5]
│       │   ├── mistune [required: >=2.0.3,<4, installed: 3.0.2]
│       │   ├── nbclient [required: >=0.5.0, installed: 0.10.0]
│       │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.1]
│       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│       │   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│       │   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│       │   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│       │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│       │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│       │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│       │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│       │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│       │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│       │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│       │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│       │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│       │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│       │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│       │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│       │   ├── packaging [required: Any, installed: 24.2]
│       │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│       │   ├── Pygments [required: >=2.4.1, installed: 2.18.0]
│       │   ├── tinycss2 [required: Any, installed: 1.3.0]
│       │   │   └── webencodings [required: >=0.4, installed: 0.5.1]
│       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│       ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│       │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│       │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│       │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│       │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│       │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│       │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│       │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│       ├── overrides [required: >=5.0, installed: 7.7.0]
│       ├── packaging [required: >=22.0, installed: 24.2]
│       ├── prometheus_client [required: >=0.9, installed: 0.20.0]
│       ├── pyzmq [required: >=24, installed: 26.0.3]
│       ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│       ├── terminado [required: >=0.8.3, installed: 0.18.1]
│       │   ├── ptyprocess [required: Any, installed: 0.7.0]
│       │   └── tornado [required: >=6.1.0, installed: 6.4]
│       ├── tornado [required: >=6.2.0, installed: 6.4]
│       ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│       └── websocket-client [required: >=1.7, installed: 1.8.0]
├── prometheus_client [required: Any, installed: 0.20.0]
├── pyzmq [required: >=17, installed: 26.0.3]
├── Send2Trash [required: >=1.8.0, installed: 1.8.3]
├── terminado [required: >=0.8.3, installed: 0.18.1]
│   ├── ptyprocess [required: Any, installed: 0.7.0]
│   └── tornado [required: >=6.1.0, installed: 6.4]
├── tornado [required: >=6.1, installed: 6.4]
└── traitlets [required: >=4.2.1, installed: 5.14.3]
nbgitpuller==1.2.2
├── jupyter_server [required: >=1.10.1, installed: 2.14.0]
│   ├── anyio [required: >=3.1.0, installed: 4.9.0]
│   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   ├── argon2-cffi [required: >=21.1, installed: 23.1.0]
│   │   └── argon2-cffi-bindings [required: Any, installed: 21.2.0]
│   │       └── cffi [required: >=1.0.1, installed: 1.16.0]
│   │           └── pycparser [required: Any, installed: 2.22]
│   ├── Jinja2 [required: >=3.0.3, installed: 3.1.4]
│   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   ├── jupyter_client [required: >=7.4.4, installed: 8.6.1]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter-events [required: >=0.9.0, installed: 0.10.0]
│   │   ├── jsonschema [required: >=4.18.0, installed: 4.22.0]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   ├── referencing [required: Any, installed: 0.35.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   ├── rfc3339-validator [required: Any, installed: 0.1.4]
│   │   │   └── six [required: Any, installed: 1.16.0]
│   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       └── tornado [required: >=6.1.0, installed: 6.4]
│   ├── nbconvert [required: >=6.4.4, installed: 7.16.4]
│   │   ├── beautifulsoup4 [required: Any, installed: 4.12.3]
│   │   │   └── soupsieve [required: >1.2, installed: 2.5]
│   │   ├── bleach [required: !=5.0.0, installed: 6.1.0]
│   │   │   ├── six [required: >=1.9.0, installed: 1.16.0]
│   │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │   ├── Jinja2 [required: >=3.0, installed: 3.1.4]
│   │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   ├── jupyter_core [required: >=4.7, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │   ├── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   ├── mistune [required: >=2.0.3,<4, installed: 3.0.2]
│   │   ├── nbclient [required: >=0.5.0, installed: 0.10.0]
│   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── packaging [required: Any, installed: 24.2]
│   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │   ├── Pygments [required: >=2.4.1, installed: 2.18.0]
│   │   ├── tinycss2 [required: Any, installed: 1.3.0]
│   │   │   └── webencodings [required: >=0.4, installed: 0.5.1]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── overrides [required: >=5.0, installed: 7.7.0]
│   ├── packaging [required: >=22.0, installed: 24.2]
│   ├── prometheus_client [required: >=0.9, installed: 0.20.0]
│   ├── pyzmq [required: >=24, installed: 26.0.3]
│   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   └── tornado [required: >=6.1.0, installed: 6.4]
│   ├── tornado [required: >=6.2.0, installed: 6.4]
│   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   └── websocket-client [required: >=1.7, installed: 1.8.0]
└── tornado [required: Any, installed: 6.4]
nlopt==2.8.0
notebook==7.2.0
├── jupyter_server [required: >=2.4.0,<3, installed: 2.14.0]
│   ├── anyio [required: >=3.1.0, installed: 4.9.0]
│   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   ├── argon2-cffi [required: >=21.1, installed: 23.1.0]
│   │   └── argon2-cffi-bindings [required: Any, installed: 21.2.0]
│   │       └── cffi [required: >=1.0.1, installed: 1.16.0]
│   │           └── pycparser [required: Any, installed: 2.22]
│   ├── Jinja2 [required: >=3.0.3, installed: 3.1.4]
│   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   ├── jupyter_client [required: >=7.4.4, installed: 8.6.1]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter-events [required: >=0.9.0, installed: 0.10.0]
│   │   ├── jsonschema [required: >=4.18.0, installed: 4.22.0]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   ├── referencing [required: Any, installed: 0.35.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   ├── rfc3339-validator [required: Any, installed: 0.1.4]
│   │   │   └── six [required: Any, installed: 1.16.0]
│   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       └── tornado [required: >=6.1.0, installed: 6.4]
│   ├── nbconvert [required: >=6.4.4, installed: 7.16.4]
│   │   ├── beautifulsoup4 [required: Any, installed: 4.12.3]
│   │   │   └── soupsieve [required: >1.2, installed: 2.5]
│   │   ├── bleach [required: !=5.0.0, installed: 6.1.0]
│   │   │   ├── six [required: >=1.9.0, installed: 1.16.0]
│   │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │   ├── Jinja2 [required: >=3.0, installed: 3.1.4]
│   │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   ├── jupyter_core [required: >=4.7, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │   ├── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   ├── mistune [required: >=2.0.3,<4, installed: 3.0.2]
│   │   ├── nbclient [required: >=0.5.0, installed: 0.10.0]
│   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── packaging [required: Any, installed: 24.2]
│   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │   ├── Pygments [required: >=2.4.1, installed: 2.18.0]
│   │   ├── tinycss2 [required: Any, installed: 1.3.0]
│   │   │   └── webencodings [required: >=0.4, installed: 0.5.1]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── overrides [required: >=5.0, installed: 7.7.0]
│   ├── packaging [required: >=22.0, installed: 24.2]
│   ├── prometheus_client [required: >=0.9, installed: 0.20.0]
│   ├── pyzmq [required: >=24, installed: 26.0.3]
│   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   └── tornado [required: >=6.1.0, installed: 6.4]
│   ├── tornado [required: >=6.2.0, installed: 6.4]
│   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   └── websocket-client [required: >=1.7, installed: 1.8.0]
├── jupyterlab [required: >=4.2.0,<4.3, installed: 4.2.0]
│   ├── async-lru [required: >=1.0.0, installed: 2.0.4]
│   ├── httpx [required: >=0.25.0, installed: 0.27.0]
│   │   ├── anyio [required: Any, installed: 4.9.0]
│   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   ├── httpcore [required: ==1.*, installed: 1.0.5]
│   │   │   ├── certifi [required: Any, installed: 2025.1.31]
│   │   │   └── h11 [required: >=0.13,<0.15, installed: 0.14.0]
│   │   ├── idna [required: Any, installed: 3.7]
│   │   └── sniffio [required: Any, installed: 1.3.1]
│   ├── ipykernel [required: >=6.5.0, installed: 6.29.3]
│   │   ├── comm [required: >=0.1.1, installed: 0.2.2]
│   │   │   └── traitlets [required: >=4, installed: 5.14.3]
│   │   ├── debugpy [required: >=1.6.5, installed: 1.8.1]
│   │   ├── ipython [required: >=7.23.1, installed: 8.24.0]
│   │   │   ├── decorator [required: Any, installed: 5.1.1]
│   │   │   ├── jedi [required: >=0.16, installed: 0.19.1]
│   │   │   │   └── parso [required: >=0.8.3,<0.9.0, installed: 0.8.4]
│   │   │   ├── matplotlib-inline [required: Any, installed: 0.1.7]
│   │   │   │   └── traitlets [required: Any, installed: 5.14.3]
│   │   │   ├── pexpect [required: >4.3, installed: 4.9.0]
│   │   │   │   └── ptyprocess [required: >=0.5, installed: 0.7.0]
│   │   │   ├── prompt-toolkit [required: >=3.0.41,<3.1.0, installed: 3.0.42]
│   │   │   │   └── wcwidth [required: Any, installed: 0.2.13]
│   │   │   ├── Pygments [required: >=2.4.0, installed: 2.18.0]
│   │   │   ├── stack-data [required: Any, installed: 0.6.2]
│   │   │   │   ├── asttokens [required: >=2.1.0, installed: 2.4.1]
│   │   │   │   │   └── six [required: >=1.12.0, installed: 1.16.0]
│   │   │   │   ├── executing [required: >=1.2.0, installed: 2.0.1]
│   │   │   │   └── pure-eval [required: Any, installed: 0.2.2]
│   │   │   ├── traitlets [required: >=5.13.0, installed: 5.14.3]
│   │   │   └── typing_extensions [required: >=4.6, installed: 4.12.2]
│   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── matplotlib-inline [required: >=0.1, installed: 0.1.7]
│   │   │   └── traitlets [required: Any, installed: 5.14.3]
│   │   ├── nest_asyncio [required: Any, installed: 1.6.0]
│   │   ├── packaging [required: Any, installed: 24.2]
│   │   ├── psutil [required: Any, installed: 5.9.8]
│   │   ├── pyzmq [required: >=24, installed: 26.0.3]
│   │   ├── tornado [required: >=6.1, installed: 6.4]
│   │   └── traitlets [required: >=5.4.0, installed: 5.14.3]
│   ├── Jinja2 [required: >=3.0.3, installed: 3.1.4]
│   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   ├── jupyter_core [required: Any, installed: 5.7.2]
│   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter-lsp [required: >=2.0.0, installed: 2.2.5]
│   │   └── jupyter_server [required: >=1.1.2, installed: 2.14.0]
│   │       ├── anyio [required: >=3.1.0, installed: 4.9.0]
│   │       │   ├── idna [required: >=2.8, installed: 3.7]
│   │       │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │       │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │       ├── argon2-cffi [required: >=21.1, installed: 23.1.0]
│   │       │   └── argon2-cffi-bindings [required: Any, installed: 21.2.0]
│   │       │       └── cffi [required: >=1.0.1, installed: 1.16.0]
│   │       │           └── pycparser [required: Any, installed: 2.22]
│   │       ├── Jinja2 [required: >=3.0.3, installed: 3.1.4]
│   │       │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │       ├── jupyter_client [required: >=7.4.4, installed: 8.6.1]
│   │       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │       │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │       │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │       │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │       │   ├── tornado [required: >=6.2, installed: 6.4]
│   │       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │       │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       ├── jupyter-events [required: >=0.9.0, installed: 0.10.0]
│   │       │   ├── jsonschema [required: >=4.18.0, installed: 4.22.0]
│   │       │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │       │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │       │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │       │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │       │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │       │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │       │   ├── referencing [required: Any, installed: 0.35.1]
│   │       │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   ├── rfc3339-validator [required: Any, installed: 0.1.4]
│   │       │   │   └── six [required: Any, installed: 1.16.0]
│   │       │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │       │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       │       └── tornado [required: >=6.1.0, installed: 6.4]
│   │       ├── nbconvert [required: >=6.4.4, installed: 7.16.4]
│   │       │   ├── beautifulsoup4 [required: Any, installed: 4.12.3]
│   │       │   │   └── soupsieve [required: >1.2, installed: 2.5]
│   │       │   ├── bleach [required: !=5.0.0, installed: 6.1.0]
│   │       │   │   ├── six [required: >=1.9.0, installed: 1.16.0]
│   │       │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │       │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │       │   ├── Jinja2 [required: >=3.0, installed: 3.1.4]
│   │       │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │       │   ├── jupyter_core [required: >=4.7, installed: 5.7.2]
│   │       │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │       │   ├── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │       │   ├── mistune [required: >=2.0.3,<4, installed: 3.0.2]
│   │       │   ├── nbclient [required: >=0.5.0, installed: 0.10.0]
│   │       │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.1]
│   │       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │       │   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │       │   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │       │   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │       │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │       │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │       │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │       │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │       │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │       │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │       │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │       │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │       │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │       │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │       │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       │   ├── packaging [required: Any, installed: 24.2]
│   │       │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │       │   ├── Pygments [required: >=2.4.1, installed: 2.18.0]
│   │       │   ├── tinycss2 [required: Any, installed: 1.3.0]
│   │       │   │   └── webencodings [required: >=0.4, installed: 0.5.1]
│   │       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │       │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │       │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │       │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │       │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │       │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │       │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │       │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       ├── overrides [required: >=5.0, installed: 7.7.0]
│   │       ├── packaging [required: >=22.0, installed: 24.2]
│   │       ├── prometheus_client [required: >=0.9, installed: 0.20.0]
│   │       ├── pyzmq [required: >=24, installed: 26.0.3]
│   │       ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   │       ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       │   └── tornado [required: >=6.1.0, installed: 6.4]
│   │       ├── tornado [required: >=6.2.0, installed: 6.4]
│   │       ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   │       └── websocket-client [required: >=1.7, installed: 1.8.0]
│   ├── jupyter_server [required: >=2.4.0,<3, installed: 2.14.0]
│   │   ├── anyio [required: >=3.1.0, installed: 4.9.0]
│   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   ├── argon2-cffi [required: >=21.1, installed: 23.1.0]
│   │   │   └── argon2-cffi-bindings [required: Any, installed: 21.2.0]
│   │   │       └── cffi [required: >=1.0.1, installed: 1.16.0]
│   │   │           └── pycparser [required: Any, installed: 2.22]
│   │   ├── Jinja2 [required: >=3.0.3, installed: 3.1.4]
│   │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   ├── jupyter_client [required: >=7.4.4, installed: 8.6.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter-events [required: >=0.9.0, installed: 0.10.0]
│   │   │   ├── jsonschema [required: >=4.18.0, installed: 4.22.0]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   │   ├── referencing [required: Any, installed: 0.35.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   ├── rfc3339-validator [required: Any, installed: 0.1.4]
│   │   │   │   └── six [required: Any, installed: 1.16.0]
│   │   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   │       └── tornado [required: >=6.1.0, installed: 6.4]
│   │   ├── nbconvert [required: >=6.4.4, installed: 7.16.4]
│   │   │   ├── beautifulsoup4 [required: Any, installed: 4.12.3]
│   │   │   │   └── soupsieve [required: >1.2, installed: 2.5]
│   │   │   ├── bleach [required: !=5.0.0, installed: 6.1.0]
│   │   │   │   ├── six [required: >=1.9.0, installed: 1.16.0]
│   │   │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │   │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │   │   ├── Jinja2 [required: >=3.0, installed: 3.1.4]
│   │   │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   │   ├── jupyter_core [required: >=4.7, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │   │   ├── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   │   ├── mistune [required: >=2.0.3,<4, installed: 3.0.2]
│   │   │   ├── nbclient [required: >=0.5.0, installed: 0.10.0]
│   │   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.1]
│   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   │   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   │   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   ├── packaging [required: Any, installed: 24.2]
│   │   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │   │   ├── Pygments [required: >=2.4.1, installed: 2.18.0]
│   │   │   ├── tinycss2 [required: Any, installed: 1.3.0]
│   │   │   │   └── webencodings [required: >=0.4, installed: 0.5.1]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── overrides [required: >=5.0, installed: 7.7.0]
│   │   ├── packaging [required: >=22.0, installed: 24.2]
│   │   ├── prometheus_client [required: >=0.9, installed: 0.20.0]
│   │   ├── pyzmq [required: >=24, installed: 26.0.3]
│   │   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   │   ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   │   └── tornado [required: >=6.1.0, installed: 6.4]
│   │   ├── tornado [required: >=6.2.0, installed: 6.4]
│   │   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   │   └── websocket-client [required: >=1.7, installed: 1.8.0]
│   ├── jupyterlab_server [required: >=2.27.1,<3, installed: 2.27.1]
│   │   ├── Babel [required: >=2.10, installed: 2.14.0]
│   │   ├── Jinja2 [required: >=3.0.3, installed: 3.1.4]
│   │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   ├── json5 [required: >=0.9.0, installed: 0.9.25]
│   │   ├── jsonschema [required: >=4.18.0, installed: 4.22.0]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   ├── jupyter_server [required: >=1.21,<3, installed: 2.14.0]
│   │   │   ├── anyio [required: >=3.1.0, installed: 4.9.0]
│   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   │   ├── argon2-cffi [required: >=21.1, installed: 23.1.0]
│   │   │   │   └── argon2-cffi-bindings [required: Any, installed: 21.2.0]
│   │   │   │       └── cffi [required: >=1.0.1, installed: 1.16.0]
│   │   │   │           └── pycparser [required: Any, installed: 2.22]
│   │   │   ├── Jinja2 [required: >=3.0.3, installed: 3.1.4]
│   │   │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   │   ├── jupyter_client [required: >=7.4.4, installed: 8.6.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyter-events [required: >=0.9.0, installed: 0.10.0]
│   │   │   │   ├── jsonschema [required: >=4.18.0, installed: 4.22.0]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │   │   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   │   │   ├── referencing [required: Any, installed: 0.35.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   ├── rfc3339-validator [required: Any, installed: 0.1.4]
│   │   │   │   │   └── six [required: Any, installed: 1.16.0]
│   │   │   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │   │   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   │   │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   │   │       └── tornado [required: >=6.1.0, installed: 6.4]
│   │   │   ├── nbconvert [required: >=6.4.4, installed: 7.16.4]
│   │   │   │   ├── beautifulsoup4 [required: Any, installed: 4.12.3]
│   │   │   │   │   └── soupsieve [required: >1.2, installed: 2.5]
│   │   │   │   ├── bleach [required: !=5.0.0, installed: 6.1.0]
│   │   │   │   │   ├── six [required: >=1.9.0, installed: 1.16.0]
│   │   │   │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │   │   │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │   │   │   ├── Jinja2 [required: >=3.0, installed: 3.1.4]
│   │   │   │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   │   │   ├── jupyter_core [required: >=4.7, installed: 5.7.2]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │   │   │   ├── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   │   │   ├── mistune [required: >=2.0.3,<4, installed: 3.0.2]
│   │   │   │   ├── nbclient [required: >=0.5.0, installed: 0.10.0]
│   │   │   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.1]
│   │   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   │   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   │   │   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   │   │   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │   │   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   │   ├── packaging [required: Any, installed: 24.2]
│   │   │   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │   │   │   ├── Pygments [required: >=2.4.1, installed: 2.18.0]
│   │   │   │   ├── tinycss2 [required: Any, installed: 1.3.0]
│   │   │   │   │   └── webencodings [required: >=0.4, installed: 0.5.1]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   ├── overrides [required: >=5.0, installed: 7.7.0]
│   │   │   ├── packaging [required: >=22.0, installed: 24.2]
│   │   │   ├── prometheus_client [required: >=0.9, installed: 0.20.0]
│   │   │   ├── pyzmq [required: >=24, installed: 26.0.3]
│   │   │   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   │   │   ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   │   │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   │   │   └── tornado [required: >=6.1.0, installed: 6.4]
│   │   │   ├── tornado [required: >=6.2.0, installed: 6.4]
│   │   │   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   │   │   └── websocket-client [required: >=1.7, installed: 1.8.0]
│   │   ├── packaging [required: >=21.3, installed: 24.2]
│   │   └── requests [required: >=2.31, installed: 2.32.3]
│   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
│   ├── notebook_shim [required: >=0.2, installed: 0.2.4]
│   │   └── jupyter_server [required: >=1.8,<3, installed: 2.14.0]
│   │       ├── anyio [required: >=3.1.0, installed: 4.9.0]
│   │       │   ├── idna [required: >=2.8, installed: 3.7]
│   │       │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │       │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │       ├── argon2-cffi [required: >=21.1, installed: 23.1.0]
│   │       │   └── argon2-cffi-bindings [required: Any, installed: 21.2.0]
│   │       │       └── cffi [required: >=1.0.1, installed: 1.16.0]
│   │       │           └── pycparser [required: Any, installed: 2.22]
│   │       ├── Jinja2 [required: >=3.0.3, installed: 3.1.4]
│   │       │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │       ├── jupyter_client [required: >=7.4.4, installed: 8.6.1]
│   │       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │       │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │       │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │       │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │       │   ├── tornado [required: >=6.2, installed: 6.4]
│   │       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │       │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       ├── jupyter-events [required: >=0.9.0, installed: 0.10.0]
│   │       │   ├── jsonschema [required: >=4.18.0, installed: 4.22.0]
│   │       │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │       │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │       │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │       │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │       │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │       │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │       │   ├── referencing [required: Any, installed: 0.35.1]
│   │       │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   ├── rfc3339-validator [required: Any, installed: 0.1.4]
│   │       │   │   └── six [required: Any, installed: 1.16.0]
│   │       │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │       │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       │       └── tornado [required: >=6.1.0, installed: 6.4]
│   │       ├── nbconvert [required: >=6.4.4, installed: 7.16.4]
│   │       │   ├── beautifulsoup4 [required: Any, installed: 4.12.3]
│   │       │   │   └── soupsieve [required: >1.2, installed: 2.5]
│   │       │   ├── bleach [required: !=5.0.0, installed: 6.1.0]
│   │       │   │   ├── six [required: >=1.9.0, installed: 1.16.0]
│   │       │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │       │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │       │   ├── Jinja2 [required: >=3.0, installed: 3.1.4]
│   │       │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │       │   ├── jupyter_core [required: >=4.7, installed: 5.7.2]
│   │       │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │       │   ├── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │       │   ├── mistune [required: >=2.0.3,<4, installed: 3.0.2]
│   │       │   ├── nbclient [required: >=0.5.0, installed: 0.10.0]
│   │       │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.1]
│   │       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │       │   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │       │   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │       │   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │       │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │       │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │       │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │       │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │       │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │       │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │       │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │       │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │       │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │       │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │       │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       │   ├── packaging [required: Any, installed: 24.2]
│   │       │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │       │   ├── Pygments [required: >=2.4.1, installed: 2.18.0]
│   │       │   ├── tinycss2 [required: Any, installed: 1.3.0]
│   │       │   │   └── webencodings [required: >=0.4, installed: 0.5.1]
│   │       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │       │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │       │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │       │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │       │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │       │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │       │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │       │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │       │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       ├── overrides [required: >=5.0, installed: 7.7.0]
│   │       ├── packaging [required: >=22.0, installed: 24.2]
│   │       ├── prometheus_client [required: >=0.9, installed: 0.20.0]
│   │       ├── pyzmq [required: >=24, installed: 26.0.3]
│   │       ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   │       ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       │   └── tornado [required: >=6.1.0, installed: 6.4]
│   │       ├── tornado [required: >=6.2.0, installed: 6.4]
│   │       ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   │       └── websocket-client [required: >=1.7, installed: 1.8.0]
│   ├── packaging [required: Any, installed: 24.2]
│   ├── tornado [required: >=6.2.0, installed: 6.4]
│   └── traitlets [required: Any, installed: 5.14.3]
├── jupyterlab_server [required: >=2.27.1,<3, installed: 2.27.1]
│   ├── Babel [required: >=2.10, installed: 2.14.0]
│   ├── Jinja2 [required: >=3.0.3, installed: 3.1.4]
│   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   ├── json5 [required: >=0.9.0, installed: 0.9.25]
│   ├── jsonschema [required: >=4.18.0, installed: 4.22.0]
│   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   ├── jupyter_server [required: >=1.21,<3, installed: 2.14.0]
│   │   ├── anyio [required: >=3.1.0, installed: 4.9.0]
│   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│   │   ├── argon2-cffi [required: >=21.1, installed: 23.1.0]
│   │   │   └── argon2-cffi-bindings [required: Any, installed: 21.2.0]
│   │   │       └── cffi [required: >=1.0.1, installed: 1.16.0]
│   │   │           └── pycparser [required: Any, installed: 2.22]
│   │   ├── Jinja2 [required: >=3.0.3, installed: 3.1.4]
│   │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   ├── jupyter_client [required: >=7.4.4, installed: 8.6.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter-events [required: >=0.9.0, installed: 0.10.0]
│   │   │   ├── jsonschema [required: >=4.18.0, installed: 4.22.0]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │   │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│   │   │   ├── referencing [required: Any, installed: 0.35.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   ├── rfc3339-validator [required: Any, installed: 0.1.4]
│   │   │   │   └── six [required: Any, installed: 1.16.0]
│   │   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   │       └── tornado [required: >=6.1.0, installed: 6.4]
│   │   ├── nbconvert [required: >=6.4.4, installed: 7.16.4]
│   │   │   ├── beautifulsoup4 [required: Any, installed: 4.12.3]
│   │   │   │   └── soupsieve [required: >1.2, installed: 2.5]
│   │   │   ├── bleach [required: !=5.0.0, installed: 6.1.0]
│   │   │   │   ├── six [required: >=1.9.0, installed: 1.16.0]
│   │   │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │   │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │   │   ├── Jinja2 [required: >=3.0, installed: 3.1.4]
│   │   │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   │   ├── jupyter_core [required: >=4.7, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │   │   ├── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   │   │   ├── mistune [required: >=2.0.3,<4, installed: 3.0.2]
│   │   │   ├── nbclient [required: >=0.5.0, installed: 0.10.0]
│   │   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.1]
│   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   │   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│   │   │   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│   │   │   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   ├── packaging [required: Any, installed: 24.2]
│   │   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │   │   ├── Pygments [required: >=2.4.1, installed: 2.18.0]
│   │   │   ├── tinycss2 [required: Any, installed: 1.3.0]
│   │   │   │   └── webencodings [required: >=0.4, installed: 0.5.1]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── overrides [required: >=5.0, installed: 7.7.0]
│   │   ├── packaging [required: >=22.0, installed: 24.2]
│   │   ├── prometheus_client [required: >=0.9, installed: 0.20.0]
│   │   ├── pyzmq [required: >=24, installed: 26.0.3]
│   │   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   │   ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   │   └── tornado [required: >=6.1.0, installed: 6.4]
│   │   ├── tornado [required: >=6.2.0, installed: 6.4]
│   │   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   │   └── websocket-client [required: >=1.7, installed: 1.8.0]
│   ├── packaging [required: >=21.3, installed: 24.2]
│   └── requests [required: >=2.31, installed: 2.32.3]
│       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│       ├── idna [required: >=2.5,<4, installed: 3.7]
│       └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
├── notebook_shim [required: >=0.2,<0.3, installed: 0.2.4]
│   └── jupyter_server [required: >=1.8,<3, installed: 2.14.0]
│       ├── anyio [required: >=3.1.0, installed: 4.9.0]
│       │   ├── idna [required: >=2.8, installed: 3.7]
│       │   ├── sniffio [required: >=1.1, installed: 1.3.1]
│       │   └── typing_extensions [required: >=4.5, installed: 4.12.2]
│       ├── argon2-cffi [required: >=21.1, installed: 23.1.0]
│       │   └── argon2-cffi-bindings [required: Any, installed: 21.2.0]
│       │       └── cffi [required: >=1.0.1, installed: 1.16.0]
│       │           └── pycparser [required: Any, installed: 2.22]
│       ├── Jinja2 [required: >=3.0.3, installed: 3.1.4]
│       │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│       ├── jupyter_client [required: >=7.4.4, installed: 8.6.1]
│       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│       │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│       │   │   └── six [required: >=1.5, installed: 1.16.0]
│       │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│       │   ├── tornado [required: >=6.2, installed: 6.4]
│       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│       │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       ├── jupyter-events [required: >=0.9.0, installed: 0.10.0]
│       │   ├── jsonschema [required: >=4.18.0, installed: 4.22.0]
│       │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│       │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│       │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│       │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│       │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│       │   ├── PyYAML [required: >=5.3, installed: 6.0.1]
│       │   ├── referencing [required: Any, installed: 0.35.1]
│       │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   ├── rfc3339-validator [required: Any, installed: 0.1.4]
│       │   │   └── six [required: Any, installed: 1.16.0]
│       │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│       │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│       │       ├── ptyprocess [required: Any, installed: 0.7.0]
│       │       └── tornado [required: >=6.1.0, installed: 6.4]
│       ├── nbconvert [required: >=6.4.4, installed: 7.16.4]
│       │   ├── beautifulsoup4 [required: Any, installed: 4.12.3]
│       │   │   └── soupsieve [required: >1.2, installed: 2.5]
│       │   ├── bleach [required: !=5.0.0, installed: 6.1.0]
│       │   │   ├── six [required: >=1.9.0, installed: 1.16.0]
│       │   │   └── webencodings [required: Any, installed: 0.5.1]
│       │   ├── defusedxml [required: Any, installed: 0.7.1]
│       │   ├── Jinja2 [required: >=3.0, installed: 3.1.4]
│       │   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│       │   ├── jupyter_core [required: >=4.7, installed: 5.7.2]
│       │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│       │   ├── MarkupSafe [required: >=2.0, installed: 2.1.5]
│       │   ├── mistune [required: >=2.0.3,<4, installed: 3.0.2]
│       │   ├── nbclient [required: >=0.5.0, installed: 0.10.0]
│       │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.1]
│       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│       │   │   │   │   └── six [required: >=1.5, installed: 1.16.0]
│       │   │   │   ├── pyzmq [required: >=23.0, installed: 26.0.3]
│       │   │   │   ├── tornado [required: >=6.2, installed: 6.4]
│       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│       │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│       │   │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│       │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│       │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│       │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│       │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│       │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│       │   │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│       │   │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│       │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│       │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│       │   │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│       │   ├── packaging [required: Any, installed: 24.2]
│       │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│       │   ├── Pygments [required: >=2.4.1, installed: 2.18.0]
│       │   ├── tinycss2 [required: Any, installed: 1.3.0]
│       │   │   └── webencodings [required: >=0.4, installed: 0.5.1]
│       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│       ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│       │   ├── fastjsonschema [required: >=2.15, installed: 2.19.1]
│       │   ├── jsonschema [required: >=2.6, installed: 4.22.0]
│       │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│       │   │   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│       │   │   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│       │   │   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│       │   │   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
│       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.7.2]
│       │   │   ├── platformdirs [required: >=2.5, installed: 4.2.2]
│       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│       ├── overrides [required: >=5.0, installed: 7.7.0]
│       ├── packaging [required: >=22.0, installed: 24.2]
│       ├── prometheus_client [required: >=0.9, installed: 0.20.0]
│       ├── pyzmq [required: >=24, installed: 26.0.3]
│       ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│       ├── terminado [required: >=0.8.3, installed: 0.18.1]
│       │   ├── ptyprocess [required: Any, installed: 0.7.0]
│       │   └── tornado [required: >=6.1.0, installed: 6.4]
│       ├── tornado [required: >=6.2.0, installed: 6.4]
│       ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│       └── websocket-client [required: >=1.7, installed: 1.8.0]
└── tornado [required: >=6.2.0, installed: 6.4]
pickleshare==0.7.5
pip==25.0.1
pkgutil_resolve_name==1.3.10
pycurl==7.45.3
PyJWT==2.8.0
pypdf==5.4.0
PySocks==1.7.1
pytz==2024.1
qianfan==0.4.12.3
├── aiohttp [required: >=3.7.0, installed: 3.11.13]
│   ├── aiohappyeyeballs [required: >=2.3.0, installed: 2.4.8]
│   ├── aiosignal [required: >=1.1.2, installed: 1.3.2]
│   │   └── frozenlist [required: >=1.1.0, installed: 1.5.0]
│   ├── attrs [required: >=17.3.0, installed: 23.2.0]
│   ├── frozenlist [required: >=1.1.1, installed: 1.5.0]
│   ├── multidict [required: >=4.5,<7.0, installed: 6.1.0]
│   ├── propcache [required: >=0.2.0, installed: 0.3.0]
│   └── yarl [required: >=1.17.0,<2.0, installed: 1.18.3]
│       ├── idna [required: >=2.0, installed: 3.7]
│       ├── multidict [required: >=4.0, installed: 6.1.0]
│       └── propcache [required: >=0.2.0, installed: 0.3.0]
├── aiolimiter [required: >=1.1.0, installed: 1.2.1]
├── bce-python-sdk [required: >=0.8.79, installed: 0.9.29]
│   ├── future [required: >=0.6.0, installed: 1.0.0]
│   ├── pycryptodome [required: >=3.8.0, installed: 3.22.0]
│   └── six [required: >=1.4.0, installed: 1.16.0]
├── cachetools [required: >=5.0.0, installed: 5.5.2]
├── diskcache [required: >=5.6.3, installed: 5.6.3]
├── multiprocess [required: >=0.70.12, installed: 0.70.17]
│   └── dill [required: >=0.3.9, installed: 0.3.9]
├── prompt-toolkit [required: >=3.0.38, installed: 3.0.42]
│   └── wcwidth [required: Any, installed: 0.2.13]
├── pydantic [required: >=1.0, installed: 2.10.6]
│   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
├── python-dotenv [required: >=1.0, installed: 1.0.1]
├── PyYAML [required: >=6.0.1,<7.0.0, installed: 6.0.1]
├── requests [required: >=2.24, installed: 2.32.3]
│   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   ├── idna [required: >=2.5,<4, installed: 3.7]
│   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
├── rich [required: >=13.0.0, installed: 13.9.4]
│   ├── markdown-it-py [required: >=2.2.0, installed: 3.0.0]
│   │   └── mdurl [required: ~=0.1, installed: 0.1.2]
│   └── Pygments [required: >=2.13.0,<3.0.0, installed: 2.18.0]
├── tenacity [required: >=8.2.3,<9.0.0, installed: 8.5.0]
└── typer [required: >=0.9.0, installed: 0.15.2]
    ├── click [required: >=8.0.0, installed: 8.1.8]
    ├── rich [required: >=10.11.0, installed: 13.9.4]
    │   ├── markdown-it-py [required: >=2.2.0, installed: 3.0.0]
    │   │   └── mdurl [required: ~=0.1, installed: 0.1.2]
    │   └── Pygments [required: >=2.13.0,<3.0.0, installed: 2.18.0]
    ├── shellingham [required: >=1.3.0, installed: 1.5.4]
    └── typing_extensions [required: >=3.7.4.3, installed: 4.12.2]
tensorflow==2.18.0
├── absl-py [required: >=1.0.0, installed: 2.1.0]
├── astunparse [required: >=1.6.0, installed: 1.6.3]
│   ├── six [required: >=1.6.1,<2.0, installed: 1.16.0]
│   └── wheel [required: >=0.23.0,<1.0, installed: 0.43.0]
├── flatbuffers [required: >=24.3.25, installed: 25.2.10]
├── gast [required: >=0.2.1,!=0.5.2,!=0.5.1,!=0.5.0, installed: 0.6.0]
├── google-pasta [required: >=0.1.1, installed: 0.2.0]
│   └── six [required: Any, installed: 1.16.0]
├── grpcio [required: >=1.24.3,<2.0, installed: 1.71.0]
├── h5py [required: >=3.11.0, installed: 3.13.0]
│   └── numpy [required: >=1.19.3, installed: 1.26.4]
├── keras [required: >=3.5.0, installed: 3.8.0]
│   ├── absl-py [required: Any, installed: 2.1.0]
│   ├── h5py [required: Any, installed: 3.13.0]
│   │   └── numpy [required: >=1.19.3, installed: 1.26.4]
│   ├── ml-dtypes [required: Any, installed: 0.4.1]
│   │   ├── numpy [required: >1.20, installed: 1.26.4]
│   │   ├── numpy [required: >=1.21.2, installed: 1.26.4]
│   │   └── numpy [required: >=1.23.3, installed: 1.26.4]
│   ├── namex [required: Any, installed: 0.0.8]
│   ├── numpy [required: Any, installed: 1.26.4]
│   ├── optree [required: Any, installed: 0.14.1]
│   │   └── typing_extensions [required: >=4.5.0, installed: 4.12.2]
│   ├── packaging [required: Any, installed: 24.2]
│   └── rich [required: Any, installed: 13.9.4]
│       ├── markdown-it-py [required: >=2.2.0, installed: 3.0.0]
│       │   └── mdurl [required: ~=0.1, installed: 0.1.2]
│       └── Pygments [required: >=2.13.0,<3.0.0, installed: 2.18.0]
├── libclang [required: >=13.0.0, installed: 18.1.1]
├── ml-dtypes [required: >=0.4.0,<0.5.0, installed: 0.4.1]
│   ├── numpy [required: >1.20, installed: 1.26.4]
│   ├── numpy [required: >=1.21.2, installed: 1.26.4]
│   └── numpy [required: >=1.23.3, installed: 1.26.4]
├── numpy [required: >=1.26.0,<2.1.0, installed: 1.26.4]
├── opt_einsum [required: >=2.3.2, installed: 3.4.0]
├── packaging [required: Any, installed: 24.2]
├── protobuf [required: >=3.20.3,<6.0.0dev,!=4.21.5,!=4.21.4,!=4.21.3,!=4.21.2,!=4.21.1,!=4.21.0, installed: 5.29.3]
├── requests [required: >=2.21.0,<3, installed: 2.32.3]
│   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   ├── idna [required: >=2.5,<4, installed: 3.7]
│   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
├── setuptools [required: Any, installed: 69.5.1]
├── six [required: >=1.12.0, installed: 1.16.0]
├── tensorboard [required: >=2.18,<2.19, installed: 2.18.0]
│   ├── absl-py [required: >=0.4, installed: 2.1.0]
│   ├── grpcio [required: >=1.48.2, installed: 1.71.0]
│   ├── Markdown [required: >=2.6.8, installed: 3.7]
│   ├── numpy [required: >=1.12.0, installed: 1.26.4]
│   ├── packaging [required: Any, installed: 24.2]
│   ├── protobuf [required: >=3.19.6,!=4.24.0, installed: 5.29.3]
│   ├── setuptools [required: >=41.0.0, installed: 69.5.1]
│   ├── six [required: >1.9, installed: 1.16.0]
│   ├── tensorboard-data-server [required: >=0.7.0,<0.8.0, installed: 0.7.2]
│   └── Werkzeug [required: >=1.0.1, installed: 3.1.3]
│       └── MarkupSafe [required: >=2.1.1, installed: 2.1.5]
├── tensorflow-io-gcs-filesystem [required: >=0.23.1, installed: 0.37.1]
├── termcolor [required: >=1.1.0, installed: 2.5.0]
├── typing_extensions [required: >=3.6.6, installed: 4.12.2]
└── wrapt [required: >=1.11.0, installed: 1.17.2]
together==1.4.6
├── aiohttp [required: >=3.9.3,<4.0.0, installed: 3.11.13]
│   ├── aiohappyeyeballs [required: >=2.3.0, installed: 2.4.8]
│   ├── aiosignal [required: >=1.1.2, installed: 1.3.2]
│   │   └── frozenlist [required: >=1.1.0, installed: 1.5.0]
│   ├── attrs [required: >=17.3.0, installed: 23.2.0]
│   ├── frozenlist [required: >=1.1.1, installed: 1.5.0]
│   ├── multidict [required: >=4.5,<7.0, installed: 6.1.0]
│   ├── propcache [required: >=0.2.0, installed: 0.3.0]
│   └── yarl [required: >=1.17.0,<2.0, installed: 1.18.3]
│       ├── idna [required: >=2.0, installed: 3.7]
│       ├── multidict [required: >=4.0, installed: 6.1.0]
│       └── propcache [required: >=0.2.0, installed: 0.3.0]
├── click [required: >=8.1.7,<9.0.0, installed: 8.1.8]
├── eval_type_backport [required: >=0.1.3,<0.3.0, installed: 0.2.2]
├── filelock [required: >=3.13.1,<4.0.0, installed: 3.18.0]
├── numpy [required: >=1.23.5, installed: 1.26.4]
├── pillow [required: >=11.1.0,<12.0.0, installed: 11.1.0]
├── pyarrow [required: >=10.0.1, installed: 19.0.1]
├── pydantic [required: >=2.6.3,<3.0.0, installed: 2.10.6]
│   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   ├── pydantic_core [required: ==2.27.2, installed: 2.27.2]
│   │   └── typing_extensions [required: >=4.6.0,!=4.7.0, installed: 4.12.2]
│   └── typing_extensions [required: >=4.12.2, installed: 4.12.2]
├── requests [required: >=2.31.0,<3.0.0, installed: 2.32.3]
│   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   ├── idna [required: >=2.5,<4, installed: 3.7]
│   └── urllib3 [required: >=1.21.1,<3, installed: 2.2.1]
├── rich [required: >=13.8.1,<14.0.0, installed: 13.9.4]
│   ├── markdown-it-py [required: >=2.2.0, installed: 3.0.0]
│   │   └── mdurl [required: ~=0.1, installed: 0.1.2]
│   └── Pygments [required: >=2.13.0,<3.0.0, installed: 2.18.0]
├── tabulate [required: >=0.9.0,<0.10.0, installed: 0.9.0]
├── tqdm [required: >=4.66.2,<5.0.0, installed: 4.66.4]
└── typer [required: >=0.9,<0.16, installed: 0.15.2]
    ├── click [required: >=8.0.0, installed: 8.1.8]
    ├── rich [required: >=10.11.0, installed: 13.9.4]
    │   ├── markdown-it-py [required: >=2.2.0, installed: 3.0.0]
    │   │   └── mdurl [required: ~=0.1, installed: 0.1.2]
    │   └── Pygments [required: >=2.13.0,<3.0.0, installed: 2.18.0]
    ├── shellingham [required: >=1.3.0, installed: 1.5.4]
    └── typing_extensions [required: >=3.7.4.3, installed: 4.12.2]
tomli==2.0.1
typing-utils==0.1.0
uri-template==1.3.0
webcolors==1.13
```

### Conda packages
via `conda-tree -n base deptree --exclude conda-tree --small`

```
mamba==1.5.8
  ├─ conda 24.5.0 [required: >=24,<25]
  ├─ libmambapy 1.5.8 [required: 1.5.8, py311hf2555c7_0]
  │  ├─ fmt 10.2.1 [required: >=10.2.1,<11.0a0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ libgcc 14.2.0 [required: 14.2.0, h767d61c_2]
  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │     └─ _openmp_mutex 4.5 [required: >=4.5]
  │  │  │        ├─ _libgcc_mutex 0.1 [required: 0.1, conda_forge]
  │  │  │        └─ libgomp 14.2.0 [required: >=7.5.0]
  │  │  │           └─ __glibc [required: >=2.17,<3.0.a0]
  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libmamba 1.5.8 [required: 1.5.8, had39da4_0]
  │  │  ├─ fmt 10.2.1 [required: >=10.2.1,<11.0a0]
  │  │  │  └─ dependencies of fmt displayed above
  │  │  ├─ libarchive 3.7.4 [required: >=3.7.2,<3.8.0a0]
  │  │  │  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libxml2 2.12.7 [required: >=2.12.7,<3.0a0]
  │  │  │  │  ├─ icu 73.2 [required: >=73.2,<74.0a0]
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libiconv 1.17 [required: >=1.17,<2.0a0]
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ xz 5.2.6 [required: >=5.2.6,<6.0a0]
  │  │  │  │     └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │        └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  ├─ lz4-c 1.9.4 [required: >=1.9.3,<1.10.0a0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ lzo 2.10 [required: >=2.10,<3.0a0]
  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ ca-certificates 2025.1.31 [required: any]
  │  │  │  │  └─ libgcc 14.2.0 [required: >=13]
  │  │  │  │     └─ dependencies of libgcc displayed above
  │  │  │  ├─ xz 5.2.6 [required: >=5.2.6,<6.0a0]
  │  │  │  │  └─ dependencies of xz displayed above
  │  │  │  └─ zstd 1.5.6 [required: >=1.5.6,<1.6.0a0]
  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │     └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │        └─ dependencies of libzlib displayed above
  │  │  ├─ libcurl 8.8.0 [required: >=8.6.0,<9.0a0]
  │  │  │  ├─ krb5 1.21.2 [required: >=1.21.2,<1.22.0a0]
  │  │  │  │  ├─ keyutils 1.6.1 [required: >=1.6.1,<2.0a0]
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=10.3.0]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libedit 3.1.20191231 [required: >=3.1.20191231,<4.0a0]
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=7.5.0]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  └─ ncurses 6.5 [required: >=6.2,<6.3.0a0]
  │  │  │  │  │     └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │        └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  └─ openssl 3.4.1 [required: >=3.1.2,<4.0a0]
  │  │  │  │     └─ dependencies of openssl displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libnghttp2 1.58.0 [required: >=1.58.0,<2.0a0]
  │  │  │  │  ├─ c-ares 1.28.1 [required: >=1.23.0,<2.0a0]
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libev 4.33 [required: >=4.33,<5.0a0]
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  │  └─ openssl 3.4.1 [required: >=3.2.0,<4.0a0]
  │  │  │  │     └─ dependencies of openssl displayed above
  │  │  │  ├─ libssh2 1.11.0 [required: >=1.11.0,<2.0a0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  │  └─ openssl 3.4.1 [required: >=3.1.1,<4.0a0]
  │  │  │  │     └─ dependencies of openssl displayed above
  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  ├─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  │  └─ dependencies of openssl displayed above
  │  │  │  └─ zstd 1.5.6 [required: >=1.5.6,<1.6.0a0]
  │  │  │     └─ dependencies of zstd displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libsolv 0.7.29 [required: >=0.7.23]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │     └─ dependencies of libzlib displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ openssl 3.4.1 [required: >=3.2.1,<4.0a0]
  │  │  │  └─ dependencies of openssl displayed above
  │  │  ├─ reproc 14.2.4.post0 [required: >=14.2,<15.0a0]
  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  ├─ reproc-cpp 14.2.4.post0 [required: >=14.2,<15.0a0]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  └─ reproc 14.2.4.post0 [required: 14.2.4.post0, hd590300_1]
  │  │  │     └─ dependencies of reproc displayed above
  │  │  ├─ yaml-cpp 0.8.0 [required: >=0.8.0,<0.9.0a0]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  └─ zstd 1.5.6 [required: >=1.5.5,<1.6.0a0]
  │  │     └─ dependencies of zstd displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ openssl 3.4.1 [required: >=3.2.1,<4.0a0]
  │  │  └─ dependencies of openssl displayed above
  │  ├─ pybind11-abi 4 [required: 4]
  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  └─ yaml-cpp 0.8.0 [required: >=0.8.0,<0.9.0a0]
  │     └─ dependencies of yaml-cpp displayed above
  ├─ openssl 3.4.1 [required: >=3.2.1,<4.0a0]
  │  └─ dependencies of openssl displayed above
  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
pip==24.0
  ├─ python 3.11.9 [required: >=3.7]
  ├─ setuptools 69.5.1 [required: any]
  │  └─ python 3.11.9 [required: >=3.8]
  └─ wheel 0.43.0 [required: any]
     └─ python 3.11.9 [required: >=3.8]
gdal==3.9.0
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ hdf5 1.14.3 [required: >=1.14.3,<1.14.4.0a0]
  │  ├─ libaec 1.1.3 [required: >=1.1.3,<2.0a0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ libcurl 8.8.0 [required: >=8.8.0,<9.0a0]
  │  │  └─ dependencies of libcurl displayed above
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libgfortran-ng 14.2.0 [required: any]
  │  │  └─ libgfortran 14.2.0 [required: 14.2.0, h69a702a_2]
  │  │     └─ libgfortran5 14.2.0 [required: 14.2.0, hf1ad2bd_2]
  │  │        ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │        └─ libgcc 14.2.0 [required: >=14.2.0]
  │  │           └─ dependencies of libgcc displayed above
  │  ├─ libgfortran5 14.2.0 [required: >=12.3.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0a0]
  │  │  └─ dependencies of libzlib displayed above
  │  └─ openssl 3.4.1 [required: >=3.3.1,<4.0a0]
  │     └─ dependencies of openssl displayed above
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libgdal 3.9.0 [required: 3.9.0, h77540a9_5]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ blosc 1.21.5 [required: >=1.21.5,<2.0a0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  └─ dependencies of libzlib displayed above
  │  │  ├─ lz4-c 1.9.4 [required: >=1.9.3,<1.10.0a0]
  │  │  │  └─ dependencies of lz4-c displayed above
  │  │  ├─ snappy 1.2.1 [required: >=1.2.0,<1.3.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 14.2.0 [required: >=13]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  └─ libstdcxx 14.2.0 [required: >=13]
  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │     └─ libgcc 14.2.0 [required: 14.2.0, h767d61c_2]
  │  │  │        └─ dependencies of libgcc displayed above
  │  │  └─ zstd 1.5.6 [required: >=1.5.5,<1.6.0a0]
  │  │     └─ dependencies of zstd displayed above
  │  ├─ cfitsio 4.4.0 [required: >=4.4.0,<4.4.1.0a0]
  │  │  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
  │  │  │  └─ dependencies of bzip2 displayed above
  │  │  ├─ libcurl 8.8.0 [required: >=8.7.1,<9.0a0]
  │  │  │  └─ dependencies of libcurl displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libgfortran-ng 14.2.0 [required: any]
  │  │  │  └─ dependencies of libgfortran-ng displayed above
  │  │  ├─ libgfortran5 14.2.0 [required: >=12.3.0]
  │  │  │  └─ dependencies of libgfortran5 displayed above
  │  │  └─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │     └─ dependencies of libzlib displayed above
  │  ├─ freexl 2.0.0 [required: >=2.0.0,<3.0a0]
  │  │  ├─ libexpat 2.6.2 [required: >=2.5.0,<3.0a0]
  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libiconv 1.17 [required: >=1.17,<2.0a0]
  │  │  │  └─ dependencies of libiconv displayed above
  │  │  └─ minizip 4.0.6 [required: >=4.0.1,<5.0a0]
  │  │     ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
  │  │     │  └─ dependencies of bzip2 displayed above
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     ├─ libiconv 1.17 [required: >=1.17,<2.0a0]
  │  │     │  └─ dependencies of libiconv displayed above
  │  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │     ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0a0]
  │  │     │  └─ dependencies of libzlib displayed above
  │  │     ├─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │     │  └─ dependencies of openssl displayed above
  │  │     ├─ xz 5.2.6 [required: >=5.2.6,<6.0a0]
  │  │     │  └─ dependencies of xz displayed above
  │  │     └─ zstd 1.5.6 [required: >=1.5.6,<1.6.0a0]
  │  │        └─ dependencies of zstd displayed above
  │  ├─ geos 3.12.1 [required: >=3.12.1,<3.12.2.0a0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ geotiff 1.7.3 [required: >=1.7.1,<1.8.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libjpeg-turbo 3.0.0 [required: >=3.0.0,<4.0a0]
  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libtiff 4.6.0 [required: >=4.6.0,<4.8.0a0]
  │  │  │  ├─ lerc 4.0.0 [required: >=4.0.0,<5.0a0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ libdeflate 1.20 [required: >=1.20,<1.21.0a0]
  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libjpeg-turbo 3.0.0 [required: >=3.0.0,<4.0a0]
  │  │  │  │  └─ dependencies of libjpeg-turbo displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ libwebp-base 1.4.0 [required: >=1.3.2,<2.0a0]
  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  ├─ xz 5.2.6 [required: >=5.2.6,<6.0a0]
  │  │  │  │  └─ dependencies of xz displayed above
  │  │  │  └─ zstd 1.5.6 [required: >=1.5.5,<1.6.0a0]
  │  │  │     └─ dependencies of zstd displayed above
  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  └─ dependencies of libzlib displayed above
  │  │  ├─ proj 9.4.0 [required: >=9.4.0,<9.4.1.0a0]
  │  │  │  ├─ libcurl 8.8.0 [required: >=8.8.0,<9.0a0]
  │  │  │  │  └─ dependencies of libcurl displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libsqlite 3.45.3 [required: >=3.45.3,<4.0a0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │     └─ dependencies of libzlib displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ libtiff 4.6.0 [required: >=4.6.0,<4.8.0a0]
  │  │  │  │  └─ dependencies of libtiff displayed above
  │  │  │  └─ sqlite 3.45.3 [required: any]
  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │     ├─ libsqlite 3.45.3 [required: 3.45.3, h2797004_0]
  │  │  │     │  └─ dependencies of libsqlite displayed above
  │  │  │     ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │     │  └─ dependencies of libzlib displayed above
  │  │  │     ├─ ncurses 6.5 [required: >=6.4.20240210,<7.0a0]
  │  │  │     │  └─ dependencies of ncurses displayed above
  │  │  │     └─ readline 8.2 [required: >=8.2,<9.0a0]
  │  │  │        ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │        │  └─ dependencies of libgcc-ng displayed above
  │  │  │        └─ ncurses 6.5 [required: >=6.3,<7.0a0]
  │  │  │           └─ dependencies of ncurses displayed above
  │  │  └─ zlib 1.2.13 [required: any]
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     └─ libzlib 1.2.13 [required: 1.2.13, hd590300_5]
  │  │        └─ dependencies of libzlib displayed above
  │  ├─ giflib 5.2.2 [required: >=5.2.2,<5.3.0a0]
  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │     └─ dependencies of libgcc-ng displayed above
  │  ├─ hdf4 4.2.15 [required: >=4.2.15,<4.2.16.0a0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libjpeg-turbo 3.0.0 [required: >=3.0.0,<4.0a0]
  │  │  │  └─ dependencies of libjpeg-turbo displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  └─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │     └─ dependencies of libzlib displayed above
  │  ├─ hdf5 1.14.3 [required: >=1.14.3,<1.14.4.0a0]
  │  │  └─ dependencies of hdf5 displayed above
  │  ├─ json-c 0.17 [required: >=0.17,<0.18.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │     └─ dependencies of libgcc-ng displayed above
  │  ├─ kealib 1.5.3 [required: >=1.5.3,<1.6.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ hdf5 1.14.3 [required: >=1.14.3,<1.14.4.0a0]
  │  │  │  └─ dependencies of hdf5 displayed above
  │  │  ├─ libgcc 14.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  └─ libstdcxx 14.2.0 [required: >=13]
  │  │     └─ dependencies of libstdcxx displayed above
  │  ├─ lerc 4.0.0 [required: >=4.0.0,<5.0a0]
  │  │  └─ dependencies of lerc displayed above
  │  ├─ libaec 1.1.3 [required: >=1.1.3,<2.0a0]
  │  │  └─ dependencies of libaec displayed above
  │  ├─ libarchive 3.7.4 [required: >=3.7.4,<3.8.0a0]
  │  │  └─ dependencies of libarchive displayed above
  │  ├─ libcurl 8.8.0 [required: >=8.8.0,<9.0a0]
  │  │  └─ dependencies of libcurl displayed above
  │  ├─ libdeflate 1.20 [required: >=1.20,<1.21.0a0]
  │  │  └─ dependencies of libdeflate displayed above
  │  ├─ libexpat 2.6.2 [required: >=2.6.2,<3.0a0]
  │  │  └─ dependencies of libexpat displayed above
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libiconv 1.17 [required: >=1.17,<2.0a0]
  │  │  └─ dependencies of libiconv displayed above
  │  ├─ libjpeg-turbo 3.0.0 [required: >=3.0.0,<4.0a0]
  │  │  └─ dependencies of libjpeg-turbo displayed above
  │  ├─ libkml 1.3.0 [required: >=1.3.0,<1.4.0a0]
  │  │  ├─ libboost-headers 1.87.0 [required: any]
  │  │  ├─ libexpat 2.6.2 [required: >=2.5.0,<3.0a0]
  │  │  │  └─ dependencies of libexpat displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  └─ dependencies of libzlib displayed above
  │  │  └─ uriparser 0.9.8 [required: >=0.9.7,<1.0a0]
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ libnetcdf 4.9.2 [required: >=4.9.2,<4.9.3.0a0]
  │  │  ├─ blosc 1.21.5 [required: >=1.21.5,<2.0a0]
  │  │  │  └─ dependencies of blosc displayed above
  │  │  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
  │  │  │  └─ dependencies of bzip2 displayed above
  │  │  ├─ hdf4 4.2.15 [required: >=4.2.15,<4.2.16.0a0]
  │  │  │  └─ dependencies of hdf4 displayed above
  │  │  ├─ hdf5 1.14.3 [required: >=1.14.3,<1.14.4.0a0]
  │  │  │  └─ dependencies of hdf5 displayed above
  │  │  ├─ libaec 1.1.3 [required: >=1.1.3,<2.0a0]
  │  │  │  └─ dependencies of libaec displayed above
  │  │  ├─ libcurl 8.8.0 [required: >=8.8.0,<9.0a0]
  │  │  │  └─ dependencies of libcurl displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libxml2 2.12.7 [required: >=2.12.7,<3.0a0]
  │  │  │  └─ dependencies of libxml2 displayed above
  │  │  ├─ libzip 1.10.1 [required: >=1.10.1,<2.0a0]
  │  │  │  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
  │  │  │  │  └─ dependencies of bzip2 displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  └─ openssl 3.4.1 [required: >=3.1.2,<4.0a0]
  │  │  │     └─ dependencies of openssl displayed above
  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0a0]
  │  │  │  └─ dependencies of libzlib displayed above
  │  │  ├─ openssl 3.4.1 [required: >=3.3.1,<4.0a0]
  │  │  │  └─ dependencies of openssl displayed above
  │  │  ├─ zlib 1.2.13 [required: any]
  │  │  │  └─ dependencies of zlib displayed above
  │  │  └─ zstd 1.5.6 [required: >=1.5.6,<1.6.0a0]
  │  │     └─ dependencies of zstd displayed above
  │  ├─ libpng 1.6.43 [required: >=1.6.43,<1.7.0a0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │     └─ dependencies of libzlib displayed above
  │  ├─ libpq 16.3 [required: >=16.3,<17.0a0]
  │  │  ├─ krb5 1.21.2 [required: >=1.21.2,<1.22.0a0]
  │  │  │  └─ dependencies of krb5 displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │     └─ dependencies of openssl displayed above
  │  ├─ libspatialite 5.1.0 [required: >=5.1.0,<5.2.0a0]
  │  │  ├─ freexl 2.0.0 [required: >=2.0.0,<3.0a0]
  │  │  │  └─ dependencies of freexl displayed above
  │  │  ├─ geos 3.12.1 [required: >=3.12.1,<3.12.2.0a0]
  │  │  │  └─ dependencies of geos displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ librttopo 1.1.0 [required: >=1.1.0,<1.2.0a0]
  │  │  │  ├─ geos 3.12.1 [required: >=3.12.1,<3.12.2.0a0]
  │  │  │  │  └─ dependencies of geos displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libsqlite 3.45.3 [required: >=3.45.3,<4.0a0]
  │  │  │  └─ dependencies of libsqlite displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libxml2 2.12.7 [required: >=2.12.7,<3.0a0]
  │  │  │  └─ dependencies of libxml2 displayed above
  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  └─ dependencies of libzlib displayed above
  │  │  ├─ proj 9.4.0 [required: >=9.4.0,<9.4.1.0a0]
  │  │  │  └─ dependencies of proj displayed above
  │  │  ├─ sqlite 3.45.3 [required: any]
  │  │  │  └─ dependencies of sqlite displayed above
  │  │  └─ zlib 1.2.13 [required: any]
  │  │     └─ dependencies of zlib displayed above
  │  ├─ libsqlite 3.45.3 [required: >=3.45.3,<4.0a0]
  │  │  └─ dependencies of libsqlite displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ libtiff 4.6.0 [required: >=4.6.0,<4.8.0a0]
  │  │  └─ dependencies of libtiff displayed above
  │  ├─ libuuid 2.38.1 [required: >=2.38.1,<3.0a0]
  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │     └─ dependencies of libgcc-ng displayed above
  │  ├─ libwebp-base 1.4.0 [required: >=1.4.0,<2.0a0]
  │  │  └─ dependencies of libwebp-base displayed above
  │  ├─ libxml2 2.12.7 [required: >=2.12.7,<3.0a0]
  │  │  └─ dependencies of libxml2 displayed above
  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0a0]
  │  │  └─ dependencies of libzlib displayed above
  │  ├─ lz4-c 1.9.4 [required: >=1.9.3,<1.10.0a0]
  │  │  └─ dependencies of lz4-c displayed above
  │  ├─ openjpeg 2.5.2 [required: >=2.5.2,<3.0a0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libpng 1.6.43 [required: >=1.6.43,<1.7.0a0]
  │  │  │  └─ dependencies of libpng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libtiff 4.6.0 [required: >=4.6.0,<4.8.0a0]
  │  │  │  └─ dependencies of libtiff displayed above
  │  │  └─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │     └─ dependencies of libzlib displayed above
  │  ├─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  └─ dependencies of openssl displayed above
  │  ├─ pcre2 10.43 [required: >=10.43,<10.44.0a0]
  │  │  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
  │  │  │  └─ dependencies of bzip2 displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │     └─ dependencies of libzlib displayed above
  │  ├─ poppler 24.04.0 [required: >=24.4.0,<24.5.0a0]
  │  │  ├─ cairo 1.18.0 [required: >=1.18.0,<2.0a0]
  │  │  │  ├─ fontconfig 2.14.2 [required: >=2.14.2,<3.0a0]
  │  │  │  │  ├─ expat 2.6.2 [required: >=2.5.0,<3.0a0]
  │  │  │  │  │  ├─ libexpat 2.6.2 [required: 2.6.2, h59595ed_0]
  │  │  │  │  │  │  └─ dependencies of libexpat displayed above
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  ├─ libpng 1.6.43 [required: >=1.6.39,<1.7.0a0]
  │  │  │  │  │  │  └─ dependencies of libpng displayed above
  │  │  │  │  │  └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  │     └─ dependencies of libzlib displayed above
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libuuid 2.38.1 [required: >=2.32.1,<3.0a0]
  │  │  │  │  │  └─ dependencies of libuuid displayed above
  │  │  │  │  └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │     └─ dependencies of libzlib displayed above
  │  │  │  ├─ fonts-conda-ecosystem 1 [required: any]
  │  │  │  │  └─ fonts-conda-forge 1 [required: any]
  │  │  │  │     ├─ font-ttf-dejavu-sans-mono 2.37 [required: any]
  │  │  │  │     ├─ font-ttf-inconsolata 3.000 [required: any]
  │  │  │  │     ├─ font-ttf-source-code-pro 2.038 [required: any]
  │  │  │  │     └─ font-ttf-ubuntu 0.83 [required: any]
  │  │  │  ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
  │  │  │  │  └─ dependencies of freetype displayed above
  │  │  │  ├─ icu 73.2 [required: >=73.2,<74.0a0]
  │  │  │  │  └─ dependencies of icu displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libglib 2.80.2 [required: >=2.78.0,<3.0a0]
  │  │  │  │  ├─ libffi 3.4.2 [required: >=3.4,<4.0a0]
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=9.4.0]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libiconv 1.17 [required: >=1.17,<2.0a0]
  │  │  │  │  │  └─ dependencies of libiconv displayed above
  │  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  │  └─ pcre2 10.43 [required: >=10.43,<10.44.0a0]
  │  │  │  │     └─ dependencies of pcre2 displayed above
  │  │  │  ├─ libpng 1.6.43 [required: >=1.6.39,<1.7.0a0]
  │  │  │  │  └─ dependencies of libpng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ libxcb 1.15 [required: >=1.15,<1.16.0a0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ pthread-stubs 0.4 [required: any]
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=7.5.0]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ xorg-libxau 1.0.11 [required: any]
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ xorg-libxdmcp 1.1.3 [required: any]
  │  │  │  │     └─ libgcc-ng 14.2.0 [required: >=9.3.0]
  │  │  │  │        └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  ├─ pixman 0.43.2 [required: >=0.42.2,<1.0a0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ xorg-libice 1.1.1 [required: >=1.1.1,<2.0a0]
  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ xorg-libsm 1.2.4 [required: >=1.2.4,<2.0a0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libuuid 2.38.1 [required: >=2.38.1,<3.0a0]
  │  │  │  │  │  └─ dependencies of libuuid displayed above
  │  │  │  │  └─ xorg-libice 1.1.1 [required: >=1.1.1,<2.0a0]
  │  │  │  │     └─ dependencies of xorg-libice displayed above
  │  │  │  ├─ xorg-libx11 1.8.9 [required: >=1.8.6,<2.0a0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libxcb 1.15 [required: >=1.15,<1.16.0a0]
  │  │  │  │  │  └─ dependencies of libxcb displayed above
  │  │  │  │  ├─ xorg-kbproto 1.0.7 [required: any]
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=9.3.0]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ xorg-xextproto 7.3.0 [required: >=7.3.0,<8.0a0]
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ xorg-xproto 7.0.31 [required: any]
  │  │  │  │     └─ libgcc-ng 14.2.0 [required: >=9.3.0]
  │  │  │  │        └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ xorg-libxext 1.3.4 [required: >=1.3.4,<2.0a0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ xorg-libx11 1.8.9 [required: >=1.7.2,<2.0a0]
  │  │  │  │  │  └─ dependencies of xorg-libx11 displayed above
  │  │  │  │  └─ xorg-xextproto 7.3.0 [required: any]
  │  │  │  │     └─ dependencies of xorg-xextproto displayed above
  │  │  │  ├─ xorg-libxrender 0.9.11 [required: >=0.9.11,<0.10.0a0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ xorg-libx11 1.8.9 [required: >=1.8.6,<2.0a0]
  │  │  │  │  │  └─ dependencies of xorg-libx11 displayed above
  │  │  │  │  └─ xorg-renderproto 0.11.1 [required: any]
  │  │  │  │     └─ libgcc-ng 14.2.0 [required: >=9.3.0]
  │  │  │  │        └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ zlib 1.2.13 [required: any]
  │  │  │     └─ dependencies of zlib displayed above
  │  │  ├─ fontconfig 2.14.2 [required: >=2.14.2,<3.0a0]
  │  │  │  └─ dependencies of fontconfig displayed above
  │  │  ├─ fonts-conda-ecosystem 1 [required: any]
  │  │  │  └─ dependencies of fonts-conda-ecosystem displayed above
  │  │  ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
  │  │  │  └─ dependencies of freetype displayed above
  │  │  ├─ lcms2 2.16 [required: >=2.16,<3.0a0]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libjpeg-turbo 3.0.0 [required: >=3.0.0,<4.0a0]
  │  │  │  │  └─ dependencies of libjpeg-turbo displayed above
  │  │  │  └─ libtiff 4.6.0 [required: >=4.6.0,<4.8.0a0]
  │  │  │     └─ dependencies of libtiff displayed above
  │  │  ├─ libcurl 8.8.0 [required: >=8.7.1,<9.0a0]
  │  │  │  └─ dependencies of libcurl displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libglib 2.80.2 [required: >=2.80.0,<3.0a0]
  │  │  │  └─ dependencies of libglib displayed above
  │  │  ├─ libiconv 1.17 [required: >=1.17,<2.0a0]
  │  │  │  └─ dependencies of libiconv displayed above
  │  │  ├─ libjpeg-turbo 3.0.0 [required: >=3.0.0,<4.0a0]
  │  │  │  └─ dependencies of libjpeg-turbo displayed above
  │  │  ├─ libpng 1.6.43 [required: >=1.6.43,<1.7.0a0]
  │  │  │  └─ dependencies of libpng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libtiff 4.6.0 [required: >=4.6.0,<4.8.0a0]
  │  │  │  └─ dependencies of libtiff displayed above
  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  └─ dependencies of libzlib displayed above
  │  │  ├─ nspr 4.36 [required: >=4.35,<5.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 14.2.0 [required: >=13]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  └─ libstdcxx 14.2.0 [required: >=13]
  │  │  │     └─ dependencies of libstdcxx displayed above
  │  │  ├─ nss 3.100 [required: >=3.98,<4.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libsqlite 3.45.3 [required: >=3.45.3,<4.0a0]
  │  │  │  │  └─ dependencies of libsqlite displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  └─ nspr 4.36 [required: >=4.35,<5.0a0]
  │  │  │     └─ dependencies of nspr displayed above
  │  │  ├─ openjpeg 2.5.2 [required: >=2.5.2,<3.0a0]
  │  │  │  └─ dependencies of openjpeg displayed above
  │  │  └─ poppler-data 0.4.12 [required: any]
  │  ├─ postgresql 16.3 [required: any]
  │  │  ├─ krb5 1.21.2 [required: >=1.21.2,<1.22.0a0]
  │  │  │  └─ dependencies of krb5 displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libpq 16.3 [required: 16.3, ha72fbe1_0]
  │  │  │  └─ dependencies of libpq displayed above
  │  │  ├─ libxml2 2.12.7 [required: >=2.12.6,<3.0a0]
  │  │  │  └─ dependencies of libxml2 displayed above
  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  └─ dependencies of libzlib displayed above
  │  │  ├─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  └─ dependencies of openssl displayed above
  │  │  ├─ readline 8.2 [required: >=8.2,<9.0a0]
  │  │  │  └─ dependencies of readline displayed above
  │  │  ├─ tzcode 2025a [required: any]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  └─ libgcc 14.2.0 [required: >=13]
  │  │  │     └─ dependencies of libgcc displayed above
  │  │  └─ tzdata 2024a [required: any]
  │  ├─ proj 9.4.0 [required: >=9.4.0,<9.4.1.0a0]
  │  │  └─ dependencies of proj displayed above
  │  ├─ tiledb 2.23.0 [required: >=2.23.0,<2.24.0a0]
  │  │  ├─ aws-crt-cpp 0.26.9 [required: >=0.26.9,<0.26.10.0a0]
  │  │  │  ├─ aws-c-auth 0.7.22 [required: >=0.7.22,<0.7.23.0a0]
  │  │  │  │  ├─ aws-c-cal 0.6.14 [required: >=0.6.14,<0.6.15.0a0]
  │  │  │  │  │  ├─ aws-c-common 0.9.19 [required: >=0.9.19,<0.9.20.0a0]
  │  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  └─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  │  │     └─ dependencies of openssl displayed above
  │  │  │  │  ├─ aws-c-common 0.9.19 [required: >=0.9.19,<0.9.20.0a0]
  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  ├─ aws-c-http 0.8.1 [required: >=0.8.1,<0.8.2.0a0]
  │  │  │  │  │  ├─ aws-c-cal 0.6.14 [required: >=0.6.14,<0.6.15.0a0]
  │  │  │  │  │  │  └─ dependencies of aws-c-cal displayed above
  │  │  │  │  │  ├─ aws-c-common 0.9.19 [required: >=0.9.19,<0.9.20.0a0]
  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  ├─ aws-c-compression 0.2.18 [required: >=0.2.18,<0.2.19.0a0]
  │  │  │  │  │  │  ├─ aws-c-common 0.9.19 [required: >=0.9.19,<0.9.20.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  ├─ aws-c-io 0.14.8 [required: >=0.14.8,<0.14.9.0a0]
  │  │  │  │  │  │  ├─ aws-c-cal 0.6.14 [required: >=0.6.14,<0.6.15.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-c-cal displayed above
  │  │  │  │  │  │  ├─ aws-c-common 0.9.19 [required: >=0.9.19,<0.9.20.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  └─ s2n 1.4.15 [required: >=1.4.15,<1.4.16.0a0]
  │  │  │  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │     └─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  │  │  │        └─ dependencies of openssl displayed above
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ aws-c-io 0.14.8 [required: >=0.14.8,<0.14.9.0a0]
  │  │  │  │  │  └─ dependencies of aws-c-io displayed above
  │  │  │  │  ├─ aws-c-sdkutils 0.1.16 [required: >=0.1.16,<0.1.17.0a0]
  │  │  │  │  │  ├─ aws-c-common 0.9.19 [required: >=0.9.19,<0.9.20.0a0]
  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ aws-c-cal 0.6.14 [required: >=0.6.14,<0.6.15.0a0]
  │  │  │  │  └─ dependencies of aws-c-cal displayed above
  │  │  │  ├─ aws-c-common 0.9.19 [required: >=0.9.19,<0.9.20.0a0]
  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  ├─ aws-c-event-stream 0.4.2 [required: >=0.4.2,<0.4.3.0a0]
  │  │  │  │  ├─ aws-c-common 0.9.19 [required: >=0.9.19,<0.9.20.0a0]
  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  ├─ aws-c-io 0.14.8 [required: >=0.14.8,<0.14.9.0a0]
  │  │  │  │  │  └─ dependencies of aws-c-io displayed above
  │  │  │  │  ├─ aws-checksums 0.1.18 [required: >=0.1.18,<0.1.19.0a0]
  │  │  │  │  │  ├─ aws-c-common 0.9.19 [required: >=0.9.19,<0.9.20.0a0]
  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ aws-c-http 0.8.1 [required: >=0.8.1,<0.8.2.0a0]
  │  │  │  │  └─ dependencies of aws-c-http displayed above
  │  │  │  ├─ aws-c-io 0.14.8 [required: >=0.14.8,<0.14.9.0a0]
  │  │  │  │  └─ dependencies of aws-c-io displayed above
  │  │  │  ├─ aws-c-mqtt 0.10.4 [required: >=0.10.4,<0.10.5.0a0]
  │  │  │  │  ├─ aws-c-common 0.9.19 [required: >=0.9.19,<0.9.20.0a0]
  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  ├─ aws-c-http 0.8.1 [required: >=0.8.1,<0.8.2.0a0]
  │  │  │  │  │  └─ dependencies of aws-c-http displayed above
  │  │  │  │  ├─ aws-c-io 0.14.8 [required: >=0.14.8,<0.14.9.0a0]
  │  │  │  │  │  └─ dependencies of aws-c-io displayed above
  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ aws-c-s3 0.5.9 [required: >=0.5.9,<0.5.10.0a0]
  │  │  │  │  ├─ aws-c-auth 0.7.22 [required: >=0.7.22,<0.7.23.0a0]
  │  │  │  │  │  └─ dependencies of aws-c-auth displayed above
  │  │  │  │  ├─ aws-c-cal 0.6.14 [required: >=0.6.14,<0.6.15.0a0]
  │  │  │  │  │  └─ dependencies of aws-c-cal displayed above
  │  │  │  │  ├─ aws-c-common 0.9.19 [required: >=0.9.19,<0.9.20.0a0]
  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  ├─ aws-c-http 0.8.1 [required: >=0.8.1,<0.8.2.0a0]
  │  │  │  │  │  └─ dependencies of aws-c-http displayed above
  │  │  │  │  ├─ aws-c-io 0.14.8 [required: >=0.14.8,<0.14.9.0a0]
  │  │  │  │  │  └─ dependencies of aws-c-io displayed above
  │  │  │  │  ├─ aws-checksums 0.1.18 [required: >=0.1.18,<0.1.19.0a0]
  │  │  │  │  │  └─ dependencies of aws-checksums displayed above
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  │     └─ dependencies of openssl displayed above
  │  │  │  ├─ aws-c-sdkutils 0.1.16 [required: >=0.1.16,<0.1.17.0a0]
  │  │  │  │  └─ dependencies of aws-c-sdkutils displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ aws-sdk-cpp 1.11.329 [required: >=1.11.329,<1.11.330.0a0]
  │  │  │  ├─ aws-c-common 0.9.19 [required: >=0.9.19,<0.9.20.0a0]
  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  ├─ aws-c-event-stream 0.4.2 [required: >=0.4.2,<0.4.3.0a0]
  │  │  │  │  └─ dependencies of aws-c-event-stream displayed above
  │  │  │  ├─ aws-checksums 0.1.18 [required: >=0.1.18,<0.1.19.0a0]
  │  │  │  │  └─ dependencies of aws-checksums displayed above
  │  │  │  ├─ aws-crt-cpp 0.26.9 [required: >=0.26.9,<0.26.10.0a0]
  │  │  │  │  └─ dependencies of aws-crt-cpp displayed above
  │  │  │  ├─ libcurl 8.8.0 [required: >=8.8.0,<9.0a0]
  │  │  │  │  └─ dependencies of libcurl displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  └─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │     └─ dependencies of openssl displayed above
  │  │  ├─ azure-core-cpp 1.11.1 [required: >=1.11.1,<1.11.2.0a0]
  │  │  │  ├─ libcurl 8.8.0 [required: >=8.5.0,<9.0a0]
  │  │  │  │  └─ dependencies of libcurl displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  └─ openssl 3.4.1 [required: >=3.2.1,<4.0a0]
  │  │  │     └─ dependencies of openssl displayed above
  │  │  ├─ azure-identity-cpp 1.6.0 [required: >=1.6.0,<1.6.1.0a0]
  │  │  │  ├─ azure-core-cpp 1.11.1 [required: >=1.11.1,<1.11.2.0a0]
  │  │  │  │  └─ dependencies of azure-core-cpp displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  └─ openssl 3.4.1 [required: >=3.2.1,<4.0a0]
  │  │  │     └─ dependencies of openssl displayed above
  │  │  ├─ azure-storage-blobs-cpp 12.10.0 [required: >=12.10.0,<12.10.1.0a0]
  │  │  │  ├─ azure-core-cpp 1.11.1 [required: >=1.11.1,<1.11.2.0a0]
  │  │  │  │  └─ dependencies of azure-core-cpp displayed above
  │  │  │  ├─ azure-storage-common-cpp 12.5.0 [required: >=12.5.0,<12.5.1.0a0]
  │  │  │  │  ├─ azure-core-cpp 1.11.1 [required: >=1.11.1,<1.11.2.0a0]
  │  │  │  │  │  └─ dependencies of azure-core-cpp displayed above
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  ├─ libxml2 2.12.7 [required: >=2.12.5,<3.0a0]
  │  │  │  │  │  └─ dependencies of libxml2 displayed above
  │  │  │  │  └─ openssl 3.4.1 [required: >=3.2.1,<4.0a0]
  │  │  │  │     └─ dependencies of openssl displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ azure-storage-common-cpp 12.5.0 [required: >=12.5.0,<12.5.1.0a0]
  │  │  │  └─ dependencies of azure-storage-common-cpp displayed above
  │  │  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
  │  │  │  └─ dependencies of bzip2 displayed above
  │  │  ├─ fmt 10.2.1 [required: >=10.2.1,<11.0a0]
  │  │  │  └─ dependencies of fmt displayed above
  │  │  ├─ libabseil 20240116.2 [required: >=20240116.2,<20240117.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libcurl 8.8.0 [required: >=8.8.0,<9.0a0]
  │  │  │  └─ dependencies of libcurl displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libgoogle-cloud 2.24.0 [required: >=2.24.0,<2.25.0a0]
  │  │  │  ├─ libabseil 20240116.2 [required: >=20240116.2,<20240117.0a0]
  │  │  │  │  └─ dependencies of libabseil displayed above
  │  │  │  ├─ libcurl 8.8.0 [required: >=8.7.1,<9.0a0]
  │  │  │  │  └─ dependencies of libcurl displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libgrpc 1.62.2 [required: >=1.62.2,<1.63.0a0]
  │  │  │  │  ├─ c-ares 1.28.1 [required: >=1.28.1,<2.0a0]
  │  │  │  │  │  └─ dependencies of c-ares displayed above
  │  │  │  │  ├─ libabseil 20240116.2 [required: >=20240116.1,<20240117.0a0]
  │  │  │  │  │  └─ dependencies of libabseil displayed above
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libprotobuf 4.25.3 [required: >=4.25.3,<4.25.4.0a0]
  │  │  │  │  │  ├─ libabseil 20240116.2 [required: >=20240116.1,<20240117.0a0]
  │  │  │  │  │  │  └─ dependencies of libabseil displayed above
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  │  └─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  │  │     └─ dependencies of libzlib displayed above
  │  │  │  │  ├─ libre2-11 2023.09.01 [required: >=2023.9.1]
  │  │  │  │  │  ├─ libabseil 20240116.2 [required: >=20240116.1,<20240117.0a0]
  │  │  │  │  │  │  └─ dependencies of libabseil displayed above
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  │  ├─ openssl 3.4.1 [required: >=3.2.1,<4.0a0]
  │  │  │  │  │  └─ dependencies of openssl displayed above
  │  │  │  │  └─ re2 2023.09.01 [required: any]
  │  │  │  │     └─ libre2-11 2023.09.01 [required: 2023.09.01, h5a48ba9_2]
  │  │  │  │        └─ dependencies of libre2-11 displayed above
  │  │  │  ├─ libprotobuf 4.25.3 [required: >=4.25.3,<4.25.4.0a0]
  │  │  │  │  └─ dependencies of libprotobuf displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  └─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │     └─ dependencies of openssl displayed above
  │  │  ├─ libgoogle-cloud-storage 2.24.0 [required: >=2.24.0,<2.25.0a0]
  │  │  │  ├─ libabseil 20240116.2 [required: any]
  │  │  │  │  └─ dependencies of libabseil displayed above
  │  │  │  ├─ libcrc32c 1.1.2 [required: >=1.1.2,<1.2.0a0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=9.4.0]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=9.4.0]
  │  │  │  ├─ libcurl 8.8.0 [required: any]
  │  │  │  │  └─ dependencies of libcurl displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libgoogle-cloud 2.24.0 [required: 2.24.0, h2736e30_0]
  │  │  │  │  └─ dependencies of libgoogle-cloud displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  └─ openssl 3.4.1 [required: any]
  │  │  │     └─ dependencies of openssl displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libwebp-base 1.4.0 [required: >=1.4.0,<2.0a0]
  │  │  │  └─ dependencies of libwebp-base displayed above
  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  └─ dependencies of libzlib displayed above
  │  │  ├─ lz4-c 1.9.4 [required: >=1.9.3,<1.10.0a0]
  │  │  │  └─ dependencies of lz4-c displayed above
  │  │  ├─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  └─ dependencies of openssl displayed above
  │  │  ├─ spdlog 1.13.0 [required: >=1.13.0,<1.14.0a0]
  │  │  │  ├─ fmt 10.2.1 [required: >=10.2.1,<11.0a0]
  │  │  │  │  └─ dependencies of fmt displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  └─ zstd 1.5.6 [required: >=1.5.6,<1.6.0a0]
  │  │     └─ dependencies of zstd displayed above
  │  ├─ xerces-c 3.2.5 [required: >=3.2.5,<3.3.0a0]
  │  │  ├─ icu 73.2 [required: >=73.2,<74.0a0]
  │  │  │  └─ dependencies of icu displayed above
  │  │  ├─ libcurl 8.8.0 [required: >=8.5.0,<9.0a0]
  │  │  │  └─ dependencies of libcurl displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libnsl 2.0.1 [required: >=2.0.1,<2.1.0a0]
  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ xz 5.2.6 [required: >=5.2.6,<6.0a0]
  │  │  └─ dependencies of xz displayed above
  │  └─ zstd 1.5.6 [required: >=1.5.6,<1.6.0a0]
  │     └─ dependencies of zstd displayed above
  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  ├─ libxml2 2.12.7 [required: >=2.12.7,<3.0a0]
  │  └─ dependencies of libxml2 displayed above
  ├─ numpy 2.2.3 [required: >=1.19,<3]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ libopenblas 0.3.27 [required: >=0.3.27,<1.0a0]
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     ├─ libgfortran-ng 14.2.0 [required: any]
  │  │     │  └─ dependencies of libgfortran-ng displayed above
  │  │     └─ libgfortran5 14.2.0 [required: >=12.3.0]
  │  │        └─ dependencies of libgfortran5 displayed above
  │  ├─ libcblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ libblas 3.9.0 [required: 3.9.0, 22_linux64_openblas]
  │  │     └─ dependencies of libblas displayed above
  │  ├─ libgcc 14.2.0 [required: >=13]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ libblas 3.9.0 [required: 3.9.0, 22_linux64_openblas]
  │  │     └─ dependencies of libblas displayed above
  │  ├─ libstdcxx 14.2.0 [required: >=13]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  ├─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  └─ dependencies of openssl displayed above
  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
r-gstat==2.1_3
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ libgcc 14.2.0 [required: >=13]
  │  └─ dependencies of libgcc displayed above
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  ├─ _openmp_mutex 4.5 [required: >=4.5]
  │  │  └─ dependencies of _openmp_mutex displayed above
  │  ├─ _r-mutex 1.0.1 [required: 1.*, anacondar_1]
  │  ├─ bwidget 1.9.14 [required: any]
  │  │  └─ tk 8.6.13 [required: any]
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │        └─ dependencies of libzlib displayed above
  │  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
  │  │  └─ dependencies of bzip2 displayed above
  │  ├─ cairo 1.18.0 [required: >=1.18.0,<2.0a0]
  │  │  └─ dependencies of cairo displayed above
  │  ├─ curl 8.8.0 [required: any]
  │  │  ├─ krb5 1.21.2 [required: >=1.21.2,<1.22.0a0]
  │  │  │  └─ dependencies of krb5 displayed above
  │  │  ├─ libcurl 8.8.0 [required: 8.8.0, hca28451_0]
  │  │  │  └─ dependencies of libcurl displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libssh2 1.11.0 [required: >=1.11.0,<2.0a0]
  │  │  │  └─ dependencies of libssh2 displayed above
  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<2.0.0a0]
  │  │  │  └─ dependencies of libzlib displayed above
  │  │  ├─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  └─ dependencies of openssl displayed above
  │  │  └─ zstd 1.5.6 [required: >=1.5.6,<1.6.0a0]
  │  │     └─ dependencies of zstd displayed above
  │  ├─ gcc_impl_linux-64 13.2.0 [required: >=10]
  │  │  ├─ binutils_impl_linux-64 2.40 [required: >=2.40]
  │  │  │  ├─ ld_impl_linux-64 2.40 [required: 2.40, h55db66e_0]
  │  │  │  └─ sysroot_linux-64 2.12 [required: any]
  │  │  │     └─ kernel-headers_linux-64 2.6.32 [required: 2.6.32, he073ed8_17]
  │  │  ├─ libgcc-devel_linux-64 13.2.0 [required: 13.2.0, hceb6213_107]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=13.2.0]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libgomp 14.2.0 [required: >=13.2.0]
  │  │  │  └─ dependencies of libgomp displayed above
  │  │  ├─ libsanitizer 13.2.0 [required: 13.2.0, h6ddb7a1_7]
  │  │  │  └─ libgcc-ng 14.2.0 [required: >=13.2.0]
  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=13.2.0]
  │  │  └─ sysroot_linux-64 2.12 [required: any]
  │  │     └─ dependencies of sysroot_linux-64 displayed above
  │  ├─ gfortran_impl_linux-64 13.2.0 [required: any]
  │  │  ├─ gcc_impl_linux-64 13.2.0 [required: >=13.2.0]
  │  │  │  └─ dependencies of gcc_impl_linux-64 displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=4.9]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libgfortran5 14.2.0 [required: >=13.2.0]
  │  │  │  └─ dependencies of libgfortran5 displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=4.9]
  │  │  └─ sysroot_linux-64 2.12 [required: any]
  │  │     └─ dependencies of sysroot_linux-64 displayed above
  │  ├─ gxx_impl_linux-64 13.2.0 [required: >=10]
  │  │  ├─ gcc_impl_linux-64 13.2.0 [required: 13.2.0, h9eb54c0_7]
  │  │  │  └─ dependencies of gcc_impl_linux-64 displayed above
  │  │  ├─ libstdcxx-devel_linux-64 13.2.0 [required: 13.2.0, hceb6213_107]
  │  │  └─ sysroot_linux-64 2.12 [required: any]
  │  │     └─ dependencies of sysroot_linux-64 displayed above
  │  ├─ icu 73.2 [required: >=73.2,<74.0a0]
  │  │  └─ dependencies of icu displayed above
  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ dependencies of libblas displayed above
  │  ├─ libcurl 8.8.0 [required: >=8.7.1,<9.0a0]
  │  │  └─ dependencies of libcurl displayed above
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libgfortran-ng 14.2.0 [required: any]
  │  │  └─ dependencies of libgfortran-ng displayed above
  │  ├─ libgfortran5 14.2.0 [required: >=10.4.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ libglib 2.80.2 [required: >=2.80.0,<3.0a0]
  │  │  └─ dependencies of libglib displayed above
  │  ├─ libiconv 1.17 [required: >=1.17,<2.0a0]
  │  │  └─ dependencies of libiconv displayed above
  │  ├─ libjpeg-turbo 3.0.0 [required: >=3.0.0,<4.0a0]
  │  │  └─ dependencies of libjpeg-turbo displayed above
  │  ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ dependencies of liblapack displayed above
  │  ├─ libpng 1.6.43 [required: >=1.6.43,<1.7.0a0]
  │  │  └─ dependencies of libpng displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ libtiff 4.6.0 [required: >=4.6.0,<4.7.0a0]
  │  │  └─ dependencies of libtiff displayed above
  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  └─ dependencies of libzlib displayed above
  │  ├─ make 4.3 [required: any]
  │  │  └─ libgcc-ng 14.2.0 [required: >=7.5.0]
  │  │     └─ dependencies of libgcc-ng displayed above
  │  ├─ pango 1.52.2 [required: >=1.50.14,<2.0a0]
  │  │  ├─ cairo 1.18.0 [required: >=1.18.0,<2.0a0]
  │  │  │  └─ dependencies of cairo displayed above
  │  │  ├─ fontconfig 2.14.2 [required: >=2.14.2,<3.0a0]
  │  │  │  └─ dependencies of fontconfig displayed above
  │  │  ├─ fonts-conda-ecosystem 1 [required: any]
  │  │  │  └─ dependencies of fonts-conda-ecosystem displayed above
  │  │  ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
  │  │  │  └─ dependencies of freetype displayed above
  │  │  ├─ fribidi 1.0.10 [required: >=1.0.10,<2.0a0]
  │  │  │  └─ libgcc-ng 14.2.0 [required: >=7.5.0]
  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  ├─ harfbuzz 8.5.0 [required: >=8.3.0,<9.0a0]
  │  │  │  ├─ cairo 1.18.0 [required: >=1.18.0,<2.0a0]
  │  │  │  │  └─ dependencies of cairo displayed above
  │  │  │  ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
  │  │  │  │  └─ dependencies of freetype displayed above
  │  │  │  ├─ graphite2 1.3.13 [required: any]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ icu 73.2 [required: >=73.2,<74.0a0]
  │  │  │  │  └─ dependencies of icu displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libglib 2.80.2 [required: >=2.80.2,<3.0a0]
  │  │  │  │  └─ dependencies of libglib displayed above
  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libglib 2.80.2 [required: >=2.80.0,<3.0a0]
  │  │  │  └─ dependencies of libglib displayed above
  │  │  └─ libpng 1.6.43 [required: >=1.6.43,<1.7.0a0]
  │  │     └─ dependencies of libpng displayed above
  │  ├─ pcre2 10.43 [required: >=10.43,<10.44.0a0]
  │  │  └─ dependencies of pcre2 displayed above
  │  ├─ readline 8.2 [required: >=8.2,<9.0a0]
  │  │  └─ dependencies of readline displayed above
  │  ├─ sed 4.8 [required: any]
  │  │  └─ libgcc-ng 14.2.0 [required: >=7.5.0]
  │  │     └─ dependencies of libgcc-ng displayed above
  │  ├─ tk 8.6.13 [required: >=8.6.13,<8.7.0a0]
  │  │  └─ dependencies of tk displayed above
  │  ├─ tktable 2.10 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ tk 8.6.13 [required: >=8.6.13,<8.7.0a0]
  │  │     └─ dependencies of tk displayed above
  │  ├─ xorg-libxt 1.3.0 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ xorg-kbproto 1.0.7 [required: any]
  │  │  │  └─ dependencies of xorg-kbproto displayed above
  │  │  ├─ xorg-libice 1.1.1 [required: >=1.1.1,<2.0a0]
  │  │  │  └─ dependencies of xorg-libice displayed above
  │  │  ├─ xorg-libsm 1.2.4 [required: >=1.2.4,<2.0a0]
  │  │  │  └─ dependencies of xorg-libsm displayed above
  │  │  ├─ xorg-libx11 1.8.9 [required: >=1.8.6,<2.0a0]
  │  │  │  └─ dependencies of xorg-libx11 displayed above
  │  │  └─ xorg-xproto 7.0.31 [required: any]
  │  │     └─ dependencies of xorg-xproto displayed above
  │  └─ xz 5.2.6 [required: >=5.2.6,<6.0a0]
  │     └─ dependencies of xz displayed above
  ├─ r-fnn 1.1.4.1 [required: any]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 14.2.0 [required: >=13]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 14.2.0 [required: >=13]
  │  │  └─ dependencies of libstdcxx displayed above
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-lattice 0.22_6 [required: any]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-sf 1.0_16 [required: >=0.7_2]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ geos 3.12.1 [required: >=3.12.1,<3.12.2.0a0]
  │  │  └─ dependencies of geos displayed above
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libgdal 3.9.0 [required: >=3.9.0,<3.10.0a0]
  │  │  └─ dependencies of libgdal displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ proj 9.4.0 [required: >=9.4.0,<9.5.0a0]
  │  │  └─ dependencies of proj displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-classint 0.4_11 [required: >=0.4_1]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 14.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libgfortran 14.2.0 [required: any]
  │  │  │  └─ dependencies of libgfortran displayed above
  │  │  ├─ libgfortran5 14.2.0 [required: >=13.3.0]
  │  │  │  └─ dependencies of libgfortran5 displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-class 7.3_22 [required: any]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-mass 7.3_60 [required: any]
  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │        └─ dependencies of r-base displayed above
  │  │  ├─ r-e1071 1.7_14 [required: any]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-class 7.3_22 [required: any]
  │  │  │  │  └─ dependencies of r-class displayed above
  │  │  │  └─ r-proxy 0.4_27 [required: any]
  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │        └─ dependencies of r-base displayed above
  │  │  └─ r-kernsmooth 2.23_24 [required: any]
  │  │     ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │     │  └─ dependencies of libblas displayed above
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     ├─ libgfortran-ng 14.2.0 [required: any]
  │  │     │  └─ dependencies of libgfortran-ng displayed above
  │  │     ├─ libgfortran5 14.2.0 [required: >=12.3.0]
  │  │     │  └─ dependencies of libgfortran5 displayed above
  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │        └─ dependencies of r-base displayed above
  │  ├─ r-dbi 1.2.2 [required: >=0.8]
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-rcpp 1.0.12 [required: >=0.12.18]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-s2 1.1.7 [required: >=1.1.0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ openssl 3.4.1 [required: >=3.3.1,<4.0a0]
  │  │  │  └─ dependencies of openssl displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-rcpp 1.0.12 [required: any]
  │  │  │  └─ dependencies of r-rcpp displayed above
  │  │  └─ r-wk 0.9.4 [required: any]
  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │     ├─ libgcc 14.2.0 [required: >=13]
  │  │     │  └─ dependencies of libgcc displayed above
  │  │     ├─ libstdcxx 14.2.0 [required: >=13]
  │  │     │  └─ dependencies of libstdcxx displayed above
  │  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     │  └─ dependencies of r-base displayed above
  │  │     └─ r-cpp11 0.4.7 [required: any]
  │  │        └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │           └─ dependencies of r-base displayed above
  │  └─ r-units 0.8_5 [required: >=0.7_0]
  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  └─ dependencies of libgcc-ng displayed above
  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │     ├─ libudunits2 2.2.28 [required: >=2.2.28,<3.0a0]
  │     │  ├─ libexpat 2.6.2 [required: >=2.5.0,<3.0a0]
  │     │  │  └─ dependencies of libexpat displayed above
  │     │  └─ libgcc-ng 14.2.0 [required: >=12]
  │     │     └─ dependencies of libgcc-ng displayed above
  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     └─ r-rcpp 1.0.12 [required: any]
  │        └─ dependencies of r-rcpp displayed above
  ├─ r-sftime 0.3.0 [required: any]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-sf 1.0_16 [required: >=1.0.7]
  │     └─ dependencies of r-sf displayed above
  ├─ r-sp 2.2_0 [required: >=0.9_72]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 14.2.0 [required: >=13]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-lattice 0.22_6 [required: any]
  │     └─ dependencies of r-lattice displayed above
  ├─ r-spacetime 1.3_3 [required: >=1.2_8]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-intervals 0.15.5 [required: any]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 14.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libstdcxx 14.2.0 [required: >=13]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-lattice 0.22_6 [required: any]
  │  │  └─ dependencies of r-lattice displayed above
  │  ├─ r-sp 2.2_0 [required: >=1.1_0]
  │  │  └─ dependencies of r-sp displayed above
  │  ├─ r-xts 0.13.2 [required: >=0.8_8]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  └─ r-zoo 1.8_12 [required: >=1.7_12]
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     │  └─ dependencies of r-base displayed above
  │  │     └─ r-lattice 0.22_6 [required: >=0.20_27]
  │  │        └─ dependencies of r-lattice displayed above
  │  └─ r-zoo 1.8_12 [required: >=1.7_9]
  │     └─ dependencies of r-zoo displayed above
  ├─ r-stars 0.6_6 [required: any]
  │  ├─ r-abind 1.4_5 [required: any]
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-classint 0.4_11 [required: >=0.4_1]
  │  │  └─ dependencies of r-classint displayed above
  │  ├─ r-lwgeom 0.2_14 [required: any]
  │  │  ├─ geos 3.12.1 [required: >=3.12.1,<3.12.2.0a0]
  │  │  │  └─ dependencies of geos displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ proj 9.4.0 [required: >=9.4.0,<9.5.0a0]
  │  │  │  └─ dependencies of proj displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-rcpp 1.0.12 [required: any]
  │  │  │  └─ dependencies of r-rcpp displayed above
  │  │  ├─ r-sf 1.0_16 [required: >=1.0_15]
  │  │  │  └─ dependencies of r-sf displayed above
  │  │  └─ r-units 0.8_5 [required: any]
  │  │     └─ dependencies of r-units displayed above
  │  ├─ r-rlang 1.1.3 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-sf 1.0_16 [required: >=0.9_7]
  │  │  └─ dependencies of r-sf displayed above
  │  └─ r-units 0.8_5 [required: any]
  │     └─ dependencies of r-units displayed above
  └─ r-zoo 1.8_12 [required: any]
     └─ dependencies of r-zoo displayed above
r-spatial==7.3_18
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ libgcc 14.2.0 [required: >=13]
  │  └─ dependencies of libgcc displayed above
  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
     └─ dependencies of r-base displayed above
r-terra==1.7_78
  ├─ geos 3.12.1 [required: >=3.12.1,<3.12.2.0a0]
  │  └─ dependencies of geos displayed above
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libgdal 3.9.0 [required: >=3.9.0,<3.10.0a0]
  │  └─ dependencies of libgdal displayed above
  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  ├─ proj 9.4.0 [required: >=9.4.0,<9.5.0a0]
  │  └─ dependencies of proj displayed above
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  └─ r-rcpp 1.0.12 [required: >=1.0_10]
     └─ dependencies of r-rcpp displayed above
r-keras==2.15.0
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-ellipsis 0.3.2 [required: any]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-rlang 1.1.3 [required: >=0.3.0]
  │     └─ dependencies of r-rlang displayed above
  ├─ r-generics 0.1.3 [required: >=0.0.1]
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-glue 1.7.0 [required: any]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-magrittr 2.0.3 [required: any]
  │  └─ dependencies of r-magrittr displayed above
  ├─ r-r6 2.5.1 [required: any]
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-reticulate 1.40.0 [required: >1.22]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 14.2.0 [required: >=13]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 14.2.0 [required: >=13]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-here 1.0.1 [required: any]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  └─ r-rprojroot 2.0.4 [required: >=2.0.2]
  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │        └─ dependencies of r-base displayed above
  │  ├─ r-jsonlite 1.8.8 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-matrix 1.6_5 [required: any]
  │  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  └─ dependencies of libblas displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  └─ dependencies of liblapack displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  └─ r-lattice 0.22_6 [required: any]
  │  │     └─ dependencies of r-lattice displayed above
  │  ├─ r-png 0.1_8 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libpng 1.6.43 [required: >=1.6.43,<1.7.0a0]
  │  │  │  └─ dependencies of libpng displayed above
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-rappdirs 0.3.3 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-rcpp 1.0.12 [required: >=1.0.7]
  │  │  └─ dependencies of r-rcpp displayed above
  │  ├─ r-rcpptoml 0.2.2 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  └─ r-rcpp 1.0.12 [required: >=0.11.5]
  │  │     └─ dependencies of r-rcpp displayed above
  │  ├─ r-rlang 1.1.3 [required: any]
  │  │  └─ dependencies of r-rlang displayed above
  │  └─ r-withr 3.0.0 [required: any]
  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │        └─ dependencies of r-base displayed above
  ├─ r-rlang 1.1.3 [required: any]
  │  └─ dependencies of r-rlang displayed above
  ├─ r-tensorflow 2.16.0 [required: >2.7.0]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-config 0.3.2 [required: any]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  └─ r-yaml 2.3.8 [required: >=2.1.13]
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │        └─ dependencies of r-base displayed above
  │  ├─ r-processx 3.8.4 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-ps 1.7.6 [required: >=1.2.0]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  └─ r-r6 2.5.1 [required: any]
  │  │     └─ dependencies of r-r6 displayed above
  │  ├─ r-reticulate 1.40.0 [required: >=1.24]
  │  │  └─ dependencies of r-reticulate displayed above
  │  ├─ r-rstudioapi 0.16.0 [required: >=0.7]
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-tfautograph 0.3.2 [required: >=0.3.1]
  │  │  ├─ r-backports 1.4.1 [required: any]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  └─ r-reticulate 1.40.0 [required: any]
  │  │     └─ dependencies of r-reticulate displayed above
  │  ├─ r-tfruns 1.5.3 [required: >=1.0]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-base64enc 0.1_3 [required: any]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-config 0.3.2 [required: any]
  │  │  │  └─ dependencies of r-config displayed above
  │  │  ├─ r-jsonlite 1.8.8 [required: >=1.2]
  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  │  └─ dependencies of r-magrittr displayed above
  │  │  ├─ r-reticulate 1.40.0 [required: any]
  │  │  │  └─ dependencies of r-reticulate displayed above
  │  │  ├─ r-rlang 1.1.3 [required: any]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-rstudioapi 0.16.0 [required: >=0.7]
  │  │  │  └─ dependencies of r-rstudioapi displayed above
  │  │  ├─ r-tidyselect 1.2.1 [required: any]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-cli 3.6.2 [required: >=3.3.0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  ├─ r-glue 1.7.0 [required: >=1.3.0]
  │  │  │  │  └─ dependencies of r-glue displayed above
  │  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  ├─ r-cli 3.6.2 [required: >=3.4.0]
  │  │  │  │  │  └─ dependencies of r-cli displayed above
  │  │  │  │  ├─ r-glue 1.7.0 [required: any]
  │  │  │  │  │  └─ dependencies of r-glue displayed above
  │  │  │  │  └─ r-rlang 1.1.3 [required: >=1.0.6]
  │  │  │  │     └─ dependencies of r-rlang displayed above
  │  │  │  ├─ r-rlang 1.1.3 [required: >=1.0.4]
  │  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  │  ├─ r-vctrs 0.6.5 [required: >=0.5.2]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  ├─ r-cli 3.6.2 [required: >=3.4.0]
  │  │  │  │  │  └─ dependencies of r-cli displayed above
  │  │  │  │  ├─ r-glue 1.7.0 [required: any]
  │  │  │  │  │  └─ dependencies of r-glue displayed above
  │  │  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  │  │  └─ r-rlang 1.1.3 [required: >=1.0.6]
  │  │  │  │     └─ dependencies of r-rlang displayed above
  │  │  │  └─ r-withr 3.0.0 [required: any]
  │  │  │     └─ dependencies of r-withr displayed above
  │  │  ├─ r-whisker 0.4.1 [required: any]
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  └─ r-yaml 2.3.8 [required: any]
  │  │     └─ dependencies of r-yaml displayed above
  │  └─ r-yaml 2.3.8 [required: any]
  │     └─ dependencies of r-yaml displayed above
  ├─ r-tfruns 1.5.3 [required: >=1.0]
  │  └─ dependencies of r-tfruns displayed above
  └─ r-zeallot 0.1.0 [required: any]
     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
        └─ dependencies of r-base displayed above
r-spatialreg==1.3_6
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  └─ dependencies of libblas displayed above
  ├─ libgcc 14.2.0 [required: >=13]
  │  └─ dependencies of libgcc displayed above
  ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
  │  └─ dependencies of liblapack displayed above
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-boot 1.3_31 [required: any]
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-coda 0.19_4.1 [required: any]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-lattice 0.22_6 [required: any]
  │     └─ dependencies of r-lattice displayed above
  ├─ r-learnbayes 2.15.1 [required: any]
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-mass 7.3_60 [required: any]
  │  └─ dependencies of r-mass displayed above
  ├─ r-matrix 1.6_5 [required: any]
  │  └─ dependencies of r-matrix displayed above
  ├─ r-multcomp 1.4_28 [required: any]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-codetools 0.2_20 [required: any]
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-mvtnorm 1.3_3 [required: >=1.0_10]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  └─ dependencies of libblas displayed above
  │  │  ├─ libgcc 14.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libgfortran 14.2.0 [required: any]
  │  │  │  └─ dependencies of libgfortran displayed above
  │  │  ├─ libgfortran5 14.2.0 [required: >=13.3.0]
  │  │  │  └─ dependencies of libgfortran5 displayed above
  │  │  ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  └─ dependencies of liblapack displayed above
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-sandwich 3.1_1 [required: >=2.3_0]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  └─ r-zoo 1.8_12 [required: any]
  │  │     └─ dependencies of r-zoo displayed above
  │  ├─ r-survival 3.6_4 [required: >=2.39_4]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  └─ r-matrix 1.6_5 [required: any]
  │  │     └─ dependencies of r-matrix displayed above
  │  └─ r-th.data 1.1_3 [required: >=1.0_2]
  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     ├─ r-mass 7.3_60 [required: any]
  │     │  └─ dependencies of r-mass displayed above
  │     └─ r-survival 3.6_4 [required: any]
  │        └─ dependencies of r-survival displayed above
  ├─ r-nlme 3.1_164 [required: any]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libgfortran-ng 14.2.0 [required: any]
  │  │  └─ dependencies of libgfortran-ng displayed above
  │  ├─ libgfortran5 14.2.0 [required: >=12.3.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-lattice 0.22_6 [required: any]
  │     └─ dependencies of r-lattice displayed above
  ├─ r-sf 1.0_16 [required: any]
  │  └─ dependencies of r-sf displayed above
  ├─ r-spdata 2.3.4 [required: >=2.3.1]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-sp 2.2_0 [required: any]
  │     └─ dependencies of r-sp displayed above
  └─ r-spdep 1.3_10 [required: >=1.3_1]
     ├─ __glibc [required: >=2.17,<3.0.a0]
     ├─ libgcc 14.2.0 [required: >=13]
     │  └─ dependencies of libgcc displayed above
     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
     │  └─ dependencies of r-base displayed above
     ├─ r-boot 1.3_31 [required: >=1.3_1]
     │  └─ dependencies of r-boot displayed above
     ├─ r-deldir 2.0_4 [required: any]
     │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  └─ dependencies of libgcc-ng displayed above
     │  ├─ libgfortran-ng 14.2.0 [required: any]
     │  │  └─ dependencies of libgfortran-ng displayed above
     │  ├─ libgfortran5 14.2.0 [required: >=12.3.0]
     │  │  └─ dependencies of libgfortran5 displayed above
     │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
     │     └─ dependencies of r-base displayed above
     ├─ r-e1071 1.7_14 [required: any]
     │  └─ dependencies of r-e1071 displayed above
     ├─ r-s2 1.1.7 [required: any]
     │  └─ dependencies of r-s2 displayed above
     ├─ r-sf 1.0_16 [required: any]
     │  └─ dependencies of r-sf displayed above
     ├─ r-sp 2.2_0 [required: >=1.0]
     │  └─ dependencies of r-sp displayed above
     ├─ r-spdata 2.3.4 [required: >=2.3.1]
     │  └─ dependencies of r-spdata displayed above
     └─ r-units 0.8_5 [required: any]
        └─ dependencies of r-units displayed above
r-nloptr==2.1.1
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ libgcc 14.2.0 [required: >=13]
  │  └─ dependencies of libgcc displayed above
  ├─ libgfortran 14.2.0 [required: any]
  │  └─ dependencies of libgfortran displayed above
  ├─ libgfortran5 14.2.0 [required: >=13.3.0]
  │  └─ dependencies of libgfortran5 displayed above
  ├─ libstdcxx 14.2.0 [required: >=13]
  │  └─ dependencies of libstdcxx displayed above
  ├─ nlopt 2.8.0 [required: >=2.8.0,<2.9.0a0]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 14.2.0 [required: >=13]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 14.2.0 [required: >=13]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ numpy 2.2.3 [required: >=1.19,<3]
  │  │  └─ dependencies of numpy displayed above
  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
     └─ dependencies of r-base displayed above
r-caret==6.0_94
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-e1071 1.7_14 [required: any]
  │  └─ dependencies of r-e1071 displayed above
  ├─ r-foreach 1.5.2 [required: any]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-codetools 0.2_20 [required: any]
  │  │  └─ dependencies of r-codetools displayed above
  │  └─ r-iterators 1.0.14 [required: any]
  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │        └─ dependencies of r-base displayed above
  ├─ r-ggplot2 3.5.1 [required: any]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.2 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-glue 1.7.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-gtable 0.3.5 [required: >=0.1.1]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.2 [required: any]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-glue 1.7.0 [required: any]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  └─ r-rlang 1.1.3 [required: any]
  │  │     └─ dependencies of r-rlang displayed above
  │  ├─ r-isoband 0.2.7 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.1]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-mass 7.3_60 [required: any]
  │  │  └─ dependencies of r-mass displayed above
  │  ├─ r-mgcv 1.9_1 [required: any]
  │  │  ├─ _openmp_mutex 4.5 [required: >=4.5]
  │  │  │  └─ dependencies of _openmp_mutex displayed above
  │  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  └─ dependencies of libblas displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  └─ dependencies of liblapack displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-matrix 1.6_5 [required: any]
  │  │  │  └─ dependencies of r-matrix displayed above
  │  │  └─ r-nlme 3.1_164 [required: >=3.1_64]
  │  │     └─ dependencies of r-nlme displayed above
  │  ├─ r-rlang 1.1.3 [required: >=1.0.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-scales 1.3.0 [required: >=1.2.0]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-farver 2.1.2 [required: >=2.0.0]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-labeling 0.4.3 [required: any]
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-munsell 0.5.1 [required: >=0.5]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-colorspace 2.1_0 [required: any]
  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │        └─ dependencies of r-base displayed above
  │  │  ├─ r-r6 2.5.1 [required: any]
  │  │  │  └─ dependencies of r-r6 displayed above
  │  │  ├─ r-rcolorbrewer 1.1_3 [required: any]
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  └─ r-viridislite 0.4.2 [required: any]
  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │        └─ dependencies of r-base displayed above
  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-fansi 1.0.6 [required: >=0.4.0]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.0]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  │  └─ dependencies of r-magrittr displayed above
  │  │  ├─ r-pillar 1.9.0 [required: >=1.8.1]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-cli 3.6.2 [required: any]
  │  │  │  │  └─ dependencies of r-cli displayed above
  │  │  │  ├─ r-crayon 1.5.2 [required: >=1.3.4]
  │  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  │  │  └─ dependencies of r-ellipsis displayed above
  │  │  │  ├─ r-fansi 1.0.6 [required: any]
  │  │  │  │  └─ dependencies of r-fansi displayed above
  │  │  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  │  ├─ r-rlang 1.1.3 [required: >=0.3.0]
  │  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  │  ├─ r-utf8 1.2.4 [required: >=1.1.0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  └─ r-vctrs 0.6.5 [required: >=0.2.0]
  │  │  │     └─ dependencies of r-vctrs displayed above
  │  │  ├─ r-pkgconfig 2.0.3 [required: any]
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-rlang 1.1.3 [required: >=1.0.2]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.4.2]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-vctrs 0.6.5 [required: >=0.5.0]
  │  │  └─ dependencies of r-vctrs displayed above
  │  └─ r-withr 3.0.0 [required: >=2.5.0]
  │     └─ dependencies of r-withr displayed above
  ├─ r-lattice 0.22_6 [required: >=0.20]
  │  └─ dependencies of r-lattice displayed above
  ├─ r-modelmetrics 1.2.2.2 [required: >=1.2.2.2]
  │  ├─ _openmp_mutex 4.5 [required: >=4.5]
  │  │  └─ dependencies of _openmp_mutex displayed above
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-data.table 1.15.2 [required: any]
  │  │  ├─ _openmp_mutex 4.5 [required: >=4.5]
  │  │  │  └─ dependencies of _openmp_mutex displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  └─ dependencies of libzlib displayed above
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  └─ r-rcpp 1.0.12 [required: any]
  │     └─ dependencies of r-rcpp displayed above
  ├─ r-nlme 3.1_164 [required: any]
  │  └─ dependencies of r-nlme displayed above
  ├─ r-plyr 1.8.9 [required: any]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-rcpp 1.0.12 [required: >=0.11.0]
  │     └─ dependencies of r-rcpp displayed above
  ├─ r-proc 1.18.5 [required: any]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-plyr 1.8.9 [required: any]
  │  │  └─ dependencies of r-plyr displayed above
  │  └─ r-rcpp 1.0.12 [required: >=0.11.1]
  │     └─ dependencies of r-rcpp displayed above
  ├─ r-recipes 1.0.10 [required: >=0.1.10]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.2 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-clock 0.7.0 [required: >=0.6.1]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cpp11 0.4.7 [required: >=0.4.0]
  │  │  │  └─ dependencies of r-cpp11 displayed above
  │  │  ├─ r-ellipsis 0.3.2 [required: >=0.3.1]
  │  │  │  └─ dependencies of r-ellipsis displayed above
  │  │  ├─ r-rlang 1.1.3 [required: >=0.4.10]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-tzdb 0.4.0 [required: >=0.2.0]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-cpp11 0.4.7 [required: >=0.4.2]
  │  │  │     └─ dependencies of r-cpp11 displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.3.7]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-dplyr 1.1.4 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  │  └─ dependencies of r-ellipsis displayed above
  │  │  ├─ r-generics 0.1.3 [required: any]
  │  │  │  └─ dependencies of r-generics displayed above
  │  │  ├─ r-glue 1.7.0 [required: >=1.3.2]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.0]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-magrittr 2.0.3 [required: >=1.5]
  │  │  │  └─ dependencies of r-magrittr displayed above
  │  │  ├─ r-pillar 1.9.0 [required: >=1.5.1]
  │  │  │  └─ dependencies of r-pillar displayed above
  │  │  ├─ r-r6 2.5.1 [required: any]
  │  │  │  └─ dependencies of r-r6 displayed above
  │  │  ├─ r-rlang 1.1.3 [required: >=0.4.10]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-tibble 3.2.1 [required: >=2.1.3]
  │  │  │  └─ dependencies of r-tibble displayed above
  │  │  ├─ r-tidyselect 1.2.1 [required: >=1.1.0]
  │  │  │  └─ dependencies of r-tidyselect displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.3.5]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  └─ dependencies of r-ellipsis displayed above
  │  ├─ r-generics 0.1.3 [required: >=0.1.2]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-glue 1.7.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-gower 1.0.1 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-hardhat 1.3.1 [required: >=1.2.0]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-glue 1.7.0 [required: any]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-rlang 1.1.3 [required: >=0.4.1]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  │  └─ dependencies of r-tibble displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.2.0]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-ipred 0.9_14 [required: >=0.9_12]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-class 7.3_22 [required: any]
  │  │  │  └─ dependencies of r-class displayed above
  │  │  ├─ r-mass 7.3_60 [required: any]
  │  │  │  └─ dependencies of r-mass displayed above
  │  │  ├─ r-nnet 7.3_19 [required: any]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-mass 7.3_60 [required: any]
  │  │  │     └─ dependencies of r-mass displayed above
  │  │  ├─ r-prodlim 2023.08.28 [required: any]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-data.table 1.15.2 [required: any]
  │  │  │  │  └─ dependencies of r-data.table displayed above
  │  │  │  ├─ r-diagram 1.6.5 [required: any]
  │  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  └─ r-shape 1.4.6.1 [required: any]
  │  │  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │        └─ dependencies of r-base displayed above
  │  │  │  ├─ r-kernsmooth 2.23_24 [required: any]
  │  │  │  │  └─ dependencies of r-kernsmooth displayed above
  │  │  │  ├─ r-lava 1.7.3 [required: any]
  │  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  ├─ r-future.apply 1.11.2 [required: any]
  │  │  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  │  ├─ r-future 1.33.2 [required: >=1.13.0]
  │  │  │  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  │  │  ├─ r-digest 0.6.35 [required: any]
  │  │  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  │  │  │  ├─ r-globals 0.16.3 [required: >=0.16.1]
  │  │  │  │  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  │  │  │  └─ r-codetools 0.2_20 [required: any]
  │  │  │  │  │  │  │     └─ dependencies of r-codetools displayed above
  │  │  │  │  │  │  ├─ r-listenv 0.9.1 [required: >=0.8.0]
  │  │  │  │  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  │  │  │  └─ r-parallelly 1.37.1 [required: >=1.34.0]
  │  │  │  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  │        └─ dependencies of r-base displayed above
  │  │  │  │  │  └─ r-globals 0.16.3 [required: >=0.12.4]
  │  │  │  │  │     └─ dependencies of r-globals displayed above
  │  │  │  │  ├─ r-numderiv 2016.8_1.1 [required: any]
  │  │  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  │  ├─ r-progressr 0.14.0 [required: any]
  │  │  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  │  └─ r-digest 0.6.35 [required: any]
  │  │  │  │  │     └─ dependencies of r-digest displayed above
  │  │  │  │  ├─ r-squarem 2021.1 [required: any]
  │  │  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  │  └─ r-survival 3.6_4 [required: any]
  │  │  │  │     └─ dependencies of r-survival displayed above
  │  │  │  ├─ r-rcpp 1.0.12 [required: >=0.11.5]
  │  │  │  │  └─ dependencies of r-rcpp displayed above
  │  │  │  └─ r-survival 3.6_4 [required: any]
  │  │  │     └─ dependencies of r-survival displayed above
  │  │  ├─ r-rpart 4.1.23 [required: >=3.1_8]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  └─ r-survival 3.6_4 [required: any]
  │  │     └─ dependencies of r-survival displayed above
  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-lubridate 1.9.3 [required: >=1.8.0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-generics 0.1.3 [required: any]
  │  │  │  └─ dependencies of r-generics displayed above
  │  │  └─ r-timechange 0.3.0 [required: >=0.1.1]
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     │  └─ dependencies of r-base displayed above
  │  │     └─ r-cpp11 0.4.7 [required: >=0.2.7]
  │  │        └─ dependencies of r-cpp11 displayed above
  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-matrix 1.6_5 [required: any]
  │  │  └─ dependencies of r-matrix displayed above
  │  ├─ r-purrr 1.0.2 [required: >=0.2.3]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.2 [required: >=3.4]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-magrittr 2.0.3 [required: >=1.5]
  │  │  │  └─ dependencies of r-magrittr displayed above
  │  │  ├─ r-rlang 1.1.3 [required: >=0.4.10]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.5]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-rlang 1.1.3 [required: >=1.0.3]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyr 1.3.1 [required: >=1.0.0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.2 [required: >=3.4.1]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-dplyr 1.1.4 [required: >=1.0.10]
  │  │  │  └─ dependencies of r-dplyr displayed above
  │  │  ├─ r-glue 1.7.0 [required: any]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  │  └─ dependencies of r-magrittr displayed above
  │  │  ├─ r-purrr 1.0.2 [required: >=1.0.1]
  │  │  │  └─ dependencies of r-purrr displayed above
  │  │  ├─ r-rlang 1.1.3 [required: >=1.0.4]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-stringr 1.5.1 [required: >=1.5.0]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-cli 3.6.2 [required: any]
  │  │  │  │  └─ dependencies of r-cli displayed above
  │  │  │  ├─ r-glue 1.7.0 [required: >=1.6.1]
  │  │  │  │  └─ dependencies of r-glue displayed above
  │  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  │  │  └─ dependencies of r-magrittr displayed above
  │  │  │  ├─ r-rlang 1.1.3 [required: >=1.0.0]
  │  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  │  ├─ r-stringi 1.8.4 [required: >=1.5.3]
  │  │  │  │  ├─ icu 73.2 [required: >=73.2,<74.0a0]
  │  │  │  │  │  └─ dependencies of icu displayed above
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  └─ r-vctrs 0.6.5 [required: any]
  │  │  │     └─ dependencies of r-vctrs displayed above
  │  │  ├─ r-tibble 3.2.1 [required: >=2.1.1]
  │  │  │  └─ dependencies of r-tibble displayed above
  │  │  ├─ r-tidyselect 1.2.1 [required: >=1.2.0]
  │  │  │  └─ dependencies of r-tidyselect displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.5.2]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-tidyselect 1.2.1 [required: >=1.2.0]
  │  │  └─ dependencies of r-tidyselect displayed above
  │  ├─ r-timedate 4032.109 [required: any]
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-vctrs 0.6.5 [required: >=0.5.0]
  │  │  └─ dependencies of r-vctrs displayed above
  │  └─ r-withr 3.0.0 [required: any]
  │     └─ dependencies of r-withr displayed above
  ├─ r-reshape2 1.4.4 [required: any]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-plyr 1.8.9 [required: >=1.8.1]
  │  │  └─ dependencies of r-plyr displayed above
  │  ├─ r-rcpp 1.0.12 [required: any]
  │  │  └─ dependencies of r-rcpp displayed above
  │  └─ r-stringr 1.5.1 [required: any]
  │     └─ dependencies of r-stringr displayed above
  └─ r-withr 3.0.0 [required: >=2.0.0]
     └─ dependencies of r-withr displayed above
r-tidymodels==1.2.0
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-broom 1.0.6 [required: >=1.0.0]
  │  ├─ r-backports 1.4.1 [required: any]
  │  │  └─ dependencies of r-backports displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.0.0]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  └─ dependencies of r-ellipsis displayed above
  │  ├─ r-generics 0.1.3 [required: >=0.0.2]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-ggplot2 3.5.1 [required: any]
  │  │  └─ dependencies of r-ggplot2 displayed above
  │  ├─ r-glue 1.7.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-purrr 1.0.2 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.3 [required: any]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-stringr 1.5.1 [required: any]
  │  │  └─ dependencies of r-stringr displayed above
  │  ├─ r-tibble 3.2.1 [required: >=3.0.0]
  │  │  └─ dependencies of r-tibble displayed above
  │  └─ r-tidyr 1.3.1 [required: >=1.0.0]
  │     └─ dependencies of r-tidyr displayed above
  ├─ r-cli 3.6.2 [required: >=3.3.0]
  │  └─ dependencies of r-cli displayed above
  ├─ r-conflicted 1.2.0 [required: >=1.1.0]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.2 [required: >=3.4.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-memoise 2.0.1 [required: any]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cachem 1.1.0 [required: any]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-fastmap 1.2.0 [required: any]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  └─ r-rlang 1.1.3 [required: any]
  │  │  │     └─ dependencies of r-rlang displayed above
  │  │  └─ r-rlang 1.1.3 [required: >=0.4.10]
  │  │     └─ dependencies of r-rlang displayed above
  │  └─ r-rlang 1.1.3 [required: >=1.0.0]
  │     └─ dependencies of r-rlang displayed above
  ├─ r-dials 1.2.1 [required: >=1.0.0]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.2 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-dicedesign 1.10 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=0.8.5]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-glue 1.7.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-hardhat 1.3.1 [required: >=1.1.0]
  │  │  └─ dependencies of r-hardhat displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-pillar 1.9.0 [required: any]
  │  │  └─ dependencies of r-pillar displayed above
  │  ├─ r-purrr 1.0.2 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.3 [required: >=1.0.1]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-scales 1.3.0 [required: any]
  │  │  └─ dependencies of r-scales displayed above
  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-vctrs 0.6.5 [required: >=0.3.8]
  │  │  └─ dependencies of r-vctrs displayed above
  │  └─ r-withr 3.0.0 [required: any]
  │     └─ dependencies of r-withr displayed above
  ├─ r-dplyr 1.1.4 [required: >=1.0.9]
  │  └─ dependencies of r-dplyr displayed above
  ├─ r-ggplot2 3.5.1 [required: >=3.3.6]
  │  └─ dependencies of r-ggplot2 displayed above
  ├─ r-hardhat 1.3.1 [required: >=1.2.0]
  │  └─ dependencies of r-hardhat displayed above
  ├─ r-infer 1.0.7 [required: >=1.0.2]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-broom 1.0.6 [required: any]
  │  │  └─ dependencies of r-broom displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=0.7.0]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-generics 0.1.3 [required: any]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-ggplot2 3.5.1 [required: any]
  │  │  └─ dependencies of r-ggplot2 displayed above
  │  ├─ r-glue 1.7.0 [required: >=1.3.0]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-patchwork 1.2.0 [required: any]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-ggplot2 3.5.1 [required: >=3.0.0]
  │  │  │  └─ dependencies of r-ggplot2 displayed above
  │  │  └─ r-gtable 0.3.5 [required: any]
  │  │     └─ dependencies of r-gtable displayed above
  │  ├─ r-purrr 1.0.2 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.3 [required: >=0.2.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  └─ r-tidyr 1.3.1 [required: any]
  │     └─ dependencies of r-tidyr displayed above
  ├─ r-modeldata 1.3.0 [required: >=1.0.0]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-dplyr 1.1.4 [required: any]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-mass 7.3_60 [required: any]
  │  │  └─ dependencies of r-mass displayed above
  │  ├─ r-purrr 1.0.2 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.3 [required: any]
  │  │  └─ dependencies of r-rlang displayed above
  │  └─ r-tibble 3.2.1 [required: any]
  │     └─ dependencies of r-tibble displayed above
  ├─ r-parsnip 1.2.1 [required: >=1.0.0]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.2 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.1.0]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-generics 0.1.3 [required: >=0.1.2]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-ggplot2 3.5.1 [required: any]
  │  │  └─ dependencies of r-ggplot2 displayed above
  │  ├─ r-globals 0.16.3 [required: any]
  │  │  └─ dependencies of r-globals displayed above
  │  ├─ r-glue 1.7.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-hardhat 1.3.1 [required: >=1.1.0]
  │  │  └─ dependencies of r-hardhat displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-pillar 1.9.0 [required: any]
  │  │  └─ dependencies of r-pillar displayed above
  │  ├─ r-prettyunits 1.2.0 [required: any]
  │  │  ├─ r-assertthat 0.2.1 [required: any]
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  └─ r-magrittr 2.0.3 [required: any]
  │  │     └─ dependencies of r-magrittr displayed above
  │  ├─ r-purrr 1.0.2 [required: >=1.0.0]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.3 [required: >=0.3.1]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.2.1 [required: >=2.1.1]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyr 1.3.1 [required: >=1.3.0]
  │  │  └─ dependencies of r-tidyr displayed above
  │  ├─ r-vctrs 0.6.5 [required: >=0.6.0]
  │  │  └─ dependencies of r-vctrs displayed above
  │  └─ r-withr 3.0.0 [required: any]
  │     └─ dependencies of r-withr displayed above
  ├─ r-purrr 1.0.2 [required: >=0.3.4]
  │  └─ dependencies of r-purrr displayed above
  ├─ r-recipes 1.0.10 [required: >=1.0.1]
  │  └─ dependencies of r-recipes displayed above
  ├─ r-rlang 1.1.3 [required: >=1.0.3]
  │  └─ dependencies of r-rlang displayed above
  ├─ r-rsample 1.2.1 [required: >=1.0.0]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.0.0]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-furrr 0.3.1 [required: any]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  │  └─ dependencies of r-ellipsis displayed above
  │  │  ├─ r-future 1.33.2 [required: >=1.19.1]
  │  │  │  └─ dependencies of r-future displayed above
  │  │  ├─ r-globals 0.16.3 [required: >=0.13.1]
  │  │  │  └─ dependencies of r-globals displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=0.2.0]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-purrr 1.0.2 [required: >=0.3.0]
  │  │  │  └─ dependencies of r-purrr displayed above
  │  │  ├─ r-rlang 1.1.3 [required: >=0.3.0]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.3.2]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-generics 0.1.3 [required: any]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-glue 1.7.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-pillar 1.9.0 [required: any]
  │  │  └─ dependencies of r-pillar displayed above
  │  ├─ r-purrr 1.0.2 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.3 [required: >=0.4.10]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-slider 0.3.1 [required: >=0.1.5]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.2 [required: >=3.4.1]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-rlang 1.1.3 [required: >=1.0.6]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-vctrs 0.6.5 [required: >=0.5.0]
  │  │  │  └─ dependencies of r-vctrs displayed above
  │  │  └─ r-warp 0.2.1 [required: any]
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │        └─ dependencies of r-base displayed above
  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyr 1.3.1 [required: any]
  │  │  └─ dependencies of r-tidyr displayed above
  │  ├─ r-tidyselect 1.2.1 [required: any]
  │  │  └─ dependencies of r-tidyselect displayed above
  │  └─ r-vctrs 0.6.5 [required: >=0.5.0]
  │     └─ dependencies of r-vctrs displayed above
  ├─ r-rstudioapi 0.16.0 [required: >=0.13]
  │  └─ dependencies of r-rstudioapi displayed above
  ├─ r-tibble 3.2.1 [required: >=3.1.7]
  │  └─ dependencies of r-tibble displayed above
  ├─ r-tidyr 1.3.1 [required: >=1.2.0]
  │  └─ dependencies of r-tidyr displayed above
  ├─ r-tune 1.2.1 [required: >=1.0.0]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.2 [required: >=3.3.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-dials 1.2.1 [required: >=1.0.0]
  │  │  └─ dependencies of r-dials displayed above
  │  ├─ r-dofuture 1.0.1 [required: >=1.0.0]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-foreach 1.5.2 [required: >=1.5.0]
  │  │  │  └─ dependencies of r-foreach displayed above
  │  │  ├─ r-future 1.33.2 [required: >=1.32.0]
  │  │  │  └─ dependencies of r-future displayed above
  │  │  ├─ r-future.apply 1.11.2 [required: any]
  │  │  │  └─ dependencies of r-future.apply displayed above
  │  │  ├─ r-globals 0.16.3 [required: any]
  │  │  │  └─ dependencies of r-globals displayed above
  │  │  └─ r-iterators 1.0.14 [required: any]
  │  │     └─ dependencies of r-iterators displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.1.0]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-foreach 1.5.2 [required: any]
  │  │  └─ dependencies of r-foreach displayed above
  │  ├─ r-future 1.33.2 [required: >=1.33.0]
  │  │  └─ dependencies of r-future displayed above
  │  ├─ r-generics 0.1.3 [required: >=0.1.2]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-ggplot2 3.5.1 [required: any]
  │  │  └─ dependencies of r-ggplot2 displayed above
  │  ├─ r-glue 1.7.0 [required: >=1.6.2]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-gpfit 1.0_8 [required: any]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-lattice 0.22_6 [required: >=0.18_8]
  │  │  │  └─ dependencies of r-lattice displayed above
  │  │  └─ r-lhs 1.1.6 [required: >=0.5]
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     │  └─ dependencies of r-base displayed above
  │  │     └─ r-rcpp 1.0.12 [required: any]
  │  │        └─ dependencies of r-rcpp displayed above
  │  ├─ r-hardhat 1.3.1 [required: >=1.2.0]
  │  │  └─ dependencies of r-hardhat displayed above
  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.0]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-parsnip 1.2.1 [required: >=1.2.0]
  │  │  └─ dependencies of r-parsnip displayed above
  │  ├─ r-purrr 1.0.2 [required: >=1.0.0]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-recipes 1.0.10 [required: >=1.0.4]
  │  │  └─ dependencies of r-recipes displayed above
  │  ├─ r-rlang 1.1.3 [required: >=1.1.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-rsample 1.2.1 [required: >=1.2.0]
  │  │  └─ dependencies of r-rsample displayed above
  │  ├─ r-tibble 3.2.1 [required: >=3.1.0]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyr 1.3.1 [required: >=1.2.0]
  │  │  └─ dependencies of r-tidyr displayed above
  │  ├─ r-tidyselect 1.2.1 [required: >=1.1.2]
  │  │  └─ dependencies of r-tidyselect displayed above
  │  ├─ r-vctrs 0.6.5 [required: >=0.6.1]
  │  │  └─ dependencies of r-vctrs displayed above
  │  ├─ r-withr 3.0.0 [required: any]
  │  │  └─ dependencies of r-withr displayed above
  │  ├─ r-workflows 1.1.4 [required: >=1.1.4]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.2 [required: >=3.3.0]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-generics 0.1.3 [required: >=0.1.2]
  │  │  │  └─ dependencies of r-generics displayed above
  │  │  ├─ r-glue 1.7.0 [required: >=1.6.2]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-hardhat 1.3.1 [required: >=1.2.0]
  │  │  │  └─ dependencies of r-hardhat displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-modelenv 0.1.1 [required: >=0.1.0]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-glue 1.7.0 [required: any]
  │  │  │  │  └─ dependencies of r-glue displayed above
  │  │  │  ├─ r-rlang 1.1.3 [required: any]
  │  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  │  │  └─ dependencies of r-tibble displayed above
  │  │  │  └─ r-vctrs 0.6.5 [required: any]
  │  │  │     └─ dependencies of r-vctrs displayed above
  │  │  ├─ r-parsnip 1.2.1 [required: >=1.0.3]
  │  │  │  └─ dependencies of r-parsnip displayed above
  │  │  ├─ r-rlang 1.1.3 [required: >=1.0.3]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-tidyselect 1.2.1 [required: >=1.2.0]
  │  │  │  └─ dependencies of r-tidyselect displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.4.1]
  │  │     └─ dependencies of r-vctrs displayed above
  │  └─ r-yardstick 1.3.1 [required: >=1.3.0]
  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  └─ dependencies of libgcc-ng displayed above
  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     ├─ r-dplyr 1.1.4 [required: >=1.0.9]
  │     │  └─ dependencies of r-dplyr displayed above
  │     ├─ r-generics 0.1.3 [required: >=0.1.2]
  │     │  └─ dependencies of r-generics displayed above
  │     ├─ r-hardhat 1.3.1 [required: >=1.0.0]
  │     │  └─ dependencies of r-hardhat displayed above
  │     ├─ r-rlang 1.1.3 [required: >=1.0.2]
  │     │  └─ dependencies of r-rlang displayed above
  │     ├─ r-tidyselect 1.2.1 [required: >=1.1.2]
  │     │  └─ dependencies of r-tidyselect displayed above
  │     └─ r-vctrs 0.6.5 [required: >=0.4.1]
  │        └─ dependencies of r-vctrs displayed above
  ├─ r-workflows 1.1.4 [required: >=1.0.0]
  │  └─ dependencies of r-workflows displayed above
  ├─ r-workflowsets 1.1.0 [required: >=1.0.0]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.2 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.0.0]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-generics 0.1.3 [required: >=0.1.2]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-ggplot2 3.5.1 [required: any]
  │  │  └─ dependencies of r-ggplot2 displayed above
  │  ├─ r-glue 1.7.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-hardhat 1.3.1 [required: >=1.2.0]
  │  │  └─ dependencies of r-hardhat displayed above
  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.0]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-parsnip 1.2.1 [required: >=1.2.0]
  │  │  └─ dependencies of r-parsnip displayed above
  │  ├─ r-pillar 1.9.0 [required: >=1.7.0]
  │  │  └─ dependencies of r-pillar displayed above
  │  ├─ r-prettyunits 1.2.0 [required: any]
  │  │  └─ dependencies of r-prettyunits displayed above
  │  ├─ r-purrr 1.0.2 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.3 [required: >=1.1.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-rsample 1.2.1 [required: >=0.0.9]
  │  │  └─ dependencies of r-rsample displayed above
  │  ├─ r-tibble 3.2.1 [required: >=3.1.0]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyr 1.3.1 [required: any]
  │  │  └─ dependencies of r-tidyr displayed above
  │  ├─ r-tune 1.2.1 [required: >=1.2.0]
  │  │  └─ dependencies of r-tune displayed above
  │  ├─ r-vctrs 0.6.5 [required: any]
  │  │  └─ dependencies of r-vctrs displayed above
  │  ├─ r-withr 3.0.0 [required: any]
  │  │  └─ dependencies of r-withr displayed above
  │  └─ r-workflows 1.1.4 [required: >=1.1.4]
  │     └─ dependencies of r-workflows displayed above
  └─ r-yardstick 1.3.1 [required: >=1.0.0]
     └─ dependencies of r-yardstick displayed above
r-randomforest==4.7_1.1
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libgfortran-ng 14.2.0 [required: any]
  │  └─ dependencies of libgfortran-ng displayed above
  ├─ libgfortran5 14.2.0 [required: >=12.3.0]
  │  └─ dependencies of libgfortran5 displayed above
  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
     └─ dependencies of r-base displayed above
r-irkernel==1.3.2
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-crayon 1.5.2 [required: any]
  │  └─ dependencies of r-crayon displayed above
  ├─ r-digest 0.6.35 [required: any]
  │  └─ dependencies of r-digest displayed above
  ├─ r-evaluate 0.23 [required: >=0.10]
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-irdisplay 1.1 [required: >=0.3.0.9999]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-repr 1.1.7 [required: any]
  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     ├─ r-base64enc 0.1_3 [required: any]
  │     │  └─ dependencies of r-base64enc displayed above
  │     ├─ r-htmltools 0.5.8.1 [required: any]
  │     │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  │  └─ dependencies of libgcc-ng displayed above
  │     │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │     │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  │  └─ dependencies of r-base displayed above
  │     │  ├─ r-base64enc 0.1_3 [required: any]
  │     │  │  └─ dependencies of r-base64enc displayed above
  │     │  ├─ r-digest 0.6.35 [required: any]
  │     │  │  └─ dependencies of r-digest displayed above
  │     │  ├─ r-ellipsis 0.3.2 [required: any]
  │     │  │  └─ dependencies of r-ellipsis displayed above
  │     │  ├─ r-fastmap 1.2.0 [required: >=1.1.0]
  │     │  │  └─ dependencies of r-fastmap displayed above
  │     │  └─ r-rlang 1.1.3 [required: >=0.4.10]
  │     │     └─ dependencies of r-rlang displayed above
  │     ├─ r-jsonlite 1.8.8 [required: any]
  │     │  └─ dependencies of r-jsonlite displayed above
  │     └─ r-pillar 1.9.0 [required: >=1.4.0]
  │        └─ dependencies of r-pillar displayed above
  ├─ r-jsonlite 1.8.8 [required: >=0.9.6]
  │  └─ dependencies of r-jsonlite displayed above
  ├─ r-pbdzmq 0.3_11 [required: >=0.2_1]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ zeromq 4.3.5 [required: >=4.3.5,<4.4.0a0]
  │     ├─ krb5 1.21.2 [required: >=1.21.2,<1.22.0a0]
  │     │  └─ dependencies of krb5 displayed above
  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  └─ dependencies of libgcc-ng displayed above
  │     ├─ libsodium 1.0.18 [required: >=1.0.18,<1.0.19.0a0]
  │     │  └─ libgcc-ng 14.2.0 [required: >=7.5.0]
  │     │     └─ dependencies of libgcc-ng displayed above
  │     └─ libstdcxx-ng 13.2.0 [required: >=12]
  ├─ r-repr 1.1.7 [required: >=0.4.99]
  │  └─ dependencies of r-repr displayed above
  └─ r-uuid 1.2_0 [required: any]
     ├─ libgcc-ng 14.2.0 [required: >=12]
     │  └─ dependencies of libgcc-ng displayed above
     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
        └─ dependencies of r-base displayed above
r-rcurl==1.98_1.14
  ├─ libcurl 8.8.0 [required: >=8.5.0,<9.0a0]
  │  └─ dependencies of libcurl displayed above
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  └─ r-bitops 1.0_7 [required: any]
     ├─ libgcc-ng 14.2.0 [required: >=12]
     │  └─ dependencies of libgcc-ng displayed above
     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
        └─ dependencies of r-base displayed above
r-hexbin==1.28.3
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libgfortran-ng 14.2.0 [required: any]
  │  └─ dependencies of libgfortran-ng displayed above
  ├─ libgfortran5 14.2.0 [required: >=12.3.0]
  │  └─ dependencies of libgfortran5 displayed above
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  └─ r-lattice 0.22_6 [required: any]
     └─ dependencies of r-lattice displayed above
r-nycflights13==1.0.2
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  └─ r-tibble 3.2.1 [required: any]
     └─ dependencies of r-tibble displayed above
r-tidyverse==2.0.0
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-broom 1.0.6 [required: >=1.0.3]
  │  └─ dependencies of r-broom displayed above
  ├─ r-cli 3.6.2 [required: >=3.6.0]
  │  └─ dependencies of r-cli displayed above
  ├─ r-conflicted 1.2.0 [required: >=1.2.0]
  │  └─ dependencies of r-conflicted displayed above
  ├─ r-dbplyr 2.5.0 [required: >=2.3.0]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-blob 1.2.4 [required: >=1.2.0]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-rlang 1.1.3 [required: any]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.2.1]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-cli 3.6.2 [required: >=3.6.1]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-dbi 1.2.2 [required: >=1.1.3]
  │  │  └─ dependencies of r-dbi displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.1.2]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-glue 1.7.0 [required: >=1.6.2]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-pillar 1.9.0 [required: >=1.9.0]
  │  │  └─ dependencies of r-pillar displayed above
  │  ├─ r-purrr 1.0.2 [required: >=1.0.1]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-r6 2.5.1 [required: >=2.2.2]
  │  │  └─ dependencies of r-r6 displayed above
  │  ├─ r-rlang 1.1.3 [required: >=1.1.1]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.2.1 [required: >=3.2.1]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyr 1.3.1 [required: >=1.3.0]
  │  │  └─ dependencies of r-tidyr displayed above
  │  ├─ r-tidyselect 1.2.1 [required: >=1.2.1]
  │  │  └─ dependencies of r-tidyselect displayed above
  │  ├─ r-vctrs 0.6.5 [required: >=0.6.3]
  │  │  └─ dependencies of r-vctrs displayed above
  │  └─ r-withr 3.0.0 [required: >=2.5.0]
  │     └─ dependencies of r-withr displayed above
  ├─ r-dplyr 1.1.4 [required: >=1.1.0]
  │  └─ dependencies of r-dplyr displayed above
  ├─ r-dtplyr 1.3.1 [required: >=1.2.2]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-crayon 1.5.2 [required: any]
  │  │  └─ dependencies of r-crayon displayed above
  │  ├─ r-data.table 1.15.2 [required: >=1.13.0]
  │  │  └─ dependencies of r-data.table displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.0.3]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  └─ dependencies of r-ellipsis displayed above
  │  ├─ r-glue 1.7.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-rlang 1.1.3 [required: any]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyselect 1.2.1 [required: any]
  │  │  └─ dependencies of r-tidyselect displayed above
  │  └─ r-vctrs 0.6.5 [required: any]
  │     └─ dependencies of r-vctrs displayed above
  ├─ r-forcats 1.0.0 [required: >=1.0.0]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.2 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  └─ dependencies of r-ellipsis displayed above
  │  ├─ r-glue 1.7.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-rlang 1.1.3 [required: >=1.0.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  └─ r-withr 3.0.0 [required: any]
  │     └─ dependencies of r-withr displayed above
  ├─ r-ggplot2 3.5.1 [required: >=3.4.1]
  │  └─ dependencies of r-ggplot2 displayed above
  ├─ r-googledrive 2.1.1 [required: >=2.0.0]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-curl 5.1.0 [required: >=2.8.1]
  │  │  ├─ libcurl 8.8.0 [required: >=8.3.0,<9.0a0]
  │  │  │  └─ dependencies of libcurl displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-gargle 1.5.2 [required: >=0.3.1]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.2 [required: >=3.0.0]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-fs 1.6.4 [required: >=1.3.1]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-glue 1.7.0 [required: >=1.3.0]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-httr 1.4.7 [required: >=1.4.0]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-curl 5.1.0 [required: >=0.9.1]
  │  │  │  │  └─ dependencies of r-curl displayed above
  │  │  │  ├─ r-jsonlite 1.8.8 [required: any]
  │  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  │  ├─ r-mime 0.12 [required: any]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  ├─ r-openssl 2.2.0 [required: >=0.8]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  │  │  └─ dependencies of openssl displayed above
  │  │  │  │  ├─ r-askpass 1.2.0 [required: any]
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  │  └─ r-sys 3.4.2 [required: >=2.1]
  │  │  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │        └─ dependencies of r-base displayed above
  │  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  └─ r-r6 2.5.1 [required: any]
  │  │  │     └─ dependencies of r-r6 displayed above
  │  │  ├─ r-jsonlite 1.8.8 [required: any]
  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-openssl 2.2.0 [required: any]
  │  │  │  └─ dependencies of r-openssl displayed above
  │  │  ├─ r-rappdirs 0.3.3 [required: any]
  │  │  │  └─ dependencies of r-rappdirs displayed above
  │  │  ├─ r-rlang 1.1.3 [required: >=1.0.0]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-rstudioapi 0.16.0 [required: any]
  │  │  │  └─ dependencies of r-rstudioapi displayed above
  │  │  └─ r-withr 3.0.0 [required: any]
  │  │     └─ dependencies of r-withr displayed above
  │  ├─ r-glue 1.7.0 [required: >=1.2.0]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-httr 1.4.7 [required: any]
  │  │  └─ dependencies of r-httr displayed above
  │  ├─ r-jsonlite 1.8.8 [required: any]
  │  │  └─ dependencies of r-jsonlite displayed above
  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-purrr 1.0.2 [required: >=0.2.3]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.3 [required: >=0.3.1]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.2.1 [required: >=2.0.0]
  │  │  └─ dependencies of r-tibble displayed above
  │  └─ r-uuid 1.2_0 [required: any]
  │     └─ dependencies of r-uuid displayed above
  ├─ r-googlesheets4 1.1.1 [required: >=1.0.1]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cellranger 1.1.0 [required: any]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-rematch 2.0.0 [required: any]
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  └─ r-tibble 3.2.1 [required: any]
  │  │     └─ dependencies of r-tibble displayed above
  │  ├─ r-cli 3.6.2 [required: >=3.0.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-curl 5.1.0 [required: any]
  │  │  └─ dependencies of r-curl displayed above
  │  ├─ r-gargle 1.5.2 [required: >=1.2.0]
  │  │  └─ dependencies of r-gargle displayed above
  │  ├─ r-glue 1.7.0 [required: >=1.3.0]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-googledrive 2.1.1 [required: >=2.0.0]
  │  │  └─ dependencies of r-googledrive displayed above
  │  ├─ r-httr 1.4.7 [required: any]
  │  │  └─ dependencies of r-httr displayed above
  │  ├─ r-ids 1.0.1 [required: any]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-openssl 2.2.0 [required: any]
  │  │  │  └─ dependencies of r-openssl displayed above
  │  │  └─ r-uuid 1.2_0 [required: any]
  │  │     └─ dependencies of r-uuid displayed above
  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-purrr 1.0.2 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rematch2 2.1.2 [required: any]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  └─ r-tibble 3.2.1 [required: any]
  │  │     └─ dependencies of r-tibble displayed above
  │  ├─ r-rlang 1.1.3 [required: >=0.4.11]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.2.1 [required: >=2.1.1]
  │  │  └─ dependencies of r-tibble displayed above
  │  └─ r-vctrs 0.6.5 [required: >=0.2.3]
  │     └─ dependencies of r-vctrs displayed above
  ├─ r-haven 2.5.4 [required: >=2.5.1]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.2 [required: >=3.0.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-cpp11 0.4.7 [required: any]
  │  │  └─ dependencies of r-cpp11 displayed above
  │  ├─ r-forcats 1.0.0 [required: >=0.2.0]
  │  │  └─ dependencies of r-forcats displayed above
  │  ├─ r-hms 1.1.3 [required: any]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  │  └─ dependencies of r-ellipsis displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-pkgconfig 2.0.3 [required: any]
  │  │  │  └─ dependencies of r-pkgconfig displayed above
  │  │  ├─ r-rlang 1.1.3 [required: any]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.2.1]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-readr 2.1.5 [required: >=0.1.0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.2 [required: any]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-clipr 0.8.0 [required: any]
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-cpp11 0.4.7 [required: any]
  │  │  │  └─ dependencies of r-cpp11 displayed above
  │  │  ├─ r-crayon 1.5.2 [required: any]
  │  │  │  └─ dependencies of r-crayon displayed above
  │  │  ├─ r-hms 1.1.3 [required: >=0.4.1]
  │  │  │  └─ dependencies of r-hms displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=0.2.0]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-r6 2.5.1 [required: any]
  │  │  │  └─ dependencies of r-r6 displayed above
  │  │  ├─ r-rlang 1.1.3 [required: any]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  │  └─ dependencies of r-tibble displayed above
  │  │  ├─ r-tzdb 0.4.0 [required: >=0.1.1]
  │  │  │  └─ dependencies of r-tzdb displayed above
  │  │  └─ r-vroom 1.6.5 [required: >=1.5.4]
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     │  └─ dependencies of r-base displayed above
  │  │     ├─ r-bit64 4.0.5 [required: any]
  │  │     │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  │  └─ dependencies of libgcc-ng displayed above
  │  │     │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     │  │  └─ dependencies of r-base displayed above
  │  │     │  └─ r-bit 4.0.5 [required: >=4.0.0]
  │  │     │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │     │  └─ dependencies of libgcc-ng displayed above
  │  │     │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     │        └─ dependencies of r-base displayed above
  │  │     ├─ r-cli 3.6.2 [required: any]
  │  │     │  └─ dependencies of r-cli displayed above
  │  │     ├─ r-cpp11 0.4.7 [required: >=0.2.0]
  │  │     │  └─ dependencies of r-cpp11 displayed above
  │  │     ├─ r-crayon 1.5.2 [required: any]
  │  │     │  └─ dependencies of r-crayon displayed above
  │  │     ├─ r-glue 1.7.0 [required: any]
  │  │     │  └─ dependencies of r-glue displayed above
  │  │     ├─ r-hms 1.1.3 [required: any]
  │  │     │  └─ dependencies of r-hms displayed above
  │  │     ├─ r-lifecycle 1.0.4 [required: any]
  │  │     │  └─ dependencies of r-lifecycle displayed above
  │  │     ├─ r-progress 1.2.3 [required: >=1.2.1]
  │  │     │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     │  │  └─ dependencies of r-base displayed above
  │  │     │  ├─ r-crayon 1.5.2 [required: any]
  │  │     │  │  └─ dependencies of r-crayon displayed above
  │  │     │  ├─ r-hms 1.1.3 [required: any]
  │  │     │  │  └─ dependencies of r-hms displayed above
  │  │     │  ├─ r-prettyunits 1.2.0 [required: any]
  │  │     │  │  └─ dependencies of r-prettyunits displayed above
  │  │     │  └─ r-r6 2.5.1 [required: any]
  │  │     │     └─ dependencies of r-r6 displayed above
  │  │     ├─ r-rlang 1.1.3 [required: >=0.4.2]
  │  │     │  └─ dependencies of r-rlang displayed above
  │  │     ├─ r-tibble 3.2.1 [required: >=2.0.0]
  │  │     │  └─ dependencies of r-tibble displayed above
  │  │     ├─ r-tidyselect 1.2.1 [required: any]
  │  │     │  └─ dependencies of r-tidyselect displayed above
  │  │     ├─ r-tzdb 0.4.0 [required: >=0.1.1]
  │  │     │  └─ dependencies of r-tzdb displayed above
  │  │     ├─ r-vctrs 0.6.5 [required: >=0.2.0]
  │  │     │  └─ dependencies of r-vctrs displayed above
  │  │     └─ r-withr 3.0.0 [required: any]
  │  │        └─ dependencies of r-withr displayed above
  │  ├─ r-rlang 1.1.3 [required: >=0.4.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyselect 1.2.1 [required: any]
  │  │  └─ dependencies of r-tidyselect displayed above
  │  └─ r-vctrs 0.6.5 [required: >=0.3.0]
  │     └─ dependencies of r-vctrs displayed above
  ├─ r-hms 1.1.3 [required: >=1.1.2]
  │  └─ dependencies of r-hms displayed above
  ├─ r-httr 1.4.7 [required: >=1.4.4]
  │  └─ dependencies of r-httr displayed above
  ├─ r-jsonlite 1.8.8 [required: >=1.8.4]
  │  └─ dependencies of r-jsonlite displayed above
  ├─ r-lubridate 1.9.3 [required: >=1.9.2]
  │  └─ dependencies of r-lubridate displayed above
  ├─ r-magrittr 2.0.3 [required: >=2.0.3]
  │  └─ dependencies of r-magrittr displayed above
  ├─ r-modelr 0.1.11 [required: >=0.1.10]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-broom 1.0.6 [required: any]
  │  │  └─ dependencies of r-broom displayed above
  │  ├─ r-dplyr 1.1.4 [required: any]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-purrr 1.0.2 [required: >=0.2.2]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.3 [required: >=0.2.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  └─ r-tidyr 1.3.1 [required: >=0.8.0]
  │     └─ dependencies of r-tidyr displayed above
  ├─ r-pillar 1.9.0 [required: >=1.8.1]
  │  └─ dependencies of r-pillar displayed above
  ├─ r-purrr 1.0.2 [required: >=1.0.1]
  │  └─ dependencies of r-purrr displayed above
  ├─ r-ragg 1.3.2 [required: >=1.2.5]
  │  ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
  │  │  └─ dependencies of freetype displayed above
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libjpeg-turbo 3.0.0 [required: >=3.0.0,<4.0a0]
  │  │  └─ dependencies of libjpeg-turbo displayed above
  │  ├─ libpng 1.6.43 [required: >=1.6.43,<1.7.0a0]
  │  │  └─ dependencies of libpng displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ libtiff 4.6.0 [required: >=4.6.0,<4.7.0a0]
  │  │  └─ dependencies of libtiff displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-systemfonts 1.0.5 [required: >=1.0.3]
  │  │  ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
  │  │  │  └─ dependencies of freetype displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  └─ r-cpp11 0.4.7 [required: any]
  │  │     └─ dependencies of r-cpp11 displayed above
  │  └─ r-textshaping 0.3.7 [required: >=0.3.0]
  │     ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
  │     │  └─ dependencies of freetype displayed above
  │     ├─ fribidi 1.0.10 [required: >=1.0.10,<2.0a0]
  │     │  └─ dependencies of fribidi displayed above
  │     ├─ harfbuzz 8.5.0 [required: >=8.2.1,<9.0a0]
  │     │  └─ dependencies of harfbuzz displayed above
  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  └─ dependencies of libgcc-ng displayed above
  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     ├─ r-cpp11 0.4.7 [required: >=0.2.1]
  │     │  └─ dependencies of r-cpp11 displayed above
  │     └─ r-systemfonts 1.0.5 [required: >=1.0.0]
  │        └─ dependencies of r-systemfonts displayed above
  ├─ r-readr 2.1.5 [required: >=2.1.4]
  │  └─ dependencies of r-readr displayed above
  ├─ r-readxl 1.4.3 [required: >=1.4.2]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libiconv 1.17 [required: >=1.17,<2.0a0]
  │  │  └─ dependencies of libiconv displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cellranger 1.1.0 [required: any]
  │  │  └─ dependencies of r-cellranger displayed above
  │  ├─ r-cpp11 0.4.7 [required: >=0.4.0]
  │  │  └─ dependencies of r-cpp11 displayed above
  │  ├─ r-progress 1.2.3 [required: any]
  │  │  └─ dependencies of r-progress displayed above
  │  └─ r-tibble 3.2.1 [required: >=2.0.1]
  │     └─ dependencies of r-tibble displayed above
  ├─ r-reprex 2.1.0 [required: >=2.0.2]
  │  ├─ pandoc 3.2 [required: >=2.0]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-callr 3.7.6 [required: >=3.6.0]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-processx 3.8.4 [required: >=3.4.0]
  │  │  │  └─ dependencies of r-processx displayed above
  │  │  └─ r-r6 2.5.1 [required: any]
  │  │     └─ dependencies of r-r6 displayed above
  │  ├─ r-cli 3.6.2 [required: >=3.2.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-clipr 0.8.0 [required: >=0.4.0]
  │  │  └─ dependencies of r-clipr displayed above
  │  ├─ r-fs 1.6.4 [required: any]
  │  │  └─ dependencies of r-fs displayed above
  │  ├─ r-glue 1.7.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-knitr 1.46 [required: >=1.23]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-evaluate 0.23 [required: >=0.15]
  │  │  │  └─ dependencies of r-evaluate displayed above
  │  │  ├─ r-highr 0.10 [required: any]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-xfun 0.44 [required: >=0.18]
  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │        └─ dependencies of r-base displayed above
  │  │  ├─ r-xfun 0.44 [required: >=0.43]
  │  │  │  └─ dependencies of r-xfun displayed above
  │  │  └─ r-yaml 2.3.8 [required: >=2.1.19]
  │  │     └─ dependencies of r-yaml displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-rlang 1.1.3 [required: >=1.0.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-rmarkdown 2.27 [required: any]
  │  │  ├─ pandoc 3.2 [required: >=1.14]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-bslib 0.7.0 [required: >=0.2.5.1]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-base64enc 0.1_3 [required: any]
  │  │  │  │  └─ dependencies of r-base64enc displayed above
  │  │  │  ├─ r-cachem 1.1.0 [required: any]
  │  │  │  │  └─ dependencies of r-cachem displayed above
  │  │  │  ├─ r-htmltools 0.5.8.1 [required: >=0.5.7]
  │  │  │  │  └─ dependencies of r-htmltools displayed above
  │  │  │  ├─ r-jquerylib 0.1.4 [required: >=0.1.3]
  │  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  └─ r-htmltools 0.5.8.1 [required: any]
  │  │  │  │     └─ dependencies of r-htmltools displayed above
  │  │  │  ├─ r-jsonlite 1.8.8 [required: any]
  │  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  │  ├─ r-memoise 2.0.1 [required: >=2.0.1]
  │  │  │  │  └─ dependencies of r-memoise displayed above
  │  │  │  ├─ r-mime 0.12 [required: any]
  │  │  │  │  └─ dependencies of r-mime displayed above
  │  │  │  ├─ r-rlang 1.1.3 [required: any]
  │  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  │  └─ r-sass 0.4.9 [required: >=0.4.0]
  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     │  └─ dependencies of r-base displayed above
  │  │  │     ├─ r-digest 0.6.35 [required: any]
  │  │  │     │  └─ dependencies of r-digest displayed above
  │  │  │     ├─ r-fs 1.6.4 [required: any]
  │  │  │     │  └─ dependencies of r-fs displayed above
  │  │  │     ├─ r-htmltools 0.5.8.1 [required: any]
  │  │  │     │  └─ dependencies of r-htmltools displayed above
  │  │  │     ├─ r-r6 2.5.1 [required: any]
  │  │  │     │  └─ dependencies of r-r6 displayed above
  │  │  │     ├─ r-rappdirs 0.3.3 [required: any]
  │  │  │     │  └─ dependencies of r-rappdirs displayed above
  │  │  │     └─ r-rlang 1.1.3 [required: any]
  │  │  │        └─ dependencies of r-rlang displayed above
  │  │  ├─ r-evaluate 0.23 [required: >=0.13]
  │  │  │  └─ dependencies of r-evaluate displayed above
  │  │  ├─ r-fontawesome 0.5.2 [required: >=0.5.0]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-htmltools 0.5.8.1 [required: >=0.5.1.1]
  │  │  │  │  └─ dependencies of r-htmltools displayed above
  │  │  │  └─ r-rlang 1.1.3 [required: >=0.4.10]
  │  │  │     └─ dependencies of r-rlang displayed above
  │  │  ├─ r-htmltools 0.5.8.1 [required: >=0.5.1]
  │  │  │  └─ dependencies of r-htmltools displayed above
  │  │  ├─ r-jquerylib 0.1.4 [required: any]
  │  │  │  └─ dependencies of r-jquerylib displayed above
  │  │  ├─ r-jsonlite 1.8.8 [required: any]
  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  ├─ r-knitr 1.46 [required: >=1.22]
  │  │  │  └─ dependencies of r-knitr displayed above
  │  │  ├─ r-stringr 1.5.1 [required: >=1.2.0]
  │  │  │  └─ dependencies of r-stringr displayed above
  │  │  ├─ r-tinytex 0.51 [required: >=0.31]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-xfun 0.44 [required: >=0.5]
  │  │  │     └─ dependencies of r-xfun displayed above
  │  │  ├─ r-xfun 0.44 [required: >=0.36]
  │  │  │  └─ dependencies of r-xfun displayed above
  │  │  └─ r-yaml 2.3.8 [required: >=2.1.19]
  │  │     └─ dependencies of r-yaml displayed above
  │  ├─ r-rstudioapi 0.16.0 [required: any]
  │  │  └─ dependencies of r-rstudioapi displayed above
  │  └─ r-withr 3.0.0 [required: >=2.3.0]
  │     └─ dependencies of r-withr displayed above
  ├─ r-rlang 1.1.3 [required: >=1.0.6]
  │  └─ dependencies of r-rlang displayed above
  ├─ r-rstudioapi 0.16.0 [required: >=0.14]
  │  └─ dependencies of r-rstudioapi displayed above
  ├─ r-rvest 1.0.4 [required: >=1.0.3]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.2 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-glue 1.7.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-httr 1.4.7 [required: >=0.5]
  │  │  └─ dependencies of r-httr displayed above
  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.0]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-rlang 1.1.3 [required: >=1.0.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-selectr 0.4_2 [required: any]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-r6 2.5.1 [required: any]
  │  │  │  └─ dependencies of r-r6 displayed above
  │  │  └─ r-stringr 1.5.1 [required: any]
  │  │     └─ dependencies of r-stringr displayed above
  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-withr 3.0.0 [required: any]
  │  │  └─ dependencies of r-withr displayed above
  │  └─ r-xml2 1.3.6 [required: >=1.3]
  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  └─ dependencies of libgcc-ng displayed above
  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │     ├─ libxml2 2.12.7 [required: >=2.12.3,<3.0.0a0]
  │     │  └─ dependencies of libxml2 displayed above
  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     ├─ r-cli 3.6.2 [required: any]
  │     │  └─ dependencies of r-cli displayed above
  │     └─ r-rlang 1.1.3 [required: >=1.1.0]
  │        └─ dependencies of r-rlang displayed above
  ├─ r-stringr 1.5.1 [required: >=1.5.0]
  │  └─ dependencies of r-stringr displayed above
  ├─ r-tibble 3.2.1 [required: >=3.1.8]
  │  └─ dependencies of r-tibble displayed above
  ├─ r-tidyr 1.3.1 [required: >=1.3.0]
  │  └─ dependencies of r-tidyr displayed above
  └─ r-xml2 1.3.6 [required: >=1.3.3]
     └─ dependencies of r-xml2 displayed above
r-rodbc==1.3_23
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  └─ unixodbc 2.3.12 [required: >=2.3.12,<2.4.0a0]
     ├─ libedit 3.1.20191231 [required: >=3.1.20191231,<3.2.0a0]
     │  └─ dependencies of libedit displayed above
     ├─ libgcc-ng 14.2.0 [required: >=12]
     │  └─ dependencies of libgcc-ng displayed above
     ├─ libiconv 1.17 [required: >=1.17,<2.0a0]
     │  └─ dependencies of libiconv displayed above
     └─ libstdcxx-ng 13.2.0 [required: >=12]
r-forecast==8.22.0
  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  └─ dependencies of libblas displayed above
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-colorspace 2.1_0 [required: any]
  │  └─ dependencies of r-colorspace displayed above
  ├─ r-fracdiff 1.5_3 [required: any]
  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ dependencies of libblas displayed above
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-generics 0.1.3 [required: >=0.1.2]
  │  └─ dependencies of r-generics displayed above
  ├─ r-ggplot2 3.5.1 [required: >=2.2.1]
  │  └─ dependencies of r-ggplot2 displayed above
  ├─ r-lmtest 0.9_40 [required: any]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libgfortran-ng 14.2.0 [required: any]
  │  │  └─ dependencies of libgfortran-ng displayed above
  │  ├─ libgfortran5 14.2.0 [required: >=12.3.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-zoo 1.8_12 [required: any]
  │     └─ dependencies of r-zoo displayed above
  ├─ r-magrittr 2.0.3 [required: any]
  │  └─ dependencies of r-magrittr displayed above
  ├─ r-nnet 7.3_19 [required: any]
  │  └─ dependencies of r-nnet displayed above
  ├─ r-rcpp 1.0.12 [required: >=0.11.0]
  │  └─ dependencies of r-rcpp displayed above
  ├─ r-rcpparmadillo 0.12.8.3.0 [required: >=0.2.35]
  │  ├─ _openmp_mutex 4.5 [required: >=4.5]
  │  │  └─ dependencies of _openmp_mutex displayed above
  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ dependencies of libblas displayed above
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ dependencies of liblapack displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-rcpp 1.0.12 [required: >=0.11.0]
  │     └─ dependencies of r-rcpp displayed above
  ├─ r-timedate 4032.109 [required: any]
  │  └─ dependencies of r-timedate displayed above
  ├─ r-tseries 0.10_56 [required: any]
  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ dependencies of libblas displayed above
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libgfortran-ng 14.2.0 [required: any]
  │  │  └─ dependencies of libgfortran-ng displayed above
  │  ├─ libgfortran5 14.2.0 [required: >=12.3.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-quadprog 1.5_8 [required: any]
  │  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  └─ dependencies of libblas displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libgfortran-ng 14.2.0 [required: any]
  │  │  │  └─ dependencies of libgfortran-ng displayed above
  │  │  ├─ libgfortran5 14.2.0 [required: >=12.3.0]
  │  │  │  └─ dependencies of libgfortran5 displayed above
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-quantmod 0.4.26 [required: >=0.4_9]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-curl 5.1.0 [required: any]
  │  │  │  └─ dependencies of r-curl displayed above
  │  │  ├─ r-jsonlite 1.8.8 [required: >=1.1]
  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  ├─ r-ttr 0.24.4 [required: >=0.2]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-curl 5.1.0 [required: any]
  │  │  │  │  └─ dependencies of r-curl displayed above
  │  │  │  ├─ r-xts 0.13.2 [required: >=0.10_0]
  │  │  │  │  └─ dependencies of r-xts displayed above
  │  │  │  └─ r-zoo 1.8_12 [required: any]
  │  │  │     └─ dependencies of r-zoo displayed above
  │  │  ├─ r-xts 0.13.2 [required: >=0.9_0]
  │  │  │  └─ dependencies of r-xts displayed above
  │  │  └─ r-zoo 1.8_12 [required: any]
  │  │     └─ dependencies of r-zoo displayed above
  │  └─ r-zoo 1.8_12 [required: any]
  │     └─ dependencies of r-zoo displayed above
  ├─ r-urca 1.3_3 [required: any]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libgfortran-ng 14.2.0 [required: any]
  │  │  └─ dependencies of libgfortran-ng displayed above
  │  ├─ libgfortran5 14.2.0 [required: >=12.3.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-nlme 3.1_164 [required: any]
  │     └─ dependencies of r-nlme displayed above
  └─ r-zoo 1.8_12 [required: any]
     └─ dependencies of r-zoo displayed above
r-rsqlite==2.3.4
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-bit64 4.0.5 [required: any]
  │  └─ dependencies of r-bit64 displayed above
  ├─ r-blob 1.2.4 [required: >=1.2.0]
  │  └─ dependencies of r-blob displayed above
  ├─ r-cpp11 0.4.7 [required: any]
  │  └─ dependencies of r-cpp11 displayed above
  ├─ r-dbi 1.2.2 [required: >=1.1.0]
  │  └─ dependencies of r-dbi displayed above
  ├─ r-memoise 2.0.1 [required: any]
  │  └─ dependencies of r-memoise displayed above
  ├─ r-pkgconfig 2.0.3 [required: any]
  │  └─ dependencies of r-pkgconfig displayed above
  └─ r-plogr 0.2.0 [required: >=0.2.0]
     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
        └─ dependencies of r-base displayed above
r-devtools==2.4.5
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-cli 3.6.2 [required: >=3.3.0]
  │  └─ dependencies of r-cli displayed above
  ├─ r-desc 1.4.3 [required: >=1.4.1]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.2 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-r6 2.5.1 [required: any]
  │  │  └─ dependencies of r-r6 displayed above
  │  └─ r-rprojroot 2.0.4 [required: any]
  │     └─ dependencies of r-rprojroot displayed above
  ├─ r-ellipsis 0.3.2 [required: >=0.3.2]
  │  └─ dependencies of r-ellipsis displayed above
  ├─ r-fs 1.6.4 [required: >=1.5.2]
  │  └─ dependencies of r-fs displayed above
  ├─ r-lifecycle 1.0.4 [required: >=1.0.1]
  │  └─ dependencies of r-lifecycle displayed above
  ├─ r-memoise 2.0.1 [required: >=2.0.1]
  │  └─ dependencies of r-memoise displayed above
  ├─ r-miniui 0.1.1.1 [required: >=0.1.1.1]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-htmltools 0.5.8.1 [required: >=0.3]
  │  │  └─ dependencies of r-htmltools displayed above
  │  └─ r-shiny 1.8.1.1 [required: >=0.13]
  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     ├─ r-bslib 0.7.0 [required: >=0.3.0]
  │     │  └─ dependencies of r-bslib displayed above
  │     ├─ r-cachem 1.1.0 [required: any]
  │     │  └─ dependencies of r-cachem displayed above
  │     ├─ r-commonmark 1.9.1 [required: >=1.7]
  │     │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  │  └─ dependencies of libgcc-ng displayed above
  │     │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │     └─ dependencies of r-base displayed above
  │     ├─ r-crayon 1.5.2 [required: any]
  │     │  └─ dependencies of r-crayon displayed above
  │     ├─ r-ellipsis 0.3.2 [required: any]
  │     │  └─ dependencies of r-ellipsis displayed above
  │     ├─ r-fastmap 1.2.0 [required: >=1.1.0]
  │     │  └─ dependencies of r-fastmap displayed above
  │     ├─ r-fontawesome 0.5.2 [required: >=0.2.1]
  │     │  └─ dependencies of r-fontawesome displayed above
  │     ├─ r-glue 1.7.0 [required: >=1.3.2]
  │     │  └─ dependencies of r-glue displayed above
  │     ├─ r-htmltools 0.5.8.1 [required: >=0.5.2]
  │     │  └─ dependencies of r-htmltools displayed above
  │     ├─ r-httpuv 1.6.15 [required: >=1.5.2]
  │     │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  │  └─ dependencies of libgcc-ng displayed above
  │     │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │     │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  │  └─ dependencies of r-base displayed above
  │     │  ├─ r-later 1.3.2 [required: >=0.8.0]
  │     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  │  │  └─ dependencies of libgcc-ng displayed above
  │     │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │     │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  │  │  └─ dependencies of r-base displayed above
  │     │  │  ├─ r-rcpp 1.0.12 [required: >=0.12.9]
  │     │  │  │  └─ dependencies of r-rcpp displayed above
  │     │  │  └─ r-rlang 1.1.3 [required: any]
  │     │  │     └─ dependencies of r-rlang displayed above
  │     │  ├─ r-promises 1.3.0 [required: any]
  │     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  │  │  └─ dependencies of libgcc-ng displayed above
  │     │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │     │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  │  │  └─ dependencies of r-base displayed above
  │     │  │  ├─ r-fastmap 1.2.0 [required: >=1.1.0]
  │     │  │  │  └─ dependencies of r-fastmap displayed above
  │     │  │  ├─ r-later 1.3.2 [required: any]
  │     │  │  │  └─ dependencies of r-later displayed above
  │     │  │  ├─ r-magrittr 2.0.3 [required: >=1.5]
  │     │  │  │  └─ dependencies of r-magrittr displayed above
  │     │  │  ├─ r-r6 2.5.1 [required: any]
  │     │  │  │  └─ dependencies of r-r6 displayed above
  │     │  │  ├─ r-rcpp 1.0.12 [required: any]
  │     │  │  │  └─ dependencies of r-rcpp displayed above
  │     │  │  └─ r-rlang 1.1.3 [required: any]
  │     │  │     └─ dependencies of r-rlang displayed above
  │     │  ├─ r-r6 2.5.1 [required: any]
  │     │  │  └─ dependencies of r-r6 displayed above
  │     │  └─ r-rcpp 1.0.12 [required: >=1.0.7]
  │     │     └─ dependencies of r-rcpp displayed above
  │     ├─ r-jsonlite 1.8.8 [required: >=0.9.16]
  │     │  └─ dependencies of r-jsonlite displayed above
  │     ├─ r-later 1.3.2 [required: >=1.0.0]
  │     │  └─ dependencies of r-later displayed above
  │     ├─ r-lifecycle 1.0.4 [required: >=0.2.0]
  │     │  └─ dependencies of r-lifecycle displayed above
  │     ├─ r-mime 0.12 [required: >=0.3]
  │     │  └─ dependencies of r-mime displayed above
  │     ├─ r-promises 1.3.0 [required: >=1.1.0]
  │     │  └─ dependencies of r-promises displayed above
  │     ├─ r-r6 2.5.1 [required: >=2.0]
  │     │  └─ dependencies of r-r6 displayed above
  │     ├─ r-rlang 1.1.3 [required: >=0.4.10]
  │     │  └─ dependencies of r-rlang displayed above
  │     ├─ r-sourcetools 0.1.7_1 [required: any]
  │     │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  │  └─ dependencies of libgcc-ng displayed above
  │     │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │     │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │     └─ dependencies of r-base displayed above
  │     ├─ r-withr 3.0.0 [required: any]
  │     │  └─ dependencies of r-withr displayed above
  │     └─ r-xtable 1.8_4 [required: any]
  │        └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │           └─ dependencies of r-base displayed above
  ├─ r-pkgbuild 1.4.4 [required: >=1.3.1]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-callr 3.7.6 [required: >=3.2.0]
  │  │  └─ dependencies of r-callr displayed above
  │  ├─ r-cli 3.6.2 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-crayon 1.5.2 [required: any]
  │  │  └─ dependencies of r-crayon displayed above
  │  ├─ r-desc 1.4.3 [required: any]
  │  │  └─ dependencies of r-desc displayed above
  │  ├─ r-prettyunits 1.2.0 [required: any]
  │  │  └─ dependencies of r-prettyunits displayed above
  │  ├─ r-r6 2.5.1 [required: any]
  │  │  └─ dependencies of r-r6 displayed above
  │  ├─ r-rprojroot 2.0.4 [required: any]
  │  │  └─ dependencies of r-rprojroot displayed above
  │  └─ r-withr 3.0.0 [required: >=2.1.2]
  │     └─ dependencies of r-withr displayed above
  ├─ r-pkgdown 2.0.9 [required: >=2.0.6]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-bslib 0.7.0 [required: any]
  │  │  └─ dependencies of r-bslib displayed above
  │  ├─ r-callr 3.7.6 [required: >=2.0.2]
  │  │  └─ dependencies of r-callr displayed above
  │  ├─ r-crayon 1.5.2 [required: any]
  │  │  └─ dependencies of r-crayon displayed above
  │  ├─ r-desc 1.4.3 [required: any]
  │  │  └─ dependencies of r-desc displayed above
  │  ├─ r-digest 0.6.35 [required: any]
  │  │  └─ dependencies of r-digest displayed above
  │  ├─ r-downlit 0.4.3 [required: >=0.4.0]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-brio 1.1.5 [required: any]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-desc 1.4.3 [required: any]
  │  │  │  └─ dependencies of r-desc displayed above
  │  │  ├─ r-digest 0.6.35 [required: any]
  │  │  │  └─ dependencies of r-digest displayed above
  │  │  ├─ r-evaluate 0.23 [required: any]
  │  │  │  └─ dependencies of r-evaluate displayed above
  │  │  ├─ r-fansi 1.0.6 [required: any]
  │  │  │  └─ dependencies of r-fansi displayed above
  │  │  ├─ r-memoise 2.0.1 [required: any]
  │  │  │  └─ dependencies of r-memoise displayed above
  │  │  ├─ r-rlang 1.1.3 [required: any]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-vctrs 0.6.5 [required: any]
  │  │  │  └─ dependencies of r-vctrs displayed above
  │  │  ├─ r-withr 3.0.0 [required: any]
  │  │  │  └─ dependencies of r-withr displayed above
  │  │  └─ r-yaml 2.3.8 [required: any]
  │  │     └─ dependencies of r-yaml displayed above
  │  ├─ r-fs 1.6.4 [required: >=1.4.0]
  │  │  └─ dependencies of r-fs displayed above
  │  ├─ r-httr 1.4.7 [required: >=1.4.2]
  │  │  └─ dependencies of r-httr displayed above
  │  ├─ r-jsonlite 1.8.8 [required: any]
  │  │  └─ dependencies of r-jsonlite displayed above
  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-memoise 2.0.1 [required: any]
  │  │  └─ dependencies of r-memoise displayed above
  │  ├─ r-purrr 1.0.2 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-ragg 1.3.2 [required: any]
  │  │  └─ dependencies of r-ragg displayed above
  │  ├─ r-rlang 1.1.3 [required: >=0.4.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-rmarkdown 2.27 [required: >=1.1.9007]
  │  │  └─ dependencies of r-rmarkdown displayed above
  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-whisker 0.4.1 [required: any]
  │  │  └─ dependencies of r-whisker displayed above
  │  ├─ r-withr 3.0.0 [required: any]
  │  │  └─ dependencies of r-withr displayed above
  │  ├─ r-xml2 1.3.6 [required: >=1.3.1]
  │  │  └─ dependencies of r-xml2 displayed above
  │  └─ r-yaml 2.3.8 [required: any]
  │     └─ dependencies of r-yaml displayed above
  ├─ r-pkgload 1.3.4 [required: >=1.3.0]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.2 [required: >=3.3.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-crayon 1.5.2 [required: any]
  │  │  └─ dependencies of r-crayon displayed above
  │  ├─ r-desc 1.4.3 [required: any]
  │  │  └─ dependencies of r-desc displayed above
  │  ├─ r-fs 1.6.4 [required: any]
  │  │  └─ dependencies of r-fs displayed above
  │  ├─ r-glue 1.7.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-pkgbuild 1.4.4 [required: any]
  │  │  └─ dependencies of r-pkgbuild displayed above
  │  ├─ r-rlang 1.1.3 [required: >=1.1.1]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-rprojroot 2.0.4 [required: any]
  │  │  └─ dependencies of r-rprojroot displayed above
  │  └─ r-withr 3.0.0 [required: >=2.4.3]
  │     └─ dependencies of r-withr displayed above
  ├─ r-profvis 0.3.8 [required: >=0.3.7]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-htmlwidgets 1.6.4 [required: >=0.3.2]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-htmltools 0.5.8.1 [required: >=0.5.7]
  │  │  │  └─ dependencies of r-htmltools displayed above
  │  │  ├─ r-jsonlite 1.8.8 [required: >=0.9.16]
  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  ├─ r-knitr 1.46 [required: >=1.8]
  │  │  │  └─ dependencies of r-knitr displayed above
  │  │  ├─ r-rmarkdown 2.27 [required: any]
  │  │  │  └─ dependencies of r-rmarkdown displayed above
  │  │  └─ r-yaml 2.3.8 [required: any]
  │  │     └─ dependencies of r-yaml displayed above
  │  ├─ r-purrr 1.0.2 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.3 [required: >=0.4.9]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-stringr 1.5.1 [required: any]
  │  │  └─ dependencies of r-stringr displayed above
  │  └─ r-vctrs 0.6.5 [required: any]
  │     └─ dependencies of r-vctrs displayed above
  ├─ r-rcmdcheck 1.4.0 [required: >=1.4.0]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-callr 3.7.6 [required: >=3.1.1.9000]
  │  │  └─ dependencies of r-callr displayed above
  │  ├─ r-cli 3.6.2 [required: >=3.0.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-curl 5.1.0 [required: any]
  │  │  └─ dependencies of r-curl displayed above
  │  ├─ r-desc 1.4.3 [required: >=1.2.0]
  │  │  └─ dependencies of r-desc displayed above
  │  ├─ r-digest 0.6.35 [required: any]
  │  │  └─ dependencies of r-digest displayed above
  │  ├─ r-pkgbuild 1.4.4 [required: any]
  │  │  └─ dependencies of r-pkgbuild displayed above
  │  ├─ r-prettyunits 1.2.0 [required: any]
  │  │  └─ dependencies of r-prettyunits displayed above
  │  ├─ r-r6 2.5.1 [required: any]
  │  │  └─ dependencies of r-r6 displayed above
  │  ├─ r-rprojroot 2.0.4 [required: any]
  │  │  └─ dependencies of r-rprojroot displayed above
  │  ├─ r-sessioninfo 1.2.2 [required: >=1.1.1]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.2 [required: any]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  └─ r-withr 3.0.0 [required: any]
  │  │     └─ dependencies of r-withr displayed above
  │  ├─ r-withr 3.0.0 [required: any]
  │  │  └─ dependencies of r-withr displayed above
  │  └─ r-xopen 1.0.1 [required: any]
  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     └─ r-processx 3.8.4 [required: any]
  │        └─ dependencies of r-processx displayed above
  ├─ r-remotes 2.5.0 [required: >=2.4.2]
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-rlang 1.1.3 [required: >=1.0.4]
  │  └─ dependencies of r-rlang displayed above
  ├─ r-roxygen2 7.3.1 [required: >=7.2.1]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-brew 1.0_10 [required: any]
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-commonmark 1.9.1 [required: any]
  │  │  └─ dependencies of r-commonmark displayed above
  │  ├─ r-cpp11 0.4.7 [required: any]
  │  │  └─ dependencies of r-cpp11 displayed above
  │  ├─ r-desc 1.4.3 [required: >=1.2.0]
  │  │  └─ dependencies of r-desc displayed above
  │  ├─ r-digest 0.6.35 [required: any]
  │  │  └─ dependencies of r-digest displayed above
  │  ├─ r-knitr 1.46 [required: any]
  │  │  └─ dependencies of r-knitr displayed above
  │  ├─ r-pkgload 1.3.4 [required: >=1.0.2]
  │  │  └─ dependencies of r-pkgload displayed above
  │  ├─ r-purrr 1.0.2 [required: >=0.3.3]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-r6 2.5.1 [required: >=2.1.2]
  │  │  └─ dependencies of r-r6 displayed above
  │  ├─ r-rlang 1.1.3 [required: any]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-stringi 1.8.4 [required: any]
  │  │  └─ dependencies of r-stringi displayed above
  │  ├─ r-stringr 1.5.1 [required: >=1.0.0]
  │  │  └─ dependencies of r-stringr displayed above
  │  └─ r-xml2 1.3.6 [required: any]
  │     └─ dependencies of r-xml2 displayed above
  ├─ r-rversions 2.1.2 [required: >=2.1.1]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-curl 5.1.0 [required: any]
  │  │  └─ dependencies of r-curl displayed above
  │  └─ r-xml2 1.3.6 [required: >=1.0.0]
  │     └─ dependencies of r-xml2 displayed above
  ├─ r-sessioninfo 1.2.2 [required: >=1.2.2]
  │  └─ dependencies of r-sessioninfo displayed above
  ├─ r-testthat 3.2.1.1 [required: >=3.1.4]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-brio 1.1.5 [required: any]
  │  │  └─ dependencies of r-brio displayed above
  │  ├─ r-callr 3.7.6 [required: >=3.5.1]
  │  │  └─ dependencies of r-callr displayed above
  │  ├─ r-cli 3.6.2 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-crayon 1.5.2 [required: >=1.3.4]
  │  │  └─ dependencies of r-crayon displayed above
  │  ├─ r-desc 1.4.3 [required: any]
  │  │  └─ dependencies of r-desc displayed above
  │  ├─ r-digest 0.6.35 [required: any]
  │  │  └─ dependencies of r-digest displayed above
  │  ├─ r-ellipsis 0.3.2 [required: >=0.2.0]
  │  │  └─ dependencies of r-ellipsis displayed above
  │  ├─ r-evaluate 0.23 [required: any]
  │  │  └─ dependencies of r-evaluate displayed above
  │  ├─ r-jsonlite 1.8.8 [required: any]
  │  │  └─ dependencies of r-jsonlite displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-pkgload 1.3.4 [required: any]
  │  │  └─ dependencies of r-pkgload displayed above
  │  ├─ r-praise 1.0.0 [required: any]
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-processx 3.8.4 [required: any]
  │  │  └─ dependencies of r-processx displayed above
  │  ├─ r-ps 1.7.6 [required: >=1.3.4]
  │  │  └─ dependencies of r-ps displayed above
  │  ├─ r-r6 2.5.1 [required: >=2.2.0]
  │  │  └─ dependencies of r-r6 displayed above
  │  ├─ r-rlang 1.1.3 [required: >=0.4.1]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-waldo 0.5.2 [required: >=0.2.1]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.2 [required: any]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-diffobj 0.3.5 [required: >=0.3.4]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-crayon 1.5.2 [required: >=1.3.2]
  │  │  │     └─ dependencies of r-crayon displayed above
  │  │  ├─ r-fansi 1.0.6 [required: any]
  │  │  │  └─ dependencies of r-fansi displayed above
  │  │  ├─ r-glue 1.7.0 [required: any]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-rematch2 2.1.2 [required: any]
  │  │  │  └─ dependencies of r-rematch2 displayed above
  │  │  ├─ r-rlang 1.1.3 [required: >=1.0.0]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  └─ r-tibble 3.2.1 [required: any]
  │  │     └─ dependencies of r-tibble displayed above
  │  └─ r-withr 3.0.0 [required: >=2.0.0]
  │     └─ dependencies of r-withr displayed above
  ├─ r-urlchecker 1.0.1 [required: >=1.0.1]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.2 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-curl 5.1.0 [required: any]
  │  │  └─ dependencies of r-curl displayed above
  │  └─ r-xml2 1.3.6 [required: any]
  │     └─ dependencies of r-xml2 displayed above
  ├─ r-usethis 2.2.3 [required: >=2.1.6]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.2 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-clipr 0.8.0 [required: >=0.3.0]
  │  │  └─ dependencies of r-clipr displayed above
  │  ├─ r-crayon 1.5.2 [required: any]
  │  │  └─ dependencies of r-crayon displayed above
  │  ├─ r-curl 5.1.0 [required: >=2.7]
  │  │  └─ dependencies of r-curl displayed above
  │  ├─ r-desc 1.4.3 [required: any]
  │  │  └─ dependencies of r-desc displayed above
  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  └─ dependencies of r-ellipsis displayed above
  │  ├─ r-fs 1.6.4 [required: >=1.3.0]
  │  │  └─ dependencies of r-fs displayed above
  │  ├─ r-gert 2.0.1 [required: >=1.0.2]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libgit2 1.8.1 [required: >=1.8.0,<1.9.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libssh2 1.11.0 [required: >=1.11.0,<2.0a0]
  │  │  │  │  └─ dependencies of libssh2 displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  ├─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  │  └─ dependencies of openssl displayed above
  │  │  │  └─ pcre2 10.43 [required: >=10.43,<10.44.0a0]
  │  │  │     └─ dependencies of pcre2 displayed above
  │  │  ├─ r-askpass 1.2.0 [required: any]
  │  │  │  └─ dependencies of r-askpass displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-credentials 2.0.1 [required: >=1.2.1]
  │  │  │  ├─ r-askpass 1.2.0 [required: any]
  │  │  │  │  └─ dependencies of r-askpass displayed above
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-curl 5.1.0 [required: any]
  │  │  │  │  └─ dependencies of r-curl displayed above
  │  │  │  ├─ r-jsonlite 1.8.8 [required: any]
  │  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  │  ├─ r-openssl 2.2.0 [required: >=1.3]
  │  │  │  │  └─ dependencies of r-openssl displayed above
  │  │  │  └─ r-sys 3.4.2 [required: >=2.1]
  │  │  │     └─ dependencies of r-sys displayed above
  │  │  ├─ r-openssl 2.2.0 [required: >=2.0.3]
  │  │  │  └─ dependencies of r-openssl displayed above
  │  │  ├─ r-rstudioapi 0.16.0 [required: >=0.11]
  │  │  │  └─ dependencies of r-rstudioapi displayed above
  │  │  └─ r-zip 2.3.1 [required: >=2.1.0]
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │        └─ dependencies of r-base displayed above
  │  ├─ r-gh 1.4.1 [required: >=1.2.0]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.2 [required: >=3.0.1]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-gitcreds 0.1.2 [required: any]
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-httr2 1.0.1 [required: any]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-cli 3.6.2 [required: >=3.0.0]
  │  │  │  │  └─ dependencies of r-cli displayed above
  │  │  │  ├─ r-curl 5.1.0 [required: >=5.1.0]
  │  │  │  │  └─ dependencies of r-curl displayed above
  │  │  │  ├─ r-glue 1.7.0 [required: any]
  │  │  │  │  └─ dependencies of r-glue displayed above
  │  │  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  │  │  └─ dependencies of r-magrittr displayed above
  │  │  │  ├─ r-openssl 2.2.0 [required: any]
  │  │  │  │  └─ dependencies of r-openssl displayed above
  │  │  │  ├─ r-r6 2.5.1 [required: any]
  │  │  │  │  └─ dependencies of r-r6 displayed above
  │  │  │  ├─ r-rappdirs 0.3.3 [required: any]
  │  │  │  │  └─ dependencies of r-rappdirs displayed above
  │  │  │  ├─ r-rlang 1.1.3 [required: >=1.1.0]
  │  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  │  ├─ r-vctrs 0.6.5 [required: >=0.6.3]
  │  │  │  │  └─ dependencies of r-vctrs displayed above
  │  │  │  └─ r-withr 3.0.0 [required: any]
  │  │  │     └─ dependencies of r-withr displayed above
  │  │  ├─ r-ini 0.3.1 [required: any]
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-jsonlite 1.8.8 [required: any]
  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  └─ r-rlang 1.1.3 [required: >=1.0.0]
  │  │     └─ dependencies of r-rlang displayed above
  │  ├─ r-glue 1.7.0 [required: >=1.3.0]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-jsonlite 1.8.8 [required: any]
  │  │  └─ dependencies of r-jsonlite displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-purrr 1.0.2 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rappdirs 0.3.3 [required: any]
  │  │  └─ dependencies of r-rappdirs displayed above
  │  ├─ r-rlang 1.1.3 [required: >=0.4.3]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-rprojroot 2.0.4 [required: >=1.2]
  │  │  └─ dependencies of r-rprojroot displayed above
  │  ├─ r-rstudioapi 0.16.0 [required: any]
  │  │  └─ dependencies of r-rstudioapi displayed above
  │  ├─ r-whisker 0.4.1 [required: any]
  │  │  └─ dependencies of r-whisker displayed above
  │  ├─ r-withr 3.0.0 [required: >=2.3.0]
  │  │  └─ dependencies of r-withr displayed above
  │  └─ r-yaml 2.3.8 [required: any]
  │     └─ dependencies of r-yaml displayed above
  └─ r-withr 3.0.0 [required: >=2.5.0]
     └─ dependencies of r-withr displayed above
jupyterhub==4.1.5
  ├─ __unix [required: any]
  ├─ configurable-http-proxy 4.6.1 [required: >=4]
  │  └─ nodejs 20.12.2 [required: >=20.9.0,<21.0a0]
  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │     ├─ icu 73.2 [required: >=73.2,<74.0a0]
  │     │  └─ dependencies of icu displayed above
  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  └─ dependencies of libgcc-ng displayed above
  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │     ├─ libuv 1.48.0 [required: >=1.48.0,<1.49.0a0]
  │     │  └─ libgcc-ng 14.2.0 [required: >=12]
  │     │     └─ dependencies of libgcc-ng displayed above
  │     ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │     │  └─ dependencies of libzlib displayed above
  │     ├─ openssl 3.4.1 [required: >=3.2.1,<4.0a0]
  │     │  └─ dependencies of openssl displayed above
  │     └─ zlib 1.2.13 [required: any]
  │        └─ dependencies of zlib displayed above
  ├─ jupyterhub-base 4.1.5 [required: 4.1.5, pyh31011fe_0]
  │  ├─ __unix [required: any]
  │  ├─ alembic 1.13.1 [required: >=1.4]
  │  │  ├─ importlib-metadata 7.1.0 [required: any]
  │  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  │  └─ zipp 3.17.0 [required: >=0.5]
  │  │  │     └─ python 3.11.9 [required: >=3.8]
  │  │  ├─ importlib_resources 6.4.0 [required: any]
  │  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  │  └─ zipp 3.17.0 [required: >=3.1.0]
  │  │  │     └─ dependencies of zipp displayed above
  │  │  ├─ mako 1.3.5 [required: any]
  │  │  │  ├─ importlib-metadata 7.1.0 [required: any]
  │  │  │  │  └─ dependencies of importlib-metadata displayed above
  │  │  │  ├─ markupsafe 2.1.5 [required: >=0.9.2]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  └─ python 3.11.9 [required: >=3.6]
  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  ├─ sqlalchemy 2.0.30 [required: >=1.3.0]
  │  │  │  ├─ greenlet 3.0.3 [required: !=0.4.17]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  └─ typing-extensions 4.11.0 [required: >=4.6.0]
  │  │  │     └─ typing_extensions 4.11.0 [required: 4.11.0, pyha770c72_0]
  │  │  │        └─ python 3.11.9 [required: >=3.8]
  │  │  └─ typing-extensions 4.11.0 [required: >=4]
  │  │     └─ dependencies of typing-extensions displayed above
  │  ├─ async_generator 1.10 [required: >=1.9]
  │  │  └─ python 3.11.9 [required: >2.7]
  │  ├─ certipy 0.1.3 [required: >=0.1.2]
  │  │  ├─ pyopenssl 24.0.0 [required: any]
  │  │  │  ├─ cryptography 42.0.7 [required: >=41.0.5,<43]
  │  │  │  │  ├─ cffi 1.16.0 [required: >=1.12]
  │  │  │  │  │  ├─ libffi 3.4.2 [required: >=3.4,<4.0a0]
  │  │  │  │  │  │  └─ dependencies of libffi displayed above
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  ├─ pycparser 2.22 [required: any]
  │  │  │  │  │  │  └─ python 3.11.9 [required: >=3.8]
  │  │  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  │  │  └─ dependencies of openssl displayed above
  │  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  └─ python 3.11.9 [required: >=3.3]
  │  ├─ importlib-metadata 7.1.0 [required: >=3.6]
  │  │  └─ dependencies of importlib-metadata displayed above
  │  ├─ jinja2 3.1.4 [required: >=2.11.0]
  │  │  ├─ markupsafe 2.1.5 [required: >=2.0]
  │  │  │  └─ dependencies of markupsafe displayed above
  │  │  └─ python 3.11.9 [required: >=3.7]
  │  ├─ jupyter_telemetry 0.1.0 [required: >=0.1.0]
  │  │  ├─ jsonschema 4.22.0 [required: any]
  │  │  │  ├─ attrs 23.2.0 [required: >=22.2.0]
  │  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  │  ├─ importlib_resources 6.4.0 [required: >=1.4.0]
  │  │  │  │  └─ dependencies of importlib_resources displayed above
  │  │  │  ├─ jsonschema-specifications 2023.12.1 [required: >=2023.03.6]
  │  │  │  │  ├─ importlib_resources 6.4.0 [required: >=1.4.0]
  │  │  │  │  │  └─ dependencies of importlib_resources displayed above
  │  │  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  │  │  └─ referencing 0.35.1 [required: >=0.31.0]
  │  │  │  │     ├─ attrs 23.2.0 [required: >=22.2.0]
  │  │  │  │     │  └─ dependencies of attrs displayed above
  │  │  │  │     ├─ python 3.11.9 [required: >=3.8]
  │  │  │  │     └─ rpds-py 0.18.1 [required: >=0.7.0]
  │  │  │  │        ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │        │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │        ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  │        └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  ├─ pkgutil-resolve-name 1.3.10 [required: >=1.3.10]
  │  │  │  │  └─ python 3.11.9 [required: >=3.6]
  │  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  │  ├─ referencing 0.35.1 [required: >=0.28.4]
  │  │  │  │  └─ dependencies of referencing displayed above
  │  │  │  └─ rpds-py 0.18.1 [required: >=0.7.1]
  │  │  │     └─ dependencies of rpds-py displayed above
  │  │  ├─ python 3.11.9 [required: >=3.5]
  │  │  ├─ python-json-logger 2.0.7 [required: any]
  │  │  │  └─ python 3.11.9 [required: >=3.6]
  │  │  ├─ ruamel.yaml 0.18.6 [required: any]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  └─ ruamel.yaml.clib 0.2.8 [required: >=0.1.2]
  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │     ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │     └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  └─ traitlets 5.14.3 [required: any]
  │  │     └─ python 3.11.9 [required: >=3.8]
  │  ├─ oauthlib 3.2.2 [required: >=3.0]
  │  │  ├─ blinker 1.8.2 [required: any]
  │  │  │  └─ python 3.11.9 [required: >=3.8]
  │  │  ├─ cryptography 42.0.7 [required: any]
  │  │  │  └─ dependencies of cryptography displayed above
  │  │  ├─ pyjwt 2.8.0 [required: >=1.0.0]
  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  └─ python 3.11.9 [required: >=3.6]
  │  ├─ packaging 24.0 [required: any]
  │  │  └─ python 3.11.9 [required: >=3.8]
  │  ├─ pamela 1.1.0 [required: any]
  │  │  └─ python 3.11.9 [required: >=3.5]
  │  ├─ prometheus_client 0.20.0 [required: >=0.4.0]
  │  │  └─ python 3.11.9 [required: >=3.8]
  │  ├─ python 3.11.9 [required: >=3.7]
  │  ├─ python-dateutil 2.9.0 [required: any]
  │  │  ├─ python 3.11.9 [required: >=3.7]
  │  │  └─ six 1.16.0 [required: >=1.5]
  │  │     └─ python 3.11.9 [required: any]
  │  ├─ requests 2.31.0 [required: any]
  │  │  ├─ certifi 2025.1.31 [required: >=2017.4.17]
  │  │  │  └─ python 3.11.9 [required: >=3.9]
  │  │  ├─ charset-normalizer 3.3.2 [required: >=2,<4]
  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  ├─ idna 3.7 [required: >=2.5,<4]
  │  │  │  └─ python 3.11.9 [required: >=3.6]
  │  │  ├─ python 3.11.9 [required: >=3.7]
  │  │  └─ urllib3 2.2.1 [required: >=1.21.1,<3]
  │  │     ├─ brotli-python 1.1.0 [required: >=1.0.9]
  │  │     │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  │  └─ dependencies of libgcc-ng displayed above
  │  │     │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │     │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │     │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │     ├─ pysocks 1.7.1 [required: >=1.5.6,<2.0,!=1.5.7]
  │  │     │  ├─ __unix [required: any]
  │  │     │  └─ python 3.11.9 [required: >=3.8]
  │  │     └─ python 3.11.9 [required: >=3.7]
  │  ├─ sqlalchemy 2.0.30 [required: >=1.4]
  │  │  └─ dependencies of sqlalchemy displayed above
  │  ├─ tornado 6.4 [required: >=5.1]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  └─ traitlets 5.14.3 [required: >=4.3.2]
  │     └─ dependencies of traitlets displayed above
  ├─ nodejs 20.12.2 [required: >=12]
  │  └─ dependencies of nodejs displayed above
  ├─ psutil 5.9.8 [required: any]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  ├─ pycurl 7.45.3 [required: any]
  │  ├─ libcurl 8.8.0 [required: >=8.5.0,<9.0a0]
  │  │  └─ dependencies of libcurl displayed above
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ openssl 3.4.1 [required: >=3.2.1,<4.0a0]
  │  │  └─ dependencies of openssl displayed above
  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  └─ python 3.11.9 [required: >=3.7]
nbclassic==1.0.0
  ├─ argon2-cffi 23.1.0 [required: any]
  │  ├─ argon2-cffi-bindings 21.2.0 [required: any]
  │  │  ├─ cffi 1.16.0 [required: >=1.0.1]
  │  │  │  └─ dependencies of cffi displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  ├─ python 3.11.9 [required: >=3.7]
  │  └─ typing-extensions 4.11.0 [required: any]
  │     └─ dependencies of typing-extensions displayed above
  ├─ ipykernel 6.29.3 [required: any]
  │  ├─ __linux [required: any]
  │  ├─ comm 0.2.2 [required: >=0.1.1]
  │  │  ├─ python 3.11.9 [required: >=3.6]
  │  │  └─ traitlets 5.14.3 [required: >=5.3]
  │  │     └─ dependencies of traitlets displayed above
  │  ├─ debugpy 1.8.1 [required: >=1.6.5]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  ├─ ipython 8.24.0 [required: >=7.23.1]
  │  │  ├─ __unix [required: any]
  │  │  ├─ decorator 5.1.1 [required: any]
  │  │  │  └─ python 3.11.9 [required: >=3.5]
  │  │  ├─ exceptiongroup 1.2.0 [required: any]
  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  ├─ jedi 0.19.1 [required: >=0.16]
  │  │  │  ├─ parso 0.8.4 [required: >=0.8.3,<0.9.0]
  │  │  │  │  └─ python 3.11.9 [required: >=3.6]
  │  │  │  └─ python 3.11.9 [required: >=3.6]
  │  │  ├─ matplotlib-inline 0.1.7 [required: any]
  │  │  │  ├─ python 3.11.9 [required: >=3.6]
  │  │  │  └─ traitlets 5.14.3 [required: any]
  │  │  │     └─ dependencies of traitlets displayed above
  │  │  ├─ pexpect 4.9.0 [required: >4.3]
  │  │  │  ├─ ptyprocess 0.7.0 [required: >=0.5]
  │  │  │  │  └─ python 3.11.9 [required: any]
  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  ├─ pickleshare 0.7.5 [required: any]
  │  │  │  └─ python 3.11.9 [required: >=3]
  │  │  ├─ prompt-toolkit 3.0.42 [required: >=3.0.41,<3.1.0]
  │  │  │  ├─ python 3.11.9 [required: >=3.7]
  │  │  │  └─ wcwidth 0.2.13 [required: any]
  │  │  │     └─ python 3.11.9 [required: >=3.8]
  │  │  ├─ pygments 2.18.0 [required: >=2.4.0]
  │  │  │  └─ python 3.11.9 [required: >=3.8]
  │  │  ├─ python 3.11.9 [required: >=3.10]
  │  │  ├─ stack_data 0.6.2 [required: any]
  │  │  │  ├─ asttokens 2.4.1 [required: any]
  │  │  │  │  ├─ python 3.11.9 [required: >=3.5]
  │  │  │  │  └─ six 1.16.0 [required: >=1.12.0]
  │  │  │  │     └─ dependencies of six displayed above
  │  │  │  ├─ executing 2.0.1 [required: any]
  │  │  │  │  └─ python 3.11.9 [required: >=2.7]
  │  │  │  ├─ pure_eval 0.2.2 [required: any]
  │  │  │  │  └─ python 3.11.9 [required: >=3.5]
  │  │  │  └─ python 3.11.9 [required: >=3.5]
  │  │  ├─ traitlets 5.14.3 [required: >=5.13.0]
  │  │  │  └─ dependencies of traitlets displayed above
  │  │  └─ typing_extensions 4.11.0 [required: >=4.6]
  │  │     └─ dependencies of typing_extensions displayed above
  │  ├─ jupyter_client 8.6.1 [required: >=6.1.12]
  │  │  ├─ importlib_metadata 7.1.0 [required: >=4.8.3]
  │  │  │  └─ importlib-metadata 7.1.0 [required: >=7.1.0,<7.1.1.0a0]
  │  │  │     └─ dependencies of importlib-metadata displayed above
  │  │  ├─ jupyter_core 5.7.2 [required: >=4.12,!=5.0.*]
  │  │  │  ├─ platformdirs 4.2.2 [required: >=2.5]
  │  │  │  │  └─ python 3.11.9 [required: >=3.8]
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  └─ traitlets 5.14.3 [required: >=5.3]
  │  │  │     └─ dependencies of traitlets displayed above
  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  ├─ python-dateutil 2.9.0 [required: >=2.8.2]
  │  │  │  └─ dependencies of python-dateutil displayed above
  │  │  ├─ pyzmq 26.0.3 [required: >=23.0]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libsodium 1.0.18 [required: >=1.0.18,<1.0.19.0a0]
  │  │  │  │  └─ dependencies of libsodium displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  └─ zeromq 4.3.5 [required: >=4.3.5,<4.4.0a0]
  │  │  │     └─ dependencies of zeromq displayed above
  │  │  ├─ tornado 6.4 [required: >=6.2]
  │  │  │  └─ dependencies of tornado displayed above
  │  │  └─ traitlets 5.14.3 [required: >=5.3]
  │  │     └─ dependencies of traitlets displayed above
  │  ├─ jupyter_core 5.7.2 [required: >=4.12,!=5.0.*]
  │  │  └─ dependencies of jupyter_core displayed above
  │  ├─ matplotlib-inline 0.1.7 [required: >=0.1]
  │  │  └─ dependencies of matplotlib-inline displayed above
  │  ├─ nest-asyncio 1.6.0 [required: any]
  │  │  └─ python 3.11.9 [required: >=3.5]
  │  ├─ packaging 24.0 [required: any]
  │  │  └─ dependencies of packaging displayed above
  │  ├─ psutil 5.9.8 [required: any]
  │  │  └─ dependencies of psutil displayed above
  │  ├─ python 3.11.9 [required: >=3.8]
  │  ├─ pyzmq 26.0.3 [required: >=24]
  │  │  └─ dependencies of pyzmq displayed above
  │  ├─ tornado 6.4 [required: >=6.1]
  │  │  └─ dependencies of tornado displayed above
  │  └─ traitlets 5.14.3 [required: >=5.4.0]
  │     └─ dependencies of traitlets displayed above
  ├─ ipython_genutils 0.2.0 [required: any]
  │  └─ python 3.11.9 [required: any]
  ├─ jinja2 3.1.4 [required: any]
  │  └─ dependencies of jinja2 displayed above
  ├─ jupyter_client 8.6.1 [required: >=6.1.1]
  │  └─ dependencies of jupyter_client displayed above
  ├─ jupyter_core 5.7.2 [required: >=4.6.1]
  │  └─ dependencies of jupyter_core displayed above
  ├─ jupyter_server 2.14.0 [required: >=1.8]
  │  ├─ anyio 4.3.0 [required: >=3.1.0]
  │  │  ├─ exceptiongroup 1.2.0 [required: >=1.0.2]
  │  │  │  └─ dependencies of exceptiongroup displayed above
  │  │  ├─ idna 3.7 [required: >=2.8]
  │  │  │  └─ dependencies of idna displayed above
  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  ├─ sniffio 1.3.1 [required: >=1.1]
  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  └─ typing_extensions 4.11.0 [required: >=4.1]
  │  │     └─ dependencies of typing_extensions displayed above
  │  ├─ argon2-cffi 23.1.0 [required: any]
  │  │  └─ dependencies of argon2-cffi displayed above
  │  ├─ jinja2 3.1.4 [required: any]
  │  │  └─ dependencies of jinja2 displayed above
  │  ├─ jupyter_client 8.6.1 [required: >=7.4.4]
  │  │  └─ dependencies of jupyter_client displayed above
  │  ├─ jupyter_core 5.7.2 [required: >=4.12,!=5.0.*]
  │  │  └─ dependencies of jupyter_core displayed above
  │  ├─ jupyter_events 0.10.0 [required: >=0.9.0]
  │  │  ├─ jsonschema-with-format-nongpl 4.22.0 [required: >=4.18.0]
  │  │  │  ├─ fqdn 1.5.1 [required: any]
  │  │  │  │  ├─ cached-property 1.5.2 [required: >=1.3.0]
  │  │  │  │  │  └─ cached_property 1.5.2 [required: >=1.5.2,<1.5.3.0a0]
  │  │  │  │  │     └─ python 3.11.9 [required: >=3.6]
  │  │  │  │  └─ python 3.11.9 [required: >=2.7,<4]
  │  │  │  ├─ idna 3.7 [required: any]
  │  │  │  │  └─ dependencies of idna displayed above
  │  │  │  ├─ isoduration 20.11.0 [required: any]
  │  │  │  │  ├─ arrow 1.3.0 [required: >=0.15.0]
  │  │  │  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  │  │  │  ├─ python-dateutil 2.9.0 [required: >=2.7.0]
  │  │  │  │  │  │  └─ dependencies of python-dateutil displayed above
  │  │  │  │  │  └─ types-python-dateutil 2.9.0.20240316 [required: >=2.8.10]
  │  │  │  │  │     └─ python 3.11.9 [required: >=3.6]
  │  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  │  ├─ jsonpointer 2.4 [required: >1.13]
  │  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  ├─ jsonschema 4.22.0 [required: >=4.22.0,<4.22.1.0a0]
  │  │  │  │  └─ dependencies of jsonschema displayed above
  │  │  │  ├─ python 3.11.9 [required: any]
  │  │  │  ├─ rfc3339-validator 0.1.4 [required: any]
  │  │  │  │  ├─ python 3.11.9 [required: >=3.5]
  │  │  │  │  └─ six 1.16.0 [required: any]
  │  │  │  │     └─ dependencies of six displayed above
  │  │  │  ├─ rfc3986-validator 0.1.1 [required: >0.1.0]
  │  │  │  │  └─ python 3.11.9 [required: any]
  │  │  │  ├─ uri-template 1.3.0 [required: any]
  │  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  │  └─ webcolors 1.13 [required: >=1.11]
  │  │  │     └─ python 3.11.9 [required: >=3.5]
  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  ├─ python-json-logger 2.0.7 [required: >=2.0.4]
  │  │  │  └─ dependencies of python-json-logger displayed above
  │  │  ├─ pyyaml 6.0.1 [required: >=5.3]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  └─ yaml 0.2.5 [required: >=0.2.5,<0.3.0a0]
  │  │  │     └─ libgcc-ng 14.2.0 [required: >=9.4.0]
  │  │  │        └─ dependencies of libgcc-ng displayed above
  │  │  ├─ referencing 0.35.1 [required: any]
  │  │  │  └─ dependencies of referencing displayed above
  │  │  ├─ rfc3339-validator 0.1.4 [required: any]
  │  │  │  └─ dependencies of rfc3339-validator displayed above
  │  │  ├─ rfc3986-validator 0.1.1 [required: >=0.1.1]
  │  │  │  └─ dependencies of rfc3986-validator displayed above
  │  │  └─ traitlets 5.14.3 [required: >=5.3]
  │  │     └─ dependencies of traitlets displayed above
  │  ├─ jupyter_server_terminals 0.5.3 [required: any]
  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  └─ terminado 0.18.1 [required: >=0.8.3]
  │  │     ├─ __linux [required: any]
  │  │     ├─ ptyprocess 0.7.0 [required: any]
  │  │     │  └─ dependencies of ptyprocess displayed above
  │  │     ├─ python 3.11.9 [required: >=3.8]
  │  │     └─ tornado 6.4 [required: >=6.1.0]
  │  │        └─ dependencies of tornado displayed above
  │  ├─ nbconvert-core 7.16.4 [required: >=6.4.4]
  │  │  ├─ beautifulsoup4 4.12.3 [required: any]
  │  │  │  ├─ python 3.11.9 [required: >=3.6]
  │  │  │  └─ soupsieve 2.5 [required: >=1.2]
  │  │  │     └─ python 3.11.9 [required: >=3.8]
  │  │  ├─ bleach 6.1.0 [required: any]
  │  │  │  ├─ packaging 24.0 [required: any]
  │  │  │  │  └─ dependencies of packaging displayed above
  │  │  │  ├─ python 3.11.9 [required: >=3.6]
  │  │  │  ├─ setuptools 69.5.1 [required: any]
  │  │  │  │  └─ dependencies of setuptools displayed above
  │  │  │  ├─ six 1.16.0 [required: >=1.9.0]
  │  │  │  │  └─ dependencies of six displayed above
  │  │  │  └─ webencodings 0.5.1 [required: any]
  │  │  │     └─ python 3.11.9 [required: >=2.6]
  │  │  ├─ defusedxml 0.7.1 [required: any]
  │  │  │  └─ python 3.11.9 [required: >=3.6]
  │  │  ├─ entrypoints 0.4 [required: >=0.2.2]
  │  │  │  └─ python 3.11.9 [required: >=3.6]
  │  │  ├─ jinja2 3.1.4 [required: >=3.0]
  │  │  │  └─ dependencies of jinja2 displayed above
  │  │  ├─ jupyter_core 5.7.2 [required: >=4.7]
  │  │  │  └─ dependencies of jupyter_core displayed above
  │  │  ├─ jupyterlab_pygments 0.3.0 [required: any]
  │  │  │  ├─ pygments 2.18.0 [required: >=2.4.1,<3]
  │  │  │  │  └─ dependencies of pygments displayed above
  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  ├─ markupsafe 2.1.5 [required: >=2.0]
  │  │  │  └─ dependencies of markupsafe displayed above
  │  │  ├─ mistune 3.0.2 [required: >=2.0.3,<4]
  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  ├─ nbclient 0.10.0 [required: >=0.5.0]
  │  │  │  ├─ jupyter_client 8.6.1 [required: >=6.1.12]
  │  │  │  │  └─ dependencies of jupyter_client displayed above
  │  │  │  ├─ jupyter_core 5.7.2 [required: >=4.12,!=5.0.*]
  │  │  │  │  └─ dependencies of jupyter_core displayed above
  │  │  │  ├─ nbformat 5.10.4 [required: >=5.1]
  │  │  │  │  ├─ jsonschema 4.22.0 [required: >=2.6]
  │  │  │  │  │  └─ dependencies of jsonschema displayed above
  │  │  │  │  ├─ jupyter_core 5.7.2 [required: >=4.12,!=5.0.*]
  │  │  │  │  │  └─ dependencies of jupyter_core displayed above
  │  │  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  │  │  ├─ python-fastjsonschema 2.19.1 [required: >=2.15]
  │  │  │  │  │  └─ python 3.11.9 [required: >=3.3]
  │  │  │  │  └─ traitlets 5.14.3 [required: >=5.1]
  │  │  │  │     └─ dependencies of traitlets displayed above
  │  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  │  └─ traitlets 5.14.3 [required: >=5.4]
  │  │  │     └─ dependencies of traitlets displayed above
  │  │  ├─ nbformat 5.10.4 [required: >=5.1]
  │  │  │  └─ dependencies of nbformat displayed above
  │  │  ├─ packaging 24.0 [required: any]
  │  │  │  └─ dependencies of packaging displayed above
  │  │  ├─ pandocfilters 1.5.0 [required: >=1.4.1]
  │  │  │  └─ python 3.11.9 [required: !=3.0,!=3.1,!=3.2,!=3.3]
  │  │  ├─ pygments 2.18.0 [required: >=2.4.1]
  │  │  │  └─ dependencies of pygments displayed above
  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  ├─ tinycss2 1.3.0 [required: any]
  │  │  │  ├─ python 3.11.9 [required: >=3.5]
  │  │  │  └─ webencodings 0.5.1 [required: >=0.4]
  │  │  │     └─ dependencies of webencodings displayed above
  │  │  └─ traitlets 5.14.3 [required: >=5.0]
  │  │     └─ dependencies of traitlets displayed above
  │  ├─ nbformat 5.10.4 [required: >=5.3.0]
  │  │  └─ dependencies of nbformat displayed above
  │  ├─ overrides 7.7.0 [required: any]
  │  │  ├─ python 3.11.9 [required: >=3.6]
  │  │  └─ typing_utils 0.1.0 [required: any]
  │  │     └─ python 3.11.9 [required: >=3.6.1]
  │  ├─ packaging 24.0 [required: any]
  │  │  └─ dependencies of packaging displayed above
  │  ├─ prometheus_client 0.20.0 [required: any]
  │  │  └─ dependencies of prometheus_client displayed above
  │  ├─ python 3.11.9 [required: >=3.8]
  │  ├─ pyzmq 26.0.3 [required: >=24]
  │  │  └─ dependencies of pyzmq displayed above
  │  ├─ send2trash 1.8.3 [required: >=1.8.2]
  │  │  ├─ __linux [required: any]
  │  │  └─ python 3.11.9 [required: >=3.7]
  │  ├─ terminado 0.18.1 [required: >=0.8.3]
  │  │  └─ dependencies of terminado displayed above
  │  ├─ tornado 6.4 [required: >=6.2.0]
  │  │  └─ dependencies of tornado displayed above
  │  ├─ traitlets 5.14.3 [required: >=5.6.0]
  │  │  └─ dependencies of traitlets displayed above
  │  └─ websocket-client 1.8.0 [required: any]
  │     └─ python 3.11.9 [required: >=3.8]
  ├─ nbconvert 7.16.4 [required: >=5]
  │  ├─ nbconvert-core 7.16.4 [required: 7.16.4, pyhd8ed1ab_0]
  │  │  └─ dependencies of nbconvert-core displayed above
  │  └─ nbconvert-pandoc 7.16.4 [required: 7.16.4, hd8ed1ab_0]
  │     ├─ nbconvert-core 7.16.4 [required: 7.16.4, pyhd8ed1ab_0]
  │     │  └─ dependencies of nbconvert-core displayed above
  │     └─ pandoc 3.2 [required: any]
  ├─ nbformat 5.10.4 [required: any]
  │  └─ dependencies of nbformat displayed above
  ├─ nest-asyncio 1.6.0 [required: >=1.5]
  │  └─ dependencies of nest-asyncio displayed above
  ├─ notebook-shim 0.2.4 [required: >=0.2.3]
  │  ├─ jupyter_server 2.14.0 [required: >=1.8,<3]
  │  │  └─ dependencies of jupyter_server displayed above
  │  └─ python 3.11.9 [required: >=3.7]
  ├─ prometheus_client 0.20.0 [required: any]
  │  └─ dependencies of prometheus_client displayed above
  ├─ python 3.11.9 [required: >=3.7]
  ├─ pyzmq 26.0.3 [required: >=17]
  │  └─ dependencies of pyzmq displayed above
  ├─ send2trash 1.8.3 [required: >=1.8.0]
  │  └─ dependencies of send2trash displayed above
  ├─ terminado 0.18.1 [required: >=0.8.3]
  │  └─ dependencies of terminado displayed above
  ├─ tornado 6.4 [required: >=6.1]
  │  └─ dependencies of tornado displayed above
  └─ traitlets 5.14.3 [required: >=4.2.1]
     └─ dependencies of traitlets displayed above
notebook==7.2.0
  ├─ jupyter_server 2.14.0 [required: >=2.4.0,<3]
  │  └─ dependencies of jupyter_server displayed above
  ├─ jupyterlab 4.2.0 [required: >=4.2.0,<4.3]
  │  ├─ async-lru 2.0.4 [required: >=1.0.0]
  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  └─ typing_extensions 4.11.0 [required: >=4.0.0]
  │  │     └─ dependencies of typing_extensions displayed above
  │  ├─ httpx 0.27.0 [required: >=0.25.0]
  │  │  ├─ anyio 4.3.0 [required: any]
  │  │  │  └─ dependencies of anyio displayed above
  │  │  ├─ certifi 2025.1.31 [required: any]
  │  │  │  └─ dependencies of certifi displayed above
  │  │  ├─ httpcore 1.0.5 [required: 1.*]
  │  │  │  ├─ anyio 4.3.0 [required: >=3.0,<5.0]
  │  │  │  │  └─ dependencies of anyio displayed above
  │  │  │  ├─ certifi 2025.1.31 [required: any]
  │  │  │  │  └─ dependencies of certifi displayed above
  │  │  │  ├─ h11 0.14.0 [required: >=0.13,<0.15]
  │  │  │  │  ├─ python 3.11.9 [required: >=3]
  │  │  │  │  └─ typing_extensions 4.11.0 [required: any]
  │  │  │  │     └─ dependencies of typing_extensions displayed above
  │  │  │  ├─ h2 4.1.0 [required: >=3,<5]
  │  │  │  │  ├─ hpack 4.0.0 [required: >=4.0,<5]
  │  │  │  │  │  └─ python 3.11.9 [required: any]
  │  │  │  │  ├─ hyperframe 6.0.1 [required: >=6.0,<7]
  │  │  │  │  │  └─ python 3.11.9 [required: >=3.6]
  │  │  │  │  └─ python 3.11.9 [required: >=3.6.1]
  │  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  │  └─ sniffio 1.3.1 [required: 1.*]
  │  │  │     └─ dependencies of sniffio displayed above
  │  │  ├─ idna 3.7 [required: any]
  │  │  │  └─ dependencies of idna displayed above
  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  └─ sniffio 1.3.1 [required: any]
  │  │     └─ dependencies of sniffio displayed above
  │  ├─ importlib_metadata 7.1.0 [required: >=4.8.3]
  │  │  └─ dependencies of importlib_metadata displayed above
  │  ├─ importlib_resources 6.4.0 [required: >=1.4]
  │  │  └─ dependencies of importlib_resources displayed above
  │  ├─ ipykernel 6.29.3 [required: >=6.5.0]
  │  │  └─ dependencies of ipykernel displayed above
  │  ├─ jinja2 3.1.4 [required: >=3.0.3]
  │  │  └─ dependencies of jinja2 displayed above
  │  ├─ jupyter-lsp 2.2.5 [required: >=2.0.0]
  │  │  ├─ importlib-metadata 7.1.0 [required: >=4.8.3]
  │  │  │  └─ dependencies of importlib-metadata displayed above
  │  │  ├─ jupyter_server 2.14.0 [required: >=1.1.2]
  │  │  │  └─ dependencies of jupyter_server displayed above
  │  │  └─ python 3.11.9 [required: >=3.8]
  │  ├─ jupyter_core 5.7.2 [required: any]
  │  │  └─ dependencies of jupyter_core displayed above
  │  ├─ jupyter_server 2.14.0 [required: >=2.4.0,<3]
  │  │  └─ dependencies of jupyter_server displayed above
  │  ├─ jupyterlab_server 2.27.1 [required: >=2.27.1,<3]
  │  │  ├─ babel 2.14.0 [required: >=2.10]
  │  │  │  ├─ python 3.11.9 [required: >=3.7]
  │  │  │  ├─ pytz 2024.1 [required: any]
  │  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  │  └─ setuptools 69.5.1 [required: any]
  │  │  │     └─ dependencies of setuptools displayed above
  │  │  ├─ importlib-metadata 7.1.0 [required: >=4.8.3]
  │  │  │  └─ dependencies of importlib-metadata displayed above
  │  │  ├─ jinja2 3.1.4 [required: >=3.0.3]
  │  │  │  └─ dependencies of jinja2 displayed above
  │  │  ├─ json5 0.9.25 [required: >=0.9.0]
  │  │  │  └─ python 3.11.9 [required: >=3.7,<4.0]
  │  │  ├─ jsonschema 4.22.0 [required: >=4.18]
  │  │  │  └─ dependencies of jsonschema displayed above
  │  │  ├─ jupyter_server 2.14.0 [required: >=1.21,<3]
  │  │  │  └─ dependencies of jupyter_server displayed above
  │  │  ├─ packaging 24.0 [required: >=21.3]
  │  │  │  └─ dependencies of packaging displayed above
  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  └─ requests 2.31.0 [required: >=2.31]
  │  │     └─ dependencies of requests displayed above
  │  ├─ notebook-shim 0.2.4 [required: >=0.2]
  │  │  └─ dependencies of notebook-shim displayed above
  │  ├─ packaging 24.0 [required: any]
  │  │  └─ dependencies of packaging displayed above
  │  ├─ python 3.11.9 [required: >=3.8]
  │  ├─ tomli 2.0.1 [required: >=1.2.2]
  │  │  └─ python 3.11.9 [required: >=3.7]
  │  ├─ tornado 6.4 [required: >=6.2.0]
  │  │  └─ dependencies of tornado displayed above
  │  └─ traitlets 5.14.3 [required: any]
  │     └─ dependencies of traitlets displayed above
  ├─ jupyterlab_server 2.27.1 [required: >=2.27.1,<3]
  │  └─ dependencies of jupyterlab_server displayed above
  ├─ notebook-shim 0.2.4 [required: >=0.2,<0.3]
  │  └─ dependencies of notebook-shim displayed above
  ├─ python 3.11.9 [required: >=3.8]
  └─ tornado 6.4 [required: >=6.2.0]
     └─ dependencies of tornado displayed above
```

## Installed R packages

Via `R -e 'as.data.frame(installed.packages())[,c("Package", "Version")]'`

| Name | Version |
| ----------------------------- | ------------------- |
|abind|1.4-5|
|airports|0.1.0|
|arkhe|1.10.0|
|askpass|1.2.0|
|assertthat|0.2.1|
|backports|1.4.1|
|base|4.3.3|
|base64enc|0.1-3|
|beeswarm|0.4.0|
|BiasedUrn|2.0.12|
|bit|4.0.5|
|bit64|4.0.5|
|bitops|1.0-7|
|blob|1.2.4|
|boot|1.3-31|
|brew|1.0-10|
|brio|1.1.5|
|broom|1.0.6|
|bslib|0.7.0|
|cachem|1.1.0|
|callr|3.7.6|
|caret|6.0-94|
|cellranger|1.1.0|
|cherryblossom|0.1.0|
|class|7.3-22|
|classInt|0.4-11|
|cli|3.6.4|
|clipr|0.8.0|
|clock|0.7.0|
|coda|0.19-4.1|
|codetools|0.2-20|
|colorspace|2.1-0|
|commonmark|1.9.1|
|compiler|4.3.3|
|config|0.3.2|
|conflicted|1.2.0|
|cowplot|1.1.3|
|cpp11|0.5.2|
|crayon|1.5.2|
|credentials|2.0.1|
|crosstalk|1.2.1|
|curl|5.1.0|
|data.table|1.15.2|
|datasets|4.3.3|
|DBI|1.2.2|
|dbplyr|2.5.0|
|deldir|2.0-4|
|DEoptimR|1.1-3-1|
|desc|1.4.3|
|devtools|2.4.5|
|diagram|1.6.5|
|dials|1.2.1|
|DiceDesign|1.10|
|diffobj|0.3.5|
|digest|0.6.37|
|doFuture|1.0.1|
|doSNOW|1.0.20|
|downlit|0.4.3|
|dplyr|1.1.4|
|dsbox|0.1.1|
|dtplyr|1.3.1|
|e1071|1.7-14|
|ellipsis|0.3.2|
|epiR|2.0.80|
|ergm|4.8.1|
|ergm.count|4.1.2|
|ergm.multi|0.2.1.1|
|evaluate|0.23|
|fansi|1.0.6|
|farver|2.1.2|
|fastmap|1.2.0|
|fastR2|1.2.4|
|fivethirtyeight|0.6.2|
|fivethirtyeightdata|0.1.0|
|flextable|0.9.7|
|FNN|1.1.4.1|
|fontawesome|0.5.2|
|fontBitstreamVera|0.1.1|
|fontLiberation|0.1.0|
|fontquiver|0.2.1|
|forcats|1.0.0|
|foreach|1.5.2|
|forecast|8.22.0|
|fracdiff|1.5-3|
|fs|1.6.4|
|furrr|0.3.1|
|future|1.33.2|
|future.apply|1.11.2|
|gapminder|1.0.0|
|gargle|1.5.2|
|gdtools|0.4.1|
|generics|0.1.3|
|gert|2.0.1|
|ggbeeswarm|0.7.2|
|ggformula|0.12.0|
|ggplot2|3.5.1|
|ggrepel|0.9.6|
|ggridges|0.5.6|
|ggtext|0.1.2|
|gh|1.4.1|
|gitcreds|0.1.2|
|globals|0.16.3|
|glue|1.8.0|
|goftest|1.2-3|
|googledrive|2.1.1|
|googlesheets4|1.1.1|
|gower|1.0.1|
|GPfit|1.0-8|
|graphics|4.3.3|
|grDevices|4.3.3|
|grid|4.3.3|
|gridExtra|2.3|
|gridtext|0.1.5|
|gstat|2.1-3|
|gtable|0.3.5|
|hardhat|1.3.1|
|haven|2.5.4|
|here|1.0.1|
|hexbin|1.28.3|
|highr|0.11|
|hms|1.1.3|
|htmltools|0.5.8.1|
|htmlwidgets|1.6.4|
|httpuv|1.6.15|
|httr|1.4.7|
|httr2|1.0.1|
|ids|1.0.1|
|igraph|2.1.4|
|infer|1.0.7|
|ini|0.3.1|
|intervals|0.15.5|
|ipred|0.9-14|
|IRdisplay|1.1|
|IRkernel|1.3.2|
|isoband|0.2.7|
|iterators|1.0.14|
|janitor|2.2.1|
|jpeg|0.1-10|
|jquerylib|0.1.4|
|jsonlite|1.9.1|
|keras|2.15.0|
|KernSmooth|2.23-24|
|khroma|1.16.0|
|knitr|1.49|
|labeling|0.4.3|
|labelled|2.14.0|
|later|1.3.2|
|lattice|0.22-6|
|lava|1.7.3|
|lazyeval|0.2.2|
|LearnBayes|2.15.1|
|lhs|1.1.6|
|lifecycle|1.0.4|
|listenv|0.9.1|
|lmtest|0.9-40|
|lpSolveAPI|5.5.2.0-17.12|
|lubridate|1.9.4|
|lwgeom|0.2-14|
|magrittr|2.0.3|
|markdown|1.13|
|MASS|7.3-60|
|Matrix|1.6-5|
|maxLik|1.5-2.1|
|memoise|2.0.1|
|methods|4.3.3|
|mgcv|1.9-1|
|mime|0.12|
|miniUI|0.1.1.1|
|miscTools|0.6-28|
|modeldata|1.3.0|
|modelenv|0.1.1|
|ModelMetrics|1.2.2.2|
|modelr|0.1.11|
|mosaic|1.9.1|
|mosaicCore|0.9.4.0|
|mosaicData|0.20.4|
|multcomp|1.4-28|
|munsell|0.5.1|
|mvtnorm|1.3-3|
|network|1.19.0|
|networkDynamic|0.11.5|
|networkLite|1.1.0|
|nlme|3.1-164|
|nloptr|2.1.1|
|nnet|7.3-19|
|numDeriv|2016.8-1.1|
|nycflights13|1.0.2|
|officer|0.6.7|
|openintro|2.5.0|
|openssl|2.2.0|
|pander|0.6.6|
|parallel|4.3.3|
|parallelly|1.37.1|
|parsnip|1.2.1|
|patchwork|1.3.0|
|pbdZMQ|0.3-11|
|pillar|1.10.1|
|pkgbuild|1.4.4|
|pkgconfig|2.0.3|
|pkgdown|2.0.9|
|pkgload|1.3.4|
|plogr|0.2.0|
|plotly|4.10.4|
|plyr|1.8.9|
|png|0.1-8|
|polyclip|1.10-7|
|praise|1.0.0|
|prettyunits|1.2.0|
|pROC|1.18.5|
|processx|3.8.4|
|prodlim|2023.08.28|
|profvis|0.3.8|
|progress|1.2.3|
|progressr|0.14.0|
|promises|1.3.0|
|proxy|0.4-27|
|ps|1.7.6|
|purrr|1.0.2|
|quadprog|1.5-8|
|quantmod|0.4.26|
|R6|2.5.1|
|ragg|1.3.2|
|randomForest|4.7-1.1|
|rappdirs|0.3.3|
|rbibutils|2.3|
|rcarbon|1.5.1|
|rcmdcheck|1.4.0|
|RColorBrewer|1.1-3|
|Rcpp|1.0.12|
|RcppArmadillo|0.12.8.3.0|
|RcppTOML|0.2.2|
|RCurl|1.98-1.14|
|Rdpack|2.6.2|
|readr|2.1.5|
|readxl|1.4.3|
|recipes|1.0.10|
|rematch|2.0.0|
|rematch2|2.1.2|
|remotes|2.5.0|
|repr|1.1.7|
|reprex|2.1.0|
|reshape2|1.4.4|
|reticulate|1.40.0|
|rlang|1.1.5|
|rle|0.9.2|
|rmarkdown|2.27|
|robustbase|0.99-4-1|
|RODBC|1.3-23|
|roxygen2|7.3.1|
|rpart|4.1.23|
|rprojroot|2.0.4|
|rsample|1.2.1|
|RSQLite|2.3.4|
|rstudioapi|0.16.0|
|rversions|2.1.2|
|rvest|1.0.4|
|s2|1.1.7|
|sandwich|3.1-1|
|sass|0.4.9|
|scales|1.3.0|
|selectr|0.4-2|
|sessioninfo|1.2.2|
|sf|1.0-16|
|sftime|0.3.0|
|shape|1.4.6.1|
|shiny|1.8.1.1|
|skimr|2.1.5|
|slider|0.3.1|
|sna|2.8|
|snakecase|0.11.1|
|snow|0.4-4|
|sourcetools|0.1.7-1|
|sp|2.2-0|
|spacetime|1.3-3|
|spatial|7.3-18|
|spatialreg|1.3-6|
|spatstat|3.3-1|
|spatstat.data|3.1-4|
|spatstat.explore|3.3-4|
|spatstat.geom|3.3-5|
|spatstat.linnet|3.2-5|
|spatstat.model|3.3-4|
|spatstat.random|3.3-2|
|spatstat.sparse|3.1-0|
|spatstat.univar|3.1-1|
|spatstat.utils|3.1-2|
|spData|2.3.4|
|spdep|1.3-10|
|splines|4.3.3|
|SQUAREM|2021.1|
|stars|0.6-6|
|statnet|2019.6|
|statnet.common|4.11.0|
|stats|4.3.3|
|stats4|4.3.3|
|stringi|1.8.4|
|stringr|1.5.1|
|survival|3.6-4|
|sys|3.4.2|
|systemfonts|1.2.1|
|tabula|3.2.0|
|tcltk|4.3.3|
|tensor|1.5|
|tensorflow|2.16.0|
|tergm|4.2.1|
|terra|1.7-78|
|testthat|3.2.1.1|
|textshaping|0.3.7|
|tfautograph|0.3.2|
|tfruns|1.5.3|
|TH.data|1.1-3|
|tibble|3.2.1|
|tidymodels|1.2.0|
|tidyr|1.3.1|
|tidyselect|1.2.1|
|tidyverse|2.0.0|
|timechange|0.3.0|
|timeDate|4032.109|
|tinytex|0.51|
|tools|4.3.3|
|trust|0.1-8|
|tseries|0.10-56|
|tsna|0.3.5|
|TTR|0.24.4|
|tune|1.2.1|
|tzdb|0.4.0|
|units|0.8-5|
|urca|1.3-3|
|urlchecker|1.0.1|
|usdata|0.3.1|
|usethis|2.2.3|
|utf8|1.2.4|
|utils|4.3.3|
|uuid|1.2-0|
|vctrs|0.6.5|
|vipor|0.4.7|
|viridis|0.6.5|
|viridisLite|0.4.2|
|visdat|0.6.0|
|vroom|1.6.5|
|waldo|0.5.2|
|warp|0.2.1|
|wesanderson|0.3.7|
|whisker|0.4.1|
|withr|3.0.0|
|wk|0.9.4|
|workflows|1.1.4|
|workflowsets|1.1.0|
|xfun|0.51|
|xml2|1.3.6|
|xopen|1.0.1|
|xtable|1.8-4|
|xts|0.13.2|
|yaml|2.3.8|
|yardstick|1.3.1|
|zeallot|0.1.0|
|zip|2.3.1|
|zoo|1.8-12|

