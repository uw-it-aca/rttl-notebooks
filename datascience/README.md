# UW-IT JupyterHub for Teaching datascience Notebook server
Docker image for UW-IT JupyterHub for Teaching datascience Notebook server. 
- Uses Ubuntu linux 24.04 (noble) and Python 3.13.8.
- Detailed information about base datascience Notebook is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-datascience-notebook
- General information about working with base images is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html
- Installed packages and versions can be viewed in this image's [Dockerfile](Dockerfile) using `pip list` or `conda list`. Dependency trees for both Pip and Conda packages shown below.
- All packages are installed into the default Conda environment, which is active on startup.
- The JupyterLab (v4.4.9) interface is installed and is set as default

## Running Notebook locally
- `docker run -p 8888:8888 us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-datascience-notebook:2.8.0`
- Console output will include localhost url with access token.

## Accessing server shell locally
- `docker run -it --entrypoint /bin/bash us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-datascience-notebook:2.8.0`


## Installed Python packages

### Pip packages
via `pipdeptree --exclude pipdeptree`

```
altair==5.5.0
├── Jinja2 [required: Any, installed: 3.1.6]
│   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
├── jsonschema [required: >=3.0, installed: 4.25.1]
│   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
├── narwhals [required: >=1.14.2, installed: 2.8.0]
├── packaging [required: Any, installed: 25.0]
└── typing_extensions [required: >=4.10.0, installed: 4.15.0]
async_generator==1.10
blinker==1.9.0
bokeh==3.8.0
├── Jinja2 [required: >=2.9, installed: 3.1.6]
│   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
├── contourpy [required: >=1.2, installed: 1.3.3]
│   └── numpy [required: >=1.25, installed: 2.3.3]
├── narwhals [required: >=1.13, installed: 2.8.0]
├── numpy [required: >=1.16, installed: 2.3.3]
├── packaging [required: >=16.8, installed: 25.0]
├── pandas [required: >=1.2, installed: 2.3.3]
│   ├── numpy [required: >=1.26.0, installed: 2.3.3]
│   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   └── six [required: >=1.5, installed: 1.17.0]
│   ├── pytz [required: >=2020.1, installed: 2025.2]
│   └── tzdata [required: >=2022.7, installed: 2025.2]
├── pillow [required: >=7.1.0, installed: 11.3.0]
├── PyYAML [required: >=3.10, installed: 6.0.3]
├── tornado [required: >=6.2, installed: 6.5.2]
└── xyzservices [required: >=2021.09.1, installed: 2025.4.0]
Bottleneck==1.6.0
└── numpy [required: Any, installed: 2.3.3]
Brotli==1.1.0
cached-property==1.5.2
conda-libmamba-solver==25.4.0
├── boltons [required: >=23.0.0, installed: 25.0.0]
└── conda [required: >=24.11, installed: 25.9.1]
    ├── archspec [required: >=0.2.3, installed: 0.2.5]
    ├── boltons [required: >=23.0.0, installed: 25.0.0]
    ├── charset-normalizer [required: Any, installed: 3.4.3]
    ├── conda-package-handling [required: >=2.2.0, installed: 2.4.0]
    │   └── conda_package_streaming [required: >=0.9.0, installed: 0.12.0]
    │       ├── requests [required: Any, installed: 2.32.5]
    │       │   ├── charset-normalizer [required: >=2,<4, installed: 3.4.3]
    │       │   ├── idna [required: >=2.5,<4, installed: 3.11]
    │       │   ├── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
    │       │   └── certifi [required: >=2017.4.17, installed: 2025.10.5]
    │       └── zstandard [required: >=0.15, installed: 0.25.0]
    ├── distro [required: >=1.5.0, installed: 1.9.0]
    ├── frozendict [required: >=2.4.2, installed: 2.4.6]
    ├── jsonpatch [required: >=1.32, installed: 1.33]
    │   └── jsonpointer [required: >=1.9, installed: 3.0.0]
    ├── menuinst [required: >=2, installed: 2.4.0]
    ├── packaging [required: >=23.0, installed: 25.0]
    ├── platformdirs [required: >=3.10.0, installed: 4.5.0]
    ├── pluggy [required: >=1.0.0, installed: 1.6.0]
    ├── pycosat [required: >=0.6.3, installed: 0.6.6]
    ├── requests [required: >=2.28.0,<3, installed: 2.32.5]
    │   ├── charset-normalizer [required: >=2,<4, installed: 3.4.3]
    │   ├── idna [required: >=2.5,<4, installed: 3.11]
    │   ├── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
    │   └── certifi [required: >=2017.4.17, installed: 2025.10.5]
    ├── ruamel.yaml [required: >=0.11.14,<0.19, installed: 0.18.15]
    │   └── ruamel.yaml.clib [required: >=0.2.7, installed: 0.2.12]
    ├── setuptools [required: >=60.0.0, installed: 80.9.0]
    ├── tqdm [required: >=4, installed: 4.67.1]
    ├── truststore [required: >=0.8.0, installed: 0.10.3]
    └── zstandard [required: >=0.15, installed: 0.25.0]
conda-tree==1.1.1
├── networkx [required: Any, installed: 3.5]
└── colorama [required: Any, installed: 0.4.6]
Cython==3.1.4
cytoolz==1.0.1
└── toolz [required: >=0.8.0, installed: 1.0.0]
dill==0.4.0
distributed==2025.9.1
├── click [required: >=8.0, installed: 8.3.0]
├── cloudpickle [required: >=3.0.0, installed: 3.1.1]
├── dask [required: ==2025.9.1, installed: 2025.9.1]
│   ├── click [required: >=8.1, installed: 8.3.0]
│   ├── cloudpickle [required: >=3.0.0, installed: 3.1.1]
│   ├── fsspec [required: >=2021.09.0, installed: 2025.9.0]
│   ├── packaging [required: >=20.0, installed: 25.0]
│   ├── partd [required: >=1.4.0, installed: 1.4.2]
│   │   ├── locket [required: Any, installed: 1.0.0]
│   │   └── toolz [required: Any, installed: 1.0.0]
│   ├── PyYAML [required: >=5.3.1, installed: 6.0.3]
│   └── toolz [required: >=0.10.0, installed: 1.0.0]
├── Jinja2 [required: >=2.10.3, installed: 3.1.6]
│   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
├── locket [required: >=1.0.0, installed: 1.0.0]
├── msgpack [required: >=1.0.2, installed: 1.1.2]
├── packaging [required: >=20.0, installed: 25.0]
├── psutil [required: >=5.8.0, installed: 7.1.0]
├── PyYAML [required: >=5.4.1, installed: 6.0.3]
├── sortedcontainers [required: >=2.0.5, installed: 2.4.0]
├── tblib [required: >=1.6.0, installed: 3.1.0]
├── toolz [required: >=0.11.2, installed: 1.0.0]
├── tornado [required: >=6.2.0, installed: 6.5.2]
├── urllib3 [required: >=1.26.5, installed: 1.26.20]
└── zict [required: >=3.0.0, installed: 3.0.0]
exceptiongroup==1.3.0
fiona==1.10.1
├── attrs [required: >=19.2.0, installed: 25.4.0]
├── certifi [required: Any, installed: 2025.10.5]
├── click [required: ~=8.0, installed: 8.3.0]
├── click-plugins [required: >=1.0, installed: 1.1.1.2]
│   └── click [required: >=4.0, installed: 8.3.0]
└── cligj [required: >=0.5, installed: 0.7.2]
    └── click [required: >=4.0, installed: 8.3.0]
folium==0.20.0
├── branca [required: >=0.6.0, installed: 0.8.2]
│   └── Jinja2 [required: >=3, installed: 3.1.6]
│       └── MarkupSafe [required: >=2.0, installed: 3.0.3]
├── Jinja2 [required: >=2.9, installed: 3.1.6]
│   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
├── numpy [required: Any, installed: 2.3.3]
├── requests [required: Any, installed: 2.32.5]
│   ├── charset-normalizer [required: >=2,<4, installed: 3.4.3]
│   ├── idna [required: >=2.5,<4, installed: 3.11]
│   ├── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
│   └── certifi [required: >=2017.4.17, installed: 2025.10.5]
└── xyzservices [required: Any, installed: 2025.4.0]
fqdn==1.5.1
geopandas==1.1.1
├── numpy [required: >=1.24, installed: 2.3.3]
├── pyogrio [required: >=0.7.2, installed: 0.11.1]
│   ├── certifi [required: Any, installed: 2025.10.5]
│   ├── numpy [required: Any, installed: 2.3.3]
│   └── packaging [required: Any, installed: 25.0]
├── packaging [required: Any, installed: 25.0]
├── pandas [required: >=2.0.0, installed: 2.3.3]
│   ├── numpy [required: >=1.26.0, installed: 2.3.3]
│   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   └── six [required: >=1.5, installed: 1.17.0]
│   ├── pytz [required: >=2020.1, installed: 2025.2]
│   └── tzdata [required: >=2022.7, installed: 2025.2]
├── pyproj [required: >=3.5.0, installed: 3.7.2]
│   └── certifi [required: Any, installed: 2025.10.5]
└── shapely [required: >=2.0.0, installed: 2.1.2]
    └── numpy [required: >=1.21, installed: 2.3.3]
gmpy2==2.2.1
h2==4.3.0
├── hyperframe [required: >=6.1,<7, installed: 6.1.0]
└── hpack [required: >=4.1,<5, installed: 4.1.0]
h5py==3.14.0
└── numpy [required: >=1.19.3, installed: 2.3.3]
imagecodecs==2025.8.2
└── numpy [required: Any, installed: 2.3.3]
ipyleaflet==0.20.0
├── branca [required: >=0.5.0, installed: 0.8.2]
│   └── Jinja2 [required: >=3, installed: 3.1.6]
│       └── MarkupSafe [required: >=2.0, installed: 3.0.3]
├── ipywidgets [required: >=7.6.0,<9, installed: 8.1.7]
│   ├── comm [required: >=0.1.3, installed: 0.2.3]
│   ├── ipython [required: >=6.1.0, installed: 9.6.0]
│   │   ├── decorator [required: Any, installed: 5.2.1]
│   │   ├── ipython_pygments_lexers [required: Any, installed: 1.1.1]
│   │   │   └── Pygments [required: Any, installed: 2.19.2]
│   │   ├── jedi [required: >=0.16, installed: 0.19.2]
│   │   │   └── parso [required: >=0.8.4,<0.9.0, installed: 0.8.5]
│   │   ├── matplotlib-inline [required: Any, installed: 0.1.7]
│   │   │   └── traitlets [required: Any, installed: 5.14.3]
│   │   ├── pexpect [required: >4.3, installed: 4.9.0]
│   │   │   └── ptyprocess [required: >=0.5, installed: 0.7.0]
│   │   ├── prompt_toolkit [required: >=3.0.41,<3.1.0, installed: 3.0.52]
│   │   │   └── wcwidth [required: Any, installed: 0.2.14]
│   │   ├── Pygments [required: >=2.4.0, installed: 2.19.2]
│   │   ├── stack_data [required: Any, installed: 0.6.3]
│   │   │   ├── executing [required: >=1.2.0, installed: 2.2.1]
│   │   │   ├── asttokens [required: >=2.1.0, installed: 3.0.0]
│   │   │   └── pure_eval [required: Any, installed: 0.2.3]
│   │   └── traitlets [required: >=5.13.0, installed: 5.14.3]
│   ├── traitlets [required: >=4.3.1, installed: 5.14.3]
│   ├── widgetsnbextension [required: ~=4.0.14, installed: 4.0.14]
│   └── jupyterlab_widgets [required: ~=3.0.15, installed: 3.0.15]
├── jupyter-leaflet [required: >=0.20,<0.21, installed: 0.20.0]
├── traittypes [required: >=0.2.1,<3, installed: 0.2.1]
│   └── traitlets [required: >=4.2.2, installed: 5.14.3]
└── xyzservices [required: >=2021.8.1, installed: 2025.4.0]
ipympl==0.9.8
├── ipython [required: <10, installed: 9.6.0]
│   ├── decorator [required: Any, installed: 5.2.1]
│   ├── ipython_pygments_lexers [required: Any, installed: 1.1.1]
│   │   └── Pygments [required: Any, installed: 2.19.2]
│   ├── jedi [required: >=0.16, installed: 0.19.2]
│   │   └── parso [required: >=0.8.4,<0.9.0, installed: 0.8.5]
│   ├── matplotlib-inline [required: Any, installed: 0.1.7]
│   │   └── traitlets [required: Any, installed: 5.14.3]
│   ├── pexpect [required: >4.3, installed: 4.9.0]
│   │   └── ptyprocess [required: >=0.5, installed: 0.7.0]
│   ├── prompt_toolkit [required: >=3.0.41,<3.1.0, installed: 3.0.52]
│   │   └── wcwidth [required: Any, installed: 0.2.14]
│   ├── Pygments [required: >=2.4.0, installed: 2.19.2]
│   ├── stack_data [required: Any, installed: 0.6.3]
│   │   ├── executing [required: >=1.2.0, installed: 2.2.1]
│   │   ├── asttokens [required: >=2.1.0, installed: 3.0.0]
│   │   └── pure_eval [required: Any, installed: 0.2.3]
│   └── traitlets [required: >=5.13.0, installed: 5.14.3]
├── ipywidgets [required: >=7.6.0,<9, installed: 8.1.7]
│   ├── comm [required: >=0.1.3, installed: 0.2.3]
│   ├── ipython [required: >=6.1.0, installed: 9.6.0]
│   │   ├── decorator [required: Any, installed: 5.2.1]
│   │   ├── ipython_pygments_lexers [required: Any, installed: 1.1.1]
│   │   │   └── Pygments [required: Any, installed: 2.19.2]
│   │   ├── jedi [required: >=0.16, installed: 0.19.2]
│   │   │   └── parso [required: >=0.8.4,<0.9.0, installed: 0.8.5]
│   │   ├── matplotlib-inline [required: Any, installed: 0.1.7]
│   │   │   └── traitlets [required: Any, installed: 5.14.3]
│   │   ├── pexpect [required: >4.3, installed: 4.9.0]
│   │   │   └── ptyprocess [required: >=0.5, installed: 0.7.0]
│   │   ├── prompt_toolkit [required: >=3.0.41,<3.1.0, installed: 3.0.52]
│   │   │   └── wcwidth [required: Any, installed: 0.2.14]
│   │   ├── Pygments [required: >=2.4.0, installed: 2.19.2]
│   │   ├── stack_data [required: Any, installed: 0.6.3]
│   │   │   ├── executing [required: >=1.2.0, installed: 2.2.1]
│   │   │   ├── asttokens [required: >=2.1.0, installed: 3.0.0]
│   │   │   └── pure_eval [required: Any, installed: 0.2.3]
│   │   └── traitlets [required: >=5.13.0, installed: 5.14.3]
│   ├── traitlets [required: >=4.3.1, installed: 5.14.3]
│   ├── widgetsnbextension [required: ~=4.0.14, installed: 4.0.14]
│   └── jupyterlab_widgets [required: ~=3.0.15, installed: 3.0.15]
├── matplotlib [required: >=3.5.0,<4, installed: 3.10.6]
│   ├── contourpy [required: >=1.0.1, installed: 1.3.3]
│   │   └── numpy [required: >=1.25, installed: 2.3.3]
│   ├── cycler [required: >=0.10, installed: 0.12.1]
│   ├── fonttools [required: >=4.22.0, installed: 4.60.1]
│   ├── kiwisolver [required: >=1.3.1, installed: 1.4.9]
│   ├── numpy [required: >=1.23, installed: 2.3.3]
│   ├── packaging [required: >=20.0, installed: 25.0]
│   ├── pillow [required: >=8, installed: 11.3.0]
│   ├── pyparsing [required: >=2.3.1, installed: 3.2.5]
│   └── python-dateutil [required: >=2.7, installed: 2.9.0.post0]
│       └── six [required: >=1.5, installed: 1.17.0]
├── numpy [required: Any, installed: 2.3.3]
├── pillow [required: Any, installed: 11.3.0]
└── traitlets [required: <6, installed: 5.14.3]
isoduration==20.11.0
└── arrow [required: >=0.15.0, installed: 1.3.0]
    ├── python-dateutil [required: >=2.7.0, installed: 2.9.0.post0]
    │   └── six [required: >=1.5, installed: 1.17.0]
    └── types-python-dateutil [required: >=2.8.10, installed: 2.9.0.20251008]
jupyter-pluto-proxy==0.1.2
└── jupyter_server_proxy [required: >=1.5.0, installed: 4.4.0]
    ├── aiohttp [required: Any, installed: 3.13.0]
    │   ├── aiohappyeyeballs [required: >=2.5.0, installed: 2.6.1]
    │   ├── aiosignal [required: >=1.4.0, installed: 1.4.0]
    │   │   └── frozenlist [required: >=1.1.0, installed: 1.7.0]
    │   ├── attrs [required: >=17.3.0, installed: 25.4.0]
    │   ├── frozenlist [required: >=1.1.1, installed: 1.7.0]
    │   ├── multidict [required: >=4.5,<7.0, installed: 6.6.3]
    │   ├── propcache [required: >=0.2.0, installed: 0.3.1]
    │   └── yarl [required: >=1.17.0,<2.0, installed: 1.20.1]
    │       ├── idna [required: >=2.0, installed: 3.11]
    │       ├── multidict [required: >=4.0, installed: 6.6.3]
    │       └── propcache [required: >=0.2.1, installed: 0.3.1]
    ├── jupyter_server [required: >=1.24.0, installed: 2.17.0]
    │   ├── anyio [required: >=3.1.0, installed: 4.11.0]
    │   │   ├── idna [required: >=2.8, installed: 3.11]
    │   │   └── sniffio [required: >=1.1, installed: 1.3.1]
    │   ├── argon2-cffi [required: >=21.1, installed: 25.1.0]
    │   │   └── argon2-cffi-bindings [required: Any, installed: 25.1.0]
    │   │       └── cffi [required: >=1.0.1, installed: 2.0.0]
    │   │           └── pycparser [required: Any, installed: 2.22]
    │   ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
    │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
    │   ├── jupyter_client [required: >=7.4.4, installed: 8.6.3]
    │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
    │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
    │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
    │   │   │   └── six [required: >=1.5, installed: 1.17.0]
    │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
    │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
    │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
    │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
    │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   ├── jupyter-events [required: >=0.11.0, installed: 0.12.0]
    │   │   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
    │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
    │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
    │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
    │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
    │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
    │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
    │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
    │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
    │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
    │   │   ├── packaging [required: Any, installed: 25.0]
    │   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
    │   │   ├── PyYAML [required: >=5.3, installed: 6.0.3]
    │   │   ├── referencing [required: Any, installed: 0.36.2]
    │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
    │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
    │   │   ├── rfc3339_validator [required: Any, installed: 0.1.4]
    │   │   │   └── six [required: Any, installed: 1.17.0]
    │   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
    │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
    │   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
    │   │       ├── ptyprocess [required: Any, installed: 0.7.0]
    │   │       └── tornado [required: >=6.1.0, installed: 6.5.2]
    │   ├── nbconvert [required: >=6.4.4, installed: 7.16.6]
    │   │   ├── beautifulsoup4 [required: Any, installed: 4.14.2]
    │   │   │   ├── soupsieve [required: >1.2, installed: 2.8]
    │   │   │   └── typing_extensions [required: >=4.0.0, installed: 4.15.0]
    │   │   ├── bleach [required: !=5.0.0, installed: 6.2.0]
    │   │   │   └── webencodings [required: Any, installed: 0.5.1]
    │   │   ├── defusedxml [required: Any, installed: 0.7.1]
    │   │   ├── Jinja2 [required: >=3.0, installed: 3.1.6]
    │   │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
    │   │   ├── jupyter_core [required: >=4.7, installed: 5.8.1]
    │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
    │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
    │   │   ├── MarkupSafe [required: >=2.0, installed: 3.0.3]
    │   │   ├── mistune [required: >=2.0.3,<4, installed: 3.1.4]
    │   │   ├── nbclient [required: >=0.5.0, installed: 0.10.2]
    │   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.3]
    │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
    │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
    │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
    │   │   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
    │   │   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
    │   │   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
    │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
    │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
    │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
    │   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
    │   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
    │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
    │   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
    │   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
    │   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
    │   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
    │   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
    │   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
    │   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
    │   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
    │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
    │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
    │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
    │   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
    │   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
    │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
    │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
    │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
    │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
    │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
    │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
    │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
    │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
    │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
    │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
    │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
    │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
    │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
    │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
    │   │   ├── packaging [required: Any, installed: 25.0]
    │   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
    │   │   ├── Pygments [required: >=2.4.1, installed: 2.19.2]
    │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
    │   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
    │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
    │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
    │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
    │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
    │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
    │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
    │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
    │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
    │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
    │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
    │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
    │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
    │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
    │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
    │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
    │   ├── packaging [required: >=22.0, installed: 25.0]
    │   ├── prometheus_client [required: >=0.9, installed: 0.23.1]
    │   ├── pyzmq [required: >=24, installed: 27.1.0]
    │   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
    │   ├── terminado [required: >=0.8.3, installed: 0.18.1]
    │   │   ├── ptyprocess [required: Any, installed: 0.7.0]
    │   │   └── tornado [required: >=6.1.0, installed: 6.5.2]
    │   ├── tornado [required: >=6.2.0, installed: 6.5.2]
    │   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
    │   └── websocket-client [required: >=1.7, installed: 1.9.0]
    ├── simpervisor [required: >=1.0.0, installed: 1.0.0]
    ├── tornado [required: >=6.1.0, installed: 6.5.2]
    └── traitlets [required: >=5.1.0, installed: 5.14.3]
jupyter-resource-usage==1.2.0
├── jupyter_server [required: >=2.0, installed: 2.17.0]
│   ├── anyio [required: >=3.1.0, installed: 4.11.0]
│   │   ├── idna [required: >=2.8, installed: 3.11]
│   │   └── sniffio [required: >=1.1, installed: 1.3.1]
│   ├── argon2-cffi [required: >=21.1, installed: 25.1.0]
│   │   └── argon2-cffi-bindings [required: Any, installed: 25.1.0]
│   │       └── cffi [required: >=1.0.1, installed: 2.0.0]
│   │           └── pycparser [required: Any, installed: 2.22]
│   ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
│   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   ├── jupyter_client [required: >=7.4.4, installed: 8.6.3]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter-events [required: >=0.11.0, installed: 0.12.0]
│   │   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   ├── packaging [required: Any, installed: 25.0]
│   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │   ├── PyYAML [required: >=5.3, installed: 6.0.3]
│   │   ├── referencing [required: Any, installed: 0.36.2]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   ├── rfc3339_validator [required: Any, installed: 0.1.4]
│   │   │   └── six [required: Any, installed: 1.17.0]
│   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       └── tornado [required: >=6.1.0, installed: 6.5.2]
│   ├── nbconvert [required: >=6.4.4, installed: 7.16.6]
│   │   ├── beautifulsoup4 [required: Any, installed: 4.14.2]
│   │   │   ├── soupsieve [required: >1.2, installed: 2.8]
│   │   │   └── typing_extensions [required: >=4.0.0, installed: 4.15.0]
│   │   ├── bleach [required: !=5.0.0, installed: 6.2.0]
│   │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │   ├── Jinja2 [required: >=3.0, installed: 3.1.6]
│   │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   ├── jupyter_core [required: >=4.7, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │   ├── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   ├── mistune [required: >=2.0.3,<4, installed: 3.1.4]
│   │   ├── nbclient [required: >=0.5.0, installed: 0.10.2]
│   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.3]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── packaging [required: Any, installed: 25.0]
│   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │   ├── Pygments [required: >=2.4.1, installed: 2.19.2]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── packaging [required: >=22.0, installed: 25.0]
│   ├── prometheus_client [required: >=0.9, installed: 0.23.1]
│   ├── pyzmq [required: >=24, installed: 27.1.0]
│   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   └── tornado [required: >=6.1.0, installed: 6.5.2]
│   ├── tornado [required: >=6.2.0, installed: 6.5.2]
│   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   └── websocket-client [required: >=1.7, installed: 1.9.0]
├── prometheus_client [required: Any, installed: 0.23.1]
├── psutil [required: >=5.6, installed: 7.1.0]
└── pyzmq [required: >=19, installed: 27.1.0]
jupyterhub==5.4.0
├── alembic [required: >=1.4, installed: 1.17.0]
│   ├── SQLAlchemy [required: >=1.4.0, installed: 2.0.44]
│   │   ├── greenlet [required: >=1, installed: 3.2.4]
│   │   └── typing_extensions [required: >=4.6.0, installed: 4.15.0]
│   ├── Mako [required: Any, installed: 1.3.10]
│   │   └── MarkupSafe [required: >=0.9.2, installed: 3.0.3]
│   └── typing_extensions [required: >=4.12, installed: 4.15.0]
├── certipy [required: >=0.1.2, installed: 0.2.2]
│   └── cryptography [required: Any, installed: 46.0.2]
│       └── cffi [required: >=1.14, installed: 2.0.0]
│           └── pycparser [required: Any, installed: 2.22]
├── idna [required: Any, installed: 3.11]
├── Jinja2 [required: >=2.11.0, installed: 3.1.6]
│   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
├── jupyter-events [required: Any, installed: 0.12.0]
│   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
│   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   ├── packaging [required: Any, installed: 25.0]
│   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   ├── PyYAML [required: >=5.3, installed: 6.0.3]
│   ├── referencing [required: Any, installed: 0.36.2]
│   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   ├── rfc3339_validator [required: Any, installed: 0.1.4]
│   │   └── six [required: Any, installed: 1.17.0]
│   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   └── traitlets [required: >=5.3, installed: 5.14.3]
├── oauthlib [required: >=3.0, installed: 3.3.1]
├── packaging [required: Any, installed: 25.0]
├── pamela [required: >=1.1.0, installed: 1.2.0]
├── prometheus_client [required: >=0.5.0, installed: 0.23.1]
├── pydantic [required: >=2, installed: 2.12.0]
│   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   ├── pydantic_core [required: ==2.41.1, installed: 2.41.1]
│   │   └── typing_extensions [required: >=4.14.1, installed: 4.15.0]
│   ├── typing_extensions [required: >=4.14.1, installed: 4.15.0]
│   └── typing-inspection [required: >=0.4.2, installed: 0.4.2]
│       └── typing_extensions [required: >=4.12.0, installed: 4.15.0]
├── python-dateutil [required: Any, installed: 2.9.0.post0]
│   └── six [required: >=1.5, installed: 1.17.0]
├── requests [required: Any, installed: 2.32.5]
│   ├── charset-normalizer [required: >=2,<4, installed: 3.4.3]
│   ├── idna [required: >=2.5,<4, installed: 3.11]
│   ├── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
│   └── certifi [required: >=2017.4.17, installed: 2025.10.5]
├── SQLAlchemy [required: >=1.4.1, installed: 2.0.44]
│   ├── greenlet [required: >=1, installed: 3.2.4]
│   └── typing_extensions [required: >=4.6.0, installed: 4.15.0]
├── tornado [required: >=5.1, installed: 6.5.2]
└── traitlets [required: >=4.3.2, installed: 5.14.3]
jupyterlab_a11y_checker==0.2.2
jupyterlab_git==0.51.2
├── jupyter_server [required: >=2.0.1,<3, installed: 2.17.0]
│   ├── anyio [required: >=3.1.0, installed: 4.11.0]
│   │   ├── idna [required: >=2.8, installed: 3.11]
│   │   └── sniffio [required: >=1.1, installed: 1.3.1]
│   ├── argon2-cffi [required: >=21.1, installed: 25.1.0]
│   │   └── argon2-cffi-bindings [required: Any, installed: 25.1.0]
│   │       └── cffi [required: >=1.0.1, installed: 2.0.0]
│   │           └── pycparser [required: Any, installed: 2.22]
│   ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
│   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   ├── jupyter_client [required: >=7.4.4, installed: 8.6.3]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter-events [required: >=0.11.0, installed: 0.12.0]
│   │   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   ├── packaging [required: Any, installed: 25.0]
│   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │   ├── PyYAML [required: >=5.3, installed: 6.0.3]
│   │   ├── referencing [required: Any, installed: 0.36.2]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   ├── rfc3339_validator [required: Any, installed: 0.1.4]
│   │   │   └── six [required: Any, installed: 1.17.0]
│   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       └── tornado [required: >=6.1.0, installed: 6.5.2]
│   ├── nbconvert [required: >=6.4.4, installed: 7.16.6]
│   │   ├── beautifulsoup4 [required: Any, installed: 4.14.2]
│   │   │   ├── soupsieve [required: >1.2, installed: 2.8]
│   │   │   └── typing_extensions [required: >=4.0.0, installed: 4.15.0]
│   │   ├── bleach [required: !=5.0.0, installed: 6.2.0]
│   │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │   ├── Jinja2 [required: >=3.0, installed: 3.1.6]
│   │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   ├── jupyter_core [required: >=4.7, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │   ├── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   ├── mistune [required: >=2.0.3,<4, installed: 3.1.4]
│   │   ├── nbclient [required: >=0.5.0, installed: 0.10.2]
│   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.3]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── packaging [required: Any, installed: 25.0]
│   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │   ├── Pygments [required: >=2.4.1, installed: 2.19.2]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── packaging [required: >=22.0, installed: 25.0]
│   ├── prometheus_client [required: >=0.9, installed: 0.23.1]
│   ├── pyzmq [required: >=24, installed: 27.1.0]
│   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   └── tornado [required: >=6.1.0, installed: 6.5.2]
│   ├── tornado [required: >=6.2.0, installed: 6.5.2]
│   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   └── websocket-client [required: >=1.7, installed: 1.9.0]
├── nbdime [required: ~=4.0.1, installed: 4.0.2]
│   ├── colorama [required: Any, installed: 0.4.6]
│   ├── GitPython [required: !=2.1.6,!=2.1.5,!=2.1.4, installed: 3.1.45]
│   │   └── gitdb [required: >=4.0.1,<5, installed: 4.0.12]
│   │       └── smmap [required: >=3.0.1,<6, installed: 5.0.2]
│   ├── Jinja2 [required: >=2.9, installed: 3.1.6]
│   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   ├── jupyter_server [required: Any, installed: 2.17.0]
│   │   ├── anyio [required: >=3.1.0, installed: 4.11.0]
│   │   │   ├── idna [required: >=2.8, installed: 3.11]
│   │   │   └── sniffio [required: >=1.1, installed: 1.3.1]
│   │   ├── argon2-cffi [required: >=21.1, installed: 25.1.0]
│   │   │   └── argon2-cffi-bindings [required: Any, installed: 25.1.0]
│   │   │       └── cffi [required: >=1.0.1, installed: 2.0.0]
│   │   │           └── pycparser [required: Any, installed: 2.22]
│   │   ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
│   │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   ├── jupyter_client [required: >=7.4.4, installed: 8.6.3]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter-events [required: >=0.11.0, installed: 0.12.0]
│   │   │   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   ├── packaging [required: Any, installed: 25.0]
│   │   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │   │   ├── PyYAML [required: >=5.3, installed: 6.0.3]
│   │   │   ├── referencing [required: Any, installed: 0.36.2]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   ├── rfc3339_validator [required: Any, installed: 0.1.4]
│   │   │   │   └── six [required: Any, installed: 1.17.0]
│   │   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   │       └── tornado [required: >=6.1.0, installed: 6.5.2]
│   │   ├── nbconvert [required: >=6.4.4, installed: 7.16.6]
│   │   │   ├── beautifulsoup4 [required: Any, installed: 4.14.2]
│   │   │   │   ├── soupsieve [required: >1.2, installed: 2.8]
│   │   │   │   └── typing_extensions [required: >=4.0.0, installed: 4.15.0]
│   │   │   ├── bleach [required: !=5.0.0, installed: 6.2.0]
│   │   │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │   │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │   │   ├── Jinja2 [required: >=3.0, installed: 3.1.6]
│   │   │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   │   ├── jupyter_core [required: >=4.7, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │   │   ├── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   │   ├── mistune [required: >=2.0.3,<4, installed: 3.1.4]
│   │   │   ├── nbclient [required: >=0.5.0, installed: 0.10.2]
│   │   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.3]
│   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   │   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   │   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   ├── packaging [required: Any, installed: 25.0]
│   │   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │   │   ├── Pygments [required: >=2.4.1, installed: 2.19.2]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── packaging [required: >=22.0, installed: 25.0]
│   │   ├── prometheus_client [required: >=0.9, installed: 0.23.1]
│   │   ├── pyzmq [required: >=24, installed: 27.1.0]
│   │   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   │   ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   │   └── tornado [required: >=6.1.0, installed: 6.5.2]
│   │   ├── tornado [required: >=6.2.0, installed: 6.5.2]
│   │   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   │   └── websocket-client [required: >=1.7, installed: 1.9.0]
│   ├── jupyter_server_mathjax [required: >=0.2.2, installed: 0.2.6]
│   │   └── jupyter_server [required: >=1.1, installed: 2.17.0]
│   │       ├── anyio [required: >=3.1.0, installed: 4.11.0]
│   │       │   ├── idna [required: >=2.8, installed: 3.11]
│   │       │   └── sniffio [required: >=1.1, installed: 1.3.1]
│   │       ├── argon2-cffi [required: >=21.1, installed: 25.1.0]
│   │       │   └── argon2-cffi-bindings [required: Any, installed: 25.1.0]
│   │       │       └── cffi [required: >=1.0.1, installed: 2.0.0]
│   │       │           └── pycparser [required: Any, installed: 2.22]
│   │       ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
│   │       │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │       ├── jupyter_client [required: >=7.4.4, installed: 8.6.3]
│   │       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │       │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │       │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │       │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       ├── jupyter-events [required: >=0.11.0, installed: 0.12.0]
│   │       │   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
│   │       │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │       │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │       │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │       │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │       │   ├── packaging [required: Any, installed: 25.0]
│   │       │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │       │   ├── PyYAML [required: >=5.3, installed: 6.0.3]
│   │       │   ├── referencing [required: Any, installed: 0.36.2]
│   │       │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   ├── rfc3339_validator [required: Any, installed: 0.1.4]
│   │       │   │   └── six [required: Any, installed: 1.17.0]
│   │       │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │       │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       │       └── tornado [required: >=6.1.0, installed: 6.5.2]
│   │       ├── nbconvert [required: >=6.4.4, installed: 7.16.6]
│   │       │   ├── beautifulsoup4 [required: Any, installed: 4.14.2]
│   │       │   │   ├── soupsieve [required: >1.2, installed: 2.8]
│   │       │   │   └── typing_extensions [required: >=4.0.0, installed: 4.15.0]
│   │       │   ├── bleach [required: !=5.0.0, installed: 6.2.0]
│   │       │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │       │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │       │   ├── Jinja2 [required: >=3.0, installed: 3.1.6]
│   │       │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │       │   ├── jupyter_core [required: >=4.7, installed: 5.8.1]
│   │       │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │       │   ├── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │       │   ├── mistune [required: >=2.0.3,<4, installed: 3.1.4]
│   │       │   ├── nbclient [required: >=0.5.0, installed: 0.10.2]
│   │       │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.3]
│   │       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │       │   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │       │   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │       │   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │       │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │       │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │       │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │       │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │       │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │       │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │       │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │       │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │       │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │       │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │       │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       │   ├── packaging [required: Any, installed: 25.0]
│   │       │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │       │   ├── Pygments [required: >=2.4.1, installed: 2.19.2]
│   │       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │       │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │       │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │       │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │       │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │       │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │       │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       ├── packaging [required: >=22.0, installed: 25.0]
│   │       ├── prometheus_client [required: >=0.9, installed: 0.23.1]
│   │       ├── pyzmq [required: >=24, installed: 27.1.0]
│   │       ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   │       ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       │   └── tornado [required: >=6.1.0, installed: 6.5.2]
│   │       ├── tornado [required: >=6.2.0, installed: 6.5.2]
│   │       ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   │       └── websocket-client [required: >=1.7, installed: 1.9.0]
│   ├── nbformat [required: Any, installed: 5.10.4]
│   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── Pygments [required: Any, installed: 2.19.2]
│   ├── requests [required: Any, installed: 2.32.5]
│   │   ├── charset-normalizer [required: >=2,<4, installed: 3.4.3]
│   │   ├── idna [required: >=2.5,<4, installed: 3.11]
│   │   ├── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
│   │   └── certifi [required: >=2017.4.17, installed: 2025.10.5]
│   └── tornado [required: Any, installed: 6.5.2]
├── nbformat [required: Any, installed: 5.10.4]
│   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   └── traitlets [required: >=5.1, installed: 5.14.3]
├── packaging [required: Any, installed: 25.0]
├── pexpect [required: Any, installed: 4.9.0]
│   └── ptyprocess [required: >=0.5, installed: 0.7.0]
└── traitlets [required: ~=5.0, installed: 5.14.3]
libmambapy==2.3.2
lz4==4.4.4
munkres==1.1.4
nbclassic==1.3.3
├── ipykernel [required: Any, installed: 7.0.0]
│   ├── comm [required: >=0.1.1, installed: 0.2.3]
│   ├── debugpy [required: >=1.6.5, installed: 1.8.17]
│   ├── ipython [required: >=7.23.1, installed: 9.6.0]
│   │   ├── decorator [required: Any, installed: 5.2.1]
│   │   ├── ipython_pygments_lexers [required: Any, installed: 1.1.1]
│   │   │   └── Pygments [required: Any, installed: 2.19.2]
│   │   ├── jedi [required: >=0.16, installed: 0.19.2]
│   │   │   └── parso [required: >=0.8.4,<0.9.0, installed: 0.8.5]
│   │   ├── matplotlib-inline [required: Any, installed: 0.1.7]
│   │   │   └── traitlets [required: Any, installed: 5.14.3]
│   │   ├── pexpect [required: >4.3, installed: 4.9.0]
│   │   │   └── ptyprocess [required: >=0.5, installed: 0.7.0]
│   │   ├── prompt_toolkit [required: >=3.0.41,<3.1.0, installed: 3.0.52]
│   │   │   └── wcwidth [required: Any, installed: 0.2.14]
│   │   ├── Pygments [required: >=2.4.0, installed: 2.19.2]
│   │   ├── stack_data [required: Any, installed: 0.6.3]
│   │   │   ├── executing [required: >=1.2.0, installed: 2.2.1]
│   │   │   ├── asttokens [required: >=2.1.0, installed: 3.0.0]
│   │   │   └── pure_eval [required: Any, installed: 0.2.3]
│   │   └── traitlets [required: >=5.13.0, installed: 5.14.3]
│   ├── jupyter_client [required: >=8.0.0, installed: 8.6.3]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── matplotlib-inline [required: >=0.1, installed: 0.1.7]
│   │   └── traitlets [required: Any, installed: 5.14.3]
│   ├── nest_asyncio [required: >=1.4, installed: 1.6.0]
│   ├── packaging [required: >=22, installed: 25.0]
│   ├── psutil [required: >=5.7, installed: 7.1.0]
│   ├── pyzmq [required: >=25, installed: 27.1.0]
│   ├── tornado [required: >=6.2, installed: 6.5.2]
│   └── traitlets [required: >=5.4.0, installed: 5.14.3]
├── ipython_genutils [required: Any, installed: 0.2.0]
├── nest_asyncio [required: >=1.5, installed: 1.6.0]
└── notebook_shim [required: >=0.2.3, installed: 0.2.4]
    └── jupyter_server [required: >=1.8,<3, installed: 2.17.0]
        ├── anyio [required: >=3.1.0, installed: 4.11.0]
        │   ├── idna [required: >=2.8, installed: 3.11]
        │   └── sniffio [required: >=1.1, installed: 1.3.1]
        ├── argon2-cffi [required: >=21.1, installed: 25.1.0]
        │   └── argon2-cffi-bindings [required: Any, installed: 25.1.0]
        │       └── cffi [required: >=1.0.1, installed: 2.0.0]
        │           └── pycparser [required: Any, installed: 2.22]
        ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
        │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
        ├── jupyter_client [required: >=7.4.4, installed: 8.6.3]
        │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
        │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
        │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
        │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
        │   │   └── six [required: >=1.5, installed: 1.17.0]
        │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
        │   ├── tornado [required: >=6.2, installed: 6.5.2]
        │   └── traitlets [required: >=5.3, installed: 5.14.3]
        ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
        │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
        │   └── traitlets [required: >=5.3, installed: 5.14.3]
        ├── jupyter-events [required: >=0.11.0, installed: 0.12.0]
        │   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
        │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
        │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
        │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
        │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
        │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
        │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
        │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
        │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
        │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
        │   ├── packaging [required: Any, installed: 25.0]
        │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
        │   ├── PyYAML [required: >=5.3, installed: 6.0.3]
        │   ├── referencing [required: Any, installed: 0.36.2]
        │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
        │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
        │   ├── rfc3339_validator [required: Any, installed: 0.1.4]
        │   │   └── six [required: Any, installed: 1.17.0]
        │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
        │   └── traitlets [required: >=5.3, installed: 5.14.3]
        ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
        │   └── terminado [required: >=0.8.3, installed: 0.18.1]
        │       ├── ptyprocess [required: Any, installed: 0.7.0]
        │       └── tornado [required: >=6.1.0, installed: 6.5.2]
        ├── nbconvert [required: >=6.4.4, installed: 7.16.6]
        │   ├── beautifulsoup4 [required: Any, installed: 4.14.2]
        │   │   ├── soupsieve [required: >1.2, installed: 2.8]
        │   │   └── typing_extensions [required: >=4.0.0, installed: 4.15.0]
        │   ├── bleach [required: !=5.0.0, installed: 6.2.0]
        │   │   └── webencodings [required: Any, installed: 0.5.1]
        │   ├── defusedxml [required: Any, installed: 0.7.1]
        │   ├── Jinja2 [required: >=3.0, installed: 3.1.6]
        │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
        │   ├── jupyter_core [required: >=4.7, installed: 5.8.1]
        │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
        │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
        │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
        │   ├── MarkupSafe [required: >=2.0, installed: 3.0.3]
        │   ├── mistune [required: >=2.0.3,<4, installed: 3.1.4]
        │   ├── nbclient [required: >=0.5.0, installed: 0.10.2]
        │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.3]
        │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
        │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
        │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
        │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
        │   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
        │   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
        │   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
        │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
        │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
        │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
        │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
        │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
        │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
        │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
        │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
        │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
        │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
        │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
        │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
        │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
        │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
        │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
        │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
        │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
        │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
        │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
        │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
        │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
        │   ├── nbformat [required: >=5.7, installed: 5.10.4]
        │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
        │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
        │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
        │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
        │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
        │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
        │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
        │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
        │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
        │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
        │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
        │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
        │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
        │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
        │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
        │   ├── packaging [required: Any, installed: 25.0]
        │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
        │   ├── Pygments [required: >=2.4.1, installed: 2.19.2]
        │   └── traitlets [required: >=5.1, installed: 5.14.3]
        ├── nbformat [required: >=5.3.0, installed: 5.10.4]
        │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
        │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
        │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
        │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
        │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
        │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
        │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
        │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
        │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
        │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
        │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
        │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
        │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
        │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
        │   └── traitlets [required: >=5.1, installed: 5.14.3]
        ├── packaging [required: >=22.0, installed: 25.0]
        ├── prometheus_client [required: >=0.9, installed: 0.23.1]
        ├── pyzmq [required: >=24, installed: 27.1.0]
        ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
        ├── terminado [required: >=0.8.3, installed: 0.18.1]
        │   ├── ptyprocess [required: Any, installed: 0.7.0]
        │   └── tornado [required: >=6.1.0, installed: 6.5.2]
        ├── tornado [required: >=6.2.0, installed: 6.5.2]
        ├── traitlets [required: >=5.6.0, installed: 5.14.3]
        └── websocket-client [required: >=1.7, installed: 1.9.0]
nbgitpuller==1.2.2
├── jupyter_server [required: >=1.10.1, installed: 2.17.0]
│   ├── anyio [required: >=3.1.0, installed: 4.11.0]
│   │   ├── idna [required: >=2.8, installed: 3.11]
│   │   └── sniffio [required: >=1.1, installed: 1.3.1]
│   ├── argon2-cffi [required: >=21.1, installed: 25.1.0]
│   │   └── argon2-cffi-bindings [required: Any, installed: 25.1.0]
│   │       └── cffi [required: >=1.0.1, installed: 2.0.0]
│   │           └── pycparser [required: Any, installed: 2.22]
│   ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
│   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   ├── jupyter_client [required: >=7.4.4, installed: 8.6.3]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter-events [required: >=0.11.0, installed: 0.12.0]
│   │   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   ├── packaging [required: Any, installed: 25.0]
│   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │   ├── PyYAML [required: >=5.3, installed: 6.0.3]
│   │   ├── referencing [required: Any, installed: 0.36.2]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   ├── rfc3339_validator [required: Any, installed: 0.1.4]
│   │   │   └── six [required: Any, installed: 1.17.0]
│   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       └── tornado [required: >=6.1.0, installed: 6.5.2]
│   ├── nbconvert [required: >=6.4.4, installed: 7.16.6]
│   │   ├── beautifulsoup4 [required: Any, installed: 4.14.2]
│   │   │   ├── soupsieve [required: >1.2, installed: 2.8]
│   │   │   └── typing_extensions [required: >=4.0.0, installed: 4.15.0]
│   │   ├── bleach [required: !=5.0.0, installed: 6.2.0]
│   │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │   ├── Jinja2 [required: >=3.0, installed: 3.1.6]
│   │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   ├── jupyter_core [required: >=4.7, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │   ├── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   ├── mistune [required: >=2.0.3,<4, installed: 3.1.4]
│   │   ├── nbclient [required: >=0.5.0, installed: 0.10.2]
│   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.3]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── packaging [required: Any, installed: 25.0]
│   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │   ├── Pygments [required: >=2.4.1, installed: 2.19.2]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── packaging [required: >=22.0, installed: 25.0]
│   ├── prometheus_client [required: >=0.9, installed: 0.23.1]
│   ├── pyzmq [required: >=24, installed: 27.1.0]
│   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   └── tornado [required: >=6.1.0, installed: 6.5.2]
│   ├── tornado [required: >=6.2.0, installed: 6.5.2]
│   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   └── websocket-client [required: >=1.7, installed: 1.9.0]
└── tornado [required: Any, installed: 6.5.2]
notebook==7.4.7
├── jupyter_server [required: >=2.4.0,<3, installed: 2.17.0]
│   ├── anyio [required: >=3.1.0, installed: 4.11.0]
│   │   ├── idna [required: >=2.8, installed: 3.11]
│   │   └── sniffio [required: >=1.1, installed: 1.3.1]
│   ├── argon2-cffi [required: >=21.1, installed: 25.1.0]
│   │   └── argon2-cffi-bindings [required: Any, installed: 25.1.0]
│   │       └── cffi [required: >=1.0.1, installed: 2.0.0]
│   │           └── pycparser [required: Any, installed: 2.22]
│   ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
│   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   ├── jupyter_client [required: >=7.4.4, installed: 8.6.3]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter-events [required: >=0.11.0, installed: 0.12.0]
│   │   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   ├── packaging [required: Any, installed: 25.0]
│   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │   ├── PyYAML [required: >=5.3, installed: 6.0.3]
│   │   ├── referencing [required: Any, installed: 0.36.2]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   ├── rfc3339_validator [required: Any, installed: 0.1.4]
│   │   │   └── six [required: Any, installed: 1.17.0]
│   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       └── tornado [required: >=6.1.0, installed: 6.5.2]
│   ├── nbconvert [required: >=6.4.4, installed: 7.16.6]
│   │   ├── beautifulsoup4 [required: Any, installed: 4.14.2]
│   │   │   ├── soupsieve [required: >1.2, installed: 2.8]
│   │   │   └── typing_extensions [required: >=4.0.0, installed: 4.15.0]
│   │   ├── bleach [required: !=5.0.0, installed: 6.2.0]
│   │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │   ├── Jinja2 [required: >=3.0, installed: 3.1.6]
│   │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   ├── jupyter_core [required: >=4.7, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │   ├── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   ├── mistune [required: >=2.0.3,<4, installed: 3.1.4]
│   │   ├── nbclient [required: >=0.5.0, installed: 0.10.2]
│   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.3]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── packaging [required: Any, installed: 25.0]
│   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │   ├── Pygments [required: >=2.4.1, installed: 2.19.2]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   ├── packaging [required: >=22.0, installed: 25.0]
│   ├── prometheus_client [required: >=0.9, installed: 0.23.1]
│   ├── pyzmq [required: >=24, installed: 27.1.0]
│   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   └── tornado [required: >=6.1.0, installed: 6.5.2]
│   ├── tornado [required: >=6.2.0, installed: 6.5.2]
│   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   └── websocket-client [required: >=1.7, installed: 1.9.0]
├── jupyterlab_server [required: >=2.27.1,<3, installed: 2.27.3]
│   ├── babel [required: >=2.10, installed: 2.17.0]
│   ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
│   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   ├── json5 [required: >=0.9.0, installed: 0.12.1]
│   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
│   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   ├── jupyter_server [required: >=1.21,<3, installed: 2.17.0]
│   │   ├── anyio [required: >=3.1.0, installed: 4.11.0]
│   │   │   ├── idna [required: >=2.8, installed: 3.11]
│   │   │   └── sniffio [required: >=1.1, installed: 1.3.1]
│   │   ├── argon2-cffi [required: >=21.1, installed: 25.1.0]
│   │   │   └── argon2-cffi-bindings [required: Any, installed: 25.1.0]
│   │   │       └── cffi [required: >=1.0.1, installed: 2.0.0]
│   │   │           └── pycparser [required: Any, installed: 2.22]
│   │   ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
│   │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   ├── jupyter_client [required: >=7.4.4, installed: 8.6.3]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter-events [required: >=0.11.0, installed: 0.12.0]
│   │   │   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   ├── packaging [required: Any, installed: 25.0]
│   │   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │   │   ├── PyYAML [required: >=5.3, installed: 6.0.3]
│   │   │   ├── referencing [required: Any, installed: 0.36.2]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   ├── rfc3339_validator [required: Any, installed: 0.1.4]
│   │   │   │   └── six [required: Any, installed: 1.17.0]
│   │   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   │       └── tornado [required: >=6.1.0, installed: 6.5.2]
│   │   ├── nbconvert [required: >=6.4.4, installed: 7.16.6]
│   │   │   ├── beautifulsoup4 [required: Any, installed: 4.14.2]
│   │   │   │   ├── soupsieve [required: >1.2, installed: 2.8]
│   │   │   │   └── typing_extensions [required: >=4.0.0, installed: 4.15.0]
│   │   │   ├── bleach [required: !=5.0.0, installed: 6.2.0]
│   │   │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │   │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │   │   ├── Jinja2 [required: >=3.0, installed: 3.1.6]
│   │   │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   │   ├── jupyter_core [required: >=4.7, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │   │   ├── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   │   ├── mistune [required: >=2.0.3,<4, installed: 3.1.4]
│   │   │   ├── nbclient [required: >=0.5.0, installed: 0.10.2]
│   │   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.3]
│   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   │   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   │   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   ├── packaging [required: Any, installed: 25.0]
│   │   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │   │   ├── Pygments [required: >=2.4.1, installed: 2.19.2]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── packaging [required: >=22.0, installed: 25.0]
│   │   ├── prometheus_client [required: >=0.9, installed: 0.23.1]
│   │   ├── pyzmq [required: >=24, installed: 27.1.0]
│   │   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   │   ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   │   └── tornado [required: >=6.1.0, installed: 6.5.2]
│   │   ├── tornado [required: >=6.2.0, installed: 6.5.2]
│   │   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   │   └── websocket-client [required: >=1.7, installed: 1.9.0]
│   ├── packaging [required: >=21.3, installed: 25.0]
│   └── requests [required: >=2.31, installed: 2.32.5]
│       ├── charset-normalizer [required: >=2,<4, installed: 3.4.3]
│       ├── idna [required: >=2.5,<4, installed: 3.11]
│       ├── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
│       └── certifi [required: >=2017.4.17, installed: 2025.10.5]
├── jupyterlab [required: >=4.4.9,<4.5, installed: 4.4.9]
│   ├── async-lru [required: >=1.0.0, installed: 2.0.5]
│   ├── httpx [required: >=0.25.0,<1, installed: 0.28.1]
│   │   ├── anyio [required: Any, installed: 4.11.0]
│   │   │   ├── idna [required: >=2.8, installed: 3.11]
│   │   │   └── sniffio [required: >=1.1, installed: 1.3.1]
│   │   ├── certifi [required: Any, installed: 2025.10.5]
│   │   ├── httpcore [required: ==1.*, installed: 1.0.9]
│   │   │   ├── certifi [required: Any, installed: 2025.10.5]
│   │   │   └── h11 [required: >=0.16, installed: 0.16.0]
│   │   └── idna [required: Any, installed: 3.11]
│   ├── ipykernel [required: >=6.5.0,!=6.30.0, installed: 7.0.0]
│   │   ├── comm [required: >=0.1.1, installed: 0.2.3]
│   │   ├── debugpy [required: >=1.6.5, installed: 1.8.17]
│   │   ├── ipython [required: >=7.23.1, installed: 9.6.0]
│   │   │   ├── decorator [required: Any, installed: 5.2.1]
│   │   │   ├── ipython_pygments_lexers [required: Any, installed: 1.1.1]
│   │   │   │   └── Pygments [required: Any, installed: 2.19.2]
│   │   │   ├── jedi [required: >=0.16, installed: 0.19.2]
│   │   │   │   └── parso [required: >=0.8.4,<0.9.0, installed: 0.8.5]
│   │   │   ├── matplotlib-inline [required: Any, installed: 0.1.7]
│   │   │   │   └── traitlets [required: Any, installed: 5.14.3]
│   │   │   ├── pexpect [required: >4.3, installed: 4.9.0]
│   │   │   │   └── ptyprocess [required: >=0.5, installed: 0.7.0]
│   │   │   ├── prompt_toolkit [required: >=3.0.41,<3.1.0, installed: 3.0.52]
│   │   │   │   └── wcwidth [required: Any, installed: 0.2.14]
│   │   │   ├── Pygments [required: >=2.4.0, installed: 2.19.2]
│   │   │   ├── stack_data [required: Any, installed: 0.6.3]
│   │   │   │   ├── executing [required: >=1.2.0, installed: 2.2.1]
│   │   │   │   ├── asttokens [required: >=2.1.0, installed: 3.0.0]
│   │   │   │   └── pure_eval [required: Any, installed: 0.2.3]
│   │   │   └── traitlets [required: >=5.13.0, installed: 5.14.3]
│   │   ├── jupyter_client [required: >=8.0.0, installed: 8.6.3]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── matplotlib-inline [required: >=0.1, installed: 0.1.7]
│   │   │   └── traitlets [required: Any, installed: 5.14.3]
│   │   ├── nest_asyncio [required: >=1.4, installed: 1.6.0]
│   │   ├── packaging [required: >=22, installed: 25.0]
│   │   ├── psutil [required: >=5.7, installed: 7.1.0]
│   │   ├── pyzmq [required: >=25, installed: 27.1.0]
│   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   └── traitlets [required: >=5.4.0, installed: 5.14.3]
│   ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
│   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   ├── jupyter_core [required: Any, installed: 5.8.1]
│   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   ├── jupyter-lsp [required: >=2.0.0, installed: 2.3.0]
│   │   └── jupyter_server [required: >=1.1.2, installed: 2.17.0]
│   │       ├── anyio [required: >=3.1.0, installed: 4.11.0]
│   │       │   ├── idna [required: >=2.8, installed: 3.11]
│   │       │   └── sniffio [required: >=1.1, installed: 1.3.1]
│   │       ├── argon2-cffi [required: >=21.1, installed: 25.1.0]
│   │       │   └── argon2-cffi-bindings [required: Any, installed: 25.1.0]
│   │       │       └── cffi [required: >=1.0.1, installed: 2.0.0]
│   │       │           └── pycparser [required: Any, installed: 2.22]
│   │       ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
│   │       │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │       ├── jupyter_client [required: >=7.4.4, installed: 8.6.3]
│   │       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │       │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │       │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │       │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       ├── jupyter-events [required: >=0.11.0, installed: 0.12.0]
│   │       │   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
│   │       │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │       │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │       │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │       │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │       │   ├── packaging [required: Any, installed: 25.0]
│   │       │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │       │   ├── PyYAML [required: >=5.3, installed: 6.0.3]
│   │       │   ├── referencing [required: Any, installed: 0.36.2]
│   │       │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   ├── rfc3339_validator [required: Any, installed: 0.1.4]
│   │       │   │   └── six [required: Any, installed: 1.17.0]
│   │       │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │       │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       │       └── tornado [required: >=6.1.0, installed: 6.5.2]
│   │       ├── nbconvert [required: >=6.4.4, installed: 7.16.6]
│   │       │   ├── beautifulsoup4 [required: Any, installed: 4.14.2]
│   │       │   │   ├── soupsieve [required: >1.2, installed: 2.8]
│   │       │   │   └── typing_extensions [required: >=4.0.0, installed: 4.15.0]
│   │       │   ├── bleach [required: !=5.0.0, installed: 6.2.0]
│   │       │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │       │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │       │   ├── Jinja2 [required: >=3.0, installed: 3.1.6]
│   │       │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │       │   ├── jupyter_core [required: >=4.7, installed: 5.8.1]
│   │       │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │       │   ├── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │       │   ├── mistune [required: >=2.0.3,<4, installed: 3.1.4]
│   │       │   ├── nbclient [required: >=0.5.0, installed: 0.10.2]
│   │       │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.3]
│   │       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │       │   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │       │   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │       │   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │       │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │       │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │       │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │       │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │       │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │       │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │       │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │       │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │       │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │       │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │       │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       │   ├── packaging [required: Any, installed: 25.0]
│   │       │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │       │   ├── Pygments [required: >=2.4.1, installed: 2.19.2]
│   │       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │       │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │       │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │       │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │       │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │       │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │       │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       ├── packaging [required: >=22.0, installed: 25.0]
│   │       ├── prometheus_client [required: >=0.9, installed: 0.23.1]
│   │       ├── pyzmq [required: >=24, installed: 27.1.0]
│   │       ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   │       ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       │   └── tornado [required: >=6.1.0, installed: 6.5.2]
│   │       ├── tornado [required: >=6.2.0, installed: 6.5.2]
│   │       ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   │       └── websocket-client [required: >=1.7, installed: 1.9.0]
│   ├── jupyter_server [required: >=2.4.0,<3, installed: 2.17.0]
│   │   ├── anyio [required: >=3.1.0, installed: 4.11.0]
│   │   │   ├── idna [required: >=2.8, installed: 3.11]
│   │   │   └── sniffio [required: >=1.1, installed: 1.3.1]
│   │   ├── argon2-cffi [required: >=21.1, installed: 25.1.0]
│   │   │   └── argon2-cffi-bindings [required: Any, installed: 25.1.0]
│   │   │       └── cffi [required: >=1.0.1, installed: 2.0.0]
│   │   │           └── pycparser [required: Any, installed: 2.22]
│   │   ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
│   │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   ├── jupyter_client [required: >=7.4.4, installed: 8.6.3]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter-events [required: >=0.11.0, installed: 0.12.0]
│   │   │   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   ├── packaging [required: Any, installed: 25.0]
│   │   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │   │   ├── PyYAML [required: >=5.3, installed: 6.0.3]
│   │   │   ├── referencing [required: Any, installed: 0.36.2]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   ├── rfc3339_validator [required: Any, installed: 0.1.4]
│   │   │   │   └── six [required: Any, installed: 1.17.0]
│   │   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   │       └── tornado [required: >=6.1.0, installed: 6.5.2]
│   │   ├── nbconvert [required: >=6.4.4, installed: 7.16.6]
│   │   │   ├── beautifulsoup4 [required: Any, installed: 4.14.2]
│   │   │   │   ├── soupsieve [required: >1.2, installed: 2.8]
│   │   │   │   └── typing_extensions [required: >=4.0.0, installed: 4.15.0]
│   │   │   ├── bleach [required: !=5.0.0, installed: 6.2.0]
│   │   │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │   │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │   │   ├── Jinja2 [required: >=3.0, installed: 3.1.6]
│   │   │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   │   ├── jupyter_core [required: >=4.7, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │   │   ├── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   │   ├── mistune [required: >=2.0.3,<4, installed: 3.1.4]
│   │   │   ├── nbclient [required: >=0.5.0, installed: 0.10.2]
│   │   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.3]
│   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   │   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   │   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   ├── packaging [required: Any, installed: 25.0]
│   │   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │   │   ├── Pygments [required: >=2.4.1, installed: 2.19.2]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   ├── packaging [required: >=22.0, installed: 25.0]
│   │   ├── prometheus_client [required: >=0.9, installed: 0.23.1]
│   │   ├── pyzmq [required: >=24, installed: 27.1.0]
│   │   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   │   ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   │   └── tornado [required: >=6.1.0, installed: 6.5.2]
│   │   ├── tornado [required: >=6.2.0, installed: 6.5.2]
│   │   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   │   └── websocket-client [required: >=1.7, installed: 1.9.0]
│   ├── jupyterlab_server [required: >=2.27.1,<3, installed: 2.27.3]
│   │   ├── babel [required: >=2.10, installed: 2.17.0]
│   │   ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
│   │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   ├── json5 [required: >=0.9.0, installed: 0.12.1]
│   │   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
│   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   ├── jupyter_server [required: >=1.21,<3, installed: 2.17.0]
│   │   │   ├── anyio [required: >=3.1.0, installed: 4.11.0]
│   │   │   │   ├── idna [required: >=2.8, installed: 3.11]
│   │   │   │   └── sniffio [required: >=1.1, installed: 1.3.1]
│   │   │   ├── argon2-cffi [required: >=21.1, installed: 25.1.0]
│   │   │   │   └── argon2-cffi-bindings [required: Any, installed: 25.1.0]
│   │   │   │       └── cffi [required: >=1.0.1, installed: 2.0.0]
│   │   │   │           └── pycparser [required: Any, installed: 2.22]
│   │   │   ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
│   │   │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   │   ├── jupyter_client [required: >=7.4.4, installed: 8.6.3]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyter-events [required: >=0.11.0, installed: 0.12.0]
│   │   │   │   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   │   ├── packaging [required: Any, installed: 25.0]
│   │   │   │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │   │   │   ├── PyYAML [required: >=5.3, installed: 6.0.3]
│   │   │   │   ├── referencing [required: Any, installed: 0.36.2]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   ├── rfc3339_validator [required: Any, installed: 0.1.4]
│   │   │   │   │   └── six [required: Any, installed: 1.17.0]
│   │   │   │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │   │   │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   │   │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   │   │       └── tornado [required: >=6.1.0, installed: 6.5.2]
│   │   │   ├── nbconvert [required: >=6.4.4, installed: 7.16.6]
│   │   │   │   ├── beautifulsoup4 [required: Any, installed: 4.14.2]
│   │   │   │   │   ├── soupsieve [required: >1.2, installed: 2.8]
│   │   │   │   │   └── typing_extensions [required: >=4.0.0, installed: 4.15.0]
│   │   │   │   ├── bleach [required: !=5.0.0, installed: 6.2.0]
│   │   │   │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │   │   │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │   │   │   ├── Jinja2 [required: >=3.0, installed: 3.1.6]
│   │   │   │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   │   │   ├── jupyter_core [required: >=4.7, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │   │   │   ├── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │   │   │   ├── mistune [required: >=2.0.3,<4, installed: 3.1.4]
│   │   │   │   ├── nbclient [required: >=0.5.0, installed: 0.10.2]
│   │   │   │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.3]
│   │   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   │   │   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │   │   │   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │   │   │   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │   │   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │   │   │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   │   ├── packaging [required: Any, installed: 25.0]
│   │   │   │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │   │   │   ├── Pygments [required: >=2.4.1, installed: 2.19.2]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │   │   ├── packaging [required: >=22.0, installed: 25.0]
│   │   │   ├── prometheus_client [required: >=0.9, installed: 0.23.1]
│   │   │   ├── pyzmq [required: >=24, installed: 27.1.0]
│   │   │   ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   │   │   ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │   │   │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │   │   │   └── tornado [required: >=6.1.0, installed: 6.5.2]
│   │   │   ├── tornado [required: >=6.2.0, installed: 6.5.2]
│   │   │   ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   │   │   └── websocket-client [required: >=1.7, installed: 1.9.0]
│   │   ├── packaging [required: >=21.3, installed: 25.0]
│   │   └── requests [required: >=2.31, installed: 2.32.5]
│   │       ├── charset-normalizer [required: >=2,<4, installed: 3.4.3]
│   │       ├── idna [required: >=2.5,<4, installed: 3.11]
│   │       ├── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
│   │       └── certifi [required: >=2017.4.17, installed: 2025.10.5]
│   ├── notebook_shim [required: >=0.2, installed: 0.2.4]
│   │   └── jupyter_server [required: >=1.8,<3, installed: 2.17.0]
│   │       ├── anyio [required: >=3.1.0, installed: 4.11.0]
│   │       │   ├── idna [required: >=2.8, installed: 3.11]
│   │       │   └── sniffio [required: >=1.1, installed: 1.3.1]
│   │       ├── argon2-cffi [required: >=21.1, installed: 25.1.0]
│   │       │   └── argon2-cffi-bindings [required: Any, installed: 25.1.0]
│   │       │       └── cffi [required: >=1.0.1, installed: 2.0.0]
│   │       │           └── pycparser [required: Any, installed: 2.22]
│   │       ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
│   │       │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │       ├── jupyter_client [required: >=7.4.4, installed: 8.6.3]
│   │       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │       │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │       │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │       │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       ├── jupyter-events [required: >=0.11.0, installed: 0.12.0]
│   │       │   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
│   │       │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │       │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │       │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │       │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │       │   ├── packaging [required: Any, installed: 25.0]
│   │       │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│   │       │   ├── PyYAML [required: >=5.3, installed: 6.0.3]
│   │       │   ├── referencing [required: Any, installed: 0.36.2]
│   │       │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   ├── rfc3339_validator [required: Any, installed: 0.1.4]
│   │       │   │   └── six [required: Any, installed: 1.17.0]
│   │       │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│   │       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│   │       │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       │       ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       │       └── tornado [required: >=6.1.0, installed: 6.5.2]
│   │       ├── nbconvert [required: >=6.4.4, installed: 7.16.6]
│   │       │   ├── beautifulsoup4 [required: Any, installed: 4.14.2]
│   │       │   │   ├── soupsieve [required: >1.2, installed: 2.8]
│   │       │   │   └── typing_extensions [required: >=4.0.0, installed: 4.15.0]
│   │       │   ├── bleach [required: !=5.0.0, installed: 6.2.0]
│   │       │   │   └── webencodings [required: Any, installed: 0.5.1]
│   │       │   ├── defusedxml [required: Any, installed: 0.7.1]
│   │       │   ├── Jinja2 [required: >=3.0, installed: 3.1.6]
│   │       │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │       │   ├── jupyter_core [required: >=4.7, installed: 5.8.1]
│   │       │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│   │       │   ├── MarkupSafe [required: >=2.0, installed: 3.0.3]
│   │       │   ├── mistune [required: >=2.0.3,<4, installed: 3.1.4]
│   │       │   ├── nbclient [required: >=0.5.0, installed: 0.10.2]
│   │       │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.3]
│   │       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │       │   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│   │       │   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│   │       │   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│   │       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│   │       │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │       │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │       │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │       │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │       │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│   │       │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│   │       │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │       │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │       │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │       │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │       │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       │   ├── packaging [required: Any, installed: 25.0]
│   │       │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│   │       │   ├── Pygments [required: >=2.4.1, installed: 2.19.2]
│   │       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│   │       │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│   │       │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│   │       │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│   │       │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│   │       │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│   │       │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│   │       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│   │       │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│   │       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│   │       │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│   │       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│   │       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│   │       ├── packaging [required: >=22.0, installed: 25.0]
│   │       ├── prometheus_client [required: >=0.9, installed: 0.23.1]
│   │       ├── pyzmq [required: >=24, installed: 27.1.0]
│   │       ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│   │       ├── terminado [required: >=0.8.3, installed: 0.18.1]
│   │       │   ├── ptyprocess [required: Any, installed: 0.7.0]
│   │       │   └── tornado [required: >=6.1.0, installed: 6.5.2]
│   │       ├── tornado [required: >=6.2.0, installed: 6.5.2]
│   │       ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│   │       └── websocket-client [required: >=1.7, installed: 1.9.0]
│   ├── packaging [required: Any, installed: 25.0]
│   ├── setuptools [required: >=41.1.0, installed: 80.9.0]
│   ├── tornado [required: >=6.2.0, installed: 6.5.2]
│   └── traitlets [required: Any, installed: 5.14.3]
├── notebook_shim [required: >=0.2,<0.3, installed: 0.2.4]
│   └── jupyter_server [required: >=1.8,<3, installed: 2.17.0]
│       ├── anyio [required: >=3.1.0, installed: 4.11.0]
│       │   ├── idna [required: >=2.8, installed: 3.11]
│       │   └── sniffio [required: >=1.1, installed: 1.3.1]
│       ├── argon2-cffi [required: >=21.1, installed: 25.1.0]
│       │   └── argon2-cffi-bindings [required: Any, installed: 25.1.0]
│       │       └── cffi [required: >=1.0.1, installed: 2.0.0]
│       │           └── pycparser [required: Any, installed: 2.22]
│       ├── Jinja2 [required: >=3.0.3, installed: 3.1.6]
│       │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│       ├── jupyter_client [required: >=7.4.4, installed: 8.6.3]
│       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│       │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│       │   │   └── six [required: >=1.5, installed: 1.17.0]
│       │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│       │   ├── tornado [required: >=6.2, installed: 6.5.2]
│       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│       │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       ├── jupyter-events [required: >=0.11.0, installed: 0.12.0]
│       │   ├── jsonschema [required: >=4.18.0, installed: 4.25.1]
│       │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│       │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│       │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│       │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│       │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│       │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│       │   ├── packaging [required: Any, installed: 25.0]
│       │   ├── python-json-logger [required: >=2.0.4, installed: 2.0.7]
│       │   ├── PyYAML [required: >=5.3, installed: 6.0.3]
│       │   ├── referencing [required: Any, installed: 0.36.2]
│       │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│       │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│       │   ├── rfc3339_validator [required: Any, installed: 0.1.4]
│       │   │   └── six [required: Any, installed: 1.17.0]
│       │   ├── rfc3986-validator [required: >=0.1.1, installed: 0.1.1]
│       │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       ├── jupyter_server_terminals [required: >=0.4.4, installed: 0.5.3]
│       │   └── terminado [required: >=0.8.3, installed: 0.18.1]
│       │       ├── ptyprocess [required: Any, installed: 0.7.0]
│       │       └── tornado [required: >=6.1.0, installed: 6.5.2]
│       ├── nbconvert [required: >=6.4.4, installed: 7.16.6]
│       │   ├── beautifulsoup4 [required: Any, installed: 4.14.2]
│       │   │   ├── soupsieve [required: >1.2, installed: 2.8]
│       │   │   └── typing_extensions [required: >=4.0.0, installed: 4.15.0]
│       │   ├── bleach [required: !=5.0.0, installed: 6.2.0]
│       │   │   └── webencodings [required: Any, installed: 0.5.1]
│       │   ├── defusedxml [required: Any, installed: 0.7.1]
│       │   ├── Jinja2 [required: >=3.0, installed: 3.1.6]
│       │   │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
│       │   ├── jupyter_core [required: >=4.7, installed: 5.8.1]
│       │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   ├── jupyterlab_pygments [required: Any, installed: 0.3.0]
│       │   ├── MarkupSafe [required: >=2.0, installed: 3.0.3]
│       │   ├── mistune [required: >=2.0.3,<4, installed: 3.1.4]
│       │   ├── nbclient [required: >=0.5.0, installed: 0.10.2]
│       │   │   ├── jupyter_client [required: >=6.1.12, installed: 8.6.3]
│       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   │   │   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│       │   │   │   │   └── six [required: >=1.5, installed: 1.17.0]
│       │   │   │   ├── pyzmq [required: >=23.0, installed: 27.1.0]
│       │   │   │   ├── tornado [required: >=6.2, installed: 6.5.2]
│       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   │   ├── nbformat [required: >=5.1, installed: 5.10.4]
│       │   │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│       │   │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│       │   │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│       │   │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│       │   │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│       │   │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│       │   │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│       │   │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│       │   │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│       │   │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│       │   │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│       │   │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│       │   │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│       │   │   └── traitlets [required: >=5.4, installed: 5.14.3]
│       │   ├── nbformat [required: >=5.7, installed: 5.10.4]
│       │   │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│       │   │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│       │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│       │   │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│       │   │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│       │   │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│       │   │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│       │   │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│       │   │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│       │   │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│       │   │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│       │   │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│       │   │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│       │   │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   │   └── traitlets [required: >=5.1, installed: 5.14.3]
│       │   ├── packaging [required: Any, installed: 25.0]
│       │   ├── pandocfilters [required: >=1.4.1, installed: 1.5.0]
│       │   ├── Pygments [required: >=2.4.1, installed: 2.19.2]
│       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│       ├── nbformat [required: >=5.3.0, installed: 5.10.4]
│       │   ├── fastjsonschema [required: >=2.15, installed: 2.21.2]
│       │   ├── jsonschema [required: >=2.6, installed: 4.25.1]
│       │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│       │   │   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2025.9.1]
│       │   │   │   └── referencing [required: >=0.31.0, installed: 0.36.2]
│       │   │   │       ├── attrs [required: >=22.2.0, installed: 25.4.0]
│       │   │   │       └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│       │   │   ├── referencing [required: >=0.28.4, installed: 0.36.2]
│       │   │   │   ├── attrs [required: >=22.2.0, installed: 25.4.0]
│       │   │   │   └── rpds-py [required: >=0.7.0, installed: 0.27.1]
│       │   │   └── rpds-py [required: >=0.7.1, installed: 0.27.1]
│       │   ├── jupyter_core [required: >=4.12,!=5.0.*, installed: 5.8.1]
│       │   │   ├── platformdirs [required: >=2.5, installed: 4.5.0]
│       │   │   └── traitlets [required: >=5.3, installed: 5.14.3]
│       │   └── traitlets [required: >=5.1, installed: 5.14.3]
│       ├── packaging [required: >=22.0, installed: 25.0]
│       ├── prometheus_client [required: >=0.9, installed: 0.23.1]
│       ├── pyzmq [required: >=24, installed: 27.1.0]
│       ├── Send2Trash [required: >=1.8.2, installed: 1.8.3]
│       ├── terminado [required: >=0.8.3, installed: 0.18.1]
│       │   ├── ptyprocess [required: Any, installed: 0.7.0]
│       │   └── tornado [required: >=6.1.0, installed: 6.5.2]
│       ├── tornado [required: >=6.2.0, installed: 6.5.2]
│       ├── traitlets [required: >=5.6.0, installed: 5.14.3]
│       └── websocket-client [required: >=1.7, installed: 1.9.0]
└── tornado [required: >=6.2.0, installed: 6.5.2]
numba==0.62.1
├── llvmlite [required: >=0.45.0dev0,<0.46, installed: 0.45.1]
└── numpy [required: >=1.22,<2.4, installed: 2.3.3]
openpyxl==3.1.5
└── et_xmlfile [required: Any, installed: 2.0.0]
overrides==7.7.0
pickleshare==0.7.5
pip==25.2
protobuf==6.31.1
pyarrow==21.0.0
PyJWT==2.10.1
PySocks==1.7.1
PyWavelets==1.9.0
└── numpy [required: >=1.25,<3, installed: 2.3.3]
requests-html==0.10.0
├── requests [required: Any, installed: 2.32.5]
│   ├── charset-normalizer [required: >=2,<4, installed: 3.4.3]
│   ├── idna [required: >=2.5,<4, installed: 3.11]
│   ├── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
│   └── certifi [required: >=2017.4.17, installed: 2025.10.5]
├── pyquery [required: Any, installed: 2.0.1]
│   ├── lxml [required: >=2.1, installed: 6.0.2]
│   └── cssselect [required: >=1.2.0, installed: 1.3.0]
├── fake-useragent [required: Any, installed: 2.2.0]
├── parse [required: Any, installed: 1.20.2]
├── bs4 [required: Any, installed: 0.0.2]
│   └── beautifulsoup4 [required: Any, installed: 4.14.2]
│       ├── soupsieve [required: >1.2, installed: 2.8]
│       └── typing_extensions [required: >=4.0.0, installed: 4.15.0]
├── w3lib [required: Any, installed: 2.3.1]
└── pyppeteer [required: >=0.0.14, installed: 2.0.0]
    ├── appdirs [required: >=1.4.3,<2.0.0, installed: 1.4.4]
    ├── certifi [required: >=2023, installed: 2025.10.5]
    ├── importlib_metadata [required: >=1.4, installed: 8.7.0]
    │   └── zipp [required: >=3.20, installed: 3.23.0]
    ├── pyee [required: >=11.0.0,<12.0.0, installed: 11.1.1]
    │   └── typing_extensions [required: Any, installed: 4.15.0]
    ├── tqdm [required: >=4.42.1,<5.0.0, installed: 4.67.1]
    ├── urllib3 [required: >=1.25.8,<2.0.0, installed: 1.26.20]
    └── websockets [required: >=10.0,<11.0, installed: 10.4]
rfc3987-syntax==1.1.0
└── lark [required: >=1.2.2, installed: 1.3.0]
rpy2==3.6.4
├── rpy2-rinterface [required: >=3.6.3, installed: 3.6.3]
│   └── cffi [required: >=1.15.1, installed: 2.0.0]
│       └── pycparser [required: Any, installed: 2.22]
└── rpy2-robjects [required: >=3.6.3, installed: 3.6.3]
    ├── rpy2-rinterface [required: >=3.6.0, installed: 3.6.3]
    │   └── cffi [required: >=1.15.1, installed: 2.0.0]
    │       └── pycparser [required: Any, installed: 2.22]
    ├── Jinja2 [required: Any, installed: 3.1.6]
    │   └── MarkupSafe [required: >=2.0, installed: 3.0.3]
    └── tzlocal [required: Any, installed: 5.3.1]
scikit-image==0.25.2
├── numpy [required: >=1.24, installed: 2.3.3]
├── scipy [required: >=1.11.4, installed: 1.16.2]
│   └── numpy [required: >=1.25.2,<2.6, installed: 2.3.3]
├── networkx [required: >=3.0, installed: 3.5]
├── pillow [required: >=10.1, installed: 11.3.0]
├── imageio [required: >=2.33,!=2.35.0, installed: 2.37.0]
│   ├── numpy [required: Any, installed: 2.3.3]
│   └── pillow [required: >=8.3.2, installed: 11.3.0]
├── tifffile [required: >=2022.8.12, installed: 2025.10.4]
│   └── numpy [required: Any, installed: 2.3.3]
├── packaging [required: >=21, installed: 25.0]
└── lazy_loader [required: >=0.4, installed: 0.4]
    └── packaging [required: Any, installed: 25.0]
scikit-learn==1.7.2
├── numpy [required: >=1.22.0, installed: 2.3.3]
├── scipy [required: >=1.8.0, installed: 1.16.2]
│   └── numpy [required: >=1.25.2,<2.6, installed: 2.3.3]
├── joblib [required: >=1.2.0, installed: 1.5.2]
└── threadpoolctl [required: >=3.1.0, installed: 3.6.0]
seaborn==0.13.2
├── numpy [required: >=1.20,!=1.24.0, installed: 2.3.3]
├── pandas [required: >=1.2, installed: 2.3.3]
│   ├── numpy [required: >=1.26.0, installed: 2.3.3]
│   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   └── six [required: >=1.5, installed: 1.17.0]
│   ├── pytz [required: >=2020.1, installed: 2025.2]
│   └── tzdata [required: >=2022.7, installed: 2025.2]
└── matplotlib [required: >=3.4,!=3.6.1, installed: 3.10.6]
    ├── contourpy [required: >=1.0.1, installed: 1.3.3]
    │   └── numpy [required: >=1.25, installed: 2.3.3]
    ├── cycler [required: >=0.10, installed: 0.12.1]
    ├── fonttools [required: >=4.22.0, installed: 4.60.1]
    ├── kiwisolver [required: >=1.3.1, installed: 1.4.9]
    ├── numpy [required: >=1.23, installed: 2.3.3]
    ├── packaging [required: >=20.0, installed: 25.0]
    ├── pillow [required: >=8, installed: 11.3.0]
    ├── pyparsing [required: >=2.3.1, installed: 3.2.5]
    └── python-dateutil [required: >=2.7, installed: 2.9.0.post0]
        └── six [required: >=1.5, installed: 1.17.0]
statsmodels==0.14.5
├── numpy [required: >=1.22.3,<3, installed: 2.3.3]
├── scipy [required: >=1.8,!=1.9.2, installed: 1.16.2]
│   └── numpy [required: >=1.25.2,<2.6, installed: 2.3.3]
├── pandas [required: >=1.4,!=2.1.0, installed: 2.3.3]
│   ├── numpy [required: >=1.26.0, installed: 2.3.3]
│   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
│   │   └── six [required: >=1.5, installed: 1.17.0]
│   ├── pytz [required: >=2020.1, installed: 2025.2]
│   └── tzdata [required: >=2022.7, installed: 2025.2]
├── patsy [required: >=0.5.6, installed: 1.0.1]
│   └── numpy [required: >=1.4, installed: 2.3.3]
└── packaging [required: >=21.3, installed: 25.0]
sympy==1.14.0
└── mpmath [required: >=1.1.0,<1.4, installed: 1.3.0]
tables==3.10.2
├── numpy [required: >=1.20.0, installed: 2.3.3]
├── numexpr [required: >=2.6.2, installed: 2.14.0]
│   └── numpy [required: >=1.23.0, installed: 2.3.3]
├── packaging [required: Any, installed: 25.0]
├── py-cpuinfo [required: Any, installed: 9.0.0]
└── typing_extensions [required: >=4.4.0, installed: 4.15.0]
tinycss2==1.4.0
└── webencodings [required: >=0.4, installed: 0.5.1]
tomli==2.3.0
typing_utils==0.1.0
uri-template==1.3.0
webcolors==24.11.1
xlrd==2.0.2
```


### Conda packages
via `conda-tree -n base deptree --exclude conda-tree --small`
```
mamba==2.3.2
  ├─ libmamba 2.3.2 [required: >=2.3.2,<2.4.0a0]
  │  ├─ cpp-expected 1.3.1 [required: >=1.3.1,<1.3.2.0a0]
  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  └─ libgcc 15.2.0 [required: 15.2.0, h767d61c_7]
  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │     └─ _openmp_mutex 4.5 [required: >=4.5]
  │  │  │        ├─ _libgcc_mutex 0.1 [required: 0.1, conda_forge]
  │  │  │        └─ libgomp 15.2.0 [required: >=7.5.0]
  │  │  │           └─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  └─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ yaml-cpp 0.8.0 [required: >=0.8.0,<0.9.0a0]
  │  │  ├─ libstdcxx 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  └─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ zstd 1.5.7 [required: >=1.5.7,<1.6.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libstdcxx 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │     └─ libgcc 15.2.0 [required: >=13]
  │  │        └─ dependencies of libgcc displayed above
  │  ├─ nlohmann_json-abi 3.12.0 [required: 3.12.0]
  │  ├─ openssl 3.5.4 [required: >=3.5.4,<4.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ ca-certificates 2025.10.5 [required: any]
  │  │  │  └─ __unix [required: any]
  │  │  └─ libgcc 15.2.0 [required: >=14]
  │  │     └─ dependencies of libgcc displayed above
  │  ├─ reproc 14.2.5.post0 [required: >=14.2,<15.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  └─ libgcc 15.2.0 [required: >=13]
  │  │     └─ dependencies of libgcc displayed above
  │  ├─ fmt 11.2.0 [required: >=11.2.0,<11.3.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  └─ libstdcxx 15.2.0 [required: >=13]
  │  │     └─ dependencies of libstdcxx displayed above
  │  ├─ simdjson 4.0.7 [required: >=4.0.7,<4.1.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  └─ libstdcxx 15.2.0 [required: >=14]
  │  │     └─ dependencies of libstdcxx displayed above
  │  ├─ reproc-cpp 14.2.5.post0 [required: >=14.2,<15.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libstdcxx 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  └─ reproc 14.2.5.post0 [required: 14.2.5.post0, hb9d3cd8_0]
  │  │     └─ dependencies of reproc displayed above
  │  ├─ libarchive 3.8.1 [required: >=3.8.1,<3.9.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  └─ libgcc 15.2.0 [required: >=14]
  │  │  │     └─ dependencies of libgcc displayed above
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ liblzma 5.8.1 [required: >=5.8.1,<6.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  └─ libgcc 15.2.0 [required: >=13]
  │  │  │     └─ dependencies of libgcc displayed above
  │  │  ├─ libxml2 2.15.0 [required: any]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ icu 75.1 [required: >=75.1,<76.0a0]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libgcc-ng 15.2.0 [required: >=12]
  │  │  │  │  │  └─ libgcc 15.2.0 [required: 15.2.0, h767d61c_7]
  │  │  │  │  │     └─ dependencies of libgcc displayed above
  │  │  │  │  └─ libstdcxx-ng 15.2.0 [required: >=12]
  │  │  │  │     └─ libstdcxx 15.2.0 [required: 15.2.0, h8f9b012_7]
  │  │  │  │        └─ dependencies of libstdcxx displayed above
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ libiconv 1.18 [required: >=1.18,<2.0a0]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  └─ libgcc 15.2.0 [required: >=14]
  │  │  │  │     └─ dependencies of libgcc displayed above
  │  │  │  ├─ liblzma 5.8.1 [required: >=5.8.1,<6.0a0]
  │  │  │  │  └─ dependencies of liblzma displayed above
  │  │  │  ├─ libxml2-16 2.15.0 [required: 2.15.0, ha9997c6_1]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ icu 75.1 [required: >=75.1,<76.0a0]
  │  │  │  │  │  └─ dependencies of icu displayed above
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  ├─ libiconv 1.18 [required: >=1.18,<2.0a0]
  │  │  │  │  │  └─ dependencies of libiconv displayed above
  │  │  │  │  ├─ liblzma 5.8.1 [required: >=5.8.1,<6.0a0]
  │  │  │  │  │  └─ dependencies of liblzma displayed above
  │  │  │  │  └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │  │     └─ dependencies of libzlib displayed above
  │  │  │  └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │     └─ dependencies of libzlib displayed above
  │  │  ├─ libxml2-16 2.15.0 [required: >=2.14.6]
  │  │  │  └─ dependencies of libxml2-16 displayed above
  │  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │  └─ dependencies of libzlib displayed above
  │  │  ├─ lz4-c 1.10.0 [required: >=1.10.0,<1.11.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  └─ libstdcxx 15.2.0 [required: >=13]
  │  │  │     └─ dependencies of libstdcxx displayed above
  │  │  ├─ lzo 2.10 [required: >=2.10,<3.0a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  └─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ openssl 3.5.4 [required: >=3.5.2,<4.0a0]
  │  │  │  └─ dependencies of openssl displayed above
  │  │  └─ zstd 1.5.7 [required: >=1.5.7,<1.6.0a0]
  │  │     └─ dependencies of zstd displayed above
  │  ├─ libsolv 0.7.35 [required: >=0.7.35,<0.8.0a0]
  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │     └─ dependencies of libzlib displayed above
  │  └─ libcurl 8.14.1 [required: >=8.14.1,<9.0a0]
  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │     ├─ krb5 1.21.3 [required: >=1.21.3,<1.22.0a0]
  │     │  ├─ keyutils 1.6.3 [required: >=1.6.1,<2.0a0]
  │     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │     │  │  └─ libgcc 15.2.0 [required: >=13]
  │     │  │     └─ dependencies of libgcc displayed above
  │     │  ├─ libedit 3.1.20250104 [required: >=3.1.20191231,<4.0a0]
  │     │  │  ├─ ncurses 6.5 [required: >=6.5,<7.0a0]
  │     │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │     │  │  │  └─ libgcc 15.2.0 [required: >=13]
  │     │  │  │     └─ dependencies of libgcc displayed above
  │     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │     │  │  └─ libgcc 15.2.0 [required: >=13]
  │     │  │     └─ dependencies of libgcc displayed above
  │     │  ├─ libgcc-ng 15.2.0 [required: >=12]
  │     │  │  └─ dependencies of libgcc-ng displayed above
  │     │  ├─ libstdcxx-ng 15.2.0 [required: >=12]
  │     │  │  └─ dependencies of libstdcxx-ng displayed above
  │     │  └─ openssl 3.5.4 [required: >=3.3.1,<4.0a0]
  │     │     └─ dependencies of openssl displayed above
  │     ├─ libgcc 15.2.0 [required: >=13]
  │     │  └─ dependencies of libgcc displayed above
  │     ├─ libnghttp2 1.67.0 [required: >=1.64.0,<2.0a0]
  │     │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │     │  ├─ c-ares 1.34.5 [required: >=1.34.5,<2.0a0]
  │     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │     │  │  └─ libgcc 15.2.0 [required: >=13]
  │     │  │     └─ dependencies of libgcc displayed above
  │     │  ├─ libev 4.33 [required: >=4.33,<5.0a0]
  │     │  │  └─ libgcc-ng 15.2.0 [required: >=12]
  │     │  │     └─ dependencies of libgcc-ng displayed above
  │     │  ├─ libgcc 15.2.0 [required: >=14]
  │     │  │  └─ dependencies of libgcc displayed above
  │     │  ├─ libstdcxx 15.2.0 [required: >=14]
  │     │  │  └─ dependencies of libstdcxx displayed above
  │     │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │     │  │  └─ dependencies of libzlib displayed above
  │     │  └─ openssl 3.5.4 [required: >=3.5.2,<4.0a0]
  │     │     └─ dependencies of openssl displayed above
  │     ├─ libssh2 1.11.1 [required: >=1.11.1,<2.0a0]
  │     │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │     │  ├─ libgcc 15.2.0 [required: >=13]
  │     │  │  └─ dependencies of libgcc displayed above
  │     │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │     │  │  └─ dependencies of libzlib displayed above
  │     │  └─ openssl 3.5.4 [required: >=3.5.0,<4.0a0]
  │     │     └─ dependencies of openssl displayed above
  │     ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │     │  └─ dependencies of libzlib displayed above
  │     ├─ openssl 3.5.4 [required: >=3.5.0,<4.0a0]
  │     │  └─ dependencies of openssl displayed above
  │     └─ zstd 1.5.7 [required: >=1.5.7,<1.6.0a0]
  │        └─ dependencies of zstd displayed above
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ reproc 14.2.5.post0 [required: >=14.2,<15.0a0]
  │  └─ dependencies of reproc displayed above
  ├─ reproc-cpp 14.2.5.post0 [required: >=14.2,<15.0a0]
  │  └─ dependencies of reproc-cpp displayed above
  └─ zstd 1.5.7 [required: >=1.5.7,<1.6.0a0]
     └─ dependencies of zstd displayed above
jupyter-resource-usage==1.2.0
  ├─ jupyter_server 2.17.0 [required: >=2.0.0,<3]
  │  ├─ anyio 4.11.0 [required: >=3.1.0]
  │  │  ├─ exceptiongroup 1.3.0 [required: >=1.0.2]
  │  │  │  ├─ python 3.13.8 [required: >=3.9]
  │  │  │  └─ typing_extensions 4.15.0 [required: >=4.6.0]
  │  │  │     └─ python 3.13.8 [required: any]
  │  │  ├─ idna 3.11 [required: >=2.8]
  │  │  │  └─ python 3.13.8 [required: >=3.10]
  │  │  ├─ python 3.13.8 [required: any]
  │  │  ├─ sniffio 1.3.1 [required: >=1.1]
  │  │  │  └─ python 3.13.8 [required: >=3.9]
  │  │  └─ typing_extensions 4.15.0 [required: >=4.5]
  │  │     └─ dependencies of typing_extensions displayed above
  │  ├─ argon2-cffi 25.1.0 [required: >=21.1]
  │  │  ├─ argon2-cffi-bindings 25.1.0 [required: any]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ cffi 2.0.0 [required: >=1.0.1]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libffi 3.4.6 [required: >=3.4.6,<3.5.0a0]
  │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  │  └─ libgcc 15.2.0 [required: >=13]
  │  │  │  │  │     └─ dependencies of libgcc displayed above
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  ├─ pycparser 2.22 [required: any]
  │  │  │  │  │  └─ python 3.13.8 [required: any]
  │  │  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  ├─ python 3.13.8 [required: >=3.9]
  │  │  └─ typing-extensions 4.15.0 [required: any]
  │  │     └─ typing_extensions 4.15.0 [required: ==4.15.0, pyhcf101f3_0]
  │  │        └─ dependencies of typing_extensions displayed above
  │  ├─ jinja2 3.1.6 [required: >=3.0.3]
  │  │  ├─ markupsafe 3.0.3 [required: >=2.0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ jupyter_client 8.6.3 [required: >=7.4.4]
  │  │  ├─ importlib-metadata 8.7.0 [required: >=4.8.3]
  │  │  │  ├─ python 3.13.8 [required: any]
  │  │  │  └─ zipp 3.23.0 [required: >=3.20]
  │  │  │     └─ python 3.13.8 [required: >=3.9]
  │  │  ├─ jupyter_core 5.8.1 [required: >=4.12,!=5.0.*]
  │  │  │  ├─ __unix [required: any]
  │  │  │  ├─ platformdirs 4.5.0 [required: >=2.5]
  │  │  │  │  └─ python 3.13.8 [required: any]
  │  │  │  ├─ python 3.13.8 [required: >=3.8]
  │  │  │  └─ traitlets 5.14.3 [required: >=5.3]
  │  │  │     └─ python 3.13.8 [required: >=3.9]
  │  │  ├─ python 3.13.8 [required: >=3.9]
  │  │  ├─ python-dateutil 2.9.0.post0 [required: >=2.8.2]
  │  │  │  ├─ python 3.13.8 [required: any]
  │  │  │  └─ six 1.17.0 [required: >=1.5]
  │  │  │     └─ python 3.13.8 [required: any]
  │  │  ├─ pyzmq 27.1.0 [required: >=23.0]
  │  │  │  ├─ python 3.13.8 [required: any]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ _python_abi3_support 1.0 [required: 1.*]
  │  │  │  │  ├─ cpython 3.13.8 [required: any]
  │  │  │  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  │  │  │  └─ python_abi 3.13 [required: *, *_cp313]
  │  │  │  │  └─ python-gil 3.13.8 [required: any]
  │  │  │  │     ├─ cpython 3.13.8 [required: 3.13.8.*]
  │  │  │  │     │  └─ dependencies of cpython displayed above
  │  │  │  │     └─ python_abi 3.13 [required: *, *_cp313]
  │  │  │  ├─ cpython 3.13.8 [required: >=3.12]
  │  │  │  │  └─ dependencies of cpython displayed above
  │  │  │  └─ zeromq 4.3.5 [required: >=4.3.5,<4.4.0a0]
  │  │  │     ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │     │  └─ dependencies of libstdcxx displayed above
  │  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │  │     │  └─ dependencies of libgcc displayed above
  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │     ├─ libsodium 1.0.20 [required: >=1.0.20,<1.0.21.0a0]
  │  │  │     │  └─ libgcc-ng 15.2.0 [required: >=12]
  │  │  │     │     └─ dependencies of libgcc-ng displayed above
  │  │  │     └─ krb5 1.21.3 [required: >=1.21.3,<1.22.0a0]
  │  │  │        └─ dependencies of krb5 displayed above
  │  │  ├─ tornado 6.5.2 [required: >=6.2]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  └─ traitlets 5.14.3 [required: >=5.3]
  │  │     └─ dependencies of traitlets displayed above
  │  ├─ jupyter_core 5.8.1 [required: >=4.12,!=5.0.*]
  │  │  └─ dependencies of jupyter_core displayed above
  │  ├─ jupyter_events 0.12.0 [required: >=0.11.0]
  │  │  ├─ jsonschema-with-format-nongpl 4.25.1 [required: >=4.18.0]
  │  │  │  ├─ jsonschema 4.25.1 [required: >=4.25.1,<4.25.2.0a0]
  │  │  │  │  ├─ attrs 25.4.0 [required: >=22.2.0]
  │  │  │  │  │  └─ python 3.13.8 [required: >=3.10]
  │  │  │  │  ├─ jsonschema-specifications 2025.9.1 [required: >=2023.3.6]
  │  │  │  │  │  ├─ python 3.13.8 [required: any]
  │  │  │  │  │  └─ referencing 0.36.2 [required: >=0.31.0]
  │  │  │  │  │     ├─ attrs 25.4.0 [required: >=22.2.0]
  │  │  │  │  │     │  └─ dependencies of attrs displayed above
  │  │  │  │  │     ├─ python 3.13.8 [required: any]
  │  │  │  │  │     ├─ rpds-py 0.27.1 [required: >=0.7.0]
  │  │  │  │  │     │  ├─ python 3.13.8 [required: any]
  │  │  │  │  │     │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  │     │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │     │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  │     │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  │  │  │     └─ typing_extensions 4.15.0 [required: >=4.4.0]
  │  │  │  │  │        └─ dependencies of typing_extensions displayed above
  │  │  │  │  ├─ python 3.13.8 [required: any]
  │  │  │  │  ├─ referencing 0.36.2 [required: >=0.28.4]
  │  │  │  │  │  └─ dependencies of referencing displayed above
  │  │  │  │  └─ rpds-py 0.27.1 [required: >=0.7.1]
  │  │  │  │     └─ dependencies of rpds-py displayed above
  │  │  │  ├─ fqdn 1.5.1 [required: any]
  │  │  │  │  ├─ cached-property 1.5.2 [required: >=1.3.0]
  │  │  │  │  │  └─ cached_property 1.5.2 [required: >=1.5.2,<1.5.3.0a0]
  │  │  │  │  │     └─ python 3.13.8 [required: >=3.6]
  │  │  │  │  └─ python 3.13.8 [required: >=3.9,<4]
  │  │  │  ├─ idna 3.11 [required: any]
  │  │  │  │  └─ dependencies of idna displayed above
  │  │  │  ├─ isoduration 20.11.0 [required: any]
  │  │  │  │  ├─ arrow 1.3.0 [required: >=0.15.0]
  │  │  │  │  │  ├─ python 3.13.8 [required: >=3.9]
  │  │  │  │  │  ├─ python-dateutil 2.9.0.post0 [required: >=2.7.0]
  │  │  │  │  │  │  └─ dependencies of python-dateutil displayed above
  │  │  │  │  │  └─ types-python-dateutil 2.9.0.20251008 [required: >=2.8.10]
  │  │  │  │  │     └─ python 3.13.8 [required: >=3.10]
  │  │  │  │  └─ python 3.13.8 [required: >=3.9]
  │  │  │  ├─ jsonpointer 3.0.0 [required: >1.13]
  │  │  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  │  ├─ rfc3339-validator 0.1.4 [required: any]
  │  │  │  │  ├─ python 3.13.8 [required: >=3.9]
  │  │  │  │  └─ six 1.17.0 [required: any]
  │  │  │  │     └─ dependencies of six displayed above
  │  │  │  ├─ rfc3986-validator 0.1.1 [required: >0.1.0]
  │  │  │  │  └─ python 3.13.8 [required: any]
  │  │  │  ├─ rfc3987-syntax 1.1.0 [required: >=1.1.0]
  │  │  │  │  ├─ python 3.13.8 [required: any]
  │  │  │  │  └─ lark 1.3.0 [required: >=1.2.2]
  │  │  │  │     └─ python 3.13.8 [required: >=3.10]
  │  │  │  ├─ uri-template 1.3.0 [required: any]
  │  │  │  │  └─ python 3.13.8 [required: >=3.9]
  │  │  │  └─ webcolors 24.11.1 [required: >=24.6.0]
  │  │  │     └─ python 3.13.8 [required: >=3.9]
  │  │  ├─ packaging 25.0 [required: any]
  │  │  │  └─ python 3.13.8 [required: any]
  │  │  ├─ python 3.13.8 [required: any]
  │  │  ├─ python-json-logger 2.0.7 [required: >=2.0.4]
  │  │  │  └─ python 3.13.8 [required: >=3.6]
  │  │  ├─ pyyaml 6.0.3 [required: >=5.3]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  │  ├─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  │  └─ yaml 0.2.5 [required: >=0.2.5,<0.3.0a0]
  │  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │  │     │  └─ dependencies of libgcc displayed above
  │  │  │     └─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ referencing 0.36.2 [required: any]
  │  │  │  └─ dependencies of referencing displayed above
  │  │  ├─ rfc3339-validator 0.1.4 [required: any]
  │  │  │  └─ dependencies of rfc3339-validator displayed above
  │  │  ├─ rfc3986-validator 0.1.1 [required: >=0.1.1]
  │  │  │  └─ dependencies of rfc3986-validator displayed above
  │  │  └─ traitlets 5.14.3 [required: >=5.3]
  │  │     └─ dependencies of traitlets displayed above
  │  ├─ jupyter_server_terminals 0.5.3 [required: >=0.4.4]
  │  │  ├─ python 3.13.8 [required: >=3.9]
  │  │  └─ terminado 0.18.1 [required: >=0.8.3]
  │  │     ├─ __linux [required: any]
  │  │     ├─ ptyprocess 0.7.0 [required: any]
  │  │     │  └─ python 3.13.8 [required: >=3.9]
  │  │     ├─ python 3.13.8 [required: >=3.8]
  │  │     └─ tornado 6.5.2 [required: >=6.1.0]
  │  │        └─ dependencies of tornado displayed above
  │  ├─ nbconvert-core 7.16.6 [required: >=6.4.4]
  │  │  ├─ beautifulsoup4 4.14.2 [required: any]
  │  │  │  ├─ python 3.13.8 [required: >=3.10]
  │  │  │  ├─ soupsieve 2.8 [required: >=1.2]
  │  │  │  │  └─ python 3.13.8 [required: >=3.10]
  │  │  │  └─ typing-extensions 4.15.0 [required: any]
  │  │  │     └─ dependencies of typing-extensions displayed above
  │  │  ├─ bleach-with-css 6.2.0 [required: !=5.0.0]
  │  │  │  ├─ bleach 6.2.0 [required: ==6.2.0, pyh29332c3_4]
  │  │  │  │  ├─ python 3.13.8 [required: any]
  │  │  │  │  └─ webencodings 0.5.1 [required: any]
  │  │  │  │     └─ python 3.13.8 [required: >=3.9]
  │  │  │  └─ tinycss2 1.4.0 [required: any]
  │  │  │     ├─ python 3.13.8 [required: >=3.5]
  │  │  │     └─ webencodings 0.5.1 [required: >=0.4]
  │  │  │        └─ dependencies of webencodings displayed above
  │  │  ├─ defusedxml 0.7.1 [required: any]
  │  │  │  └─ python 3.13.8 [required: >=3.6]
  │  │  ├─ importlib-metadata 8.7.0 [required: >=3.6]
  │  │  │  └─ dependencies of importlib-metadata displayed above
  │  │  ├─ jinja2 3.1.6 [required: >=3.0]
  │  │  │  └─ dependencies of jinja2 displayed above
  │  │  ├─ jupyter_core 5.8.1 [required: >=4.7]
  │  │  │  └─ dependencies of jupyter_core displayed above
  │  │  ├─ jupyterlab_pygments 0.3.0 [required: any]
  │  │  │  ├─ pygments 2.19.2 [required: >=2.4.1,<3]
  │  │  │  │  └─ python 3.13.8 [required: >=3.9]
  │  │  │  └─ python 3.13.8 [required: >=3.9]
  │  │  ├─ markupsafe 3.0.3 [required: >=2.0]
  │  │  │  └─ dependencies of markupsafe displayed above
  │  │  ├─ mistune 3.1.4 [required: >=2.0.3,<4]
  │  │  │  ├─ python 3.13.8 [required: any]
  │  │  │  └─ typing_extensions 4.15.0 [required: any]
  │  │  │     └─ dependencies of typing_extensions displayed above
  │  │  ├─ nbclient 0.10.2 [required: >=0.5.0]
  │  │  │  ├─ jupyter_client 8.6.3 [required: >=6.1.12]
  │  │  │  │  └─ dependencies of jupyter_client displayed above
  │  │  │  ├─ jupyter_core 5.8.1 [required: >=4.12,!=5.0.*]
  │  │  │  │  └─ dependencies of jupyter_core displayed above
  │  │  │  ├─ nbformat 5.10.4 [required: >=5.1]
  │  │  │  │  ├─ jsonschema 4.25.1 [required: >=2.6]
  │  │  │  │  │  └─ dependencies of jsonschema displayed above
  │  │  │  │  ├─ jupyter_core 5.8.1 [required: >=4.12,!=5.0.*]
  │  │  │  │  │  └─ dependencies of jupyter_core displayed above
  │  │  │  │  ├─ python 3.13.8 [required: >=3.9]
  │  │  │  │  ├─ python-fastjsonschema 2.21.2 [required: >=2.15]
  │  │  │  │  │  └─ python 3.13.8 [required: any]
  │  │  │  │  └─ traitlets 5.14.3 [required: >=5.1]
  │  │  │  │     └─ dependencies of traitlets displayed above
  │  │  │  ├─ python 3.13.8 [required: >=3.8]
  │  │  │  └─ traitlets 5.14.3 [required: >=5.4]
  │  │  │     └─ dependencies of traitlets displayed above
  │  │  ├─ nbformat 5.10.4 [required: >=5.7]
  │  │  │  └─ dependencies of nbformat displayed above
  │  │  ├─ packaging 25.0 [required: any]
  │  │  │  └─ dependencies of packaging displayed above
  │  │  ├─ pandocfilters 1.5.0 [required: >=1.4.1]
  │  │  │  └─ python 3.13.8 [required: !=3.0,!=3.1,!=3.2,!=3.3]
  │  │  ├─ pygments 2.19.2 [required: >=2.4.1]
  │  │  │  └─ dependencies of pygments displayed above
  │  │  ├─ python 3.13.8 [required: any]
  │  │  └─ traitlets 5.14.3 [required: >=5.1]
  │  │     └─ dependencies of traitlets displayed above
  │  ├─ nbformat 5.10.4 [required: >=5.3.0]
  │  │  └─ dependencies of nbformat displayed above
  │  ├─ overrides 7.7.0 [required: >=5.0]
  │  │  ├─ python 3.13.8 [required: >=3.9]
  │  │  └─ typing_utils 0.1.0 [required: any]
  │  │     └─ python 3.13.8 [required: >=3.9]
  │  ├─ packaging 25.0 [required: >=22.0]
  │  │  └─ dependencies of packaging displayed above
  │  ├─ prometheus_client 0.23.1 [required: >=0.9]
  │  │  └─ python 3.13.8 [required: >=3.10]
  │  ├─ python 3.13.8 [required: any]
  │  ├─ pyzmq 27.1.0 [required: >=24]
  │  │  └─ dependencies of pyzmq displayed above
  │  ├─ send2trash 1.8.3 [required: >=1.8.2]
  │  │  ├─ __linux [required: any]
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ terminado 0.18.1 [required: >=0.8.3]
  │  │  └─ dependencies of terminado displayed above
  │  ├─ tornado 6.5.2 [required: >=6.2.0]
  │  │  └─ dependencies of tornado displayed above
  │  ├─ traitlets 5.14.3 [required: >=5.6.0]
  │  │  └─ dependencies of traitlets displayed above
  │  └─ websocket-client 1.9.0 [required: >=1.7]
  │     └─ python 3.13.8 [required: >=3.10]
  ├─ psutil 7.1.0 [required: >=5.6.0]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  ├─ python 3.13.8 [required: >=3.9]
  └─ pyzmq 27.1.0 [required: >=19]
     └─ dependencies of pyzmq displayed above
nodejs==24.9.0
  ├─ __glibc [required: >=2.28,<3.0.a0]
  ├─ libstdcxx 15.2.0 [required: >=14]
  │  └─ dependencies of libstdcxx displayed above
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ libuv 1.51.0 [required: >=1.51.0,<2.0a0]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  └─ libgcc 15.2.0 [required: >=14]
  │     └─ dependencies of libgcc displayed above
  ├─ openssl 3.5.4 [required: >=3.5.3,<4.0a0]
  │  └─ dependencies of openssl displayed above
  ├─ icu 75.1 [required: >=75.1,<76.0a0]
  │  └─ dependencies of icu displayed above
  └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
     └─ dependencies of libzlib displayed above
r-nycflights13==1.0.2
  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ _openmp_mutex 4.5 [required: >=4.5]
  │  │  └─ dependencies of _openmp_mutex displayed above
  │  ├─ _r-mutex 1.0.1 [required: 1.*, anacondar_1]
  │  ├─ bwidget 1.10.1 [required: any]
  │  │  └─ tk 8.6.13 [required: any]
  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │     ├─ libgcc 15.2.0 [required: >=13]
  │  │     │  └─ dependencies of libgcc displayed above
  │  │     └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │        └─ dependencies of libzlib displayed above
  │  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
  │  │  └─ dependencies of bzip2 displayed above
  │  ├─ cairo 1.18.4 [required: >=1.18.4,<2.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ fontconfig 2.15.0 [required: >=2.15.0,<3.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ freetype 2.14.1 [required: >=2.12.1,<3.0a0]
  │  │  │  │  ├─ libfreetype 2.14.1 [required: 2.14.1, ha770c72_0]
  │  │  │  │  │  └─ libfreetype6 2.14.1 [required: >=2.14.1]
  │  │  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │     │  └─ dependencies of libgcc displayed above
  │  │  │  │  │     ├─ libpng 1.6.50 [required: >=1.6.50,<1.7.0a0]
  │  │  │  │  │     │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │     │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  │     │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  │     │  └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │  │  │     │     └─ dependencies of libzlib displayed above
  │  │  │  │  │     └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │  │  │        └─ dependencies of libzlib displayed above
  │  │  │  │  └─ libfreetype6 2.14.1 [required: 2.14.1, h73754d4_0]
  │  │  │  │     └─ dependencies of libfreetype6 displayed above
  │  │  │  ├─ libexpat 2.7.1 [required: >=2.6.3,<3.0a0]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  └─ libgcc 15.2.0 [required: >=14]
  │  │  │  │     └─ dependencies of libgcc displayed above
  │  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ libuuid 2.41.2 [required: >=2.38.1,<3.0a0]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  └─ libgcc 15.2.0 [required: >=14]
  │  │  │  │     └─ dependencies of libgcc displayed above
  │  │  │  └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │     └─ dependencies of libzlib displayed above
  │  │  ├─ fonts-conda-ecosystem 1 [required: any]
  │  │  │  └─ fonts-conda-forge 1 [required: any]
  │  │  │     ├─ font-ttf-dejavu-sans-mono 2.37 [required: any]
  │  │  │     ├─ font-ttf-inconsolata 3.000 [required: any]
  │  │  │     ├─ font-ttf-source-code-pro 2.038 [required: any]
  │  │  │     └─ font-ttf-ubuntu 0.83 [required: any]
  │  │  ├─ freetype 2.14.1 [required: >=2.12.1,<3.0a0]
  │  │  │  └─ dependencies of freetype displayed above
  │  │  ├─ icu 75.1 [required: >=75.1,<76.0a0]
  │  │  │  └─ dependencies of icu displayed above
  │  │  ├─ libexpat 2.7.1 [required: >=2.6.4,<3.0a0]
  │  │  │  └─ dependencies of libexpat displayed above
  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libglib 2.86.0 [required: >=2.82.2,<3.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libffi 3.4.6 [required: >=3.4.6,<3.5.0a0]
  │  │  │  │  └─ dependencies of libffi displayed above
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ libiconv 1.18 [required: >=1.18,<2.0a0]
  │  │  │  │  └─ dependencies of libiconv displayed above
  │  │  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  └─ pcre2 10.46 [required: >=10.46,<10.47.0a0]
  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │     ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
  │  │  │     │  └─ dependencies of bzip2 displayed above
  │  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │  │     │  └─ dependencies of libgcc displayed above
  │  │  │     └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │        └─ dependencies of libzlib displayed above
  │  │  ├─ libpng 1.6.50 [required: >=1.6.47,<1.7.0a0]
  │  │  │  └─ dependencies of libpng displayed above
  │  │  ├─ libstdcxx 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  ├─ libxcb 1.17.0 [required: >=1.17.0,<2.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ pthread-stubs 0.4 [required: any]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  └─ libgcc 15.2.0 [required: >=13]
  │  │  │  │     └─ dependencies of libgcc displayed above
  │  │  │  ├─ xorg-libxau 1.0.12 [required: >=1.0.11,<2.0a0]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  └─ libgcc 15.2.0 [required: >=13]
  │  │  │  │     └─ dependencies of libgcc displayed above
  │  │  │  └─ xorg-libxdmcp 1.1.5 [required: any]
  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │     └─ libgcc 15.2.0 [required: >=13]
  │  │  │        └─ dependencies of libgcc displayed above
  │  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │  └─ dependencies of libzlib displayed above
  │  │  ├─ pixman 0.46.4 [required: >=0.44.2,<1.0a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  └─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ xorg-libice 1.1.2 [required: >=1.1.2,<2.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  └─ libgcc 15.2.0 [required: >=13]
  │  │  │     └─ dependencies of libgcc displayed above
  │  │  ├─ xorg-libsm 1.2.6 [required: >=1.2.5,<2.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ libuuid 2.41.2 [required: >=2.38.1,<3.0a0]
  │  │  │  │  └─ dependencies of libuuid displayed above
  │  │  │  └─ xorg-libice 1.1.2 [required: >=1.1.2,<2.0a0]
  │  │  │     └─ dependencies of xorg-libice displayed above
  │  │  ├─ xorg-libx11 1.8.12 [required: >=1.8.11,<2.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  └─ libxcb 1.17.0 [required: >=1.17.0,<2.0a0]
  │  │  │     └─ dependencies of libxcb displayed above
  │  │  ├─ xorg-libxext 1.3.6 [required: >=1.3.6,<2.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  └─ xorg-libx11 1.8.12 [required: >=1.8.10,<2.0a0]
  │  │  │     └─ dependencies of xorg-libx11 displayed above
  │  │  └─ xorg-libxrender 0.9.12 [required: >=0.9.12,<0.10.0a0]
  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │     ├─ libgcc 15.2.0 [required: >=13]
  │  │     │  └─ dependencies of libgcc displayed above
  │  │     └─ xorg-libx11 1.8.12 [required: >=1.8.10,<2.0a0]
  │  │        └─ dependencies of xorg-libx11 displayed above
  │  ├─ curl 8.14.1 [required: any]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ krb5 1.21.3 [required: >=1.21.3,<1.22.0a0]
  │  │  │  └─ dependencies of krb5 displayed above
  │  │  ├─ libcurl 8.14.1 [required: 8.14.1, h332b0f4_0]
  │  │  │  └─ dependencies of libcurl displayed above
  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libssh2 1.11.1 [required: >=1.11.1,<2.0a0]
  │  │  │  └─ dependencies of libssh2 displayed above
  │  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │  └─ dependencies of libzlib displayed above
  │  │  ├─ openssl 3.5.4 [required: >=3.5.0,<4.0a0]
  │  │  │  └─ dependencies of openssl displayed above
  │  │  └─ zstd 1.5.7 [required: >=1.5.7,<1.6.0a0]
  │  │     └─ dependencies of zstd displayed above
  │  ├─ gcc_impl_linux-64 15.2.0 [required: >=10]
  │  │  ├─ binutils_impl_linux-64 2.44 [required: >=2.40]
  │  │  │  ├─ ld_impl_linux-64 2.44 [required: 2.44, ha97dd6f_2]
  │  │  │  │  └─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  └─ sysroot_linux-64 2.34 [required: any]
  │  │  │     ├─ __glibc [required: >=2.34]
  │  │  │     ├─ kernel-headers_linux-64 5.14.0 [required: 5.14.0, he073ed8_2]
  │  │  │     └─ tzdata 2025b [required: any]
  │  │  ├─ libgcc 15.2.0 [required: >=15.2.0]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libgcc-devel_linux-64 15.2.0 [required: 15.2.0, h73f6952_107]
  │  │  │  └─ __unix [required: any]
  │  │  ├─ libgomp 15.2.0 [required: >=15.2.0]
  │  │  │  └─ dependencies of libgomp displayed above
  │  │  ├─ libsanitizer 15.2.0 [required: 15.2.0, hb13aed2_7]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=15.2.0]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  └─ libstdcxx 15.2.0 [required: >=15.2.0]
  │  │  │     └─ dependencies of libstdcxx displayed above
  │  │  ├─ libstdcxx 15.2.0 [required: >=15.2.0]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  └─ sysroot_linux-64 2.34 [required: any]
  │  │     └─ dependencies of sysroot_linux-64 displayed above
  │  ├─ gfortran_impl_linux-64 15.2.0 [required: any]
  │  │  ├─ gcc_impl_linux-64 15.2.0 [required: >=15.2.0]
  │  │  │  └─ dependencies of gcc_impl_linux-64 displayed above
  │  │  ├─ libgcc 15.2.0 [required: >=15.2.0]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libgfortran5 15.2.0 [required: >=15.2.0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  └─ libgcc 15.2.0 [required: >=15.2.0]
  │  │  │     └─ dependencies of libgcc displayed above
  │  │  ├─ libstdcxx 15.2.0 [required: >=15.2.0]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  └─ sysroot_linux-64 2.34 [required: any]
  │  │     └─ dependencies of sysroot_linux-64 displayed above
  │  ├─ gsl 2.7 [required: >=2.7,<2.8.0a0]
  │  │  ├─ libblas 3.9.0 [required: >=3.8.0,<4.0a0]
  │  │  │  └─ libopenblas 0.3.30 [required: >=0.3.30,<1.0a0]
  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │  │     │  └─ dependencies of libgcc displayed above
  │  │  │     ├─ libgfortran 15.2.0 [required: any]
  │  │  │     │  └─ libgfortran5 15.2.0 [required: 15.2.0, hcd61629_7]
  │  │  │     │     └─ dependencies of libgfortran5 displayed above
  │  │  │     └─ libgfortran5 15.2.0 [required: >=14.3.0]
  │  │  │        └─ dependencies of libgfortran5 displayed above
  │  │  ├─ libcblas 3.9.0 [required: >=3.8.0,<4.0a0]
  │  │  │  └─ libblas 3.9.0 [required: 3.9.0, 37_h4a7cf45_openblas]
  │  │  │     └─ dependencies of libblas displayed above
  │  │  └─ libgcc-ng 15.2.0 [required: >=9.3.0]
  │  │     └─ dependencies of libgcc-ng displayed above
  │  ├─ gxx_impl_linux-64 15.2.0 [required: >=10]
  │  │  ├─ gcc_impl_linux-64 15.2.0 [required: 15.2.0, hcacfade_7]
  │  │  │  └─ dependencies of gcc_impl_linux-64 displayed above
  │  │  ├─ libstdcxx-devel_linux-64 15.2.0 [required: 15.2.0, h73f6952_107]
  │  │  │  └─ __unix [required: any]
  │  │  ├─ sysroot_linux-64 2.34 [required: any]
  │  │  │  └─ dependencies of sysroot_linux-64 displayed above
  │  │  └─ tzdata 2025b [required: any]
  │  ├─ icu 75.1 [required: >=75.1,<76.0a0]
  │  │  └─ dependencies of icu displayed above
  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ dependencies of libblas displayed above
  │  ├─ libcurl 8.14.1 [required: >=8.14.1,<9.0a0]
  │  │  └─ dependencies of libcurl displayed above
  │  ├─ libdeflate 1.24 [required: >=1.24,<1.25.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  └─ libgcc 15.2.0 [required: >=13]
  │  │     └─ dependencies of libgcc displayed above
  │  ├─ libexpat 2.7.1 [required: >=2.7.1,<3.0a0]
  │  │  └─ dependencies of libexpat displayed above
  │  ├─ libgcc 15.2.0 [required: any]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libgcc-ng 15.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libgfortran 15.2.0 [required: any]
  │  │  └─ dependencies of libgfortran displayed above
  │  ├─ libgfortran-ng 15.2.0 [required: any]
  │  │  └─ libgfortran 15.2.0 [required: 15.2.0, h69a702a_7]
  │  │     └─ dependencies of libgfortran displayed above
  │  ├─ libgfortran5 15.2.0 [required: >=10.4.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ libglib 2.86.0 [required: >=2.86.0,<3.0a0]
  │  │  └─ dependencies of libglib displayed above
  │  ├─ libiconv 1.18 [required: >=1.18,<2.0a0]
  │  │  └─ dependencies of libiconv displayed above
  │  ├─ libjpeg-turbo 3.1.0 [required: >=3.1.0,<4.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  └─ libgcc 15.2.0 [required: >=13]
  │  │     └─ dependencies of libgcc displayed above
  │  ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ libblas 3.9.0 [required: 3.9.0, 37_h4a7cf45_openblas]
  │  │     └─ dependencies of libblas displayed above
  │  ├─ liblzma 5.8.1 [required: >=5.8.1,<6.0a0]
  │  │  └─ dependencies of liblzma displayed above
  │  ├─ libpng 1.6.50 [required: >=1.6.50,<1.7.0a0]
  │  │  └─ dependencies of libpng displayed above
  │  ├─ libstdcxx 15.2.0 [required: any]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ libstdcxx-ng 15.2.0 [required: >=12]
  │  │  └─ dependencies of libstdcxx-ng displayed above
  │  ├─ libtiff 4.7.1 [required: >=4.7.1,<4.8.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ lerc 4.0.0 [required: >=4.0.0,<5.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  └─ libstdcxx 15.2.0 [required: >=13]
  │  │  │     └─ dependencies of libstdcxx displayed above
  │  │  ├─ libdeflate 1.24 [required: >=1.24,<1.25.0a0]
  │  │  │  └─ dependencies of libdeflate displayed above
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libjpeg-turbo 3.1.0 [required: >=3.1.0,<4.0a0]
  │  │  │  └─ dependencies of libjpeg-turbo displayed above
  │  │  ├─ liblzma 5.8.1 [required: >=5.8.1,<6.0a0]
  │  │  │  └─ dependencies of liblzma displayed above
  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  ├─ libwebp-base 1.6.0 [required: >=1.6.0,<2.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  └─ libgcc 15.2.0 [required: >=14]
  │  │  │     └─ dependencies of libgcc displayed above
  │  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │  └─ dependencies of libzlib displayed above
  │  │  └─ zstd 1.5.7 [required: >=1.5.7,<1.6.0a0]
  │  │     └─ dependencies of zstd displayed above
  │  ├─ libuuid 2.41.2 [required: >=2.41.2,<3.0a0]
  │  │  └─ dependencies of libuuid displayed above
  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  └─ dependencies of libzlib displayed above
  │  ├─ make 4.4.1 [required: any]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  └─ libgcc 15.2.0 [required: >=13]
  │  │     └─ dependencies of libgcc displayed above
  │  ├─ pango 1.56.4 [required: >=1.56.4,<2.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ cairo 1.18.4 [required: >=1.18.4,<2.0a0]
  │  │  │  └─ dependencies of cairo displayed above
  │  │  ├─ fontconfig 2.15.0 [required: >=2.15.0,<3.0a0]
  │  │  │  └─ dependencies of fontconfig displayed above
  │  │  ├─ fonts-conda-ecosystem 1 [required: any]
  │  │  │  └─ dependencies of fonts-conda-ecosystem displayed above
  │  │  ├─ fribidi 1.0.16 [required: >=1.0.10,<2.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  └─ libgcc 15.2.0 [required: >=14]
  │  │  │     └─ dependencies of libgcc displayed above
  │  │  ├─ harfbuzz 12.1.0 [required: >=11.0.1]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ cairo 1.18.4 [required: >=1.18.4,<2.0a0]
  │  │  │  │  └─ dependencies of cairo displayed above
  │  │  │  ├─ graphite2 1.3.14 [required: >=1.3.14,<2.0a0]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  └─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │     └─ dependencies of libstdcxx displayed above
  │  │  │  ├─ icu 75.1 [required: >=75.1,<76.0a0]
  │  │  │  │  └─ dependencies of icu displayed above
  │  │  │  ├─ libexpat 2.7.1 [required: >=2.7.1,<3.0a0]
  │  │  │  │  └─ dependencies of libexpat displayed above
  │  │  │  ├─ libfreetype 2.14.1 [required: >=2.14.1]
  │  │  │  │  └─ dependencies of libfreetype displayed above
  │  │  │  ├─ libfreetype6 2.14.1 [required: >=2.14.1]
  │  │  │  │  └─ dependencies of libfreetype6 displayed above
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ libglib 2.86.0 [required: >=2.86.0,<3.0a0]
  │  │  │  │  └─ dependencies of libglib displayed above
  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │     └─ dependencies of libzlib displayed above
  │  │  ├─ libexpat 2.7.1 [required: >=2.7.0,<3.0a0]
  │  │  │  └─ dependencies of libexpat displayed above
  │  │  ├─ libfreetype 2.14.1 [required: >=2.13.3]
  │  │  │  └─ dependencies of libfreetype displayed above
  │  │  ├─ libfreetype6 2.14.1 [required: >=2.13.3]
  │  │  │  └─ dependencies of libfreetype6 displayed above
  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libglib 2.86.0 [required: >=2.84.2,<3.0a0]
  │  │  │  └─ dependencies of libglib displayed above
  │  │  ├─ libpng 1.6.50 [required: >=1.6.49,<1.7.0a0]
  │  │  │  └─ dependencies of libpng displayed above
  │  │  └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │     └─ dependencies of libzlib displayed above
  │  ├─ pcre2 10.46 [required: >=10.46,<10.47.0a0]
  │  │  └─ dependencies of pcre2 displayed above
  │  ├─ readline 8.2 [required: >=8.2,<9.0a0]
  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  └─ ncurses 6.5 [required: >=6.5,<7.0a0]
  │  │     └─ dependencies of ncurses displayed above
  │  ├─ sed 4.9 [required: any]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  └─ libgcc 15.2.0 [required: >=13]
  │  │     └─ dependencies of libgcc displayed above
  │  ├─ tk 8.6.13 [required: >=8.6.13,<8.7.0a0]
  │  │  └─ dependencies of tk displayed above
  │  ├─ tktable 2.10 [required: any]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  └─ tk 8.6.13 [required: >=8.6.13,<8.7.0a0]
  │  │     └─ dependencies of tk displayed above
  │  ├─ tzdata 2025b [required: >=2024a]
  │  └─ xorg-libxt 1.3.1 [required: any]
  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │     ├─ libgcc 15.2.0 [required: >=13]
  │     │  └─ dependencies of libgcc displayed above
  │     ├─ xorg-libice 1.1.2 [required: >=1.1.1,<2.0a0]
  │     │  └─ dependencies of xorg-libice displayed above
  │     ├─ xorg-libsm 1.2.6 [required: >=1.2.4,<2.0a0]
  │     │  └─ dependencies of xorg-libsm displayed above
  │     └─ xorg-libx11 1.8.12 [required: >=1.8.10,<2.0a0]
  │        └─ dependencies of xorg-libx11 displayed above
  └─ r-tibble 3.3.0 [required: any]
     ├─ __glibc [required: >=2.17,<3.0.a0]
     ├─ libgcc 15.2.0 [required: >=14]
     │  └─ dependencies of libgcc displayed above
     ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
     │  └─ dependencies of r-base displayed above
     ├─ r-fansi 1.0.6 [required: >=0.4.0]
     │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  └─ dependencies of libgcc displayed above
     │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
     │     └─ dependencies of r-base displayed above
     ├─ r-lifecycle 1.0.4 [required: >=1.0.0]
     │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
     │  │  └─ dependencies of r-base displayed above
     │  ├─ r-cli 3.6.5 [required: >=3.4.0]
     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libgcc displayed above
     │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
     │  │     └─ dependencies of r-base displayed above
     │  ├─ r-glue 1.8.0 [required: any]
     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libgcc displayed above
     │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
     │  │     └─ dependencies of r-base displayed above
     │  └─ r-rlang 1.1.6 [required: >=1.0.6]
     │     ├─ __glibc [required: >=2.17,<3.0.a0]
     │     ├─ libgcc 15.2.0 [required: >=14]
     │     │  └─ dependencies of libgcc displayed above
     │     ├─ libstdcxx 15.2.0 [required: >=14]
     │     │  └─ dependencies of libstdcxx displayed above
     │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
     │        └─ dependencies of r-base displayed above
     ├─ r-magrittr 2.0.4 [required: any]
     │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  └─ dependencies of libgcc displayed above
     │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
     │     └─ dependencies of r-base displayed above
     ├─ r-pillar 1.11.1 [required: >=1.8.1]
     │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
     │  │  └─ dependencies of r-base displayed above
     │  ├─ r-cli 3.6.5 [required: any]
     │  │  └─ dependencies of r-cli displayed above
     │  ├─ r-crayon 1.5.3 [required: >=1.3.4]
     │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
     │  │     └─ dependencies of r-base displayed above
     │  ├─ r-ellipsis 0.3.2 [required: any]
     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libgcc displayed above
     │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
     │  │  │  └─ dependencies of r-base displayed above
     │  │  └─ r-rlang 1.1.6 [required: >=0.3.0]
     │  │     └─ dependencies of r-rlang displayed above
     │  ├─ r-fansi 1.0.6 [required: any]
     │  │  └─ dependencies of r-fansi displayed above
     │  ├─ r-lifecycle 1.0.4 [required: any]
     │  │  └─ dependencies of r-lifecycle displayed above
     │  ├─ r-rlang 1.1.6 [required: >=0.3.0]
     │  │  └─ dependencies of r-rlang displayed above
     │  ├─ r-utf8 1.2.6 [required: >=1.1.0]
     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libgcc displayed above
     │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
     │  │     └─ dependencies of r-base displayed above
     │  └─ r-vctrs 0.6.5 [required: >=0.2.0]
     │     ├─ __glibc [required: >=2.17,<3.0.a0]
     │     ├─ libgcc 15.2.0 [required: >=14]
     │     │  └─ dependencies of libgcc displayed above
     │     ├─ libstdcxx 15.2.0 [required: >=14]
     │     │  └─ dependencies of libstdcxx displayed above
     │     ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
     │     │  └─ dependencies of r-base displayed above
     │     ├─ r-cli 3.6.5 [required: >=3.4.0]
     │     │  └─ dependencies of r-cli displayed above
     │     ├─ r-glue 1.8.0 [required: any]
     │     │  └─ dependencies of r-glue displayed above
     │     ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
     │     │  └─ dependencies of r-lifecycle displayed above
     │     └─ r-rlang 1.1.6 [required: >=1.0.6]
     │        └─ dependencies of r-rlang displayed above
     ├─ r-pkgconfig 2.0.3 [required: any]
     │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
     │     └─ dependencies of r-base displayed above
     ├─ r-rlang 1.1.6 [required: >=1.0.2]
     │  └─ dependencies of r-rlang displayed above
     └─ r-vctrs 0.6.5 [required: >=0.4.2]
        └─ dependencies of r-vctrs displayed above
r-tidymodels==1.4.1
  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-broom 1.0.10 [required: >=1.0.9]
  │  ├─ r-backports 1.5.0 [required: any]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.0.0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  │  └─ dependencies of r-ellipsis displayed above
  │  │  ├─ r-generics 0.1.4 [required: any]
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-glue 1.8.0 [required: >=1.3.2]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.0]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-magrittr 2.0.4 [required: >=1.5]
  │  │  │  └─ dependencies of r-magrittr displayed above
  │  │  ├─ r-pillar 1.11.1 [required: >=1.5.1]
  │  │  │  └─ dependencies of r-pillar displayed above
  │  │  ├─ r-r6 2.6.1 [required: any]
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-rlang 1.1.6 [required: >=0.4.10]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-tibble 3.3.0 [required: >=2.1.3]
  │  │  │  └─ dependencies of r-tibble displayed above
  │  │  ├─ r-tidyselect 1.2.1 [required: >=1.1.0]
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-cli 3.6.5 [required: >=3.3.0]
  │  │  │  │  └─ dependencies of r-cli displayed above
  │  │  │  ├─ r-glue 1.8.0 [required: >=1.3.0]
  │  │  │  │  └─ dependencies of r-glue displayed above
  │  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  │  ├─ r-rlang 1.1.6 [required: >=1.0.4]
  │  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  │  ├─ r-vctrs 0.6.5 [required: >=0.5.2]
  │  │  │  │  └─ dependencies of r-vctrs displayed above
  │  │  │  └─ r-withr 3.0.2 [required: any]
  │  │  │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │        └─ dependencies of r-base displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.3.5]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  └─ dependencies of r-ellipsis displayed above
  │  ├─ r-generics 0.1.4 [required: >=0.0.2]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-ggplot2 4.0.0 [required: any]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.5 [required: any]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-glue 1.8.0 [required: any]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-gtable 0.3.6 [required: >=0.3.6]
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-cli 3.6.5 [required: any]
  │  │  │  │  └─ dependencies of r-cli displayed above
  │  │  │  ├─ r-glue 1.8.0 [required: any]
  │  │  │  │  └─ dependencies of r-glue displayed above
  │  │  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  │  └─ r-rlang 1.1.6 [required: any]
  │  │  │     └─ dependencies of r-rlang displayed above
  │  │  ├─ r-isoband 0.2.7 [required: any]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.1]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-rlang 1.1.6 [required: >=1.1.0]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-s7 0.2.0 [required: any]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-scales 1.4.0 [required: >=1.4.0]
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-farver 2.1.2 [required: >=2.0.0]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  ├─ r-labeling 0.4.3 [required: any]
  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  │  ├─ r-munsell 0.5.1 [required: >=0.5]
  │  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  └─ r-colorspace 2.1_2 [required: any]
  │  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │     │  └─ dependencies of libgcc displayed above
  │  │  │  │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │        └─ dependencies of r-base displayed above
  │  │  │  ├─ r-r6 2.6.1 [required: any]
  │  │  │  │  └─ dependencies of r-r6 displayed above
  │  │  │  ├─ r-rcolorbrewer 1.1_3 [required: any]
  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  └─ r-viridislite 0.4.2 [required: any]
  │  │  │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │        └─ dependencies of r-base displayed above
  │  │  ├─ r-vctrs 0.6.5 [required: >=0.6.0]
  │  │  │  └─ dependencies of r-vctrs displayed above
  │  │  └─ r-withr 3.0.2 [required: >=2.5.0]
  │  │     └─ dependencies of r-withr displayed above
  │  ├─ r-glue 1.8.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-purrr 1.1.0 [required: any]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.5 [required: >=3.4]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-magrittr 2.0.4 [required: >=1.5]
  │  │  │  └─ dependencies of r-magrittr displayed above
  │  │  ├─ r-rlang 1.1.6 [required: >=0.4.10]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.5]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-rlang 1.1.6 [required: any]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-stringr 1.5.2 [required: any]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.5 [required: any]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-glue 1.8.0 [required: >=1.6.1]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-magrittr 2.0.4 [required: any]
  │  │  │  └─ dependencies of r-magrittr displayed above
  │  │  ├─ r-rlang 1.1.6 [required: >=1.0.0]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-stringi 1.8.7 [required: >=1.5.3]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ icu 75.1 [required: >=75.1,<76.0a0]
  │  │  │  │  └─ dependencies of icu displayed above
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  └─ r-vctrs 0.6.5 [required: any]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-tibble 3.3.0 [required: >=3.0.0]
  │  │  └─ dependencies of r-tibble displayed above
  │  └─ r-tidyr 1.3.1 [required: >=1.0.0]
  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │     ├─ libgcc 15.2.0 [required: >=14]
  │     │  └─ dependencies of libgcc displayed above
  │     ├─ libstdcxx 15.2.0 [required: >=14]
  │     │  └─ dependencies of libstdcxx displayed above
  │     ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     ├─ r-cli 3.6.5 [required: >=3.4.1]
  │     │  └─ dependencies of r-cli displayed above
  │     ├─ r-dplyr 1.1.4 [required: >=1.0.10]
  │     │  └─ dependencies of r-dplyr displayed above
  │     ├─ r-glue 1.8.0 [required: any]
  │     │  └─ dependencies of r-glue displayed above
  │     ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │     │  └─ dependencies of r-lifecycle displayed above
  │     ├─ r-magrittr 2.0.4 [required: any]
  │     │  └─ dependencies of r-magrittr displayed above
  │     ├─ r-purrr 1.1.0 [required: >=1.0.1]
  │     │  └─ dependencies of r-purrr displayed above
  │     ├─ r-rlang 1.1.6 [required: >=1.0.4]
  │     │  └─ dependencies of r-rlang displayed above
  │     ├─ r-stringr 1.5.2 [required: >=1.5.0]
  │     │  └─ dependencies of r-stringr displayed above
  │     ├─ r-tibble 3.3.0 [required: >=2.1.1]
  │     │  └─ dependencies of r-tibble displayed above
  │     ├─ r-tidyselect 1.2.1 [required: >=1.2.0]
  │     │  └─ dependencies of r-tidyselect displayed above
  │     └─ r-vctrs 0.6.5 [required: >=0.5.2]
  │        └─ dependencies of r-vctrs displayed above
  ├─ r-cli 3.6.5 [required: >=3.6.5]
  │  └─ dependencies of r-cli displayed above
  ├─ r-conflicted 1.2.0 [required: >=1.2.0]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.5 [required: >=3.4.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-memoise 2.0.1 [required: any]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cachem 1.1.0 [required: any]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-fastmap 1.2.0 [required: any]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  └─ r-rlang 1.1.6 [required: any]
  │  │  │     └─ dependencies of r-rlang displayed above
  │  │  └─ r-rlang 1.1.6 [required: >=0.4.10]
  │  │     └─ dependencies of r-rlang displayed above
  │  └─ r-rlang 1.1.6 [required: >=1.0.0]
  │     └─ dependencies of r-rlang displayed above
  ├─ r-dials 1.4.2 [required: >=1.4.2]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.5 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-dicedesign 1.10 [required: any]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=0.8.5]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-glue 1.8.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-hardhat 1.4.2 [required: >=1.1.0]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.5 [required: >=3.6.0]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-glue 1.8.0 [required: >=1.6.2]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-rlang 1.1.6 [required: >=1.1.0]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-sparsevctrs 0.3.4 [required: >=0.2.0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-cli 3.6.5 [required: >=3.4.0]
  │  │  │  │  └─ dependencies of r-cli displayed above
  │  │  │  ├─ r-rlang 1.1.6 [required: >=1.1.0]
  │  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  │  └─ r-vctrs 0.6.5 [required: any]
  │  │  │     └─ dependencies of r-vctrs displayed above
  │  │  ├─ r-tibble 3.3.0 [required: >=3.2.1]
  │  │  │  └─ dependencies of r-tibble displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.6.0]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-pillar 1.11.1 [required: any]
  │  │  └─ dependencies of r-pillar displayed above
  │  ├─ r-purrr 1.1.0 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.6 [required: >=1.1.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-scales 1.4.0 [required: >=1.3.0]
  │  │  └─ dependencies of r-scales displayed above
  │  ├─ r-sfd 0.1.0 [required: any]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.5 [required: any]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-rlang 1.1.6 [required: any]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  └─ r-tibble 3.3.0 [required: any]
  │  │     └─ dependencies of r-tibble displayed above
  │  ├─ r-tibble 3.3.0 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-vctrs 0.6.5 [required: >=0.3.8]
  │  │  └─ dependencies of r-vctrs displayed above
  │  └─ r-withr 3.0.2 [required: any]
  │     └─ dependencies of r-withr displayed above
  ├─ r-dplyr 1.1.4 [required: >=1.1.4]
  │  └─ dependencies of r-dplyr displayed above
  ├─ r-ggplot2 4.0.0 [required: >=3.5.2]
  │  └─ dependencies of r-ggplot2 displayed above
  ├─ r-hardhat 1.4.2 [required: >=1.4.2]
  │  └─ dependencies of r-hardhat displayed above
  ├─ r-infer 1.0.9 [required: >=1.0.9]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-broom 1.0.10 [required: any]
  │  │  └─ dependencies of r-broom displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=0.7.0]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-generics 0.1.4 [required: any]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-ggplot2 4.0.0 [required: any]
  │  │  └─ dependencies of r-ggplot2 displayed above
  │  ├─ r-glue 1.8.0 [required: >=1.3.0]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-magrittr 2.0.4 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-patchwork 1.3.2 [required: any]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-ggplot2 4.0.0 [required: >=3.0.0]
  │  │  │  └─ dependencies of r-ggplot2 displayed above
  │  │  └─ r-gtable 0.3.6 [required: any]
  │  │     └─ dependencies of r-gtable displayed above
  │  ├─ r-purrr 1.1.0 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.6 [required: >=0.2.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.3.0 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  └─ r-tidyr 1.3.1 [required: any]
  │     └─ dependencies of r-tidyr displayed above
  ├─ r-modeldata 1.5.1 [required: >=1.5.1]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-dplyr 1.1.4 [required: any]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-mass 7.3_65 [required: any]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-purrr 1.1.0 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.6 [required: any]
  │  │  └─ dependencies of r-rlang displayed above
  │  └─ r-tibble 3.3.0 [required: any]
  │     └─ dependencies of r-tibble displayed above
  ├─ r-parsnip 1.3.3 [required: >=1.3.2]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.5 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.1.0]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-generics 0.1.4 [required: >=0.1.2]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-ggplot2 4.0.0 [required: any]
  │  │  └─ dependencies of r-ggplot2 displayed above
  │  ├─ r-globals 0.18.0 [required: any]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  └─ r-codetools 0.2_20 [required: any]
  │  │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │        └─ dependencies of r-base displayed above
  │  ├─ r-glue 1.8.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-hardhat 1.4.2 [required: >=1.1.0]
  │  │  └─ dependencies of r-hardhat displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-magrittr 2.0.4 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-pillar 1.11.1 [required: any]
  │  │  └─ dependencies of r-pillar displayed above
  │  ├─ r-prettyunits 1.2.0 [required: any]
  │  │  ├─ r-assertthat 0.2.1 [required: any]
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  └─ r-magrittr 2.0.4 [required: any]
  │  │     └─ dependencies of r-magrittr displayed above
  │  ├─ r-purrr 1.1.0 [required: >=1.0.0]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.6 [required: >=0.3.1]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.3.0 [required: >=2.1.1]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyr 1.3.1 [required: >=1.3.0]
  │  │  └─ dependencies of r-tidyr displayed above
  │  ├─ r-vctrs 0.6.5 [required: >=0.6.0]
  │  │  └─ dependencies of r-vctrs displayed above
  │  └─ r-withr 3.0.2 [required: any]
  │     └─ dependencies of r-withr displayed above
  ├─ r-purrr 1.1.0 [required: >=1.1.0]
  │  └─ dependencies of r-purrr displayed above
  ├─ r-recipes 1.3.1 [required: >=1.3.1]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.5 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-clock 0.7.3 [required: >=0.6.1]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.5 [required: >=3.6.4]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-cpp11 0.5.2 [required: >=0.5.2]
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.4]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-rlang 1.1.6 [required: >=1.1.5]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-tzdb 0.5.0 [required: >=0.5.0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-cpp11 0.5.2 [required: >=0.5.2]
  │  │  │     └─ dependencies of r-cpp11 displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.6.5]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.1.0]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-generics 0.1.4 [required: >=0.1.2]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-glue 1.8.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-gower 1.0.1 [required: any]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-hardhat 1.4.2 [required: >=1.4.1]
  │  │  └─ dependencies of r-hardhat displayed above
  │  ├─ r-ipred 0.9_15 [required: >=0.9_12]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-class 7.3_23 [required: any]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-mass 7.3_65 [required: any]
  │  │  │     └─ dependencies of r-mass displayed above
  │  │  ├─ r-mass 7.3_65 [required: any]
  │  │  │  └─ dependencies of r-mass displayed above
  │  │  ├─ r-nnet 7.3_20 [required: any]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-mass 7.3_65 [required: any]
  │  │  │     └─ dependencies of r-mass displayed above
  │  │  ├─ r-prodlim 2025.04.28 [required: any]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-data.table 1.17.8 [required: any]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ _openmp_mutex 4.5 [required: >=4.5]
  │  │  │  │  │  └─ dependencies of _openmp_mutex displayed above
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  ├─ r-diagram 1.6.5 [required: any]
  │  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  └─ r-shape 1.4.6.1 [required: any]
  │  │  │  │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │        └─ dependencies of r-base displayed above
  │  │  │  ├─ r-ggplot2 4.0.0 [required: any]
  │  │  │  │  └─ dependencies of r-ggplot2 displayed above
  │  │  │  ├─ r-kernsmooth 2.23_26 [required: any]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  │  │  └─ dependencies of libblas displayed above
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  ├─ libgfortran 15.2.0 [required: any]
  │  │  │  │  │  └─ dependencies of libgfortran displayed above
  │  │  │  │  ├─ libgfortran5 15.2.0 [required: >=14.3.0]
  │  │  │  │  │  └─ dependencies of libgfortran5 displayed above
  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  ├─ r-lava 1.8.1 [required: any]
  │  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  ├─ r-cli 3.6.5 [required: any]
  │  │  │  │  │  └─ dependencies of r-cli displayed above
  │  │  │  │  ├─ r-future.apply 1.20.0 [required: any]
  │  │  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  │  ├─ r-future 1.67.0 [required: >=1.28.0]
  │  │  │  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  │  │  ├─ r-digest 0.6.37 [required: any]
  │  │  │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  │  │  │  ├─ r-globals 0.18.0 [required: >=0.16.1]
  │  │  │  │  │  │  │  └─ dependencies of r-globals displayed above
  │  │  │  │  │  │  ├─ r-listenv 0.9.1 [required: >=0.8.0]
  │  │  │  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  │  │  │  └─ r-parallelly 1.45.1 [required: >=1.34.0]
  │  │  │  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  │     │  └─ dependencies of libgcc displayed above
  │  │  │  │  │  │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │  │        └─ dependencies of r-base displayed above
  │  │  │  │  │  └─ r-globals 0.18.0 [required: >=0.16.1]
  │  │  │  │  │     └─ dependencies of r-globals displayed above
  │  │  │  │  ├─ r-numderiv 2016.8_1.1 [required: any]
  │  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  │  ├─ r-progressr 0.16.0 [required: any]
  │  │  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  │  └─ r-digest 0.6.37 [required: any]
  │  │  │  │  │     └─ dependencies of r-digest displayed above
  │  │  │  │  ├─ r-squarem 2021.1 [required: any]
  │  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  │  └─ r-survival 3.8_3 [required: any]
  │  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │     │  └─ dependencies of libgcc displayed above
  │  │  │  │     ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │     │  └─ dependencies of r-base displayed above
  │  │  │  │     └─ r-matrix 1.7_4 [required: any]
  │  │  │  │        ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │        ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  │        │  └─ dependencies of libblas displayed above
  │  │  │  │        ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │        │  └─ dependencies of libgcc displayed above
  │  │  │  │        ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  │        │  └─ dependencies of liblapack displayed above
  │  │  │  │        ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │        │  └─ dependencies of r-base displayed above
  │  │  │  │        └─ r-lattice 0.22_7 [required: any]
  │  │  │  │           ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │           ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │           │  └─ dependencies of libgcc displayed above
  │  │  │  │           └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │              └─ dependencies of r-base displayed above
  │  │  │  ├─ r-rcpp 1.1.0 [required: >=0.11.5]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  ├─ r-rlang 1.1.6 [required: any]
  │  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  │  └─ r-survival 3.8_3 [required: any]
  │  │  │     └─ dependencies of r-survival displayed above
  │  │  ├─ r-rpart 4.1.24 [required: >=3.1_8]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  └─ r-survival 3.8_3 [required: any]
  │  │     └─ dependencies of r-survival displayed above
  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-lubridate 1.9.4 [required: >=1.8.0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-generics 0.1.4 [required: any]
  │  │  │  └─ dependencies of r-generics displayed above
  │  │  └─ r-timechange 0.3.0 [required: >=0.1.1]
  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │     │  └─ dependencies of libgcc displayed above
  │  │     ├─ libstdcxx 15.2.0 [required: >=14]
  │  │     │  └─ dependencies of libstdcxx displayed above
  │  │     ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     │  └─ dependencies of r-base displayed above
  │  │     └─ r-cpp11 0.5.2 [required: >=0.2.7]
  │  │        └─ dependencies of r-cpp11 displayed above
  │  ├─ r-magrittr 2.0.4 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-matrix 1.7_4 [required: any]
  │  │  └─ dependencies of r-matrix displayed above
  │  ├─ r-purrr 1.1.0 [required: >=1.0.0]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.6 [required: >=1.1.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-sparsevctrs 0.3.4 [required: >=0.3.0]
  │  │  └─ dependencies of r-sparsevctrs displayed above
  │  ├─ r-tibble 3.3.0 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyr 1.3.1 [required: >=1.0.0]
  │  │  └─ dependencies of r-tidyr displayed above
  │  ├─ r-tidyselect 1.2.1 [required: >=1.2.0]
  │  │  └─ dependencies of r-tidyselect displayed above
  │  ├─ r-timedate 4041.110 [required: any]
  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-vctrs 0.6.5 [required: >=0.5.0]
  │  │  └─ dependencies of r-vctrs displayed above
  │  └─ r-withr 3.0.2 [required: any]
  │     └─ dependencies of r-withr displayed above
  ├─ r-rlang 1.1.6 [required: >=1.1.6]
  │  └─ dependencies of r-rlang displayed above
  ├─ r-rsample 1.3.1 [required: >=1.3.1]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.0.0]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-furrr 0.3.1 [required: any]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  │  └─ dependencies of r-ellipsis displayed above
  │  │  ├─ r-future 1.67.0 [required: >=1.19.1]
  │  │  │  └─ dependencies of r-future displayed above
  │  │  ├─ r-globals 0.18.0 [required: >=0.13.1]
  │  │  │  └─ dependencies of r-globals displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=0.2.0]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-purrr 1.1.0 [required: >=0.3.0]
  │  │  │  └─ dependencies of r-purrr displayed above
  │  │  ├─ r-rlang 1.1.6 [required: >=0.3.0]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.3.2]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-generics 0.1.4 [required: any]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-glue 1.8.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-pillar 1.11.1 [required: any]
  │  │  └─ dependencies of r-pillar displayed above
  │  ├─ r-purrr 1.1.0 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.6 [required: >=0.4.10]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-slider 0.3.2 [required: >=0.1.5]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.5 [required: >=3.4.1]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-rlang 1.1.6 [required: >=1.0.6]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-vctrs 0.6.5 [required: >=0.5.0]
  │  │  │  └─ dependencies of r-vctrs displayed above
  │  │  └─ r-warp 0.2.1 [required: any]
  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │     │  └─ dependencies of libgcc displayed above
  │  │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │        └─ dependencies of r-base displayed above
  │  ├─ r-tibble 3.3.0 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyr 1.3.1 [required: any]
  │  │  └─ dependencies of r-tidyr displayed above
  │  ├─ r-tidyselect 1.2.1 [required: any]
  │  │  └─ dependencies of r-tidyselect displayed above
  │  └─ r-vctrs 0.6.5 [required: >=0.5.0]
  │     └─ dependencies of r-vctrs displayed above
  ├─ r-rstudioapi 0.17.1 [required: >=0.17.1]
  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-tailor 0.1.0 [required: >=0.1.0]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.5 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-dplyr 1.1.4 [required: any]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-generics 0.1.4 [required: any]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-hardhat 1.4.2 [required: any]
  │  │  └─ dependencies of r-hardhat displayed above
  │  ├─ r-purrr 1.1.0 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.6 [required: >=1.1.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.3.0 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyselect 1.2.1 [required: any]
  │  │  └─ dependencies of r-tidyselect displayed above
  │  └─ r-vctrs 0.6.5 [required: any]
  │     └─ dependencies of r-vctrs displayed above
  ├─ r-tidyr 1.3.1 [required: >=1.3.1]
  │  └─ dependencies of r-tidyr displayed above
  ├─ r-tune 2.0.0 [required: >=1.3.0]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.5 [required: >=3.3.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-dials 1.4.2 [required: >=1.3.0.9000]
  │  │  └─ dependencies of r-dials displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.1.0]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-generics 0.1.4 [required: >=0.1.2]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-ggplot2 4.0.0 [required: any]
  │  │  └─ dependencies of r-ggplot2 displayed above
  │  ├─ r-glue 1.8.0 [required: >=1.6.2]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-gpfit 1.0_9 [required: any]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-lattice 0.22_7 [required: >=0.18_8]
  │  │  │  └─ dependencies of r-lattice displayed above
  │  │  └─ r-lhs 1.2.0 [required: >=0.5]
  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │     │  └─ dependencies of libgcc displayed above
  │  │     ├─ libstdcxx 15.2.0 [required: >=14]
  │  │     │  └─ dependencies of libstdcxx displayed above
  │  │     ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     │  └─ dependencies of r-base displayed above
  │  │     └─ r-rcpp 1.1.0 [required: any]
  │  │        └─ dependencies of r-rcpp displayed above
  │  ├─ r-hardhat 1.4.2 [required: >=1.4.2]
  │  │  └─ dependencies of r-hardhat displayed above
  │  ├─ r-parsnip 1.3.3 [required: >=1.2.1.9003]
  │  │  └─ dependencies of r-parsnip displayed above
  │  ├─ r-purrr 1.1.0 [required: >=1.0.0]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-recipes 1.3.1 [required: >=1.1.0.9001]
  │  │  └─ dependencies of r-recipes displayed above
  │  ├─ r-rlang 1.1.6 [required: >=1.1.4]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-rsample 1.3.1 [required: >=1.3.0.9003]
  │  │  └─ dependencies of r-rsample displayed above
  │  ├─ r-tailor 0.1.0 [required: >=0.1.0]
  │  │  └─ dependencies of r-tailor displayed above
  │  ├─ r-tibble 3.3.0 [required: >=3.1.0]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyr 1.3.1 [required: >=1.2.0]
  │  │  └─ dependencies of r-tidyr displayed above
  │  ├─ r-tidyselect 1.2.1 [required: >=1.1.2]
  │  │  └─ dependencies of r-tidyselect displayed above
  │  ├─ r-vctrs 0.6.5 [required: >=0.6.1]
  │  │  └─ dependencies of r-vctrs displayed above
  │  ├─ r-withr 3.0.2 [required: any]
  │  │  └─ dependencies of r-withr displayed above
  │  ├─ r-workflows 1.3.0 [required: >=1.3.0]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.5 [required: >=3.3.0]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-generics 0.1.4 [required: >=0.1.2]
  │  │  │  └─ dependencies of r-generics displayed above
  │  │  ├─ r-glue 1.8.0 [required: >=1.6.2]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-hardhat 1.4.2 [required: >=1.4.1]
  │  │  │  └─ dependencies of r-hardhat displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-modelenv 0.2.0 [required: >=0.1.0]
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-glue 1.8.0 [required: any]
  │  │  │  │  └─ dependencies of r-glue displayed above
  │  │  │  ├─ r-rlang 1.1.6 [required: any]
  │  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  │  ├─ r-tibble 3.3.0 [required: any]
  │  │  │  │  └─ dependencies of r-tibble displayed above
  │  │  │  └─ r-vctrs 0.6.5 [required: any]
  │  │  │     └─ dependencies of r-vctrs displayed above
  │  │  ├─ r-parsnip 1.3.3 [required: >=1.3.0]
  │  │  │  └─ dependencies of r-parsnip displayed above
  │  │  ├─ r-recipes 1.3.1 [required: >=1.1.1]
  │  │  │  └─ dependencies of r-recipes displayed above
  │  │  ├─ r-rlang 1.1.6 [required: >=1.1.0]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-sparsevctrs 0.3.4 [required: >=0.2.0]
  │  │  │  └─ dependencies of r-sparsevctrs displayed above
  │  │  ├─ r-tidyselect 1.2.1 [required: >=1.2.0]
  │  │  │  └─ dependencies of r-tidyselect displayed above
  │  │  ├─ r-vctrs 0.6.5 [required: >=0.4.1]
  │  │  │  └─ dependencies of r-vctrs displayed above
  │  │  └─ r-withr 3.0.2 [required: any]
  │  │     └─ dependencies of r-withr displayed above
  │  └─ r-yardstick 1.3.2 [required: >=1.3.0]
  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │     ├─ libgcc 15.2.0 [required: >=14]
  │     │  └─ dependencies of libgcc displayed above
  │     ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     ├─ r-cli 3.6.5 [required: any]
  │     │  └─ dependencies of r-cli displayed above
  │     ├─ r-dplyr 1.1.4 [required: >=1.1.0]
  │     │  └─ dependencies of r-dplyr displayed above
  │     ├─ r-generics 0.1.4 [required: >=0.1.2]
  │     │  └─ dependencies of r-generics displayed above
  │     ├─ r-hardhat 1.4.2 [required: >=1.3.0]
  │     │  └─ dependencies of r-hardhat displayed above
  │     ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │     │  └─ dependencies of r-lifecycle displayed above
  │     ├─ r-rlang 1.1.6 [required: >=1.1.4]
  │     │  └─ dependencies of r-rlang displayed above
  │     ├─ r-tibble 3.3.0 [required: any]
  │     │  └─ dependencies of r-tibble displayed above
  │     ├─ r-tidyselect 1.2.1 [required: >=1.2.0]
  │     │  └─ dependencies of r-tidyselect displayed above
  │     ├─ r-vctrs 0.6.5 [required: >=0.5.0]
  │     │  └─ dependencies of r-vctrs displayed above
  │     └─ r-withr 3.0.2 [required: any]
  │        └─ dependencies of r-withr displayed above
  ├─ r-workflows 1.3.0 [required: >=1.3.0]
  │  └─ dependencies of r-workflows displayed above
  ├─ r-workflowsets 1.1.1 [required: >=1.1.1]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.5 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.0.0]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-generics 0.1.4 [required: >=0.1.2]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-ggplot2 4.0.0 [required: any]
  │  │  └─ dependencies of r-ggplot2 displayed above
  │  ├─ r-glue 1.8.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-hardhat 1.4.2 [required: >=1.2.0]
  │  │  └─ dependencies of r-hardhat displayed above
  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.0]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-parsnip 1.3.3 [required: >=1.2.0]
  │  │  └─ dependencies of r-parsnip displayed above
  │  ├─ r-pillar 1.11.1 [required: >=1.7.0]
  │  │  └─ dependencies of r-pillar displayed above
  │  ├─ r-prettyunits 1.2.0 [required: any]
  │  │  └─ dependencies of r-prettyunits displayed above
  │  ├─ r-purrr 1.1.0 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.6 [required: >=1.1.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-rsample 1.3.1 [required: >=0.0.9]
  │  │  └─ dependencies of r-rsample displayed above
  │  ├─ r-tibble 3.3.0 [required: >=3.1.0]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyr 1.3.1 [required: any]
  │  │  └─ dependencies of r-tidyr displayed above
  │  ├─ r-tune 2.0.0 [required: >=1.2.0]
  │  │  └─ dependencies of r-tune displayed above
  │  ├─ r-vctrs 0.6.5 [required: any]
  │  │  └─ dependencies of r-vctrs displayed above
  │  ├─ r-withr 3.0.2 [required: any]
  │  │  └─ dependencies of r-withr displayed above
  │  └─ r-workflows 1.3.0 [required: >=1.1.4]
  │     └─ dependencies of r-workflows displayed above
  └─ r-yardstick 1.3.2 [required: >=1.3.2]
     └─ dependencies of r-yardstick displayed above
r-tidyverse==2.0.0
  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-broom 1.0.10 [required: >=1.0.3]
  │  └─ dependencies of r-broom displayed above
  ├─ r-cli 3.6.5 [required: >=3.6.0]
  │  └─ dependencies of r-cli displayed above
  ├─ r-conflicted 1.2.0 [required: >=1.2.0]
  │  └─ dependencies of r-conflicted displayed above
  ├─ r-dbplyr 2.5.1 [required: >=2.3.0]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-blob 1.2.4 [required: >=1.2.0]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-rlang 1.1.6 [required: any]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.2.1]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-cli 3.6.5 [required: >=3.6.1]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-dbi 1.2.3 [required: >=1.1.3]
  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.1.2]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-glue 1.8.0 [required: >=1.6.2]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-magrittr 2.0.4 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-pillar 1.11.1 [required: >=1.9.0]
  │  │  └─ dependencies of r-pillar displayed above
  │  ├─ r-purrr 1.1.0 [required: >=1.0.1]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-r6 2.6.1 [required: >=2.2.2]
  │  │  └─ dependencies of r-r6 displayed above
  │  ├─ r-rlang 1.1.6 [required: >=1.1.1]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.3.0 [required: >=3.2.1]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyr 1.3.1 [required: >=1.3.0]
  │  │  └─ dependencies of r-tidyr displayed above
  │  ├─ r-tidyselect 1.2.1 [required: >=1.2.1]
  │  │  └─ dependencies of r-tidyselect displayed above
  │  ├─ r-vctrs 0.6.5 [required: >=0.6.3]
  │  │  └─ dependencies of r-vctrs displayed above
  │  └─ r-withr 3.0.2 [required: >=2.5.0]
  │     └─ dependencies of r-withr displayed above
  ├─ r-dplyr 1.1.4 [required: >=1.1.0]
  │  └─ dependencies of r-dplyr displayed above
  ├─ r-dtplyr 1.3.2 [required: >=1.2.2]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-crayon 1.5.3 [required: any]
  │  │  └─ dependencies of r-crayon displayed above
  │  ├─ r-data.table 1.17.8 [required: >=1.13.0]
  │  │  └─ dependencies of r-data.table displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.0.3]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  └─ dependencies of r-ellipsis displayed above
  │  ├─ r-glue 1.8.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-rlang 1.1.6 [required: any]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.3.0 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyselect 1.2.1 [required: any]
  │  │  └─ dependencies of r-tidyselect displayed above
  │  └─ r-vctrs 0.6.5 [required: any]
  │     └─ dependencies of r-vctrs displayed above
  ├─ r-forcats 1.0.1 [required: >=1.0.0]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.5 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  └─ dependencies of r-ellipsis displayed above
  │  ├─ r-glue 1.8.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-magrittr 2.0.4 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-rlang 1.1.6 [required: >=1.0.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.3.0 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  └─ r-withr 3.0.2 [required: any]
  │     └─ dependencies of r-withr displayed above
  ├─ r-ggplot2 4.0.0 [required: >=3.4.1]
  │  └─ dependencies of r-ggplot2 displayed above
  ├─ r-googledrive 2.1.2 [required: >=2.0.0]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.5 [required: >=3.0.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-gargle 1.6.0 [required: >=1.6.0]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.5 [required: >=3.0.0]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-fs 1.6.6 [required: >=1.3.1]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-glue 1.8.0 [required: >=1.3.0]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-httr 1.4.7 [required: >=1.4.0]
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-curl 7.0.0 [required: >=0.9.1]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libcurl 8.14.1 [required: >=8.14.1,<9.0a0]
  │  │  │  │  │  └─ dependencies of libcurl displayed above
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  ├─ r-jsonlite 2.0.0 [required: any]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  ├─ r-mime 0.13 [required: any]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  ├─ r-openssl 2.3.4 [required: >=0.8]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  ├─ openssl 3.5.4 [required: >=3.5.3,<4.0a0]
  │  │  │  │  │  └─ dependencies of openssl displayed above
  │  │  │  │  ├─ r-askpass 1.2.1 [required: any]
  │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  │  └─ r-sys 3.4.3 [required: >=2.1]
  │  │  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │     │  └─ dependencies of libgcc displayed above
  │  │  │  │  │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │        └─ dependencies of r-base displayed above
  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  └─ r-r6 2.6.1 [required: any]
  │  │  │     └─ dependencies of r-r6 displayed above
  │  │  ├─ r-jsonlite 2.0.0 [required: any]
  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-openssl 2.3.4 [required: any]
  │  │  │  └─ dependencies of r-openssl displayed above
  │  │  ├─ r-rappdirs 0.3.3 [required: any]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-rlang 1.1.6 [required: >=1.0.0]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-rstudioapi 0.17.1 [required: any]
  │  │  │  └─ dependencies of r-rstudioapi displayed above
  │  │  └─ r-withr 3.0.2 [required: any]
  │  │     └─ dependencies of r-withr displayed above
  │  ├─ r-glue 1.8.0 [required: >=1.4.2]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-httr 1.4.7 [required: any]
  │  │  └─ dependencies of r-httr displayed above
  │  ├─ r-jsonlite 2.0.0 [required: any]
  │  │  └─ dependencies of r-jsonlite displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-magrittr 2.0.4 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-pillar 1.11.1 [required: >=1.9.0]
  │  │  └─ dependencies of r-pillar displayed above
  │  ├─ r-purrr 1.1.0 [required: >=1.0.1]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.6 [required: >=1.0.2]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.3.0 [required: >=2.0.0]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-uuid 1.2_1 [required: any]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-vctrs 0.6.5 [required: >=0.3.0]
  │  │  └─ dependencies of r-vctrs displayed above
  │  └─ r-withr 3.0.2 [required: any]
  │     └─ dependencies of r-withr displayed above
  ├─ r-googlesheets4 1.1.2 [required: >=1.0.1]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cellranger 1.1.0 [required: any]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-rematch 2.0.0 [required: any]
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  └─ r-tibble 3.3.0 [required: any]
  │  │     └─ dependencies of r-tibble displayed above
  │  ├─ r-cli 3.6.5 [required: >=3.0.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-curl 7.0.0 [required: any]
  │  │  └─ dependencies of r-curl displayed above
  │  ├─ r-gargle 1.6.0 [required: >=1.2.0]
  │  │  └─ dependencies of r-gargle displayed above
  │  ├─ r-glue 1.8.0 [required: >=1.3.0]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-googledrive 2.1.2 [required: >=2.0.0]
  │  │  └─ dependencies of r-googledrive displayed above
  │  ├─ r-httr 1.4.7 [required: any]
  │  │  └─ dependencies of r-httr displayed above
  │  ├─ r-ids 1.0.1 [required: any]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-openssl 2.3.4 [required: any]
  │  │  │  └─ dependencies of r-openssl displayed above
  │  │  └─ r-uuid 1.2_1 [required: any]
  │  │     └─ dependencies of r-uuid displayed above
  │  ├─ r-magrittr 2.0.4 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-purrr 1.1.0 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rematch2 2.1.2 [required: any]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  └─ r-tibble 3.3.0 [required: any]
  │  │     └─ dependencies of r-tibble displayed above
  │  ├─ r-rlang 1.1.6 [required: >=0.4.11]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.3.0 [required: >=2.1.1]
  │  │  └─ dependencies of r-tibble displayed above
  │  └─ r-vctrs 0.6.5 [required: >=0.2.3]
  │     └─ dependencies of r-vctrs displayed above
  ├─ r-haven 2.5.5 [required: >=2.5.1]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  └─ dependencies of libzlib displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.5 [required: >=3.0.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-cpp11 0.5.2 [required: any]
  │  │  └─ dependencies of r-cpp11 displayed above
  │  ├─ r-forcats 1.0.1 [required: >=0.2.0]
  │  │  └─ dependencies of r-forcats displayed above
  │  ├─ r-hms 1.1.3 [required: any]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  │  └─ dependencies of r-ellipsis displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-pkgconfig 2.0.3 [required: any]
  │  │  │  └─ dependencies of r-pkgconfig displayed above
  │  │  ├─ r-rlang 1.1.6 [required: any]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.2.1]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-readr 2.1.5 [required: >=0.1.0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.5 [required: any]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-clipr 0.8.0 [required: any]
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-cpp11 0.5.2 [required: any]
  │  │  │  └─ dependencies of r-cpp11 displayed above
  │  │  ├─ r-crayon 1.5.3 [required: any]
  │  │  │  └─ dependencies of r-crayon displayed above
  │  │  ├─ r-hms 1.1.3 [required: >=0.4.1]
  │  │  │  └─ dependencies of r-hms displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=0.2.0]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-r6 2.6.1 [required: any]
  │  │  │  └─ dependencies of r-r6 displayed above
  │  │  ├─ r-rlang 1.1.6 [required: any]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-tibble 3.3.0 [required: any]
  │  │  │  └─ dependencies of r-tibble displayed above
  │  │  ├─ r-tzdb 0.5.0 [required: >=0.1.1]
  │  │  │  └─ dependencies of r-tzdb displayed above
  │  │  └─ r-vroom 1.6.6 [required: >=1.5.4]
  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │     │  └─ dependencies of libgcc displayed above
  │  │     ├─ libstdcxx 15.2.0 [required: >=14]
  │  │     │  └─ dependencies of libstdcxx displayed above
  │  │     ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     │  └─ dependencies of r-base displayed above
  │  │     ├─ r-bit64 4.6.0_1 [required: any]
  │  │     │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │     │  ├─ libgcc 15.2.0 [required: >=14]
  │  │     │  │  └─ dependencies of libgcc displayed above
  │  │     │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     │  │  └─ dependencies of r-base displayed above
  │  │     │  └─ r-bit 4.6.0 [required: >=4.0.0]
  │  │     │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │     │     ├─ libgcc 15.2.0 [required: >=14]
  │  │     │     │  └─ dependencies of libgcc displayed above
  │  │     │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     │        └─ dependencies of r-base displayed above
  │  │     ├─ r-cli 3.6.5 [required: any]
  │  │     │  └─ dependencies of r-cli displayed above
  │  │     ├─ r-cpp11 0.5.2 [required: >=0.2.0]
  │  │     │  └─ dependencies of r-cpp11 displayed above
  │  │     ├─ r-crayon 1.5.3 [required: any]
  │  │     │  └─ dependencies of r-crayon displayed above
  │  │     ├─ r-glue 1.8.0 [required: any]
  │  │     │  └─ dependencies of r-glue displayed above
  │  │     ├─ r-hms 1.1.3 [required: any]
  │  │     │  └─ dependencies of r-hms displayed above
  │  │     ├─ r-lifecycle 1.0.4 [required: any]
  │  │     │  └─ dependencies of r-lifecycle displayed above
  │  │     ├─ r-progress 1.2.3 [required: >=1.2.1]
  │  │     │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     │  │  └─ dependencies of r-base displayed above
  │  │     │  ├─ r-crayon 1.5.3 [required: any]
  │  │     │  │  └─ dependencies of r-crayon displayed above
  │  │     │  ├─ r-hms 1.1.3 [required: any]
  │  │     │  │  └─ dependencies of r-hms displayed above
  │  │     │  ├─ r-prettyunits 1.2.0 [required: any]
  │  │     │  │  └─ dependencies of r-prettyunits displayed above
  │  │     │  └─ r-r6 2.6.1 [required: any]
  │  │     │     └─ dependencies of r-r6 displayed above
  │  │     ├─ r-rlang 1.1.6 [required: >=0.4.2]
  │  │     │  └─ dependencies of r-rlang displayed above
  │  │     ├─ r-tibble 3.3.0 [required: >=2.0.0]
  │  │     │  └─ dependencies of r-tibble displayed above
  │  │     ├─ r-tidyselect 1.2.1 [required: any]
  │  │     │  └─ dependencies of r-tidyselect displayed above
  │  │     ├─ r-tzdb 0.5.0 [required: >=0.1.1]
  │  │     │  └─ dependencies of r-tzdb displayed above
  │  │     ├─ r-vctrs 0.6.5 [required: >=0.2.0]
  │  │     │  └─ dependencies of r-vctrs displayed above
  │  │     └─ r-withr 3.0.2 [required: any]
  │  │        └─ dependencies of r-withr displayed above
  │  ├─ r-rlang 1.1.6 [required: >=0.4.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.3.0 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyselect 1.2.1 [required: any]
  │  │  └─ dependencies of r-tidyselect displayed above
  │  └─ r-vctrs 0.6.5 [required: >=0.3.0]
  │     └─ dependencies of r-vctrs displayed above
  ├─ r-hms 1.1.3 [required: >=1.1.2]
  │  └─ dependencies of r-hms displayed above
  ├─ r-httr 1.4.7 [required: >=1.4.4]
  │  └─ dependencies of r-httr displayed above
  ├─ r-jsonlite 2.0.0 [required: >=1.8.4]
  │  └─ dependencies of r-jsonlite displayed above
  ├─ r-lubridate 1.9.4 [required: >=1.9.2]
  │  └─ dependencies of r-lubridate displayed above
  ├─ r-magrittr 2.0.4 [required: >=2.0.3]
  │  └─ dependencies of r-magrittr displayed above
  ├─ r-modelr 0.1.11 [required: >=0.1.10]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-broom 1.0.10 [required: any]
  │  │  └─ dependencies of r-broom displayed above
  │  ├─ r-dplyr 1.1.4 [required: any]
  │  │  └─ dependencies of r-dplyr displayed above
  │  ├─ r-magrittr 2.0.4 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-purrr 1.1.0 [required: >=0.2.2]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.6 [required: >=0.2.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.3.0 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  └─ r-tidyr 1.3.1 [required: >=0.8.0]
  │     └─ dependencies of r-tidyr displayed above
  ├─ r-pillar 1.11.1 [required: >=1.8.1]
  │  └─ dependencies of r-pillar displayed above
  ├─ r-purrr 1.1.0 [required: >=1.0.1]
  │  └─ dependencies of r-purrr displayed above
  ├─ r-ragg 1.5.0 [required: >=1.2.5]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libfreetype 2.14.1 [required: >=2.14.0]
  │  │  └─ dependencies of libfreetype displayed above
  │  ├─ libfreetype6 2.14.1 [required: >=2.14.0]
  │  │  └─ dependencies of libfreetype6 displayed above
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libjpeg-turbo 3.1.0 [required: >=3.1.0,<4.0a0]
  │  │  └─ dependencies of libjpeg-turbo displayed above
  │  ├─ libpng 1.6.50 [required: >=1.6.50,<1.7.0a0]
  │  │  └─ dependencies of libpng displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ libtiff 4.7.1 [required: >=4.7.0,<4.8.0a0]
  │  │  └─ dependencies of libtiff displayed above
  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  └─ dependencies of libzlib displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-systemfonts 1.3.1 [required: >=1.0.3]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libfreetype 2.14.1 [required: >=2.14.1]
  │  │  │  └─ dependencies of libfreetype displayed above
  │  │  ├─ libfreetype6 2.14.1 [required: >=2.14.1]
  │  │  │  └─ dependencies of libfreetype6 displayed above
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-base64enc 0.1_3 [required: any]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-cpp11 0.5.2 [required: >=0.2.1]
  │  │  │  └─ dependencies of r-cpp11 displayed above
  │  │  ├─ r-jsonlite 2.0.0 [required: any]
  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  └─ r-lifecycle 1.0.4 [required: any]
  │  │     └─ dependencies of r-lifecycle displayed above
  │  └─ r-textshaping 1.0.4 [required: >=0.3.0]
  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │     ├─ fribidi 1.0.16 [required: >=1.0.16,<2.0a0]
  │     │  └─ dependencies of fribidi displayed above
  │     ├─ harfbuzz 12.1.0 [required: >=12.1.0]
  │     │  └─ dependencies of harfbuzz displayed above
  │     ├─ libfreetype 2.14.1 [required: >=2.14.1]
  │     │  └─ dependencies of libfreetype displayed above
  │     ├─ libfreetype6 2.14.1 [required: >=2.14.1]
  │     │  └─ dependencies of libfreetype6 displayed above
  │     ├─ libgcc 15.2.0 [required: >=14]
  │     │  └─ dependencies of libgcc displayed above
  │     ├─ libstdcxx 15.2.0 [required: >=14]
  │     │  └─ dependencies of libstdcxx displayed above
  │     ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     ├─ r-cpp11 0.5.2 [required: >=0.2.1]
  │     │  └─ dependencies of r-cpp11 displayed above
  │     ├─ r-lifecycle 1.0.4 [required: any]
  │     │  └─ dependencies of r-lifecycle displayed above
  │     ├─ r-stringi 1.8.7 [required: any]
  │     │  └─ dependencies of r-stringi displayed above
  │     └─ r-systemfonts 1.3.1 [required: >=1.3.0]
  │        └─ dependencies of r-systemfonts displayed above
  ├─ r-readr 2.1.5 [required: >=2.1.4]
  │  └─ dependencies of r-readr displayed above
  ├─ r-readxl 1.4.5 [required: >=1.4.2]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libiconv 1.18 [required: >=1.18,<2.0a0]
  │  │  └─ dependencies of libiconv displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cellranger 1.1.0 [required: any]
  │  │  └─ dependencies of r-cellranger displayed above
  │  ├─ r-cpp11 0.5.2 [required: >=0.4.0]
  │  │  └─ dependencies of r-cpp11 displayed above
  │  ├─ r-progress 1.2.3 [required: any]
  │  │  └─ dependencies of r-progress displayed above
  │  └─ r-tibble 3.3.0 [required: >=2.0.1]
  │     └─ dependencies of r-tibble displayed above
  ├─ r-reprex 2.1.1 [required: >=2.0.2]
  │  ├─ pandoc 3.8.2 [required: >=2.0]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-callr 3.7.6 [required: >=3.6.0]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-processx 3.8.6 [required: >=3.4.0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-ps 1.9.1 [required: >=1.2.0]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  └─ r-r6 2.6.1 [required: any]
  │  │  │     └─ dependencies of r-r6 displayed above
  │  │  └─ r-r6 2.6.1 [required: any]
  │  │     └─ dependencies of r-r6 displayed above
  │  ├─ r-cli 3.6.5 [required: >=3.2.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-clipr 0.8.0 [required: >=0.4.0]
  │  │  └─ dependencies of r-clipr displayed above
  │  ├─ r-fs 1.6.6 [required: any]
  │  │  └─ dependencies of r-fs displayed above
  │  ├─ r-glue 1.8.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-knitr 1.50 [required: >=1.23]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-evaluate 1.0.5 [required: >=0.15]
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-highr 0.11 [required: >=0.11]
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-xfun 0.53 [required: >=0.18]
  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │  │     │  └─ dependencies of libgcc displayed above
  │  │  │     ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │     │  └─ dependencies of libstdcxx displayed above
  │  │  │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │        └─ dependencies of r-base displayed above
  │  │  ├─ r-xfun 0.53 [required: >=0.51]
  │  │  │  └─ dependencies of r-xfun displayed above
  │  │  └─ r-yaml 2.3.10 [required: >=2.1.19]
  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │     │  └─ dependencies of libgcc displayed above
  │  │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │        └─ dependencies of r-base displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-rlang 1.1.6 [required: >=1.0.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-rmarkdown 2.30 [required: any]
  │  │  ├─ pandoc 3.8.2 [required: >=1.14]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-bslib 0.9.0 [required: >=0.2.5.1]
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-base64enc 0.1_3 [required: any]
  │  │  │  │  └─ dependencies of r-base64enc displayed above
  │  │  │  ├─ r-cachem 1.1.0 [required: any]
  │  │  │  │  └─ dependencies of r-cachem displayed above
  │  │  │  ├─ r-htmltools 0.5.8.1 [required: >=0.5.7]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  ├─ r-base64enc 0.1_3 [required: any]
  │  │  │  │  │  └─ dependencies of r-base64enc displayed above
  │  │  │  │  ├─ r-digest 0.6.37 [required: any]
  │  │  │  │  │  └─ dependencies of r-digest displayed above
  │  │  │  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  │  │  │  └─ dependencies of r-ellipsis displayed above
  │  │  │  │  ├─ r-fastmap 1.2.0 [required: >=1.1.0]
  │  │  │  │  │  └─ dependencies of r-fastmap displayed above
  │  │  │  │  └─ r-rlang 1.1.6 [required: >=0.4.10]
  │  │  │  │     └─ dependencies of r-rlang displayed above
  │  │  │  ├─ r-jquerylib 0.1.4 [required: >=0.1.3]
  │  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  └─ r-htmltools 0.5.8.1 [required: any]
  │  │  │  │     └─ dependencies of r-htmltools displayed above
  │  │  │  ├─ r-jsonlite 2.0.0 [required: any]
  │  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  │  ├─ r-memoise 2.0.1 [required: >=2.0.1]
  │  │  │  │  └─ dependencies of r-memoise displayed above
  │  │  │  ├─ r-mime 0.13 [required: any]
  │  │  │  │  └─ dependencies of r-mime displayed above
  │  │  │  ├─ r-rlang 1.1.6 [required: any]
  │  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  │  └─ r-sass 0.4.10 [required: >=0.4.0]
  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │  │     │  └─ dependencies of libgcc displayed above
  │  │  │     ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │     │  └─ dependencies of libstdcxx displayed above
  │  │  │     ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     │  └─ dependencies of r-base displayed above
  │  │  │     ├─ r-digest 0.6.37 [required: any]
  │  │  │     │  └─ dependencies of r-digest displayed above
  │  │  │     ├─ r-fs 1.6.6 [required: any]
  │  │  │     │  └─ dependencies of r-fs displayed above
  │  │  │     ├─ r-htmltools 0.5.8.1 [required: any]
  │  │  │     │  └─ dependencies of r-htmltools displayed above
  │  │  │     ├─ r-r6 2.6.1 [required: any]
  │  │  │     │  └─ dependencies of r-r6 displayed above
  │  │  │     ├─ r-rappdirs 0.3.3 [required: any]
  │  │  │     │  └─ dependencies of r-rappdirs displayed above
  │  │  │     └─ r-rlang 1.1.6 [required: any]
  │  │  │        └─ dependencies of r-rlang displayed above
  │  │  ├─ r-evaluate 1.0.5 [required: >=0.13]
  │  │  │  └─ dependencies of r-evaluate displayed above
  │  │  ├─ r-fontawesome 0.5.3 [required: >=0.5.0]
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-htmltools 0.5.8.1 [required: >=0.5.1.1]
  │  │  │  │  └─ dependencies of r-htmltools displayed above
  │  │  │  └─ r-rlang 1.1.6 [required: >=0.4.10]
  │  │  │     └─ dependencies of r-rlang displayed above
  │  │  ├─ r-htmltools 0.5.8.1 [required: >=0.5.1]
  │  │  │  └─ dependencies of r-htmltools displayed above
  │  │  ├─ r-jquerylib 0.1.4 [required: any]
  │  │  │  └─ dependencies of r-jquerylib displayed above
  │  │  ├─ r-jsonlite 2.0.0 [required: any]
  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  ├─ r-knitr 1.50 [required: >=1.43]
  │  │  │  └─ dependencies of r-knitr displayed above
  │  │  ├─ r-tinytex 0.57 [required: >=0.31]
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-xfun 0.53 [required: >=0.5]
  │  │  │     └─ dependencies of r-xfun displayed above
  │  │  ├─ r-xfun 0.53 [required: >=0.36]
  │  │  │  └─ dependencies of r-xfun displayed above
  │  │  └─ r-yaml 2.3.10 [required: >=2.1.19]
  │  │     └─ dependencies of r-yaml displayed above
  │  ├─ r-rstudioapi 0.17.1 [required: any]
  │  │  └─ dependencies of r-rstudioapi displayed above
  │  └─ r-withr 3.0.2 [required: >=2.3.0]
  │     └─ dependencies of r-withr displayed above
  ├─ r-rlang 1.1.6 [required: >=1.0.6]
  │  └─ dependencies of r-rlang displayed above
  ├─ r-rstudioapi 0.17.1 [required: >=0.14]
  │  └─ dependencies of r-rstudioapi displayed above
  ├─ r-rvest 1.0.5 [required: >=1.0.3]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.5 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-glue 1.8.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-httr 1.4.7 [required: >=0.5]
  │  │  └─ dependencies of r-httr displayed above
  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.0]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-magrittr 2.0.4 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-rlang 1.1.6 [required: >=1.0.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-selectr 0.4_2 [required: any]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-r6 2.6.1 [required: any]
  │  │  │  └─ dependencies of r-r6 displayed above
  │  │  └─ r-stringr 1.5.2 [required: any]
  │  │     └─ dependencies of r-stringr displayed above
  │  ├─ r-tibble 3.3.0 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-withr 3.0.2 [required: any]
  │  │  └─ dependencies of r-withr displayed above
  │  └─ r-xml2 1.4.0 [required: >=1.3]
  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │     ├─ libgcc 15.2.0 [required: >=14]
  │     │  └─ dependencies of libgcc displayed above
  │     ├─ liblzma 5.8.1 [required: >=5.8.1,<6.0a0]
  │     │  └─ dependencies of liblzma displayed above
  │     ├─ libstdcxx 15.2.0 [required: >=14]
  │     │  └─ dependencies of libstdcxx displayed above
  │     ├─ libxml2 2.15.0 [required: any]
  │     │  └─ dependencies of libxml2 displayed above
  │     ├─ libxml2-16 2.15.0 [required: >=2.14.6]
  │     │  └─ dependencies of libxml2-16 displayed above
  │     ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │     │  └─ dependencies of libzlib displayed above
  │     ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     ├─ r-cli 3.6.5 [required: any]
  │     │  └─ dependencies of r-cli displayed above
  │     └─ r-rlang 1.1.6 [required: >=1.1.0]
  │        └─ dependencies of r-rlang displayed above
  ├─ r-stringr 1.5.2 [required: >=1.5.0]
  │  └─ dependencies of r-stringr displayed above
  ├─ r-tibble 3.3.0 [required: >=3.1.8]
  │  └─ dependencies of r-tibble displayed above
  ├─ r-tidyr 1.3.1 [required: >=1.3.0]
  │  └─ dependencies of r-tidyr displayed above
  └─ r-xml2 1.4.0 [required: >=1.3.3]
     └─ dependencies of r-xml2 displayed above
r-caret==6.0_94
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-e1071 1.7_16 [required: any]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-class 7.3_23 [required: any]
  │  │  └─ dependencies of r-class displayed above
  │  └─ r-proxy 0.4_27 [required: any]
  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │     ├─ libgcc 15.2.0 [required: >=14]
  │     │  └─ dependencies of libgcc displayed above
  │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │        └─ dependencies of r-base displayed above
  ├─ r-foreach 1.5.2 [required: any]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-codetools 0.2_20 [required: any]
  │  │  └─ dependencies of r-codetools displayed above
  │  └─ r-iterators 1.0.14 [required: any]
  │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │        └─ dependencies of r-base displayed above
  ├─ r-ggplot2 4.0.0 [required: any]
  │  └─ dependencies of r-ggplot2 displayed above
  ├─ r-lattice 0.22_7 [required: >=0.20]
  │  └─ dependencies of r-lattice displayed above
  ├─ r-modelmetrics 1.2.2.2 [required: >=1.2.2.2]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ _openmp_mutex 4.5 [required: >=4.5]
  │  │  └─ dependencies of _openmp_mutex displayed above
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-data.table 1.17.8 [required: any]
  │  │  └─ dependencies of r-data.table displayed above
  │  └─ r-rcpp 1.1.0 [required: any]
  │     └─ dependencies of r-rcpp displayed above
  ├─ r-nlme 3.1_168 [required: any]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libgfortran 15.2.0 [required: any]
  │  │  └─ dependencies of libgfortran displayed above
  │  ├─ libgfortran5 15.2.0 [required: >=14.3.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-lattice 0.22_7 [required: any]
  │     └─ dependencies of r-lattice displayed above
  ├─ r-plyr 1.8.9 [required: any]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-rcpp 1.1.0 [required: >=0.11.0]
  │     └─ dependencies of r-rcpp displayed above
  ├─ r-proc 1.19.0.1 [required: any]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-plyr 1.8.9 [required: any]
  │  │  └─ dependencies of r-plyr displayed above
  │  └─ r-rcpp 1.1.0 [required: >=0.11.1]
  │     └─ dependencies of r-rcpp displayed above
  ├─ r-recipes 1.3.1 [required: >=0.1.10]
  │  └─ dependencies of r-recipes displayed above
  ├─ r-reshape2 1.4.4 [required: any]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-plyr 1.8.9 [required: >=1.8.1]
  │  │  └─ dependencies of r-plyr displayed above
  │  ├─ r-rcpp 1.1.0 [required: any]
  │  │  └─ dependencies of r-rcpp displayed above
  │  └─ r-stringr 1.5.2 [required: any]
  │     └─ dependencies of r-stringr displayed above
  └─ r-withr 3.0.2 [required: >=2.0.0]
     └─ dependencies of r-withr displayed above
rpy2==3.6.4
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ cffi 2.0.0 [required: >=1.15.1]
  │  └─ dependencies of cffi displayed above
  ├─ jinja2 3.1.6 [required: any]
  │  └─ dependencies of jinja2 displayed above
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ liblzma 5.8.1 [required: >=5.8.1,<6.0a0]
  │  └─ dependencies of liblzma displayed above
  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  └─ dependencies of libzlib displayed above
  ├─ packaging 25.0 [required: any]
  │  └─ dependencies of packaging displayed above
  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  ├─ python_abi 3.13 [required: 3.13.*, *_cp313]
  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  └─ dependencies of r-base displayed above
  └─ tzlocal 5.3.1 [required: any]
     ├─ python 3.13.8 [required: any]
     └─ __unix [required: any]
r-devtools==2.4.6
  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-cli 3.6.5 [required: >=3.3.0]
  │  └─ dependencies of r-cli displayed above
  ├─ r-desc 1.4.3 [required: >=1.4.1]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.5 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-r6 2.6.1 [required: any]
  │  │  └─ dependencies of r-r6 displayed above
  │  └─ r-rprojroot 2.1.1 [required: any]
  │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │        └─ dependencies of r-base displayed above
  ├─ r-ellipsis 0.3.2 [required: >=0.3.2]
  │  └─ dependencies of r-ellipsis displayed above
  ├─ r-fs 1.6.6 [required: >=1.5.2]
  │  └─ dependencies of r-fs displayed above
  ├─ r-lifecycle 1.0.4 [required: >=1.0.1]
  │  └─ dependencies of r-lifecycle displayed above
  ├─ r-memoise 2.0.1 [required: >=2.0.1]
  │  └─ dependencies of r-memoise displayed above
  ├─ r-miniui 0.1.2 [required: >=0.1.1.1]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-htmltools 0.5.8.1 [required: >=0.3]
  │  │  └─ dependencies of r-htmltools displayed above
  │  └─ r-shiny 1.11.1 [required: >=0.13]
  │     ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     ├─ r-bslib 0.9.0 [required: >=0.6.0]
  │     │  └─ dependencies of r-bslib displayed above
  │     ├─ r-cachem 1.1.0 [required: >=1.1.0]
  │     │  └─ dependencies of r-cachem displayed above
  │     ├─ r-commonmark 2.0.0 [required: >=1.7]
  │     │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │     │  ├─ libgcc 15.2.0 [required: >=14]
  │     │  │  └─ dependencies of libgcc displayed above
  │     │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     │     └─ dependencies of r-base displayed above
  │     ├─ r-crayon 1.5.3 [required: any]
  │     │  └─ dependencies of r-crayon displayed above
  │     ├─ r-fastmap 1.2.0 [required: >=1.1.1]
  │     │  └─ dependencies of r-fastmap displayed above
  │     ├─ r-fontawesome 0.5.3 [required: >=0.4.0]
  │     │  └─ dependencies of r-fontawesome displayed above
  │     ├─ r-glue 1.8.0 [required: >=1.3.2]
  │     │  └─ dependencies of r-glue displayed above
  │     ├─ r-htmltools 0.5.8.1 [required: >=0.5.4]
  │     │  └─ dependencies of r-htmltools displayed above
  │     ├─ r-httpuv 1.6.16 [required: >=1.5.2]
  │     │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │     │  ├─ libgcc 15.2.0 [required: >=14]
  │     │  │  └─ dependencies of libgcc displayed above
  │     │  ├─ libstdcxx 15.2.0 [required: >=14]
  │     │  │  └─ dependencies of libstdcxx displayed above
  │     │  ├─ libuv 1.51.0 [required: >=1.51.0,<2.0a0]
  │     │  │  └─ dependencies of libuv displayed above
  │     │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │     │  │  └─ dependencies of libzlib displayed above
  │     │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     │  │  └─ dependencies of r-base displayed above
  │     │  ├─ r-later 1.4.4 [required: >=0.8.0]
  │     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │     │  │  ├─ libgcc 15.2.0 [required: >=14]
  │     │  │  │  └─ dependencies of libgcc displayed above
  │     │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │     │  │  │  └─ dependencies of libstdcxx displayed above
  │     │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     │  │  │  └─ dependencies of r-base displayed above
  │     │  │  ├─ r-rcpp 1.1.0 [required: >=0.12.9]
  │     │  │  │  └─ dependencies of r-rcpp displayed above
  │     │  │  └─ r-rlang 1.1.6 [required: any]
  │     │  │     └─ dependencies of r-rlang displayed above
  │     │  ├─ r-promises 1.3.3 [required: any]
  │     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │     │  │  ├─ libgcc 15.2.0 [required: >=14]
  │     │  │  │  └─ dependencies of libgcc displayed above
  │     │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │     │  │  │  └─ dependencies of libstdcxx displayed above
  │     │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     │  │  │  └─ dependencies of r-base displayed above
  │     │  │  ├─ r-fastmap 1.2.0 [required: >=1.1.0]
  │     │  │  │  └─ dependencies of r-fastmap displayed above
  │     │  │  ├─ r-later 1.4.4 [required: any]
  │     │  │  │  └─ dependencies of r-later displayed above
  │     │  │  ├─ r-magrittr 2.0.4 [required: >=1.5]
  │     │  │  │  └─ dependencies of r-magrittr displayed above
  │     │  │  ├─ r-r6 2.6.1 [required: any]
  │     │  │  │  └─ dependencies of r-r6 displayed above
  │     │  │  ├─ r-rcpp 1.1.0 [required: any]
  │     │  │  │  └─ dependencies of r-rcpp displayed above
  │     │  │  └─ r-rlang 1.1.6 [required: any]
  │     │  │     └─ dependencies of r-rlang displayed above
  │     │  ├─ r-r6 2.6.1 [required: any]
  │     │  │  └─ dependencies of r-r6 displayed above
  │     │  └─ r-rcpp 1.1.0 [required: >=1.0.7]
  │     │     └─ dependencies of r-rcpp displayed above
  │     ├─ r-jsonlite 2.0.0 [required: >=0.9.16]
  │     │  └─ dependencies of r-jsonlite displayed above
  │     ├─ r-later 1.4.4 [required: >=1.0.0]
  │     │  └─ dependencies of r-later displayed above
  │     ├─ r-lifecycle 1.0.4 [required: >=0.2.0]
  │     │  └─ dependencies of r-lifecycle displayed above
  │     ├─ r-mime 0.13 [required: >=0.3]
  │     │  └─ dependencies of r-mime displayed above
  │     ├─ r-promises 1.3.3 [required: >=1.1.0]
  │     │  └─ dependencies of r-promises displayed above
  │     ├─ r-r6 2.6.1 [required: >=2.0]
  │     │  └─ dependencies of r-r6 displayed above
  │     ├─ r-rlang 1.1.6 [required: >=0.4.10]
  │     │  └─ dependencies of r-rlang displayed above
  │     ├─ r-sourcetools 0.1.7_1 [required: any]
  │     │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │     │  ├─ libgcc 15.2.0 [required: >=14]
  │     │  │  └─ dependencies of libgcc displayed above
  │     │  ├─ libstdcxx 15.2.0 [required: >=14]
  │     │  │  └─ dependencies of libstdcxx displayed above
  │     │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     │     └─ dependencies of r-base displayed above
  │     ├─ r-withr 3.0.2 [required: any]
  │     │  └─ dependencies of r-withr displayed above
  │     └─ r-xtable 1.8_4 [required: any]
  │        └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │           └─ dependencies of r-base displayed above
  ├─ r-pkgbuild 1.4.8 [required: >=1.3.1]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-callr 3.7.6 [required: >=3.2.0]
  │  │  └─ dependencies of r-callr displayed above
  │  ├─ r-cli 3.6.5 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-crayon 1.5.3 [required: any]
  │  │  └─ dependencies of r-crayon displayed above
  │  ├─ r-desc 1.4.3 [required: any]
  │  │  └─ dependencies of r-desc displayed above
  │  ├─ r-prettyunits 1.2.0 [required: any]
  │  │  └─ dependencies of r-prettyunits displayed above
  │  ├─ r-r6 2.6.1 [required: any]
  │  │  └─ dependencies of r-r6 displayed above
  │  ├─ r-rprojroot 2.1.1 [required: any]
  │  │  └─ dependencies of r-rprojroot displayed above
  │  └─ r-withr 3.0.2 [required: >=2.1.2]
  │     └─ dependencies of r-withr displayed above
  ├─ r-pkgdown 2.1.3 [required: >=2.0.6]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-bslib 0.9.0 [required: >=0.5.1]
  │  │  └─ dependencies of r-bslib displayed above
  │  ├─ r-callr 3.7.6 [required: >=3.7.3]
  │  │  └─ dependencies of r-callr displayed above
  │  ├─ r-cli 3.6.5 [required: >=3.6.1]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-desc 1.4.3 [required: >=1.4.0]
  │  │  └─ dependencies of r-desc displayed above
  │  ├─ r-downlit 0.4.4 [required: >=0.4.4]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-brio 1.1.5 [required: any]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-desc 1.4.3 [required: any]
  │  │  │  └─ dependencies of r-desc displayed above
  │  │  ├─ r-digest 0.6.37 [required: any]
  │  │  │  └─ dependencies of r-digest displayed above
  │  │  ├─ r-evaluate 1.0.5 [required: any]
  │  │  │  └─ dependencies of r-evaluate displayed above
  │  │  ├─ r-fansi 1.0.6 [required: any]
  │  │  │  └─ dependencies of r-fansi displayed above
  │  │  ├─ r-memoise 2.0.1 [required: any]
  │  │  │  └─ dependencies of r-memoise displayed above
  │  │  ├─ r-rlang 1.1.6 [required: any]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-vctrs 0.6.5 [required: any]
  │  │  │  └─ dependencies of r-vctrs displayed above
  │  │  ├─ r-withr 3.0.2 [required: any]
  │  │  │  └─ dependencies of r-withr displayed above
  │  │  └─ r-yaml 2.3.10 [required: any]
  │  │     └─ dependencies of r-yaml displayed above
  │  ├─ r-fontawesome 0.5.3 [required: any]
  │  │  └─ dependencies of r-fontawesome displayed above
  │  ├─ r-fs 1.6.6 [required: >=1.4.0]
  │  │  └─ dependencies of r-fs displayed above
  │  ├─ r-httr2 1.2.1 [required: >=1.0.2]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.5 [required: >=3.0.0]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-curl 7.0.0 [required: >=5.1.0]
  │  │  │  └─ dependencies of r-curl displayed above
  │  │  ├─ r-glue 1.8.0 [required: any]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-magrittr 2.0.4 [required: any]
  │  │  │  └─ dependencies of r-magrittr displayed above
  │  │  ├─ r-openssl 2.3.4 [required: any]
  │  │  │  └─ dependencies of r-openssl displayed above
  │  │  ├─ r-r6 2.6.1 [required: any]
  │  │  │  └─ dependencies of r-r6 displayed above
  │  │  ├─ r-rappdirs 0.3.3 [required: any]
  │  │  │  └─ dependencies of r-rappdirs displayed above
  │  │  ├─ r-rlang 1.1.6 [required: >=1.1.0]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-vctrs 0.6.5 [required: >=0.6.3]
  │  │  │  └─ dependencies of r-vctrs displayed above
  │  │  └─ r-withr 3.0.2 [required: any]
  │  │     └─ dependencies of r-withr displayed above
  │  ├─ r-jsonlite 2.0.0 [required: any]
  │  │  └─ dependencies of r-jsonlite displayed above
  │  ├─ r-openssl 2.3.4 [required: any]
  │  │  └─ dependencies of r-openssl displayed above
  │  ├─ r-purrr 1.1.0 [required: >=1.0.0]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-ragg 1.5.0 [required: >=1.4.0]
  │  │  └─ dependencies of r-ragg displayed above
  │  ├─ r-rlang 1.1.6 [required: >=1.1.4]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-rmarkdown 2.30 [required: >=2.27]
  │  │  └─ dependencies of r-rmarkdown displayed above
  │  ├─ r-tibble 3.3.0 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-whisker 0.4.1 [required: any]
  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-withr 3.0.2 [required: >=2.4.3]
  │  │  └─ dependencies of r-withr displayed above
  │  ├─ r-xml2 1.4.0 [required: >=1.3.1]
  │  │  └─ dependencies of r-xml2 displayed above
  │  └─ r-yaml 2.3.10 [required: any]
  │     └─ dependencies of r-yaml displayed above
  ├─ r-pkgload 1.4.1 [required: >=1.3.0]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.5 [required: >=3.3.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-desc 1.4.3 [required: any]
  │  │  └─ dependencies of r-desc displayed above
  │  ├─ r-fs 1.6.6 [required: any]
  │  │  └─ dependencies of r-fs displayed above
  │  ├─ r-glue 1.8.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-pkgbuild 1.4.8 [required: any]
  │  │  └─ dependencies of r-pkgbuild displayed above
  │  ├─ r-processx 3.8.6 [required: any]
  │  │  └─ dependencies of r-processx displayed above
  │  ├─ r-rlang 1.1.6 [required: >=1.1.1]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-rprojroot 2.1.1 [required: any]
  │  │  └─ dependencies of r-rprojroot displayed above
  │  └─ r-withr 3.0.2 [required: >=2.4.3]
  │     └─ dependencies of r-withr displayed above
  ├─ r-profvis 0.4.0 [required: >=0.3.7]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-htmlwidgets 1.6.4 [required: >=0.3.2]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-htmltools 0.5.8.1 [required: >=0.5.7]
  │  │  │  └─ dependencies of r-htmltools displayed above
  │  │  ├─ r-jsonlite 2.0.0 [required: >=0.9.16]
  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  ├─ r-knitr 1.50 [required: >=1.8]
  │  │  │  └─ dependencies of r-knitr displayed above
  │  │  ├─ r-rmarkdown 2.30 [required: any]
  │  │  │  └─ dependencies of r-rmarkdown displayed above
  │  │  └─ r-yaml 2.3.10 [required: any]
  │  │     └─ dependencies of r-yaml displayed above
  │  ├─ r-purrr 1.1.0 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.6 [required: >=0.4.9]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-stringr 1.5.2 [required: any]
  │  │  └─ dependencies of r-stringr displayed above
  │  └─ r-vctrs 0.6.5 [required: any]
  │     └─ dependencies of r-vctrs displayed above
  ├─ r-rcmdcheck 1.4.0 [required: >=1.4.0]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-callr 3.7.6 [required: >=3.1.1.9000]
  │  │  └─ dependencies of r-callr displayed above
  │  ├─ r-cli 3.6.5 [required: >=3.0.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-curl 7.0.0 [required: any]
  │  │  └─ dependencies of r-curl displayed above
  │  ├─ r-desc 1.4.3 [required: >=1.2.0]
  │  │  └─ dependencies of r-desc displayed above
  │  ├─ r-digest 0.6.37 [required: any]
  │  │  └─ dependencies of r-digest displayed above
  │  ├─ r-pkgbuild 1.4.8 [required: any]
  │  │  └─ dependencies of r-pkgbuild displayed above
  │  ├─ r-prettyunits 1.2.0 [required: any]
  │  │  └─ dependencies of r-prettyunits displayed above
  │  ├─ r-r6 2.6.1 [required: any]
  │  │  └─ dependencies of r-r6 displayed above
  │  ├─ r-rprojroot 2.1.1 [required: any]
  │  │  └─ dependencies of r-rprojroot displayed above
  │  ├─ r-sessioninfo 1.2.3 [required: >=1.1.1]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.5 [required: any]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  └─ r-withr 3.0.2 [required: any]
  │  │     └─ dependencies of r-withr displayed above
  │  ├─ r-withr 3.0.2 [required: any]
  │  │  └─ dependencies of r-withr displayed above
  │  └─ r-xopen 1.0.1 [required: any]
  │     ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     └─ r-processx 3.8.6 [required: any]
  │        └─ dependencies of r-processx displayed above
  ├─ r-remotes 2.5.0 [required: >=2.4.2]
  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-rlang 1.1.6 [required: >=1.0.4]
  │  └─ dependencies of r-rlang displayed above
  ├─ r-roxygen2 7.3.3 [required: >=7.2.1]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-brew 1.0_10 [required: any]
  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-commonmark 2.0.0 [required: any]
  │  │  └─ dependencies of r-commonmark displayed above
  │  ├─ r-cpp11 0.5.2 [required: any]
  │  │  └─ dependencies of r-cpp11 displayed above
  │  ├─ r-desc 1.4.3 [required: >=1.2.0]
  │  │  └─ dependencies of r-desc displayed above
  │  ├─ r-digest 0.6.37 [required: any]
  │  │  └─ dependencies of r-digest displayed above
  │  ├─ r-knitr 1.50 [required: any]
  │  │  └─ dependencies of r-knitr displayed above
  │  ├─ r-pkgload 1.4.1 [required: >=1.0.2]
  │  │  └─ dependencies of r-pkgload displayed above
  │  ├─ r-purrr 1.1.0 [required: >=0.3.3]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-r6 2.6.1 [required: >=2.1.2]
  │  │  └─ dependencies of r-r6 displayed above
  │  ├─ r-rlang 1.1.6 [required: any]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-stringi 1.8.7 [required: any]
  │  │  └─ dependencies of r-stringi displayed above
  │  ├─ r-stringr 1.5.2 [required: >=1.0.0]
  │  │  └─ dependencies of r-stringr displayed above
  │  └─ r-xml2 1.4.0 [required: any]
  │     └─ dependencies of r-xml2 displayed above
  ├─ r-rversions 3.0.0 [required: >=2.1.1]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-curl 7.0.0 [required: any]
  │  │  └─ dependencies of r-curl displayed above
  │  └─ r-xml2 1.4.0 [required: >=1.0.0]
  │     └─ dependencies of r-xml2 displayed above
  ├─ r-sessioninfo 1.2.3 [required: >=1.2.2]
  │  └─ dependencies of r-sessioninfo displayed above
  ├─ r-testthat 3.2.3 [required: >=3.1.4]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-brio 1.1.5 [required: >=1.1.3]
  │  │  └─ dependencies of r-brio displayed above
  │  ├─ r-callr 3.7.6 [required: >=3.7.3]
  │  │  └─ dependencies of r-callr displayed above
  │  ├─ r-cli 3.6.5 [required: >=3.6.1]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-desc 1.4.3 [required: >=1.4.2]
  │  │  └─ dependencies of r-desc displayed above
  │  ├─ r-digest 0.6.37 [required: >=0.6.33]
  │  │  └─ dependencies of r-digest displayed above
  │  ├─ r-evaluate 1.0.5 [required: >=1.0.1]
  │  │  └─ dependencies of r-evaluate displayed above
  │  ├─ r-jsonlite 2.0.0 [required: >=1.8.7]
  │  │  └─ dependencies of r-jsonlite displayed above
  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-magrittr 2.0.4 [required: >=2.0.3]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-pkgload 1.4.1 [required: >=1.3.2.1]
  │  │  └─ dependencies of r-pkgload displayed above
  │  ├─ r-praise 1.0.0 [required: >=1.0.0]
  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-processx 3.8.6 [required: >=3.8.2]
  │  │  └─ dependencies of r-processx displayed above
  │  ├─ r-ps 1.9.1 [required: >=1.7.5]
  │  │  └─ dependencies of r-ps displayed above
  │  ├─ r-r6 2.6.1 [required: >=2.5.1]
  │  │  └─ dependencies of r-r6 displayed above
  │  ├─ r-rlang 1.1.6 [required: >=1.1.1]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-waldo 0.6.2 [required: >=0.6.0]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.5 [required: any]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-diffobj 0.3.6 [required: >=0.3.4]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-crayon 1.5.3 [required: >=1.3.2]
  │  │  │     └─ dependencies of r-crayon displayed above
  │  │  ├─ r-fansi 1.0.6 [required: any]
  │  │  │  └─ dependencies of r-fansi displayed above
  │  │  ├─ r-glue 1.8.0 [required: any]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-rematch2 2.1.2 [required: any]
  │  │  │  └─ dependencies of r-rematch2 displayed above
  │  │  ├─ r-rlang 1.1.6 [required: >=1.0.0]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  └─ r-tibble 3.3.0 [required: any]
  │  │     └─ dependencies of r-tibble displayed above
  │  └─ r-withr 3.0.2 [required: >=3.0.2]
  │     └─ dependencies of r-withr displayed above
  ├─ r-urlchecker 1.0.1 [required: >=1.0.1]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.5 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-curl 7.0.0 [required: any]
  │  │  └─ dependencies of r-curl displayed above
  │  └─ r-xml2 1.4.0 [required: any]
  │     └─ dependencies of r-xml2 displayed above
  ├─ r-usethis 3.2.1 [required: >=2.1.6]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.5 [required: any]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-clipr 0.8.0 [required: >=0.3.0]
  │  │  └─ dependencies of r-clipr displayed above
  │  ├─ r-crayon 1.5.3 [required: any]
  │  │  └─ dependencies of r-crayon displayed above
  │  ├─ r-curl 7.0.0 [required: >=2.7]
  │  │  └─ dependencies of r-curl displayed above
  │  ├─ r-desc 1.4.3 [required: any]
  │  │  └─ dependencies of r-desc displayed above
  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  └─ dependencies of r-ellipsis displayed above
  │  ├─ r-fs 1.6.6 [required: >=1.3.0]
  │  │  └─ dependencies of r-fs displayed above
  │  ├─ r-gert 2.1.5 [required: >=1.0.2]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libgit2 1.9.1 [required: >=1.9.1,<1.10.0a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libssh2 1.11.1 [required: >=1.11.1,<2.0a0]
  │  │  │  │  └─ dependencies of libssh2 displayed above
  │  │  │  ├─ openssl 3.5.4 [required: >=3.5.3,<4.0a0]
  │  │  │  │  └─ dependencies of openssl displayed above
  │  │  │  ├─ pcre2 10.46 [required: >=10.46,<10.47.0a0]
  │  │  │  │  └─ dependencies of pcre2 displayed above
  │  │  │  └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │     └─ dependencies of libzlib displayed above
  │  │  ├─ r-askpass 1.2.1 [required: any]
  │  │  │  └─ dependencies of r-askpass displayed above
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-credentials 2.0.3 [required: >=1.2.1]
  │  │  │  ├─ r-askpass 1.2.1 [required: any]
  │  │  │  │  └─ dependencies of r-askpass displayed above
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-curl 7.0.0 [required: any]
  │  │  │  │  └─ dependencies of r-curl displayed above
  │  │  │  ├─ r-jsonlite 2.0.0 [required: any]
  │  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  │  ├─ r-openssl 2.3.4 [required: >=1.3]
  │  │  │  │  └─ dependencies of r-openssl displayed above
  │  │  │  └─ r-sys 3.4.3 [required: >=2.1]
  │  │  │     └─ dependencies of r-sys displayed above
  │  │  ├─ r-openssl 2.3.4 [required: >=2.0.3]
  │  │  │  └─ dependencies of r-openssl displayed above
  │  │  ├─ r-rstudioapi 0.17.1 [required: >=0.11]
  │  │  │  └─ dependencies of r-rstudioapi displayed above
  │  │  └─ r-zip 2.3.3 [required: >=2.1.0]
  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │     ├─ libgcc 15.2.0 [required: >=14]
  │  │     │  └─ dependencies of libgcc displayed above
  │  │     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │        └─ dependencies of r-base displayed above
  │  ├─ r-gh 1.5.0 [required: >=1.2.0]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.5 [required: >=3.0.1]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-gitcreds 0.1.2 [required: any]
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-httr2 1.2.1 [required: any]
  │  │  │  └─ dependencies of r-httr2 displayed above
  │  │  ├─ r-ini 0.3.1 [required: any]
  │  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-jsonlite 2.0.0 [required: any]
  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  └─ r-rlang 1.1.6 [required: >=1.0.0]
  │  │     └─ dependencies of r-rlang displayed above
  │  ├─ r-glue 1.8.0 [required: >=1.3.0]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-jsonlite 2.0.0 [required: any]
  │  │  └─ dependencies of r-jsonlite displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-purrr 1.1.0 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rappdirs 0.3.3 [required: any]
  │  │  └─ dependencies of r-rappdirs displayed above
  │  ├─ r-rlang 1.1.6 [required: >=0.4.3]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-rprojroot 2.1.1 [required: >=1.2]
  │  │  └─ dependencies of r-rprojroot displayed above
  │  ├─ r-rstudioapi 0.17.1 [required: any]
  │  │  └─ dependencies of r-rstudioapi displayed above
  │  ├─ r-whisker 0.4.1 [required: any]
  │  │  └─ dependencies of r-whisker displayed above
  │  ├─ r-withr 3.0.2 [required: >=2.3.0]
  │  │  └─ dependencies of r-withr displayed above
  │  └─ r-yaml 2.3.10 [required: any]
  │     └─ dependencies of r-yaml displayed above
  └─ r-withr 3.0.2 [required: >=2.5.0]
     └─ dependencies of r-withr displayed above
r-irkernel==1.3.2
  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-crayon 1.5.3 [required: any]
  │  └─ dependencies of r-crayon displayed above
  ├─ r-digest 0.6.37 [required: any]
  │  └─ dependencies of r-digest displayed above
  ├─ r-evaluate 1.0.5 [required: >=0.10]
  │  └─ dependencies of r-evaluate displayed above
  ├─ r-irdisplay 1.1 [required: >=0.3.0.9999]
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-repr 1.1.7 [required: any]
  │     ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     ├─ r-base64enc 0.1_3 [required: any]
  │     │  └─ dependencies of r-base64enc displayed above
  │     ├─ r-htmltools 0.5.8.1 [required: any]
  │     │  └─ dependencies of r-htmltools displayed above
  │     ├─ r-jsonlite 2.0.0 [required: any]
  │     │  └─ dependencies of r-jsonlite displayed above
  │     └─ r-pillar 1.11.1 [required: >=1.4.0]
  │        └─ dependencies of r-pillar displayed above
  ├─ r-jsonlite 2.0.0 [required: >=0.9.6]
  │  └─ dependencies of r-jsonlite displayed above
  ├─ r-pbdzmq 0.3_14 [required: >=0.2_1]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ zeromq 4.3.5 [required: >=4.3.5,<4.4.0a0]
  │     └─ dependencies of zeromq displayed above
  ├─ r-repr 1.1.7 [required: >=0.4.99]
  │  └─ dependencies of r-repr displayed above
  └─ r-uuid 1.2_1 [required: any]
     └─ dependencies of r-uuid displayed above
r-rodbc==1.3_26
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  └─ dependencies of r-base displayed above
  └─ unixodbc 2.3.12 [required: >=2.3.12,<2.4.0a0]
     ├─ libedit 3.1.20250104 [required: >=3.1.20191231,<3.2.0a0]
     │  └─ dependencies of libedit displayed above
     ├─ libgcc-ng 15.2.0 [required: >=12]
     │  └─ dependencies of libgcc-ng displayed above
     ├─ libiconv 1.18 [required: >=1.17,<2.0a0]
     │  └─ dependencies of libiconv displayed above
     └─ libstdcxx-ng 15.2.0 [required: >=12]
        └─ dependencies of libstdcxx-ng displayed above
r-rsqlite==2.4.3
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ libstdcxx 15.2.0 [required: >=14]
  │  └─ dependencies of libstdcxx displayed above
  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-bit64 4.6.0_1 [required: any]
  │  └─ dependencies of r-bit64 displayed above
  ├─ r-blob 1.2.4 [required: >=1.2.0]
  │  └─ dependencies of r-blob displayed above
  ├─ r-cpp11 0.5.2 [required: any]
  │  └─ dependencies of r-cpp11 displayed above
  ├─ r-dbi 1.2.3 [required: >=1.1.0]
  │  └─ dependencies of r-dbi displayed above
  ├─ r-memoise 2.0.1 [required: any]
  │  └─ dependencies of r-memoise displayed above
  ├─ r-pkgconfig 2.0.3 [required: any]
  │  └─ dependencies of r-pkgconfig displayed above
  └─ r-plogr 0.2.0 [required: >=0.2.0]
     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
        └─ dependencies of r-base displayed above
r-rcurl==1.98_1.17
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ libcurl 8.14.1 [required: >=8.14.1,<9.0a0]
  │  └─ dependencies of libcurl displayed above
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ liblzma 5.8.1 [required: >=5.8.1,<6.0a0]
  │  └─ dependencies of liblzma displayed above
  ├─ libxml2 2.15.0 [required: any]
  │  └─ dependencies of libxml2 displayed above
  ├─ libxml2-16 2.15.0 [required: >=2.14.6]
  │  └─ dependencies of libxml2-16 displayed above
  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  └─ dependencies of libzlib displayed above
  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  └─ dependencies of r-base displayed above
  └─ r-bitops 1.0_9 [required: any]
     ├─ __glibc [required: >=2.17,<3.0.a0]
     ├─ libgcc 15.2.0 [required: >=14]
     │  └─ dependencies of libgcc displayed above
     └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
        └─ dependencies of r-base displayed above
r-randomforest==4.7_1.2
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ libgfortran 15.2.0 [required: any]
  │  └─ dependencies of libgfortran displayed above
  ├─ libgfortran5 15.2.0 [required: >=14.3.0]
  │  └─ dependencies of libgfortran5 displayed above
  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
     └─ dependencies of r-base displayed above
r-forecast==8.24.0
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  └─ dependencies of libblas displayed above
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ libstdcxx 15.2.0 [required: >=14]
  │  └─ dependencies of libstdcxx displayed above
  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-colorspace 2.1_2 [required: any]
  │  └─ dependencies of r-colorspace displayed above
  ├─ r-fracdiff 1.5_3 [required: any]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ dependencies of libblas displayed above
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-generics 0.1.4 [required: >=0.1.2]
  │  └─ dependencies of r-generics displayed above
  ├─ r-ggplot2 4.0.0 [required: >=2.2.1]
  │  └─ dependencies of r-ggplot2 displayed above
  ├─ r-lmtest 0.9_40 [required: any]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libgfortran 15.2.0 [required: any]
  │  │  └─ dependencies of libgfortran displayed above
  │  ├─ libgfortran5 15.2.0 [required: >=14.3.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-zoo 1.8_14 [required: any]
  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │     ├─ libgcc 15.2.0 [required: >=14]
  │     │  └─ dependencies of libgcc displayed above
  │     ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     └─ r-lattice 0.22_7 [required: >=0.20_27]
  │        └─ dependencies of r-lattice displayed above
  ├─ r-magrittr 2.0.4 [required: any]
  │  └─ dependencies of r-magrittr displayed above
  ├─ r-nnet 7.3_20 [required: any]
  │  └─ dependencies of r-nnet displayed above
  ├─ r-rcpp 1.1.0 [required: >=0.11.0]
  │  └─ dependencies of r-rcpp displayed above
  ├─ r-rcpparmadillo 15.0.2_2 [required: >=0.2.35]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ _openmp_mutex 4.5 [required: >=4.5]
  │  │  └─ dependencies of _openmp_mutex displayed above
  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ dependencies of libblas displayed above
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ dependencies of liblapack displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-rcpp 1.1.0 [required: >=0.11.0]
  │     └─ dependencies of r-rcpp displayed above
  ├─ r-timedate 4041.110 [required: any]
  │  └─ dependencies of r-timedate displayed above
  ├─ r-tseries 0.10_58 [required: any]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ dependencies of libblas displayed above
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libgfortran 15.2.0 [required: any]
  │  │  └─ dependencies of libgfortran displayed above
  │  ├─ libgfortran5 15.2.0 [required: >=14.3.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-quadprog 1.5_8 [required: any]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  └─ dependencies of libblas displayed above
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libgfortran 15.2.0 [required: any]
  │  │  │  └─ dependencies of libgfortran displayed above
  │  │  ├─ libgfortran5 15.2.0 [required: >=14.3.0]
  │  │  │  └─ dependencies of libgfortran5 displayed above
  │  │  └─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-quantmod 0.4.28 [required: >=0.4_9]
  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-curl 7.0.0 [required: any]
  │  │  │  └─ dependencies of r-curl displayed above
  │  │  ├─ r-jsonlite 2.0.0 [required: >=1.1]
  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  ├─ r-ttr 0.24.4 [required: >=0.2]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-curl 7.0.0 [required: any]
  │  │  │  │  └─ dependencies of r-curl displayed above
  │  │  │  ├─ r-xts 0.14.1 [required: >=0.10_0]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  └─ r-zoo 1.8_14 [required: >=1.7_12]
  │  │  │  │     └─ dependencies of r-zoo displayed above
  │  │  │  └─ r-zoo 1.8_14 [required: any]
  │  │  │     └─ dependencies of r-zoo displayed above
  │  │  ├─ r-xts 0.14.1 [required: >=0.9_0]
  │  │  │  └─ dependencies of r-xts displayed above
  │  │  └─ r-zoo 1.8_14 [required: any]
  │  │     └─ dependencies of r-zoo displayed above
  │  └─ r-zoo 1.8_14 [required: any]
  │     └─ dependencies of r-zoo displayed above
  ├─ r-urca 1.3_4 [required: any]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libgfortran 15.2.0 [required: any]
  │  │  └─ dependencies of libgfortran displayed above
  │  ├─ libgfortran5 15.2.0 [required: >=14.3.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-nlme 3.1_168 [required: any]
  │     └─ dependencies of r-nlme displayed above
  ├─ r-withr 3.0.2 [required: any]
  │  └─ dependencies of r-withr displayed above
  └─ r-zoo 1.8_14 [required: any]
     └─ dependencies of r-zoo displayed above
r-hexbin==1.28.5
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ libgfortran 15.2.0 [required: any]
  │  └─ dependencies of libgfortran displayed above
  ├─ libgfortran5 15.2.0 [required: >=14.3.0]
  │  └─ dependencies of libgfortran5 displayed above
  ├─ r-base 4.4.3 [required: >=4.4,<4.5.0a0]
  │  └─ dependencies of r-base displayed above
  └─ r-lattice 0.22_7 [required: any]
     └─ dependencies of r-lattice displayed above
jupyter-pluto-proxy==0.1.2
  ├─ jupyter-server-proxy 4.4.0 [required: >=1.5.0]
  │  ├─ aiohttp 3.13.0 [required: any]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ aiohappyeyeballs 2.6.1 [required: >=2.5.0]
  │  │  │  └─ python 3.13.8 [required: >=3.9]
  │  │  ├─ aiosignal 1.4.0 [required: >=1.4.0]
  │  │  │  ├─ frozenlist 1.7.0 [required: >=1.1.0]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  │  ├─ python 3.13.8 [required: >=3.9]
  │  │  │  └─ typing_extensions 4.15.0 [required: >=4.2]
  │  │  │     └─ dependencies of typing_extensions displayed above
  │  │  ├─ attrs 25.4.0 [required: >=17.3.0]
  │  │  │  └─ dependencies of attrs displayed above
  │  │  ├─ frozenlist 1.7.0 [required: >=1.1.1]
  │  │  │  └─ dependencies of frozenlist displayed above
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ multidict 6.6.3 [required: >=4.5,<7.0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  ├─ propcache 0.3.1 [required: >=0.2.0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  ├─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  └─ yarl 1.20.1 [required: >=1.17.0,<2.0]
  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │     ├─ idna 3.11 [required: >=2.0]
  │  │     │  └─ dependencies of idna displayed above
  │  │     ├─ libgcc 15.2.0 [required: >=13]
  │  │     │  └─ dependencies of libgcc displayed above
  │  │     ├─ multidict 6.6.3 [required: >=4.0]
  │  │     │  └─ dependencies of multidict displayed above
  │  │     ├─ propcache 0.3.1 [required: >=0.2.1]
  │  │     │  └─ dependencies of propcache displayed above
  │  │     ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │     └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  ├─ importlib-metadata 8.7.0 [required: >=4.8.3]
  │  │  └─ dependencies of importlib-metadata displayed above
  │  ├─ jupyter_server 2.17.0 [required: >=1.24.0]
  │  │  └─ dependencies of jupyter_server displayed above
  │  ├─ python 3.13.8 [required: >=3.9]
  │  ├─ simpervisor 1.0.0 [required: >=1.0.0]
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ tornado 6.5.2 [required: >=6.1.0]
  │  │  └─ dependencies of tornado displayed above
  │  └─ traitlets 5.14.3 [required: >=5.1.1]
  │     └─ dependencies of traitlets displayed above
  └─ python 3.13.8 [required: >=3.7]
bottleneck==1.6.0
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ numpy 2.3.3 [required: >=1.23,<3]
  │  ├─ python 3.13.8 [required: any]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ dependencies of liblapack displayed above
  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ dependencies of libblas displayed above
  │  ├─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  └─ libcblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │     └─ dependencies of libcblas displayed above
  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
openpyxl==3.1.5
  ├─ et_xmlfile 2.0.0 [required: any]
  │  └─ python 3.13.8 [required: >=3.9]
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
blas==2.137
  └─ blas-devel 3.9.0 [required: 3.9.0, 37*_openblas]
     ├─ libblas 3.9.0 [required: 3.9.0, 37_h4a7cf45_openblas]
     │  └─ dependencies of libblas displayed above
     ├─ libcblas 3.9.0 [required: 3.9.0, 37_h0358290_openblas]
     │  └─ dependencies of libcblas displayed above
     ├─ liblapack 3.9.0 [required: 3.9.0, 37_h47877c9_openblas]
     │  └─ dependencies of liblapack displayed above
     ├─ liblapacke 3.9.0 [required: 3.9.0, 37_h6ae95b6_openblas]
     │  ├─ libblas 3.9.0 [required: 3.9.0, 37_h4a7cf45_openblas]
     │  │  └─ dependencies of libblas displayed above
     │  ├─ libcblas 3.9.0 [required: 3.9.0, 37_h0358290_openblas]
     │  │  └─ dependencies of libcblas displayed above
     │  └─ liblapack 3.9.0 [required: 3.9.0, 37_h47877c9_openblas]
     │     └─ dependencies of liblapack displayed above
     └─ openblas 0.3.30 [required: 0.3.30.*]
        └─ libopenblas 0.3.30 [required: 0.3.30, pthreads_h94d23a6_2]
           └─ dependencies of libopenblas displayed above
altair==5.5.0
  ├─ importlib-metadata 8.7.0 [required: any]
  │  └─ dependencies of importlib-metadata displayed above
  ├─ jinja2 3.1.6 [required: any]
  │  └─ dependencies of jinja2 displayed above
  ├─ jsonschema 4.25.1 [required: >=3.0]
  │  └─ dependencies of jsonschema displayed above
  ├─ narwhals 2.8.0 [required: >=1.14.2]
  │  └─ python 3.13.8 [required: any]
  ├─ packaging 25.0 [required: any]
  │  └─ dependencies of packaging displayed above
  ├─ python 3.13.8 [required: >=3.9]
  └─ typing-extensions 4.15.0 [required: >=4.10.0]
     └─ dependencies of typing-extensions displayed above
jupyterlab-git==0.51.2
  ├─ jupyter_server 2.17.0 [required: >=2.0,<3.0]
  │  └─ dependencies of jupyter_server displayed above
  ├─ nbdime 4.0.2 [required: >=4.0,<5.0]
  │  ├─ colorama 0.4.6 [required: any]
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ gitpython 3.1.45 [required: !=2.1.4,!=2.1.5,!=2.1.6]
  │  │  ├─ gitdb 4.0.12 [required: >=4.0.1,<5]
  │  │  │  ├─ python 3.13.8 [required: >=3.9]
  │  │  │  └─ smmap 5.0.2 [required: >=3.0.1,<6]
  │  │  │     └─ python 3.13.8 [required: >=3.9]
  │  │  ├─ python 3.13.8 [required: >=3.9]
  │  │  └─ typing_extensions 4.15.0 [required: >=3.10.0.2]
  │  │     └─ dependencies of typing_extensions displayed above
  │  ├─ jinja2 3.1.6 [required: >=2.9]
  │  │  └─ dependencies of jinja2 displayed above
  │  ├─ jupyter-server-mathjax 0.2.6 [required: >=0.2.2]
  │  │  ├─ jupyter_server 2.17.0 [required: >=1.1,<3]
  │  │  │  └─ dependencies of jupyter_server displayed above
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ jupyter_server 2.17.0 [required: any]
  │  │  └─ dependencies of jupyter_server displayed above
  │  ├─ nbformat 5.10.4 [required: any]
  │  │  └─ dependencies of nbformat displayed above
  │  ├─ pygments 2.19.2 [required: any]
  │  │  └─ dependencies of pygments displayed above
  │  ├─ python 3.13.8 [required: >=3.9]
  │  ├─ requests 2.32.5 [required: any]
  │  │  ├─ certifi 2025.10.5 [required: >=2017.4.17]
  │  │  │  └─ python 3.13.8 [required: >=3.10]
  │  │  ├─ charset-normalizer 3.4.3 [required: >=2,<4]
  │  │  │  └─ python 3.13.8 [required: >=3.9]
  │  │  ├─ idna 3.11 [required: >=2.5,<4]
  │  │  │  └─ dependencies of idna displayed above
  │  │  ├─ python 3.13.8 [required: >=3.9]
  │  │  └─ urllib3 2.5.0 [required: >=1.21.1,<3]
  │  │     ├─ brotli-python 1.1.0 [required: >=1.0.9]
  │  │     │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │     │  ├─ libgcc 15.2.0 [required: >=14]
  │  │     │  │  └─ dependencies of libgcc displayed above
  │  │     │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │     │  │  └─ dependencies of libstdcxx displayed above
  │  │     │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │     │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │     ├─ h2 4.3.0 [required: >=4,<5]
  │  │     │  ├─ python 3.13.8 [required: any]
  │  │     │  ├─ hyperframe 6.1.0 [required: >=6.1,<7]
  │  │     │  │  └─ python 3.13.8 [required: >=3.9]
  │  │     │  └─ hpack 4.1.0 [required: >=4.1,<5]
  │  │     │     └─ python 3.13.8 [required: >=3.9]
  │  │     ├─ pysocks 1.7.1 [required: >=1.5.6,<2.0,!=1.5.7]
  │  │     │  ├─ __unix [required: any]
  │  │     │  └─ python 3.13.8 [required: >=3.9]
  │  │     ├─ python 3.13.8 [required: >=3.9]
  │  │     └─ zstandard 0.25.0 [required: >=0.18.0]
  │  │        ├─ python 3.13.8 [required: any]
  │  │        ├─ cffi 2.0.0 [required: >=1.11]
  │  │        │  └─ dependencies of cffi displayed above
  │  │        ├─ zstd 1.5.7 [required: >=1.5.7,<1.6.0a0]
  │  │        │  └─ dependencies of zstd displayed above
  │  │        ├─ libgcc 15.2.0 [required: >=14]
  │  │        │  └─ dependencies of libgcc displayed above
  │  │        ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │        └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  └─ tornado 6.5.2 [required: any]
  │     └─ dependencies of tornado displayed above
  ├─ nbformat 5.10.4 [required: any]
  │  └─ dependencies of nbformat displayed above
  ├─ packaging 25.0 [required: any]
  │  └─ dependencies of packaging displayed above
  ├─ pexpect 4.9.0 [required: any]
  │  ├─ ptyprocess 0.7.0 [required: >=0.5]
  │  │  └─ dependencies of ptyprocess displayed above
  │  └─ python 3.13.8 [required: >=3.9]
  ├─ python 3.13.8 [required: >=3.9,<4.0]
  └─ traitlets 5.14.3 [required: >=5.0,<6.0]
     └─ dependencies of traitlets displayed above
numba==0.62.1
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ _openmp_mutex 4.5 [required: >=4.5]
  │  └─ dependencies of _openmp_mutex displayed above
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ libstdcxx 15.2.0 [required: >=14]
  │  └─ dependencies of libstdcxx displayed above
  ├─ llvmlite 0.45.1 [required: >=0.45.0,<0.46.0a0]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  └─ dependencies of libzlib displayed above
  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  ├─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  └─ zstd 1.5.7 [required: >=1.5.7,<1.6.0a0]
  │     └─ dependencies of zstd displayed above
  ├─ numpy 2.3.3 [required: >=1.24,<2.4]
  │  └─ dependencies of numpy displayed above
  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
seaborn==0.13.2
  ├─ seaborn-base 0.13.2 [required: 0.13.2, pyhd8ed1ab_3]
  │  ├─ matplotlib-base 3.10.6 [required: >=3.4,!=3.6.1]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ contourpy 1.3.3 [required: >=1.0.1]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  ├─ numpy 2.3.3 [required: >=1.25]
  │  │  │  │  └─ dependencies of numpy displayed above
  │  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  ├─ cycler 0.12.1 [required: >=0.10]
  │  │  │  └─ python 3.13.8 [required: >=3.9]
  │  │  ├─ fonttools 4.60.1 [required: >=4.22.0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ brotli 1.1.0 [required: any]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ brotli-bin 1.1.0 [required: 1.1.0, hb03c661_4]
  │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  │  ├─ libbrotlidec 1.1.0 [required: 1.1.0, hb03c661_4]
  │  │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  │  │  ├─ libbrotlicommon 1.1.0 [required: 1.1.0, hb03c661_4]
  │  │  │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  │  │  │  └─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  │  │     └─ dependencies of libgcc displayed above
  │  │  │  │  │  │  └─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  │     └─ dependencies of libgcc displayed above
  │  │  │  │  │  ├─ libbrotlienc 1.1.0 [required: 1.1.0, hb03c661_4]
  │  │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  │  │  ├─ libbrotlicommon 1.1.0 [required: 1.1.0, hb03c661_4]
  │  │  │  │  │  │  │  └─ dependencies of libbrotlicommon displayed above
  │  │  │  │  │  │  └─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  │     └─ dependencies of libgcc displayed above
  │  │  │  │  │  └─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │     └─ dependencies of libgcc displayed above
  │  │  │  │  ├─ libbrotlidec 1.1.0 [required: 1.1.0, hb03c661_4]
  │  │  │  │  │  └─ dependencies of libbrotlidec displayed above
  │  │  │  │  ├─ libbrotlienc 1.1.0 [required: 1.1.0, hb03c661_4]
  │  │  │  │  │  └─ dependencies of libbrotlienc displayed above
  │  │  │  │  └─ libgcc 15.2.0 [required: >=14]
  │  │  │  │     └─ dependencies of libgcc displayed above
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ munkres 1.1.4 [required: any]
  │  │  │  │  └─ python 3.13.8 [required: >=3.9]
  │  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  ├─ freetype 2.14.1 [required: any]
  │  │  │  └─ dependencies of freetype displayed above
  │  │  ├─ kiwisolver 1.4.9 [required: >=1.3.1]
  │  │  │  ├─ python 3.13.8 [required: any]
  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  ├─ libfreetype 2.14.1 [required: >=2.13.3]
  │  │  │  └─ dependencies of libfreetype displayed above
  │  │  ├─ libfreetype6 2.14.1 [required: >=2.13.3]
  │  │  │  └─ dependencies of libfreetype6 displayed above
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  ├─ numpy 2.3.3 [required: >=1.23,<3]
  │  │  │  └─ dependencies of numpy displayed above
  │  │  ├─ packaging 25.0 [required: >=20.0]
  │  │  │  └─ dependencies of packaging displayed above
  │  │  ├─ pillow 11.3.0 [required: >=8]
  │  │  │  ├─ python 3.13.8 [required: any]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ openjpeg 2.5.4 [required: >=2.5.3,<3.0a0]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  ├─ libpng 1.6.50 [required: >=1.6.50,<1.7.0a0]
  │  │  │  │  │  └─ dependencies of libpng displayed above
  │  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  │  ├─ libtiff 4.7.1 [required: >=4.7.1,<4.8.0a0]
  │  │  │  │  │  └─ dependencies of libtiff displayed above
  │  │  │  │  └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │  │     └─ dependencies of libzlib displayed above
  │  │  │  ├─ libwebp-base 1.6.0 [required: >=1.6.0,<2.0a0]
  │  │  │  │  └─ dependencies of libwebp-base displayed above
  │  │  │  ├─ tk 8.6.13 [required: >=8.6.13,<8.7.0a0]
  │  │  │  │  └─ dependencies of tk displayed above
  │  │  │  ├─ libtiff 4.7.1 [required: >=4.7.0,<4.8.0a0]
  │  │  │  │  └─ dependencies of libtiff displayed above
  │  │  │  ├─ libxcb 1.17.0 [required: >=1.17.0,<2.0a0]
  │  │  │  │  └─ dependencies of libxcb displayed above
  │  │  │  ├─ libfreetype 2.14.1 [required: >=2.14.1]
  │  │  │  │  └─ dependencies of libfreetype displayed above
  │  │  │  ├─ libfreetype6 2.14.1 [required: >=2.14.1]
  │  │  │  │  └─ dependencies of libfreetype6 displayed above
  │  │  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  ├─ libjpeg-turbo 3.1.0 [required: >=3.1.0,<4.0a0]
  │  │  │  │  └─ dependencies of libjpeg-turbo displayed above
  │  │  │  ├─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  │  └─ lcms2 2.17 [required: >=2.17,<3.0a0]
  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │     ├─ libgcc 15.2.0 [required: >=13]
  │  │  │     │  └─ dependencies of libgcc displayed above
  │  │  │     ├─ libjpeg-turbo 3.1.0 [required: >=3.0.0,<4.0a0]
  │  │  │     │  └─ dependencies of libjpeg-turbo displayed above
  │  │  │     └─ libtiff 4.7.1 [required: >=4.7.0,<4.8.0a0]
  │  │  │        └─ dependencies of libtiff displayed above
  │  │  ├─ pyparsing 3.2.5 [required: >=2.3.1]
  │  │  │  └─ python 3.13.8 [required: any]
  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  ├─ python-dateutil 2.9.0.post0 [required: >=2.7]
  │  │  │  └─ dependencies of python-dateutil displayed above
  │  │  ├─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  ├─ qhull 2020.2 [required: >=2020.2,<2020.3.0a0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc-ng 15.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ libstdcxx-ng 15.2.0 [required: >=12]
  │  │  │     └─ dependencies of libstdcxx-ng displayed above
  │  │  └─ tk 8.6.13 [required: >=8.6.13,<8.7.0a0]
  │  │     └─ dependencies of tk displayed above
  │  ├─ numpy 2.3.3 [required: >=1.20,!=1.24.0]
  │  │  └─ dependencies of numpy displayed above
  │  ├─ pandas 2.3.3 [required: >=1.2]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  ├─ numpy 2.3.3 [required: >=1.23,<3]
  │  │  │  └─ dependencies of numpy displayed above
  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  ├─ python-dateutil 2.9.0.post0 [required: >=2.8.2]
  │  │  │  └─ dependencies of python-dateutil displayed above
  │  │  ├─ python-tzdata 2025.2 [required: >=2022.7]
  │  │  │  └─ python 3.13.8 [required: >=3.9]
  │  │  ├─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  └─ pytz 2025.2 [required: >=2020.1]
  │  │     └─ python 3.13.8 [required: >=3.9]
  │  ├─ python 3.13.8 [required: >=3.9]
  │  └─ scipy 1.16.2 [required: >=1.7]
  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │     ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │     │  └─ dependencies of libblas displayed above
  │     ├─ libcblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │     │  └─ dependencies of libcblas displayed above
  │     ├─ libgcc 15.2.0 [required: >=14]
  │     │  └─ dependencies of libgcc displayed above
  │     ├─ libgfortran 15.2.0 [required: any]
  │     │  └─ dependencies of libgfortran displayed above
  │     ├─ libgfortran5 15.2.0 [required: >=14.3.0]
  │     │  └─ dependencies of libgfortran5 displayed above
  │     ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
  │     │  └─ dependencies of liblapack displayed above
  │     ├─ libstdcxx 15.2.0 [required: >=14]
  │     │  └─ dependencies of libstdcxx displayed above
  │     ├─ numpy 2.3.3 [required: >=1.25.2]
  │     │  └─ dependencies of numpy displayed above
  │     ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │     └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  └─ statsmodels 0.14.5 [required: >=0.12]
     ├─ __glibc [required: >=2.17,<3.0.a0]
     ├─ libgcc 15.2.0 [required: >=14]
     │  └─ dependencies of libgcc displayed above
     ├─ numpy 2.3.3 [required: >=1.23,<3]
     │  └─ dependencies of numpy displayed above
     ├─ packaging 25.0 [required: >=21.3]
     │  └─ dependencies of packaging displayed above
     ├─ pandas 2.3.3 [required: !=2.1.0,>=1.4]
     │  └─ dependencies of pandas displayed above
     ├─ patsy 1.0.1 [required: >=0.5.6]
     │  ├─ numpy 2.3.3 [required: >=1.4.0]
     │  │  └─ dependencies of numpy displayed above
     │  └─ python 3.13.8 [required: >=3.9]
     ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
     ├─ python_abi 3.13 [required: 3.13.*, *_cp313]
     └─ scipy 1.16.2 [required: !=1.9.2,>=1.8]
        └─ dependencies of scipy displayed above
xlrd==2.0.2
  └─ python 3.13.8 [required: >=3.10]
sympy==1.14.0
  ├─ __unix [required: any]
  ├─ cpython 3.13.8 [required: any]
  │  └─ dependencies of cpython displayed above
  ├─ gmpy2 2.2.1 [required: >=2.0.8]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ gmp 6.3.0 [required: >=6.3.0,<7.0a0]
  │  │  ├─ libgcc-ng 15.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ libstdcxx-ng 15.2.0 [required: >=12]
  │  │     └─ dependencies of libstdcxx-ng displayed above
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ mpc 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ gmp 6.3.0 [required: >=6.3.0,<7.0a0]
  │  │  │  └─ dependencies of gmp displayed above
  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  └─ mpfr 4.2.1 [required: >=4.2.1,<5.0a0]
  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │     ├─ gmp 6.3.0 [required: >=6.3.0,<7.0a0]
  │  │     │  └─ dependencies of gmp displayed above
  │  │     └─ libgcc 15.2.0 [required: >=13]
  │  │        └─ dependencies of libgcc displayed above
  │  ├─ mpfr 4.2.1 [required: >=4.2.1,<5.0a0]
  │  │  └─ dependencies of mpfr displayed above
  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  ├─ mpmath 1.3.0 [required: >=0.19]
  │  └─ python 3.13.8 [required: >=3.9]
  └─ python 3.13.8 [required: >=3.9]
h5py==3.14.0
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ cached-property 1.5.2 [required: any]
  │  └─ dependencies of cached-property displayed above
  ├─ hdf5 1.14.6 [required: >=1.14.6,<1.14.7.0a0]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libaec 1.1.4 [required: >=1.1.4,<2.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  └─ libstdcxx 15.2.0 [required: >=13]
  │  │     └─ dependencies of libstdcxx displayed above
  │  ├─ libcurl 8.14.1 [required: >=8.14.1,<9.0a0]
  │  │  └─ dependencies of libcurl displayed above
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libgfortran 15.2.0 [required: any]
  │  │  └─ dependencies of libgfortran displayed above
  │  ├─ libgfortran5 15.2.0 [required: >=14.3.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  └─ dependencies of libzlib displayed above
  │  └─ openssl 3.5.4 [required: >=3.5.1,<4.0a0]
  │     └─ dependencies of openssl displayed above
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ numpy 2.3.3 [required: >=1.23,<3]
  │  └─ dependencies of numpy displayed above
  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
ipympl==0.9.8
  ├─ ipython 9.6.0 [required: <10]
  │  ├─ __unix [required: any]
  │  ├─ pexpect 4.9.0 [required: >4.3]
  │  │  └─ dependencies of pexpect displayed above
  │  ├─ decorator 5.2.1 [required: any]
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ exceptiongroup 1.3.0 [required: any]
  │  │  └─ dependencies of exceptiongroup displayed above
  │  ├─ ipython_pygments_lexers 1.1.1 [required: any]
  │  │  ├─ pygments 2.19.2 [required: any]
  │  │  │  └─ dependencies of pygments displayed above
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ jedi 0.19.2 [required: >=0.16]
  │  │  ├─ parso 0.8.5 [required: >=0.8.3,<0.9.0]
  │  │  │  └─ python 3.13.8 [required: any]
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ matplotlib-inline 0.1.7 [required: any]
  │  │  ├─ python 3.13.8 [required: >=3.9]
  │  │  └─ traitlets 5.14.3 [required: any]
  │  │     └─ dependencies of traitlets displayed above
  │  ├─ pickleshare 0.7.5 [required: any]
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ prompt-toolkit 3.0.52 [required: >=3.0.41,<3.1.0]
  │  │  ├─ python 3.13.8 [required: >=3.10]
  │  │  └─ wcwidth 0.2.14 [required: any]
  │  │     └─ python 3.13.8 [required: >=3.10]
  │  ├─ pygments 2.19.2 [required: >=2.4.0]
  │  │  └─ dependencies of pygments displayed above
  │  ├─ python 3.13.8 [required: any]
  │  ├─ stack_data 0.6.3 [required: any]
  │  │  ├─ asttokens 3.0.0 [required: any]
  │  │  │  └─ python 3.13.8 [required: >=3.9]
  │  │  ├─ executing 2.2.1 [required: any]
  │  │  │  └─ python 3.13.8 [required: >=3.10]
  │  │  ├─ pure_eval 0.2.3 [required: any]
  │  │  │  └─ python 3.13.8 [required: >=3.9]
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ traitlets 5.14.3 [required: >=5.13.0]
  │  │  └─ dependencies of traitlets displayed above
  │  └─ typing_extensions 4.15.0 [required: >=4.6]
  │     └─ dependencies of typing_extensions displayed above
  ├─ ipywidgets 8.1.7 [required: >=7.6.0,<9]
  │  ├─ comm 0.2.3 [required: >=0.1.3]
  │  │  └─ python 3.13.8 [required: any]
  │  ├─ ipython 9.6.0 [required: >=6.1.0]
  │  │  └─ dependencies of ipython displayed above
  │  ├─ jupyterlab_widgets 3.0.15 [required: >=3.0.15,<3.1.0]
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ python 3.13.8 [required: >=3.9]
  │  ├─ traitlets 5.14.3 [required: >=4.3.1]
  │  │  └─ dependencies of traitlets displayed above
  │  └─ widgetsnbextension 4.0.14 [required: >=4.0.14,<4.1.0]
  │     └─ python 3.13.8 [required: >=3.9]
  ├─ matplotlib-base 3.10.6 [required: >=3.5.0,<4]
  │  └─ dependencies of matplotlib-base displayed above
  ├─ numpy 2.3.3 [required: any]
  │  └─ dependencies of numpy displayed above
  ├─ pillow 11.3.0 [required: any]
  │  └─ dependencies of pillow displayed above
  ├─ python 3.13.8 [required: any]
  └─ traitlets 5.14.3 [required: <6]
     └─ dependencies of traitlets displayed above
dask==2025.9.1
  ├─ python 3.13.8 [required: any]
  ├─ dask-core 2025.9.1 [required: >=2025.9.1,<2025.9.2.0a0]
  │  ├─ python 3.13.8 [required: any]
  │  ├─ click 8.3.0 [required: >=8.1]
  │  │  ├─ __unix [required: any]
  │  │  └─ python 3.13.8 [required: >=3.10]
  │  ├─ cloudpickle 3.1.1 [required: >=3.0.0]
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ fsspec 2025.9.0 [required: >=2021.9.0]
  │  │  └─ python 3.13.8 [required: >=3.10]
  │  ├─ packaging 25.0 [required: >=20.0]
  │  │  └─ dependencies of packaging displayed above
  │  ├─ partd 1.4.2 [required: >=1.4.0]
  │  │  ├─ locket 1.0.0 [required: any]
  │  │  │  └─ python 3.13.8 [required: >=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*]
  │  │  ├─ python 3.13.8 [required: >=3.9]
  │  │  └─ toolz 1.0.0 [required: any]
  │  │     └─ python 3.13.8 [required: >=3.9]
  │  ├─ pyyaml 6.0.3 [required: >=5.3.1]
  │  │  └─ dependencies of pyyaml displayed above
  │  ├─ toolz 1.0.0 [required: >=0.10.0]
  │  │  └─ dependencies of toolz displayed above
  │  └─ importlib-metadata 8.7.0 [required: >=4.13.0]
  │     └─ dependencies of importlib-metadata displayed above
  ├─ distributed 2025.9.1 [required: >=2025.9.1,<2025.9.2.0a0]
  │  ├─ python 3.13.8 [required: any]
  │  ├─ click 8.3.0 [required: >=8.0]
  │  │  └─ dependencies of click displayed above
  │  ├─ cloudpickle 3.1.1 [required: >=3.0.0]
  │  │  └─ dependencies of cloudpickle displayed above
  │  ├─ cytoolz 1.0.1 [required: >=0.11.2]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  ├─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  └─ toolz 1.0.0 [required: >=0.10.0]
  │  │     └─ dependencies of toolz displayed above
  │  ├─ dask-core 2025.9.1 [required: >=2025.9.1,<2025.9.2.0a0]
  │  │  └─ dependencies of dask-core displayed above
  │  ├─ jinja2 3.1.6 [required: >=2.10.3]
  │  │  └─ dependencies of jinja2 displayed above
  │  ├─ locket 1.0.0 [required: >=1.0.0]
  │  │  └─ dependencies of locket displayed above
  │  ├─ msgpack-python 1.1.2 [required: >=1.0.2]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  ├─ packaging 25.0 [required: >=20.0]
  │  │  └─ dependencies of packaging displayed above
  │  ├─ psutil 7.1.0 [required: >=5.8.0]
  │  │  └─ dependencies of psutil displayed above
  │  ├─ pyyaml 6.0.3 [required: >=5.4.1]
  │  │  └─ dependencies of pyyaml displayed above
  │  ├─ sortedcontainers 2.4.0 [required: >=2.0.5]
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ tblib 3.1.0 [required: >=1.6.0]
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ toolz 1.0.0 [required: >=0.11.2]
  │  │  └─ dependencies of toolz displayed above
  │  ├─ tornado 6.5.2 [required: >=6.2.0]
  │  │  └─ dependencies of tornado displayed above
  │  ├─ urllib3 2.5.0 [required: >=1.26.5]
  │  │  └─ dependencies of urllib3 displayed above
  │  └─ zict 3.0.0 [required: >=3.0.0]
  │     └─ python 3.13.8 [required: >=3.9]
  ├─ cytoolz 1.0.1 [required: >=0.11.0]
  │  └─ dependencies of cytoolz displayed above
  ├─ lz4 4.4.4 [required: >=4.3.2]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ lz4-c 1.10.0 [required: >=1.10.0,<1.11.0a0]
  │  │  └─ dependencies of lz4-c displayed above
  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  ├─ numpy 2.3.3 [required: >=1.24]
  │  └─ dependencies of numpy displayed above
  ├─ pandas 2.3.3 [required: >=2.0]
  │  └─ dependencies of pandas displayed above
  ├─ bokeh 3.8.0 [required: >=3.1.0]
  │  ├─ contourpy 1.3.3 [required: >=1.2]
  │  │  └─ dependencies of contourpy displayed above
  │  ├─ jinja2 3.1.6 [required: >=2.9]
  │  │  └─ dependencies of jinja2 displayed above
  │  ├─ narwhals 2.8.0 [required: >=1.13]
  │  │  └─ dependencies of narwhals displayed above
  │  ├─ numpy 2.3.3 [required: >=1.16]
  │  │  └─ dependencies of numpy displayed above
  │  ├─ packaging 25.0 [required: >=16.8]
  │  │  └─ dependencies of packaging displayed above
  │  ├─ pandas 2.3.3 [required: >=1.2]
  │  │  └─ dependencies of pandas displayed above
  │  ├─ pillow 11.3.0 [required: >=7.1.0]
  │  │  └─ dependencies of pillow displayed above
  │  ├─ python 3.13.8 [required: >=3.10]
  │  ├─ pyyaml 6.0.3 [required: >=3.10]
  │  │  └─ dependencies of pyyaml displayed above
  │  ├─ tornado 6.5.2 [required: >=6.2]
  │  │  └─ dependencies of tornado displayed above
  │  └─ xyzservices 2025.4.0 [required: >=2021.09.1]
  │     └─ python 3.13.8 [required: >=3.8]
  ├─ jinja2 3.1.6 [required: >=2.10.3]
  │  └─ dependencies of jinja2 displayed above
  └─ pyarrow 21.0.0 [required: >=14.0.1]
     ├─ libarrow-acero 21.0.0 [required: 21.0.0.*]
     │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  ├─ libarrow 21.0.0 [required: 21.0.0, h56a6dad_8_cpu]
     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  ├─ aws-crt-cpp 0.34.4 [required: >=0.34.4,<0.34.5.0a0]
     │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  ├─ aws-c-io 0.22.0 [required: >=0.22.0,<0.22.1.0a0]
     │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  ├─ aws-c-cal 0.9.2 [required: >=0.9.2,<0.9.3.0a0]
     │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  │  ├─ aws-c-common 0.12.4 [required: >=0.12.4,<0.12.5.0a0]
     │  │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  │  │  └─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  │  │     └─ dependencies of libgcc displayed above
     │  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  │  └─ openssl 3.5.4 [required: >=3.5.1,<4.0a0]
     │  │  │  │  │     └─ dependencies of openssl displayed above
     │  │  │  │  ├─ s2n 1.5.26 [required: >=1.5.26,<1.5.27.0a0]
     │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  │  └─ openssl 3.5.4 [required: >=3.5.2,<4.0a0]
     │  │  │  │  │     └─ dependencies of openssl displayed above
     │  │  │  │  └─ aws-c-common 0.12.4 [required: >=0.12.4,<0.12.5.0a0]
     │  │  │  │     └─ dependencies of aws-c-common displayed above
     │  │  │  ├─ aws-c-common 0.12.4 [required: >=0.12.4,<0.12.5.0a0]
     │  │  │  │  └─ dependencies of aws-c-common displayed above
     │  │  │  ├─ aws-c-sdkutils 0.2.4 [required: >=0.2.4,<0.2.5.0a0]
     │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  └─ aws-c-common 0.12.4 [required: >=0.12.4,<0.12.5.0a0]
     │  │  │  │     └─ dependencies of aws-c-common displayed above
     │  │  │  ├─ aws-c-s3 0.8.6 [required: >=0.8.6,<0.8.7.0a0]
     │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  ├─ openssl 3.5.4 [required: >=3.5.2,<4.0a0]
     │  │  │  │  │  └─ dependencies of openssl displayed above
     │  │  │  │  ├─ aws-c-http 0.10.4 [required: >=0.10.4,<0.10.5.0a0]
     │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  │  ├─ aws-c-cal 0.9.2 [required: >=0.9.2,<0.9.3.0a0]
     │  │  │  │  │  │  └─ dependencies of aws-c-cal displayed above
     │  │  │  │  │  ├─ aws-c-compression 0.3.1 [required: >=0.3.1,<0.3.2.0a0]
     │  │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  │  │  └─ aws-c-common 0.12.4 [required: >=0.12.4,<0.12.5.0a0]
     │  │  │  │  │  │     └─ dependencies of aws-c-common displayed above
     │  │  │  │  │  ├─ aws-c-io 0.22.0 [required: >=0.22.0,<0.22.1.0a0]
     │  │  │  │  │  │  └─ dependencies of aws-c-io displayed above
     │  │  │  │  │  └─ aws-c-common 0.12.4 [required: >=0.12.4,<0.12.5.0a0]
     │  │  │  │  │     └─ dependencies of aws-c-common displayed above
     │  │  │  │  ├─ aws-c-common 0.12.4 [required: >=0.12.4,<0.12.5.0a0]
     │  │  │  │  │  └─ dependencies of aws-c-common displayed above
     │  │  │  │  ├─ aws-checksums 0.2.7 [required: >=0.2.7,<0.2.8.0a0]
     │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  │  └─ aws-c-common 0.12.4 [required: >=0.12.4,<0.12.5.0a0]
     │  │  │  │  │     └─ dependencies of aws-c-common displayed above
     │  │  │  │  ├─ aws-c-io 0.22.0 [required: >=0.22.0,<0.22.1.0a0]
     │  │  │  │  │  └─ dependencies of aws-c-io displayed above
     │  │  │  │  ├─ aws-c-auth 0.9.1 [required: >=0.9.1,<0.9.2.0a0]
     │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  │  ├─ aws-c-cal 0.9.2 [required: >=0.9.2,<0.9.3.0a0]
     │  │  │  │  │  │  └─ dependencies of aws-c-cal displayed above
     │  │  │  │  │  ├─ aws-c-io 0.22.0 [required: >=0.22.0,<0.22.1.0a0]
     │  │  │  │  │  │  └─ dependencies of aws-c-io displayed above
     │  │  │  │  │  ├─ aws-c-http 0.10.4 [required: >=0.10.4,<0.10.5.0a0]
     │  │  │  │  │  │  └─ dependencies of aws-c-http displayed above
     │  │  │  │  │  ├─ aws-c-sdkutils 0.2.4 [required: >=0.2.4,<0.2.5.0a0]
     │  │  │  │  │  │  └─ dependencies of aws-c-sdkutils displayed above
     │  │  │  │  │  └─ aws-c-common 0.12.4 [required: >=0.12.4,<0.12.5.0a0]
     │  │  │  │  │     └─ dependencies of aws-c-common displayed above
     │  │  │  │  └─ aws-c-cal 0.9.2 [required: >=0.9.2,<0.9.3.0a0]
     │  │  │  │     └─ dependencies of aws-c-cal displayed above
     │  │  │  ├─ aws-c-http 0.10.4 [required: >=0.10.4,<0.10.5.0a0]
     │  │  │  │  └─ dependencies of aws-c-http displayed above
     │  │  │  ├─ aws-c-event-stream 0.5.6 [required: >=0.5.6,<0.5.7.0a0]
     │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  ├─ aws-c-io 0.22.0 [required: >=0.22.0,<0.22.1.0a0]
     │  │  │  │  │  └─ dependencies of aws-c-io displayed above
     │  │  │  │  ├─ aws-c-common 0.12.4 [required: >=0.12.4,<0.12.5.0a0]
     │  │  │  │  │  └─ dependencies of aws-c-common displayed above
     │  │  │  │  └─ aws-checksums 0.2.7 [required: >=0.2.7,<0.2.8.0a0]
     │  │  │  │     └─ dependencies of aws-checksums displayed above
     │  │  │  ├─ aws-c-mqtt 0.13.3 [required: >=0.13.3,<0.13.4.0a0]
     │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  ├─ aws-c-common 0.12.4 [required: >=0.12.4,<0.12.5.0a0]
     │  │  │  │  │  └─ dependencies of aws-c-common displayed above
     │  │  │  │  ├─ aws-c-io 0.22.0 [required: >=0.22.0,<0.22.1.0a0]
     │  │  │  │  │  └─ dependencies of aws-c-io displayed above
     │  │  │  │  └─ aws-c-http 0.10.4 [required: >=0.10.4,<0.10.5.0a0]
     │  │  │  │     └─ dependencies of aws-c-http displayed above
     │  │  │  ├─ aws-c-cal 0.9.2 [required: >=0.9.2,<0.9.3.0a0]
     │  │  │  │  └─ dependencies of aws-c-cal displayed above
     │  │  │  └─ aws-c-auth 0.9.1 [required: >=0.9.1,<0.9.2.0a0]
     │  │  │     └─ dependencies of aws-c-auth displayed above
     │  │  ├─ aws-sdk-cpp 1.11.606 [required: >=1.11.606,<1.11.607.0a0]
     │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  ├─ aws-crt-cpp 0.34.4 [required: >=0.34.4,<0.34.5.0a0]
     │  │  │  │  └─ dependencies of aws-crt-cpp displayed above
     │  │  │  ├─ aws-c-event-stream 0.5.6 [required: >=0.5.6,<0.5.7.0a0]
     │  │  │  │  └─ dependencies of aws-c-event-stream displayed above
     │  │  │  ├─ aws-c-common 0.12.4 [required: >=0.12.4,<0.12.5.0a0]
     │  │  │  │  └─ dependencies of aws-c-common displayed above
     │  │  │  ├─ libcurl 8.14.1 [required: >=8.14.1,<9.0a0]
     │  │  │  │  └─ dependencies of libcurl displayed above
     │  │  │  └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
     │  │  │     └─ dependencies of libzlib displayed above
     │  │  ├─ azure-core-cpp 1.16.0 [required: >=1.16.0,<1.16.1.0a0]
     │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  ├─ libcurl 8.14.1 [required: >=8.14.1,<9.0a0]
     │  │  │  │  └─ dependencies of libcurl displayed above
     │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  │  └─ openssl 3.5.4 [required: >=3.5.2,<4.0a0]
     │  │  │     └─ dependencies of openssl displayed above
     │  │  ├─ azure-identity-cpp 1.12.0 [required: >=1.12.0,<1.12.1.0a0]
     │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  ├─ azure-core-cpp 1.16.0 [required: >=1.16.0,<1.16.1.0a0]
     │  │  │  │  └─ dependencies of azure-core-cpp displayed above
     │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  │  └─ openssl 3.5.4 [required: >=3.5.1,<4.0a0]
     │  │  │     └─ dependencies of openssl displayed above
     │  │  ├─ azure-storage-blobs-cpp 12.14.0 [required: >=12.14.0,<12.14.1.0a0]
     │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  ├─ azure-core-cpp 1.16.0 [required: >=1.16.0,<1.16.1.0a0]
     │  │  │  │  └─ dependencies of azure-core-cpp displayed above
     │  │  │  ├─ azure-storage-common-cpp 12.10.0 [required: >=12.10.0,<12.10.1.0a0]
     │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  ├─ azure-core-cpp 1.16.0 [required: >=1.16.0,<1.16.1.0a0]
     │  │  │  │  │  └─ dependencies of azure-core-cpp displayed above
     │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  │  │  ├─ libxml2 2.15.0 [required: any]
     │  │  │  │  │  └─ dependencies of libxml2 displayed above
     │  │  │  │  ├─ libxml2-16 2.15.0 [required: >=2.14.5]
     │  │  │  │  │  └─ dependencies of libxml2-16 displayed above
     │  │  │  │  └─ openssl 3.5.4 [required: >=3.5.2,<4.0a0]
     │  │  │  │     └─ dependencies of openssl displayed above
     │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  └─ libstdcxx 15.2.0 [required: >=14]
     │  │  │     └─ dependencies of libstdcxx displayed above
     │  │  ├─ azure-storage-files-datalake-cpp 12.12.0 [required: >=12.12.0,<12.12.1.0a0]
     │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  ├─ azure-core-cpp 1.16.0 [required: >=1.16.0,<1.16.1.0a0]
     │  │  │  │  └─ dependencies of azure-core-cpp displayed above
     │  │  │  ├─ azure-storage-blobs-cpp 12.14.0 [required: >=12.14.0,<12.14.1.0a0]
     │  │  │  │  └─ dependencies of azure-storage-blobs-cpp displayed above
     │  │  │  ├─ azure-storage-common-cpp 12.10.0 [required: >=12.10.0,<12.10.1.0a0]
     │  │  │  │  └─ dependencies of azure-storage-common-cpp displayed above
     │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  └─ libstdcxx 15.2.0 [required: >=14]
     │  │  │     └─ dependencies of libstdcxx displayed above
     │  │  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
     │  │  │  └─ dependencies of bzip2 displayed above
     │  │  ├─ glog 0.7.1 [required: >=0.7.1,<0.8.0a0]
     │  │  │  ├─ gflags 2.2.2 [required: >=2.2.2,<2.3.0a0]
     │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  ├─ libgcc 15.2.0 [required: >=13]
     │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  └─ libstdcxx 15.2.0 [required: >=13]
     │  │  │  │     └─ dependencies of libstdcxx displayed above
     │  │  │  ├─ libgcc-ng 15.2.0 [required: >=12]
     │  │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  │  └─ libstdcxx-ng 15.2.0 [required: >=12]
     │  │  │     └─ dependencies of libstdcxx-ng displayed above
     │  │  ├─ libabseil 20250512.1 [required: >=20250512.1,<20250513.0a0]
     │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  ├─ libgcc 15.2.0 [required: >=13]
     │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  └─ libstdcxx 15.2.0 [required: >=13]
     │  │  │     └─ dependencies of libstdcxx displayed above
     │  │  ├─ libbrotlidec 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  │  └─ dependencies of libbrotlidec displayed above
     │  │  ├─ libbrotlienc 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  │  └─ dependencies of libbrotlienc displayed above
     │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libgcc displayed above
     │  │  ├─ libgoogle-cloud 2.39.0 [required: >=2.39.0,<2.40.0a0]
     │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  ├─ libabseil 20250512.1 [required: >=20250512.1,<20250513.0a0]
     │  │  │  │  └─ dependencies of libabseil displayed above
     │  │  │  ├─ libcurl 8.14.1 [required: >=8.14.1,<9.0a0]
     │  │  │  │  └─ dependencies of libcurl displayed above
     │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  ├─ libgrpc 1.73.1 [required: >=1.73.1,<1.74.0a0]
     │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  ├─ c-ares 1.34.5 [required: >=1.34.5,<2.0a0]
     │  │  │  │  │  └─ dependencies of c-ares displayed above
     │  │  │  │  ├─ libabseil 20250512.1 [required: >=20250512.1,<20250513.0a0]
     │  │  │  │  │  └─ dependencies of libabseil displayed above
     │  │  │  │  ├─ libgcc 15.2.0 [required: >=13]
     │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  ├─ libprotobuf 6.31.1 [required: >=6.31.1,<6.31.2.0a0]
     │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  │  ├─ libabseil 20250512.1 [required: >=20250512.1,<20250513.0a0]
     │  │  │  │  │  │  └─ dependencies of libabseil displayed above
     │  │  │  │  │  ├─ libgcc 15.2.0 [required: >=13]
     │  │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  │  ├─ libstdcxx 15.2.0 [required: >=13]
     │  │  │  │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  │  │  │  └─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
     │  │  │  │  │     └─ dependencies of libzlib displayed above
     │  │  │  │  ├─ libre2-11 2025.08.12 [required: >=2024.7.2]
     │  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  │  │  ├─ libabseil 20250512.1 [required: >=20250512.1,<20250513.0a0]
     │  │  │  │  │  │  └─ dependencies of libabseil displayed above
     │  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  │  └─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  │  │     └─ dependencies of libstdcxx displayed above
     │  │  │  │  ├─ libstdcxx 15.2.0 [required: >=13]
     │  │  │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  │  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
     │  │  │  │  │  └─ dependencies of libzlib displayed above
     │  │  │  │  ├─ openssl 3.5.4 [required: >=3.5.1,<4.0a0]
     │  │  │  │  │  └─ dependencies of openssl displayed above
     │  │  │  │  └─ re2 2025.08.12 [required: any]
     │  │  │  │     └─ libre2-11 2025.08.12 [required: 2025.08.12, h7b12aa8_1]
     │  │  │  │        └─ dependencies of libre2-11 displayed above
     │  │  │  ├─ libprotobuf 6.31.1 [required: >=6.31.1,<6.31.2.0a0]
     │  │  │  │  └─ dependencies of libprotobuf displayed above
     │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  │  └─ openssl 3.5.4 [required: >=3.5.1,<4.0a0]
     │  │  │     └─ dependencies of openssl displayed above
     │  │  ├─ libgoogle-cloud-storage 2.39.0 [required: >=2.39.0,<2.40.0a0]
     │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  ├─ libabseil 20250512.1 [required: any]
     │  │  │  │  └─ dependencies of libabseil displayed above
     │  │  │  ├─ libcrc32c 1.1.2 [required: >=1.1.2,<1.2.0a0]
     │  │  │  │  ├─ libgcc-ng 15.2.0 [required: >=9.4.0]
     │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  │  │  └─ libstdcxx-ng 15.2.0 [required: >=9.4.0]
     │  │  │  │     └─ dependencies of libstdcxx-ng displayed above
     │  │  │  ├─ libcurl 8.14.1 [required: any]
     │  │  │  │  └─ dependencies of libcurl displayed above
     │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  ├─ libgoogle-cloud 2.39.0 [required: 2.39.0, hdb79228_0]
     │  │  │  │  └─ dependencies of libgoogle-cloud displayed above
     │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
     │  │  │  │  └─ dependencies of libzlib displayed above
     │  │  │  └─ openssl 3.5.4 [required: any]
     │  │  │     └─ dependencies of openssl displayed above
     │  │  ├─ libopentelemetry-cpp 1.21.0 [required: >=1.21.0,<1.22.0a0]
     │  │  │  ├─ libabseil 20250512.1 [required: >=20250512.1,<20250513.0a0]
     │  │  │  │  └─ dependencies of libabseil displayed above
     │  │  │  ├─ libcurl 8.14.1 [required: >=8.14.1,<9.0a0]
     │  │  │  │  └─ dependencies of libcurl displayed above
     │  │  │  ├─ libgrpc 1.73.1 [required: >=1.73.1,<1.74.0a0]
     │  │  │  │  └─ dependencies of libgrpc displayed above
     │  │  │  ├─ libopentelemetry-cpp-headers 1.21.0 [required: 1.21.0, ha770c72_1]
     │  │  │  ├─ libprotobuf 6.31.1 [required: >=6.31.1,<6.31.2.0a0]
     │  │  │  │  └─ dependencies of libprotobuf displayed above
     │  │  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
     │  │  │  │  └─ dependencies of libzlib displayed above
     │  │  │  ├─ nlohmann_json 3.12.0 [required: any]
     │  │  │  └─ prometheus-cpp 1.3.0 [required: >=1.3.0,<1.4.0a0]
     │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │     ├─ libcurl 8.14.1 [required: >=8.10.1,<9.0a0]
     │  │  │     │  └─ dependencies of libcurl displayed above
     │  │  │     ├─ libgcc 15.2.0 [required: >=13]
     │  │  │     │  └─ dependencies of libgcc displayed above
     │  │  │     ├─ libstdcxx 15.2.0 [required: >=13]
     │  │  │     │  └─ dependencies of libstdcxx displayed above
     │  │  │     ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
     │  │  │     │  └─ dependencies of libzlib displayed above
     │  │  │     └─ zlib 1.3.1 [required: any]
     │  │  │        ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │        ├─ libgcc 15.2.0 [required: >=13]
     │  │  │        │  └─ dependencies of libgcc displayed above
     │  │  │        └─ libzlib 1.3.1 [required: 1.3.1, hb9d3cd8_2]
     │  │  │           └─ dependencies of libzlib displayed above
     │  │  ├─ libprotobuf 6.31.1 [required: >=6.31.1,<6.31.2.0a0]
     │  │  │  └─ dependencies of libprotobuf displayed above
     │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
     │  │  │  └─ dependencies of libzlib displayed above
     │  │  ├─ lz4-c 1.10.0 [required: >=1.10.0,<1.11.0a0]
     │  │  │  └─ dependencies of lz4-c displayed above
     │  │  ├─ orc 2.2.1 [required: >=2.2.1,<2.2.2.0a0]
     │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  ├─ libprotobuf 6.31.1 [required: >=6.31.1,<6.31.2.0a0]
     │  │  │  │  └─ dependencies of libprotobuf displayed above
     │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
     │  │  │  │  └─ dependencies of libzlib displayed above
     │  │  │  ├─ lz4-c 1.10.0 [required: >=1.10.0,<1.11.0a0]
     │  │  │  │  └─ dependencies of lz4-c displayed above
     │  │  │  ├─ snappy 1.2.2 [required: >=1.2.2,<1.3.0a0]
     │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  │  │  └─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  ├─ tzdata 2025b [required: any]
     │  │  │  └─ zstd 1.5.7 [required: >=1.5.7,<1.6.0a0]
     │  │  │     └─ dependencies of zstd displayed above
     │  │  ├─ snappy 1.2.2 [required: >=1.2.2,<1.3.0a0]
     │  │  │  └─ dependencies of snappy displayed above
     │  │  └─ zstd 1.5.7 [required: >=1.5.7,<1.6.0a0]
     │  │     └─ dependencies of zstd displayed above
     │  ├─ libarrow-compute 21.0.0 [required: 21.0.0, h8c2c5c3_8_cpu]
     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  ├─ libarrow 21.0.0 [required: 21.0.0, h56a6dad_8_cpu]
     │  │  │  └─ dependencies of libarrow displayed above
     │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libgcc displayed above
     │  │  ├─ libre2-11 2025.08.12 [required: >=2025.8.12]
     │  │  │  └─ dependencies of libre2-11 displayed above
     │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  ├─ libutf8proc 2.11.0 [required: >=2.11.0,<2.12.0a0]
     │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  └─ libgcc 15.2.0 [required: >=14]
     │  │  │     └─ dependencies of libgcc displayed above
     │  │  └─ re2 2025.08.12 [required: any]
     │  │     └─ dependencies of re2 displayed above
     │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  └─ dependencies of libgcc displayed above
     │  └─ libstdcxx 15.2.0 [required: >=14]
     │     └─ dependencies of libstdcxx displayed above
     ├─ libarrow-dataset 21.0.0 [required: 21.0.0.*]
     │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  ├─ libarrow 21.0.0 [required: 21.0.0, h56a6dad_8_cpu]
     │  │  └─ dependencies of libarrow displayed above
     │  ├─ libarrow-acero 21.0.0 [required: 21.0.0, h635bf11_8_cpu]
     │  │  └─ dependencies of libarrow-acero displayed above
     │  ├─ libarrow-compute 21.0.0 [required: 21.0.0, h8c2c5c3_8_cpu]
     │  │  └─ dependencies of libarrow-compute displayed above
     │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  └─ dependencies of libgcc displayed above
     │  ├─ libparquet 21.0.0 [required: 21.0.0, h790f06f_8_cpu]
     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  ├─ libarrow 21.0.0 [required: 21.0.0, h56a6dad_8_cpu]
     │  │  │  └─ dependencies of libarrow displayed above
     │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libgcc displayed above
     │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  ├─ libthrift 0.22.0 [required: >=0.22.0,<0.22.1.0a0]
     │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  ├─ libevent 2.1.12 [required: >=2.1.12,<2.1.13.0a0]
     │  │  │  │  ├─ libgcc-ng 15.2.0 [required: >=12]
     │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  │  │  └─ openssl 3.5.4 [required: >=3.1.1,<4.0a0]
     │  │  │  │     └─ dependencies of openssl displayed above
     │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
     │  │  │  │  └─ dependencies of libzlib displayed above
     │  │  │  └─ openssl 3.5.4 [required: >=3.5.1,<4.0a0]
     │  │  │     └─ dependencies of openssl displayed above
     │  │  └─ openssl 3.5.4 [required: >=3.5.4,<4.0a0]
     │  │     └─ dependencies of openssl displayed above
     │  └─ libstdcxx 15.2.0 [required: >=14]
     │     └─ dependencies of libstdcxx displayed above
     ├─ libarrow-substrait 21.0.0 [required: 21.0.0.*]
     │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  ├─ libabseil 20250512.1 [required: >=20250512.1,<20250513.0a0]
     │  │  └─ dependencies of libabseil displayed above
     │  ├─ libarrow 21.0.0 [required: 21.0.0, h56a6dad_8_cpu]
     │  │  └─ dependencies of libarrow displayed above
     │  ├─ libarrow-acero 21.0.0 [required: 21.0.0, h635bf11_8_cpu]
     │  │  └─ dependencies of libarrow-acero displayed above
     │  ├─ libarrow-dataset 21.0.0 [required: 21.0.0, h635bf11_8_cpu]
     │  │  └─ dependencies of libarrow-dataset displayed above
     │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  └─ dependencies of libgcc displayed above
     │  ├─ libprotobuf 6.31.1 [required: >=6.31.1,<6.31.2.0a0]
     │  │  └─ dependencies of libprotobuf displayed above
     │  └─ libstdcxx 15.2.0 [required: >=14]
     │     └─ dependencies of libstdcxx displayed above
     ├─ libparquet 21.0.0 [required: 21.0.0.*]
     │  └─ dependencies of libparquet displayed above
     ├─ pyarrow-core 21.0.0 [required: 21.0.0, *_1_*]
     │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  ├─ libarrow 21.0.0 [required: 21.0.0.*, *cpu]
     │  │  └─ dependencies of libarrow displayed above
     │  ├─ libarrow-compute 21.0.0 [required: 21.0.0.*, *cpu]
     │  │  └─ dependencies of libarrow-compute displayed above
     │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  └─ dependencies of libgcc displayed above
     │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  └─ dependencies of libstdcxx displayed above
     │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
     │  │  └─ dependencies of libzlib displayed above
     │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
     │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
     ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
     └─ python_abi 3.13 [required: 3.13.*, *_cp313]
cython==3.1.4
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ libstdcxx 15.2.0 [required: >=14]
  │  └─ dependencies of libstdcxx displayed above
  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
scikit-learn==1.7.2
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ _openmp_mutex 4.5 [required: >=4.5]
  │  └─ dependencies of _openmp_mutex displayed above
  ├─ joblib 1.5.2 [required: >=1.2.0]
  │  ├─ python 3.13.8 [required: >=3.10]
  │  └─ setuptools 80.9.0 [required: any]
  │     └─ python 3.13.8 [required: >=3.9]
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ libstdcxx 15.2.0 [required: >=14]
  │  └─ dependencies of libstdcxx displayed above
  ├─ numpy 2.3.3 [required: >=1.23,<3]
  │  └─ dependencies of numpy displayed above
  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  ├─ python_abi 3.13 [required: 3.13.*, *_cp313]
  ├─ scipy 1.16.2 [required: >=1.8.0]
  │  └─ dependencies of scipy displayed above
  └─ threadpoolctl 3.6.0 [required: >=3.1.0]
     └─ python 3.13.8 [required: >=3.9]
pytables==3.10.2
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ blosc 1.21.6 [required: >=1.21.6,<2.0a0]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=13]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=13]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  └─ dependencies of libzlib displayed above
  │  ├─ lz4-c 1.10.0 [required: >=1.10.0,<1.11.0a0]
  │  │  └─ dependencies of lz4-c displayed above
  │  ├─ snappy 1.2.2 [required: >=1.2.1,<1.3.0a0]
  │  │  └─ dependencies of snappy displayed above
  │  └─ zstd 1.5.7 [required: >=1.5.6,<1.6.0a0]
  │     └─ dependencies of zstd displayed above
  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
  │  └─ dependencies of bzip2 displayed above
  ├─ c-blosc2 2.21.3 [required: >=2.21.3,<2.22.0a0]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ lz4-c 1.10.0 [required: >=1.10.0,<1.11.0a0]
  │  │  └─ dependencies of lz4-c displayed above
  │  ├─ zlib-ng 2.2.5 [required: >=2.2.5,<2.3.0a0]
  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  └─ dependencies of libgcc displayed above
  │  │  └─ libstdcxx 15.2.0 [required: >=14]
  │  │     └─ dependencies of libstdcxx displayed above
  │  └─ zstd 1.5.7 [required: >=1.5.7,<1.6.0a0]
  │     └─ dependencies of zstd displayed above
  ├─ hdf5 1.14.6 [required: >=1.14.6,<1.14.7.0a0]
  │  └─ dependencies of hdf5 displayed above
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ libstdcxx 15.2.0 [required: >=14]
  │  └─ dependencies of libstdcxx displayed above
  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  └─ dependencies of libzlib displayed above
  ├─ numexpr 2.14.0 [required: any]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  └─ dependencies of libstdcxx displayed above
  │  ├─ nomkl 1.0 [required: any]
  │  ├─ numpy 2.3.3 [required: >=1.23.0]
  │  │  └─ dependencies of numpy displayed above
  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  ├─ numpy 2.3.3 [required: >=1.23,<3]
  │  └─ dependencies of numpy displayed above
  ├─ packaging 25.0 [required: any]
  │  └─ dependencies of packaging displayed above
  ├─ py-cpuinfo 9.0.0 [required: any]
  │  └─ python 3.13.8 [required: >=3.9]
  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  ├─ python_abi 3.13 [required: 3.13.*, *_cp313]
  └─ typing-extensions 4.15.0 [required: >=4.4.0]
     └─ dependencies of typing-extensions displayed above
dill==0.4.0
  └─ python 3.13.8 [required: >=3.9]
scikit-image==0.25.2
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ imageio 2.37.0 [required: >=2.33,!=2.35.0]
  │  ├─ numpy 2.3.3 [required: any]
  │  │  └─ dependencies of numpy displayed above
  │  ├─ pillow 11.3.0 [required: >=8.3.2]
  │  │  └─ dependencies of pillow displayed above
  │  └─ python 3.13.8 [required: >=3.9]
  ├─ lazy-loader 0.4 [required: >=0.4]
  │  ├─ importlib-metadata 8.7.0 [required: any]
  │  │  └─ dependencies of importlib-metadata displayed above
  │  ├─ packaging 25.0 [required: any]
  │  │  └─ dependencies of packaging displayed above
  │  └─ python 3.13.8 [required: >=3.9]
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ libstdcxx 15.2.0 [required: >=14]
  │  └─ dependencies of libstdcxx displayed above
  ├─ networkx 3.5 [required: >=3.0]
  │  └─ python 3.13.8 [required: any]
  ├─ numpy 2.3.3 [required: >=1.24]
  │  └─ dependencies of numpy displayed above
  ├─ packaging 25.0 [required: >=21]
  │  └─ dependencies of packaging displayed above
  ├─ pillow 11.3.0 [required: >=10.1]
  │  └─ dependencies of pillow displayed above
  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  ├─ python_abi 3.13 [required: 3.13.*, *_cp313]
  ├─ pywavelets 1.9.0 [required: >=1.6]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  └─ dependencies of libgcc displayed above
  │  ├─ numpy 2.3.3 [required: >=1.25,<3]
  │  │  └─ dependencies of numpy displayed above
  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  ├─ scipy 1.16.2 [required: >=1.11.4]
  │  └─ dependencies of scipy displayed above
  └─ tifffile 2025.10.4 [required: >=2022.8.12]
     ├─ imagecodecs 2025.8.2 [required: >=2024.12.30]
     │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  ├─ blosc 1.21.6 [required: >=1.21.6,<2.0a0]
     │  │  └─ dependencies of blosc displayed above
     │  ├─ brunsli 0.1 [required: >=0.1,<1.0a0]
     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  ├─ libbrotlicommon 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  │  └─ dependencies of libbrotlicommon displayed above
     │  │  ├─ libbrotlidec 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  │  └─ dependencies of libbrotlidec displayed above
     │  │  ├─ libbrotlienc 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  │  └─ dependencies of libbrotlienc displayed above
     │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libgcc displayed above
     │  │  └─ libstdcxx 15.2.0 [required: >=14]
     │  │     └─ dependencies of libstdcxx displayed above
     │  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
     │  │  └─ dependencies of bzip2 displayed above
     │  ├─ c-blosc2 2.21.3 [required: >=2.21.2,<2.22.0a0]
     │  │  └─ dependencies of c-blosc2 displayed above
     │  ├─ charls 2.4.2 [required: >=2.4.2,<2.5.0a0]
     │  │  ├─ libgcc-ng 15.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  └─ libstdcxx-ng 15.2.0 [required: >=12]
     │  │     └─ dependencies of libstdcxx-ng displayed above
     │  ├─ giflib 5.2.2 [required: >=5.2.2,<5.3.0a0]
     │  │  └─ libgcc-ng 15.2.0 [required: >=12]
     │  │     └─ dependencies of libgcc-ng displayed above
     │  ├─ jxrlib 1.1 [required: >=1.1,<1.2.0a0]
     │  │  └─ libgcc-ng 15.2.0 [required: >=12]
     │  │     └─ dependencies of libgcc-ng displayed above
     │  ├─ lcms2 2.17 [required: >=2.17,<3.0a0]
     │  │  └─ dependencies of lcms2 displayed above
     │  ├─ lerc 4.0.0 [required: >=4.0.0,<5.0a0]
     │  │  └─ dependencies of lerc displayed above
     │  ├─ libaec 1.1.4 [required: >=1.1.4,<2.0a0]
     │  │  └─ dependencies of libaec displayed above
     │  ├─ libavif16 1.3.0 [required: >=1.3.0,<2.0a0]
     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  ├─ aom 3.9.1 [required: >=3.9.1,<3.10.0a0]
     │  │  │  ├─ libgcc-ng 15.2.0 [required: >=12]
     │  │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  │  └─ libstdcxx-ng 15.2.0 [required: >=12]
     │  │  │     └─ dependencies of libstdcxx-ng displayed above
     │  │  ├─ dav1d 1.2.1 [required: >=1.2.1,<1.2.2.0a0]
     │  │  │  └─ libgcc-ng 15.2.0 [required: >=12]
     │  │  │     └─ dependencies of libgcc-ng displayed above
     │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libgcc displayed above
     │  │  ├─ rav1e 0.7.1 [required: >=0.7.1,<0.8.0a0]
     │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  └─ libgcc 15.2.0 [required: >=13]
     │  │  │     └─ dependencies of libgcc displayed above
     │  │  └─ svt-av1 3.1.2 [required: >=3.1.2,<3.1.3.0a0]
     │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │     ├─ libgcc 15.2.0 [required: >=14]
     │  │     │  └─ dependencies of libgcc displayed above
     │  │     └─ libstdcxx 15.2.0 [required: >=14]
     │  │        └─ dependencies of libstdcxx displayed above
     │  ├─ libbrotlicommon 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  └─ dependencies of libbrotlicommon displayed above
     │  ├─ libbrotlidec 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  └─ dependencies of libbrotlidec displayed above
     │  ├─ libbrotlienc 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  └─ dependencies of libbrotlienc displayed above
     │  ├─ libdeflate 1.24 [required: >=1.24,<1.25.0a0]
     │  │  └─ dependencies of libdeflate displayed above
     │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  └─ dependencies of libgcc displayed above
     │  ├─ libjpeg-turbo 3.1.0 [required: >=3.1.0,<4.0a0]
     │  │  └─ dependencies of libjpeg-turbo displayed above
     │  ├─ libjxl 0.11.1 [required: >=0.11,<0.12.0a0]
     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  ├─ libbrotlidec 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  │  └─ dependencies of libbrotlidec displayed above
     │  │  ├─ libbrotlienc 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  │  └─ dependencies of libbrotlienc displayed above
     │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libgcc displayed above
     │  │  ├─ libhwy 1.3.0 [required: >=1.3.0,<1.4.0a0]
     │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  │  └─ dependencies of libgcc displayed above
     │  │  │  └─ libstdcxx 15.2.0 [required: >=14]
     │  │  │     └─ dependencies of libstdcxx displayed above
     │  │  └─ libstdcxx 15.2.0 [required: >=14]
     │  │     └─ dependencies of libstdcxx displayed above
     │  ├─ liblzma 5.8.1 [required: >=5.8.1,<6.0a0]
     │  │  └─ dependencies of liblzma displayed above
     │  ├─ libpng 1.6.50 [required: >=1.6.50,<1.7.0a0]
     │  │  └─ dependencies of libpng displayed above
     │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  └─ dependencies of libstdcxx displayed above
     │  ├─ libtiff 4.7.1 [required: >=4.7.0,<4.8.0a0]
     │  │  └─ dependencies of libtiff displayed above
     │  ├─ libwebp-base 1.6.0 [required: >=1.6.0,<2.0a0]
     │  │  └─ dependencies of libwebp-base displayed above
     │  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
     │  │  └─ dependencies of libzlib displayed above
     │  ├─ libzopfli 1.0.3 [required: >=1.0.3,<1.1.0a0]
     │  │  ├─ libgcc-ng 15.2.0 [required: >=9.3.0]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  └─ libstdcxx-ng 15.2.0 [required: >=9.3.0]
     │  │     └─ dependencies of libstdcxx-ng displayed above
     │  ├─ lz4-c 1.10.0 [required: >=1.10.0,<1.11.0a0]
     │  │  └─ dependencies of lz4-c displayed above
     │  ├─ numpy 2.3.3 [required: >=1.23,<3]
     │  │  └─ dependencies of numpy displayed above
     │  ├─ openjpeg 2.5.4 [required: >=2.5.3,<3.0a0]
     │  │  └─ dependencies of openjpeg displayed above
     │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
     │  ├─ python_abi 3.13 [required: 3.13.*, *_cp313]
     │  ├─ snappy 1.2.2 [required: >=1.2.2,<1.3.0a0]
     │  │  └─ dependencies of snappy displayed above
     │  ├─ zfp 1.0.1 [required: >=1.0.1,<2.0a0]
     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  ├─ _openmp_mutex 4.5 [required: >=4.5]
     │  │  │  └─ dependencies of _openmp_mutex displayed above
     │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libgcc displayed above
     │  │  └─ libstdcxx 15.2.0 [required: >=14]
     │  │     └─ dependencies of libstdcxx displayed above
     │  ├─ zlib-ng 2.2.5 [required: >=2.2.5,<2.3.0a0]
     │  │  └─ dependencies of zlib-ng displayed above
     │  └─ zstd 1.5.7 [required: >=1.5.7,<1.6.0a0]
     │     └─ dependencies of zstd displayed above
     ├─ numpy 2.3.3 [required: >=1.19.2]
     │  └─ dependencies of numpy displayed above
     └─ python 3.13.8 [required: >=3.11]
protobuf==6.31.1
  ├─ __glibc [required: >=2.17,<3.0.a0]
  ├─ libabseil 20250512.1 [required: >=20250512.1,<20250513.0a0]
  │  └─ dependencies of libabseil displayed above
  ├─ libgcc 15.2.0 [required: >=14]
  │  └─ dependencies of libgcc displayed above
  ├─ libstdcxx 15.2.0 [required: >=14]
  │  └─ dependencies of libstdcxx displayed above
  ├─ libzlib 1.3.1 [required: >=1.3.1,<2.0a0]
  │  └─ dependencies of libzlib displayed above
  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
jupyterhub-singleuser==5.4.0
  ├─ __unix [required: any]
  ├─ jupyterhub-base 5.4.0 [required: ==5.4.0, pyhc90fa1f_0]
  │  ├─ __unix [required: any]
  │  ├─ alembic 1.17.0 [required: >=1.4]
  │  │  ├─ mako 1.3.10 [required: any]
  │  │  │  ├─ importlib-metadata 8.7.0 [required: any]
  │  │  │  │  └─ dependencies of importlib-metadata displayed above
  │  │  │  ├─ markupsafe 3.0.3 [required: >=0.9.2]
  │  │  │  │  └─ dependencies of markupsafe displayed above
  │  │  │  └─ python 3.13.8 [required: >=3.9]
  │  │  ├─ python 3.13.8 [required: >=3.10]
  │  │  ├─ sqlalchemy 2.0.44 [required: >=1.4.0]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ greenlet 3.2.4 [required: !=0.4.17]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  │  ├─ libstdcxx 15.2.0 [required: >=14]
  │  │  │  │  │  └─ dependencies of libstdcxx displayed above
  │  │  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  │  ├─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  │  └─ typing-extensions 4.15.0 [required: >=4.6.0]
  │  │  │     └─ dependencies of typing-extensions displayed above
  │  │  ├─ tomli 2.3.0 [required: any]
  │  │  │  └─ python 3.13.8 [required: any]
  │  │  └─ typing_extensions 4.15.0 [required: >=4.12]
  │  │     └─ dependencies of typing_extensions displayed above
  │  ├─ async_generator 1.10 [required: >=1.9]
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ certipy 0.2.2 [required: >=0.1.2]
  │  │  ├─ cryptography 46.0.2 [required: any]
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ cffi 2.0.0 [required: >=1.14]
  │  │  │  │  └─ dependencies of cffi displayed above
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  ├─ openssl 3.5.4 [required: >=3.5.3,<4.0a0]
  │  │  │  │  └─ dependencies of openssl displayed above
  │  │  │  ├─ python 3.13.8 [required: >=3.13,<3.14.0a0]
  │  │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ idna 3.11 [required: any]
  │  │  └─ dependencies of idna displayed above
  │  ├─ importlib-metadata 8.7.0 [required: >=3.6]
  │  │  └─ dependencies of importlib-metadata displayed above
  │  ├─ jinja2 3.1.6 [required: >=2.11.0]
  │  │  └─ dependencies of jinja2 displayed above
  │  ├─ jupyter_events 0.12.0 [required: any]
  │  │  └─ dependencies of jupyter_events displayed above
  │  ├─ oauthlib 3.3.1 [required: >=3.0]
  │  │  ├─ blinker 1.9.0 [required: any]
  │  │  │  └─ python 3.13.8 [required: >=3.9]
  │  │  ├─ cryptography 46.0.2 [required: any]
  │  │  │  └─ dependencies of cryptography displayed above
  │  │  ├─ pyjwt 2.10.1 [required: >=1.0.0]
  │  │  │  └─ python 3.13.8 [required: >=3.9]
  │  │  └─ python 3.13.8 [required: >=3.9]
  │  ├─ packaging 25.0 [required: any]
  │  │  └─ dependencies of packaging displayed above
  │  ├─ prometheus_client 0.23.1 [required: >=0.5.0]
  │  │  └─ dependencies of prometheus_client displayed above
  │  ├─ pydantic 2.12.0 [required: >=2]
  │  │  ├─ annotated-types 0.7.0 [required: >=0.6.0]
  │  │  │  ├─ python 3.13.8 [required: >=3.9]
  │  │  │  └─ typing-extensions 4.15.0 [required: >=4.0.0]
  │  │  │     └─ dependencies of typing-extensions displayed above
  │  │  ├─ pydantic-core 2.41.1 [required: 2.41.1]
  │  │  │  ├─ python 3.13.8 [required: any]
  │  │  │  ├─ typing-extensions 4.15.0 [required: >=4.6.0,!=4.7.0]
  │  │  │  │  └─ dependencies of typing-extensions displayed above
  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  ├─ libgcc 15.2.0 [required: >=14]
  │  │  │  │  └─ dependencies of libgcc displayed above
  │  │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
  │  │  ├─ python 3.13.8 [required: >=3.10]
  │  │  ├─ typing-extensions 4.15.0 [required: >=4.6.1]
  │  │  │  └─ dependencies of typing-extensions displayed above
  │  │  ├─ typing-inspection 0.4.2 [required: >=0.4.2]
  │  │  │  ├─ python 3.13.8 [required: >=3.10]
  │  │  │  └─ typing_extensions 4.15.0 [required: >=4.12.0]
  │  │  │     └─ dependencies of typing_extensions displayed above
  │  │  └─ typing_extensions 4.15.0 [required: >=4.14.1]
  │  │     └─ dependencies of typing_extensions displayed above
  │  ├─ python 3.13.8 [required: any]
  │  ├─ python-dateutil 2.9.0.post0 [required: any]
  │  │  └─ dependencies of python-dateutil displayed above
  │  ├─ requests 2.32.5 [required: any]
  │  │  └─ dependencies of requests displayed above
  │  ├─ sqlalchemy 2.0.44 [required: >=1.4.1]
  │  │  └─ dependencies of sqlalchemy displayed above
  │  ├─ tornado 6.5.2 [required: >=5.1]
  │  │  └─ dependencies of tornado displayed above
  │  ├─ traitlets 5.14.3 [required: >=4.3.2]
  │  │  └─ dependencies of traitlets displayed above
  │  └─ pamela 1.2.0 [required: any]
  │     └─ python 3.13.8 [required: >=3.9]
  └─ jupyterlab 4.4.9 [required: >=3.1]
     ├─ async-lru 2.0.5 [required: >=1.0.0]
     │  ├─ python 3.13.8 [required: any]
     │  └─ typing_extensions 4.15.0 [required: >=4.0.0]
     │     └─ dependencies of typing_extensions displayed above
     ├─ httpx 0.28.1 [required: >=0.25.0,<1]
     │  ├─ anyio 4.11.0 [required: any]
     │  │  └─ dependencies of anyio displayed above
     │  ├─ certifi 2025.10.5 [required: any]
     │  │  └─ dependencies of certifi displayed above
     │  ├─ httpcore 1.0.9 [required: 1.*]
     │  │  ├─ python 3.13.8 [required: any]
     │  │  ├─ h11 0.16.0 [required: >=0.16]
     │  │  │  ├─ python 3.13.8 [required: >=3.9]
     │  │  │  └─ typing_extensions 4.15.0 [required: any]
     │  │  │     └─ dependencies of typing_extensions displayed above
     │  │  ├─ h2 4.3.0 [required: >=3,<5]
     │  │  │  └─ dependencies of h2 displayed above
     │  │  ├─ sniffio 1.3.1 [required: 1.*]
     │  │  │  └─ dependencies of sniffio displayed above
     │  │  ├─ anyio 4.11.0 [required: >=4.0,<5.0]
     │  │  │  └─ dependencies of anyio displayed above
     │  │  └─ certifi 2025.10.5 [required: any]
     │  │     └─ dependencies of certifi displayed above
     │  ├─ idna 3.11 [required: any]
     │  │  └─ dependencies of idna displayed above
     │  └─ python 3.13.8 [required: >=3.9]
     ├─ importlib-metadata 8.7.0 [required: >=4.8.3]
     │  └─ dependencies of importlib-metadata displayed above
     ├─ ipykernel 7.0.0 [required: >=6.5.0,!=6.30.0]
     │  ├─ python 3.13.8 [required: >=3.10]
     │  ├─ __linux [required: any]
     │  ├─ comm 0.2.3 [required: >=0.1.1]
     │  │  └─ dependencies of comm displayed above
     │  ├─ debugpy 1.8.17 [required: >=1.6.5]
     │  │  ├─ python 3.13.8 [required: any]
     │  │  ├─ libgcc 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libgcc displayed above
     │  │  ├─ libstdcxx 15.2.0 [required: >=14]
     │  │  │  └─ dependencies of libstdcxx displayed above
     │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
     │  │  └─ python_abi 3.13 [required: 3.13.*, *_cp313]
     │  ├─ ipython 9.6.0 [required: >=7.23.1]
     │  │  └─ dependencies of ipython displayed above
     │  ├─ jupyter_client 8.6.3 [required: >=8.0.0]
     │  │  └─ dependencies of jupyter_client displayed above
     │  ├─ jupyter_core 5.8.1 [required: >=4.12,!=5.0.*]
     │  │  └─ dependencies of jupyter_core displayed above
     │  ├─ matplotlib-inline 0.1.7 [required: >=0.1]
     │  │  └─ dependencies of matplotlib-inline displayed above
     │  ├─ nest-asyncio 1.6.0 [required: >=1.4]
     │  │  └─ python 3.13.8 [required: >=3.9]
     │  ├─ packaging 25.0 [required: >=22]
     │  │  └─ dependencies of packaging displayed above
     │  ├─ psutil 7.1.0 [required: >=5.7]
     │  │  └─ dependencies of psutil displayed above
     │  ├─ pyzmq 27.1.0 [required: >=25]
     │  │  └─ dependencies of pyzmq displayed above
     │  ├─ tornado 6.5.2 [required: >=6.2]
     │  │  └─ dependencies of tornado displayed above
     │  └─ traitlets 5.14.3 [required: >=5.4.0]
     │     └─ dependencies of traitlets displayed above
     ├─ jinja2 3.1.6 [required: >=3.0.3]
     │  └─ dependencies of jinja2 displayed above
     ├─ jupyter-lsp 2.3.0 [required: >=2.0.0]
     │  ├─ importlib-metadata 8.7.0 [required: >=4.8.3]
     │  │  └─ dependencies of importlib-metadata displayed above
     │  ├─ jupyter_server 2.17.0 [required: >=1.1.2]
     │  │  └─ dependencies of jupyter_server displayed above
     │  └─ python 3.13.8 [required: any]
     ├─ jupyter_core 5.8.1 [required: any]
     │  └─ dependencies of jupyter_core displayed above
     ├─ jupyter_server 2.17.0 [required: >=2.4.0,<3]
     │  └─ dependencies of jupyter_server displayed above
     ├─ jupyterlab_server 2.27.3 [required: >=2.27.1,<3]
     │  ├─ babel 2.17.0 [required: >=2.10]
     │  │  ├─ python 3.13.8 [required: >=3.9]
     │  │  └─ pytz 2025.2 [required: >=2015.7]
     │  │     └─ dependencies of pytz displayed above
     │  ├─ importlib-metadata 8.7.0 [required: >=4.8.3]
     │  │  └─ dependencies of importlib-metadata displayed above
     │  ├─ jinja2 3.1.6 [required: >=3.0.3]
     │  │  └─ dependencies of jinja2 displayed above
     │  ├─ json5 0.12.1 [required: >=0.9.0]
     │  │  └─ python 3.13.8 [required: >=3.9]
     │  ├─ jsonschema 4.25.1 [required: >=4.18]
     │  │  └─ dependencies of jsonschema displayed above
     │  ├─ jupyter_server 2.17.0 [required: >=1.21,<3]
     │  │  └─ dependencies of jupyter_server displayed above
     │  ├─ packaging 25.0 [required: >=21.3]
     │  │  └─ dependencies of packaging displayed above
     │  ├─ python 3.13.8 [required: >=3.9]
     │  └─ requests 2.32.5 [required: >=2.31]
     │     └─ dependencies of requests displayed above
     ├─ notebook-shim 0.2.4 [required: >=0.2]
     │  ├─ jupyter_server 2.17.0 [required: >=1.8,<3]
     │  │  └─ dependencies of jupyter_server displayed above
     │  └─ python 3.13.8 [required: >=3.9]
     ├─ packaging 25.0 [required: any]
     │  └─ dependencies of packaging displayed above
     ├─ python 3.13.8 [required: >=3.10]
     ├─ setuptools 80.9.0 [required: >=41.1.0]
     │  └─ dependencies of setuptools displayed above
     ├─ tomli 2.3.0 [required: >=1.2.2]
     │  └─ dependencies of tomli displayed above
     ├─ tornado 6.5.2 [required: >=6.2.0]
     │  └─ dependencies of tornado displayed above
     └─ traitlets 5.14.3 [required: any]
        └─ dependencies of traitlets displayed above
nbclassic==1.3.3
  ├─ ipykernel 7.0.0 [required: any]
  │  └─ dependencies of ipykernel displayed above
  ├─ ipython_genutils 0.2.0 [required: any]
  │  └─ python 3.13.8 [required: >=3.9]
  ├─ nest-asyncio 1.6.0 [required: >=1.5]
  │  └─ dependencies of nest-asyncio displayed above
  ├─ notebook-shim 0.2.4 [required: >=0.2.3]
  │  └─ dependencies of notebook-shim displayed above
  └─ python 3.13.8 [required: any]
notebook==7.4.7
  ├─ jupyter_server 2.17.0 [required: >=2.4.0,<3]
  │  └─ dependencies of jupyter_server displayed above
  ├─ jupyterlab 4.4.9 [required: >=4.4.9,<4.5]
  │  └─ dependencies of jupyterlab displayed above
  ├─ jupyterlab_server 2.27.3 [required: >=2.27.1,<3]
  │  └─ dependencies of jupyterlab_server displayed above
  ├─ notebook-shim 0.2.4 [required: >=0.2,<0.3]
  │  └─ dependencies of notebook-shim displayed above
  ├─ python 3.13.8 [required: >=3.10]
  └─ tornado 6.5.2 [required: >=6.2.0]
     └─ dependencies of tornado displayed above
```

