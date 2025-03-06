# UW-IT JupyterHub for Teaching datascience Notebook server
Docker image for UW-IT JupyterHub for Teaching datascience Notebook server. 
- Detailed information about base datascience Notebook is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-datascience-notebook
- General information about working with base images is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html
- Installed packages and versions can be viewed in this image's [Dockerfile](Dockerfile) using `pip list` or `conda list`. Dependency trees for both Pip and Conda packages shown below.
- All packages are installed into the default Conda environment, which is active on startup.
- The JupyterLab (v4.2.0) interface is installed and is set as default

## Running Notebook locally
- `docker run -p 8888:8888 us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-datascience-notebook:2.7.1`
- Console output will include localhost url with access token.

## Accessing server shell locally
- `docker run -it --entrypoint /bin/bash us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-datascience-notebook:2.7.1`


## Installed Python packages

### Pip packages
via `pipdeptree --exclude pipdeptree`

```
altair==5.3.0
├── Jinja2 [required: Any, installed: 3.1.4]
│   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
├── jsonschema [required: >=3.0, installed: 4.22.0]
│   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   ├── jsonschema-specifications [required: >=2023.03.6, installed: 2023.12.1]
│   │   └── referencing [required: >=0.31.0, installed: 0.35.1]
│   │       ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │       └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   ├── referencing [required: >=0.28.4, installed: 0.35.1]
│   │   ├── attrs [required: >=22.2.0, installed: 23.2.0]
│   │   └── rpds-py [required: >=0.7.0, installed: 0.18.1]
│   └── rpds-py [required: >=0.7.1, installed: 0.18.1]
├── numpy [required: Any, installed: 1.26.4]
├── packaging [required: Any, installed: 24.2]
├── pandas [required: >=0.25, installed: 2.2.2]
│   ├── numpy [required: >=1.23.2, installed: 1.26.4]
│   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   └── six [required: >=1.5, installed: 1.16.0]
│   ├── pytz [required: >=2020.1, installed: 2024.1]
│   └── tzdata [required: >=2022.7, installed: 2024.1]
└── toolz [required: Any, installed: 0.12.1]
blinker==1.8.2
bokeh==3.4.1
├── contourpy [required: >=1.2, installed: 1.2.1]
│   └── numpy [required: >=1.20, installed: 1.26.4]
├── Jinja2 [required: >=2.9, installed: 3.1.4]
│   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
├── numpy [required: >=1.16, installed: 1.26.4]
├── packaging [required: >=16.8, installed: 24.2]
├── pandas [required: >=1.2, installed: 2.2.2]
│   ├── numpy [required: >=1.23.2, installed: 1.26.4]
│   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   └── six [required: >=1.5, installed: 1.16.0]
│   ├── pytz [required: >=2020.1, installed: 2024.1]
│   └── tzdata [required: >=2022.7, installed: 2024.1]
├── pillow [required: >=7.1.0, installed: 10.3.0]
├── PyYAML [required: >=3.10, installed: 6.0.1]
├── tornado [required: >=6.2, installed: 6.4]
└── xyzservices [required: >=2021.09.1, installed: 2024.4.0]
Bottleneck==1.3.8
└── numpy [required: Any, installed: 1.26.4]
Brotli==1.1.0
cached-property==1.5.2
conda-tree==1.1.1
├── colorama [required: Any, installed: 0.4.6]
└── networkx [required: Any, installed: 3.3]
Cython==3.0.10
cytoolz==0.12.3
└── toolz [required: >=0.8.0, installed: 0.12.1]
dask-expr==1.1.1
├── dask [required: ==2024.5.1, installed: 2024.5.1]
│   ├── click [required: >=8.1, installed: 8.1.7]
│   ├── cloudpickle [required: >=1.5.0, installed: 3.0.0]
│   ├── fsspec [required: >=2021.09.0, installed: 2024.5.0]
│   ├── importlib_metadata [required: >=4.13.0, installed: 7.1.0]
│   │   └── zipp [required: >=0.5, installed: 3.17.0]
│   ├── packaging [required: >=20.0, installed: 24.2]
│   ├── partd [required: >=1.2.0, installed: 1.4.2]
│   │   ├── locket [required: Any, installed: 1.0.0]
│   │   └── toolz [required: Any, installed: 0.12.1]
│   ├── PyYAML [required: >=5.3.1, installed: 6.0.1]
│   └── toolz [required: >=0.10.0, installed: 0.12.1]
├── pandas [required: >=2, installed: 2.2.2]
│   ├── numpy [required: >=1.23.2, installed: 1.26.4]
│   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   └── six [required: >=1.5, installed: 1.16.0]
│   ├── pytz [required: >=2020.1, installed: 2024.1]
│   └── tzdata [required: >=2022.7, installed: 2024.1]
└── pyarrow [required: >=7.0.0, installed: 16.1.0]
    └── numpy [required: >=1.16.6, installed: 1.26.4]
dill==0.3.8
distributed==2024.5.1
├── click [required: >=8.0, installed: 8.1.7]
├── cloudpickle [required: >=1.5.0, installed: 3.0.0]
├── dask [required: ==2024.5.1, installed: 2024.5.1]
│   ├── click [required: >=8.1, installed: 8.1.7]
│   ├── cloudpickle [required: >=1.5.0, installed: 3.0.0]
│   ├── fsspec [required: >=2021.09.0, installed: 2024.5.0]
│   ├── importlib_metadata [required: >=4.13.0, installed: 7.1.0]
│   │   └── zipp [required: >=0.5, installed: 3.17.0]
│   ├── packaging [required: >=20.0, installed: 24.2]
│   ├── partd [required: >=1.2.0, installed: 1.4.2]
│   │   ├── locket [required: Any, installed: 1.0.0]
│   │   └── toolz [required: Any, installed: 0.12.1]
│   ├── PyYAML [required: >=5.3.1, installed: 6.0.1]
│   └── toolz [required: >=0.10.0, installed: 0.12.1]
├── Jinja2 [required: >=2.10.3, installed: 3.1.4]
│   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
├── locket [required: >=1.0.0, installed: 1.0.0]
├── msgpack [required: >=1.0.0, installed: 1.0.8]
├── packaging [required: >=20.0, installed: 24.2]
├── psutil [required: >=5.7.2, installed: 5.9.8]
├── PyYAML [required: >=5.3.1, installed: 6.0.1]
├── sortedcontainers [required: >=2.0.5, installed: 2.4.0]
├── tblib [required: >=1.6.0, installed: 3.0.0]
├── toolz [required: >=0.10.0, installed: 0.12.1]
├── tornado [required: >=6.0.4, installed: 6.4]
├── urllib3 [required: >=1.24.3, installed: 1.26.20]
└── zict [required: >=3.0.0, installed: 3.0.0]
entrypoints==0.4
exceptiongroup==1.2.0
fiona==1.10.1
├── attrs [required: >=19.2.0, installed: 23.2.0]
├── certifi [required: Any, installed: 2025.1.31]
├── click [required: ~=8.0, installed: 8.1.7]
├── click-plugins [required: >=1.0, installed: 1.1.1]
│   └── click [required: >=4.0, installed: 8.1.7]
└── cligj [required: >=0.5, installed: 0.7.2]
    └── click [required: >=4.0, installed: 8.1.7]
folium==0.19.5
├── branca [required: >=0.6.0, installed: 0.8.1]
│   └── Jinja2 [required: >=3, installed: 3.1.4]
│       └── MarkupSafe [required: >=2.0, installed: 2.1.5]
├── Jinja2 [required: >=2.9, installed: 3.1.4]
│   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
├── numpy [required: Any, installed: 1.26.4]
├── requests [required: Any, installed: 2.31.0]
│   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   ├── idna [required: >=2.5,<4, installed: 3.7]
│   └── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
└── xyzservices [required: Any, installed: 2024.4.0]
fqdn==1.5.1
geopandas==1.0.1
├── numpy [required: >=1.22, installed: 1.26.4]
├── packaging [required: Any, installed: 24.2]
├── pandas [required: >=1.4.0, installed: 2.2.2]
│   ├── numpy [required: >=1.23.2, installed: 1.26.4]
│   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   └── six [required: >=1.5, installed: 1.16.0]
│   ├── pytz [required: >=2020.1, installed: 2024.1]
│   └── tzdata [required: >=2022.7, installed: 2024.1]
├── pyogrio [required: >=0.7.2, installed: 0.10.0]
│   ├── certifi [required: Any, installed: 2025.1.31]
│   ├── numpy [required: Any, installed: 1.26.4]
│   └── packaging [required: Any, installed: 24.2]
├── pyproj [required: >=3.3.0, installed: 3.7.1]
│   └── certifi [required: Any, installed: 2025.1.31]
└── shapely [required: >=2.0.0, installed: 2.0.7]
    └── numpy [required: >=1.14,<3, installed: 1.26.4]
gmpy2==2.1.5
h2==4.1.0
├── hpack [required: >=4.0,<5, installed: 4.0.0]
└── hyperframe [required: >=6.0,<7, installed: 6.0.1]
h5py==3.11.0
└── numpy [required: >=1.17.3, installed: 1.26.4]
imagecodecs==2024.1.1
└── numpy [required: Any, installed: 1.26.4]
importlib_resources==6.4.0
ipyleaflet==0.19.2
├── branca [required: >=0.5.0, installed: 0.8.1]
│   └── Jinja2 [required: >=3, installed: 3.1.4]
│       └── MarkupSafe [required: >=2.0, installed: 2.1.5]
├── ipywidgets [required: >=7.6.0,<9, installed: 8.1.2]
│   ├── comm [required: >=0.1.3, installed: 0.2.2]
│   │   └── traitlets [required: >=4, installed: 5.14.3]
│   ├── ipython [required: >=6.1.0, installed: 8.24.0]
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
│   │   └── typing_extensions [required: >=4.6, installed: 4.11.0]
│   ├── jupyterlab_widgets [required: ~=3.0.10, installed: 3.0.10]
│   ├── traitlets [required: >=4.3.1, installed: 5.14.3]
│   └── widgetsnbextension [required: ~=4.0.10, installed: 4.0.10]
├── jupyter-leaflet [required: >=0.19,<0.20, installed: 0.19.2]
├── traittypes [required: >=0.2.1,<3, installed: 0.2.1]
│   └── traitlets [required: >=4.2.2, installed: 5.14.3]
└── xyzservices [required: >=2021.8.1, installed: 2024.4.0]
ipympl==0.9.4
├── ipython [required: <9, installed: 8.24.0]
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
│   └── typing_extensions [required: >=4.6, installed: 4.11.0]
├── ipython-genutils [required: Any, installed: 0.2.0]
├── ipywidgets [required: >=7.6.0,<9, installed: 8.1.2]
│   ├── comm [required: >=0.1.3, installed: 0.2.2]
│   │   └── traitlets [required: >=4, installed: 5.14.3]
│   ├── ipython [required: >=6.1.0, installed: 8.24.0]
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
│   │   └── typing_extensions [required: >=4.6, installed: 4.11.0]
│   ├── jupyterlab_widgets [required: ~=3.0.10, installed: 3.0.10]
│   ├── traitlets [required: >=4.3.1, installed: 5.14.3]
│   └── widgetsnbextension [required: ~=4.0.10, installed: 4.0.10]
├── matplotlib [required: >=3.4.0,<4, installed: 3.8.4]
│   ├── contourpy [required: >=1.0.1, installed: 1.2.1]
│   │   └── numpy [required: >=1.20, installed: 1.26.4]
│   ├── cycler [required: >=0.10, installed: 0.12.1]
│   ├── fonttools [required: >=4.22.0, installed: 4.51.0]
│   ├── kiwisolver [required: >=1.3.1, installed: 1.4.5]
│   ├── numpy [required: >=1.21, installed: 1.26.4]
│   ├── packaging [required: >=20.0, installed: 24.2]
│   ├── pillow [required: >=8, installed: 10.3.0]
│   ├── pyparsing [required: >=2.3.1, installed: 3.1.2]
│   └── python-dateutil [required: >=2.7, installed: 2.9.0]
│       └── six [required: >=1.5, installed: 1.16.0]
├── numpy [required: Any, installed: 1.26.4]
├── pillow [required: Any, installed: 10.3.0]
└── traitlets [required: <6, installed: 5.14.3]
isoduration==20.11.0
└── arrow [required: >=0.15.0, installed: 1.3.0]
    ├── python-dateutil [required: >=2.7.0, installed: 2.9.0]
    │   └── six [required: >=1.5, installed: 1.16.0]
    └── types-python-dateutil [required: >=2.8.10, installed: 2.9.0.20240316]
jupyter-pluto-proxy==0.1.2
└── jupyter_server_proxy [required: >=1.5.0, installed: 4.1.2]
    ├── aiohttp [required: Any, installed: 3.9.5]
    │   ├── aiosignal [required: >=1.1.2, installed: 1.3.1]
    │   │   └── frozenlist [required: >=1.1.0, installed: 1.4.1]
    │   ├── attrs [required: >=17.3.0, installed: 23.2.0]
    │   ├── frozenlist [required: >=1.1.1, installed: 1.4.1]
    │   ├── multidict [required: >=4.5,<7.0, installed: 6.0.5]
    │   └── yarl [required: >=1.0,<2.0, installed: 1.9.4]
    │       ├── idna [required: >=2.0, installed: 3.7]
    │       └── multidict [required: >=4.0, installed: 6.0.5]
    ├── jupyter_server [required: >=1.0, installed: 2.14.0]
    │   ├── anyio [required: >=3.1.0, installed: 4.3.0]
    │   │   ├── idna [required: >=2.8, installed: 3.7]
    │   │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
    ├── simpervisor [required: >=1.0, installed: 1.0.0]
    ├── tornado [required: >=5.1, installed: 6.4]
    └── traitlets [required: >=4.2.1, installed: 5.14.3]
jupyter-resource-usage==1.1.1
├── jupyter_server [required: >=2.0, installed: 2.14.0]
│   ├── anyio [required: >=3.1.0, installed: 4.3.0]
│   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
├── prometheus_client [required: Any, installed: 0.20.0]
├── psutil [required: ~=5.6, installed: 5.9.8]
└── pyzmq [required: >=19, installed: 26.0.3]
jupyterhub==4.1.5
├── alembic [required: >=1.4, installed: 1.13.1]
│   ├── Mako [required: Any, installed: 1.3.5]
│   │   └── MarkupSafe [required: >=0.9.2, installed: 2.1.5]
│   ├── SQLAlchemy [required: >=1.3.0, installed: 2.0.30]
│   │   ├── greenlet [required: !=0.4.17, installed: 3.0.3]
│   │   └── typing_extensions [required: >=4.6.0, installed: 4.11.0]
│   └── typing_extensions [required: >=4, installed: 4.11.0]
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
├── requests [required: Any, installed: 2.31.0]
│   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   ├── idna [required: >=2.5,<4, installed: 3.7]
│   └── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
├── SQLAlchemy [required: >=1.4, installed: 2.0.30]
│   ├── greenlet [required: !=0.4.17, installed: 3.0.3]
│   └── typing_extensions [required: >=4.6.0, installed: 4.11.0]
├── tornado [required: >=5.1, installed: 6.4]
└── traitlets [required: >=4.3.2, installed: 5.14.3]
jupyterlab_git==0.50.0
├── jupyter_server [required: >=2.0.1,<3, installed: 2.14.0]
│   ├── anyio [required: >=3.1.0, installed: 4.3.0]
│   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
├── nbdime [required: ~=4.0.1, installed: 4.0.1]
│   ├── colorama [required: Any, installed: 0.4.6]
│   ├── GitPython [required: !=2.1.6,!=2.1.5,!=2.1.4, installed: 3.1.43]
│   │   └── gitdb [required: >=4.0.1,<5, installed: 4.0.11]
│   │       └── smmap [required: >=3.0.1,<6, installed: 5.0.0]
│   ├── Jinja2 [required: >=2.9, installed: 3.1.4]
│   │   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
│   ├── jupyter_server [required: Any, installed: 2.14.0]
│   │   ├── anyio [required: >=3.1.0, installed: 4.3.0]
│   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
│   ├── jupyter-server-mathjax [required: >=0.2.2, installed: 0.2.6]
│   │   └── jupyter_server [required: >=1.1, installed: 2.14.0]
│   │       ├── anyio [required: >=3.1.0, installed: 4.3.0]
│   │       │   ├── idna [required: >=2.8, installed: 3.7]
│   │       │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
│   ├── nbformat [required: Any, installed: 5.10.4]
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
│   ├── Pygments [required: Any, installed: 2.18.0]
│   ├── requests [required: Any, installed: 2.31.0]
│   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   └── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
│   └── tornado [required: Any, installed: 6.4]
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
├── packaging [required: Any, installed: 24.2]
├── pexpect [required: Any, installed: 4.9.0]
│   └── ptyprocess [required: >=0.5, installed: 0.7.0]
└── traitlets [required: ~=5.0, installed: 5.14.3]
lz4==4.3.3
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
│   │       ├── requests [required: Any, installed: 2.31.0]
│   │       │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │       │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │       │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │       │   └── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
│   │       └── zstandard [required: >=0.15, installed: 0.19.0]
│   ├── distro [required: >=1.5.0, installed: 1.9.0]
│   ├── frozendict [required: >=2.4.2, installed: 2.4.4]
│   ├── jsonpatch [required: >=1.32, installed: 1.33]
│   │   └── jsonpointer [required: >=1.9, installed: 2.4]
│   ├── menuinst [required: >=2, installed: 2.0.2]
│   ├── packaging [required: >=23.0, installed: 24.2]
│   ├── platformdirs [required: >=3.10.0, installed: 4.2.2]
│   ├── pluggy [required: >=1.0.0, installed: 1.5.0]
│   ├── pycosat [required: >=0.6.3, installed: 0.6.6]
│   ├── requests [required: >=2.28.0,<3, installed: 2.31.0]
│   │   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │   ├── idna [required: >=2.5,<4, installed: 3.7]
│   │   └── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
│   ├── ruamel.yaml [required: >=0.11.14,<0.19, installed: 0.18.6]
│   │   └── ruamel.yaml.clib [required: >=0.2.7, installed: 0.2.8]
│   ├── setuptools [required: >=60.0.0, installed: 69.5.1]
│   ├── tqdm [required: >=4, installed: 4.66.4]
│   ├── truststore [required: >=0.8.0, installed: 0.8.0]
│   └── zstandard [required: >=0.15, installed: 0.19.0]
└── libmambapy [required: Any, installed: 1.5.8]
munkres==1.1.4
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
│   │   └── typing_extensions [required: >=4.6, installed: 4.11.0]
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
│   ├── anyio [required: >=3.1.0, installed: 4.3.0]
│   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
│       ├── anyio [required: >=3.1.0, installed: 4.3.0]
│       │   ├── idna [required: >=2.8, installed: 3.7]
│       │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
│   ├── anyio [required: >=3.1.0, installed: 4.3.0]
│   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
notebook==7.2.0
├── jupyter_server [required: >=2.4.0,<3, installed: 2.14.0]
│   ├── anyio [required: >=3.1.0, installed: 4.3.0]
│   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
│   │   ├── anyio [required: Any, installed: 4.3.0]
│   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
│   │   │   └── typing_extensions [required: >=4.6, installed: 4.11.0]
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
│   │       ├── anyio [required: >=3.1.0, installed: 4.3.0]
│   │       │   ├── idna [required: >=2.8, installed: 3.7]
│   │       │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
│   │   ├── anyio [required: >=3.1.0, installed: 4.3.0]
│   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
│   │   │   ├── anyio [required: >=3.1.0, installed: 4.3.0]
│   │   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
│   │   └── requests [required: >=2.31, installed: 2.31.0]
│   │       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   │       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   │       ├── idna [required: >=2.5,<4, installed: 3.7]
│   │       └── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
│   ├── notebook_shim [required: >=0.2, installed: 0.2.4]
│   │   └── jupyter_server [required: >=1.8,<3, installed: 2.14.0]
│   │       ├── anyio [required: >=3.1.0, installed: 4.3.0]
│   │       │   ├── idna [required: >=2.8, installed: 3.7]
│   │       │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
│   │   ├── anyio [required: >=3.1.0, installed: 4.3.0]
│   │   │   ├── idna [required: >=2.8, installed: 3.7]
│   │   │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
│   └── requests [required: >=2.31, installed: 2.31.0]
│       ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│       ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│       ├── idna [required: >=2.5,<4, installed: 3.7]
│       └── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
├── notebook_shim [required: >=0.2,<0.3, installed: 0.2.4]
│   └── jupyter_server [required: >=1.8,<3, installed: 2.14.0]
│       ├── anyio [required: >=3.1.0, installed: 4.3.0]
│       │   ├── idna [required: >=2.8, installed: 3.7]
│       │   └── sniffio [required: >=1.1, installed: 1.3.1]
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
numba==0.59.1
├── llvmlite [required: >=0.42.0dev0,<0.43, installed: 0.42.0]
└── numpy [required: >=1.22,<1.27, installed: 1.26.4]
openpyxl==3.1.2
└── et-xmlfile [required: Any, installed: 1.1.0]
pickleshare==0.7.5
pip==25.0.1
pkgutil_resolve_name==1.3.10
protobuf==4.25.3
pyarrow-hotfix==0.6
pycurl==7.45.3
PyJWT==2.8.0
PySocks==1.7.1
PyWavelets==1.4.1
└── numpy [required: >=1.17.3, installed: 1.26.4]
requests-html==0.10.0
├── bs4 [required: Any, installed: 0.0.2]
│   └── beautifulsoup4 [required: Any, installed: 4.12.3]
│       └── soupsieve [required: >1.2, installed: 2.5]
├── fake-useragent [required: Any, installed: 2.0.3]
├── parse [required: Any, installed: 1.20.2]
├── pyppeteer [required: >=0.0.14, installed: 2.0.0]
│   ├── appdirs [required: >=1.4.3,<2.0.0, installed: 1.4.4]
│   ├── certifi [required: >=2023, installed: 2025.1.31]
│   ├── importlib_metadata [required: >=1.4, installed: 7.1.0]
│   │   └── zipp [required: >=0.5, installed: 3.17.0]
│   ├── pyee [required: >=11.0.0,<12.0.0, installed: 11.1.1]
│   │   └── typing_extensions [required: Any, installed: 4.11.0]
│   ├── tqdm [required: >=4.42.1,<5.0.0, installed: 4.66.4]
│   ├── urllib3 [required: >=1.25.8,<2.0.0, installed: 1.26.20]
│   └── websockets [required: >=10.0,<11.0, installed: 10.4]
├── pyquery [required: Any, installed: 2.0.1]
│   ├── cssselect [required: >=1.2.0, installed: 1.2.0]
│   └── lxml [required: >=2.1, installed: 5.3.1]
├── requests [required: Any, installed: 2.31.0]
│   ├── certifi [required: >=2017.4.17, installed: 2025.1.31]
│   ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
│   ├── idna [required: >=2.5,<4, installed: 3.7]
│   └── urllib3 [required: >=1.21.1,<3, installed: 1.26.20]
└── w3lib [required: Any, installed: 2.3.1]
rpy2==3.5.11
├── cffi [required: >=1.10.0, installed: 1.16.0]
│   └── pycparser [required: Any, installed: 2.22]
├── Jinja2 [required: Any, installed: 3.1.4]
│   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
├── pytz [required: Any, installed: 2024.1]
└── tzlocal [required: Any, installed: 5.2]
scikit-image==0.22.0
├── imageio [required: >=2.27, installed: 2.34.1]
│   ├── numpy [required: Any, installed: 1.26.4]
│   └── pillow [required: >=8.3.2, installed: 10.3.0]
├── lazy_loader [required: >=0.3, installed: 0.4]
│   └── packaging [required: Any, installed: 24.2]
├── networkx [required: >=2.8, installed: 3.3]
├── numpy [required: >=1.22, installed: 1.26.4]
├── packaging [required: >=21, installed: 24.2]
├── pillow [required: >=9.0.1, installed: 10.3.0]
├── scipy [required: >=1.8, installed: 1.13.0]
│   └── numpy [required: >=1.22.4,<2.3, installed: 1.26.4]
└── tifffile [required: >=2022.8.12, installed: 2024.5.10]
    └── numpy [required: Any, installed: 1.26.4]
scikit-learn==1.4.2
├── joblib [required: >=1.2.0, installed: 1.4.2]
├── numpy [required: >=1.19.5, installed: 1.26.4]
├── scipy [required: >=1.6.0, installed: 1.13.0]
│   └── numpy [required: >=1.22.4,<2.3, installed: 1.26.4]
└── threadpoolctl [required: >=2.0.0, installed: 3.5.0]
seaborn==0.13.2
├── matplotlib [required: >=3.4,!=3.6.1, installed: 3.8.4]
│   ├── contourpy [required: >=1.0.1, installed: 1.2.1]
│   │   └── numpy [required: >=1.20, installed: 1.26.4]
│   ├── cycler [required: >=0.10, installed: 0.12.1]
│   ├── fonttools [required: >=4.22.0, installed: 4.51.0]
│   ├── kiwisolver [required: >=1.3.1, installed: 1.4.5]
│   ├── numpy [required: >=1.21, installed: 1.26.4]
│   ├── packaging [required: >=20.0, installed: 24.2]
│   ├── pillow [required: >=8, installed: 10.3.0]
│   ├── pyparsing [required: >=2.3.1, installed: 3.1.2]
│   └── python-dateutil [required: >=2.7, installed: 2.9.0]
│       └── six [required: >=1.5, installed: 1.16.0]
├── numpy [required: >=1.20,!=1.24.0, installed: 1.26.4]
└── pandas [required: >=1.2, installed: 2.2.2]
    ├── numpy [required: >=1.23.2, installed: 1.26.4]
    ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
    │   └── six [required: >=1.5, installed: 1.16.0]
    ├── pytz [required: >=2020.1, installed: 2024.1]
    └── tzdata [required: >=2022.7, installed: 2024.1]
simplegeneric==0.8.1
statsmodels==0.14.2
├── numpy [required: >=1.22.3, installed: 1.26.4]
├── packaging [required: >=21.3, installed: 24.2]
├── pandas [required: >=1.4,!=2.1.0, installed: 2.2.2]
│   ├── numpy [required: >=1.23.2, installed: 1.26.4]
│   ├── python-dateutil [required: >=2.8.2, installed: 2.9.0]
│   │   └── six [required: >=1.5, installed: 1.16.0]
│   ├── pytz [required: >=2020.1, installed: 2024.1]
│   └── tzdata [required: >=2022.7, installed: 2024.1]
├── patsy [required: >=0.5.6, installed: 0.5.6]
│   ├── numpy [required: >=1.4, installed: 1.26.4]
│   └── six [required: Any, installed: 1.16.0]
└── scipy [required: >=1.8,!=1.9.2, installed: 1.13.0]
    └── numpy [required: >=1.22.4,<2.3, installed: 1.26.4]
tables==3.9.2
├── numexpr [required: >=2.6.2, installed: 2.9.0]
│   └── numpy [required: >=1.13.3, installed: 1.26.4]
├── numpy [required: >=1.19.0, installed: 1.26.4]
├── packaging [required: Any, installed: 24.2]
└── py-cpuinfo [required: Any, installed: 9.0.0]
tomli==2.0.1
torch==2.6.0
├── filelock [required: Any, installed: 3.17.0]
├── fsspec [required: Any, installed: 2024.5.0]
├── Jinja2 [required: Any, installed: 3.1.4]
│   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
├── networkx [required: Any, installed: 3.3]
├── nvidia-cublas-cu12 [required: ==12.4.5.8, installed: 12.4.5.8]
├── nvidia-cuda-cupti-cu12 [required: ==12.4.127, installed: 12.4.127]
├── nvidia-cuda-nvrtc-cu12 [required: ==12.4.127, installed: 12.4.127]
├── nvidia-cuda-runtime-cu12 [required: ==12.4.127, installed: 12.4.127]
├── nvidia-cudnn-cu12 [required: ==9.1.0.70, installed: 9.1.0.70]
│   └── nvidia-cublas-cu12 [required: Any, installed: 12.4.5.8]
├── nvidia-cufft-cu12 [required: ==11.2.1.3, installed: 11.2.1.3]
├── nvidia-curand-cu12 [required: ==10.3.5.147, installed: 10.3.5.147]
├── nvidia-cusolver-cu12 [required: ==11.6.1.9, installed: 11.6.1.9]
│   ├── nvidia-cublas-cu12 [required: Any, installed: 12.4.5.8]
│   ├── nvidia-cusparse-cu12 [required: Any, installed: 12.3.1.170]
│   │   └── nvidia-nvjitlink-cu12 [required: Any, installed: 12.4.127]
│   └── nvidia-nvjitlink-cu12 [required: Any, installed: 12.4.127]
├── nvidia-cusparse-cu12 [required: ==12.3.1.170, installed: 12.3.1.170]
│   └── nvidia-nvjitlink-cu12 [required: Any, installed: 12.4.127]
├── nvidia-cusparselt-cu12 [required: ==0.6.2, installed: 0.6.2]
├── nvidia-nccl-cu12 [required: ==2.21.5, installed: 2.21.5]
├── nvidia-nvjitlink-cu12 [required: ==12.4.127, installed: 12.4.127]
├── nvidia-nvtx-cu12 [required: ==12.4.127, installed: 12.4.127]
├── sympy [required: ==1.13.1, installed: 1.13.1]
│   └── mpmath [required: >=1.1.0,<1.4, installed: 1.3.0]
├── triton [required: ==3.2.0, installed: 3.2.0]
└── typing_extensions [required: >=4.10.0, installed: 4.11.0]
typing-utils==0.1.0
uri-template==1.3.0
webcolors==1.13
wheel==0.43.0
xlrd==2.0.1
```


### Conda packages
via `conda-tree -n base deptree --exclude conda-tree --small`
```
pip==24.0
  ├─ python 3.11.9 [required: >=3.7]
  ├─ setuptools 69.5.1 [required: any]
  │  └─ python 3.11.9 [required: >=3.8]
  └─ wheel 0.43.0 [required: any]
     └─ python 3.11.9 [required: >=3.8]
mamba==1.5.8
  ├─ conda 24.5.0 [required: >=24,<25]
  ├─ libmambapy 1.5.8 [required: 1.5.8, py311hf2555c7_0]
  │  ├─ fmt 10.2.1 [required: >=10.2.1,<11.0a0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ libgcc 14.2.0 [required: 14.2.0, h767d61c_2]
  │  │  │     ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │     └─ _openmp_mutex 4.5 [required: >=4.5]
  │  │  │        ├─ _libgcc_mutex 0.1 [required: 0.1, conda_forge]
  │  │  │        └─ llvm-openmp 18.1.5 [required: >=9.0.1]
  │  │  │           ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │           │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │           │     └─ dependencies of libgcc-ng displayed above
  │  │  │           └─ zstd 1.5.6 [required: >=1.5.6,<1.6.0a0]
  │  │  │              ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │              │  └─ dependencies of libgcc-ng displayed above
  │  │  │              ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │              └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │                 └─ dependencies of libzlib displayed above
  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libmamba 1.5.8 [required: 1.5.8, had39da4_0]
  │  │  ├─ fmt 10.2.1 [required: >=10.2.1,<11.0a0]
  │  │  │  └─ dependencies of fmt displayed above
  │  │  ├─ libarchive 3.7.2 [required: >=3.7.2,<3.8.0a0]
  │  │  │  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libxml2 2.12.7 [required: >=2.12.2,<2.13.0a0]
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
  │  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  │  └─ xz 5.2.6 [required: >=5.2.6,<6.0a0]
  │  │  │  │     └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │        └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  ├─ lz4-c 1.9.4 [required: >=1.9.3,<1.10.0a0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ lzo 2.10 [required: >=2.10,<3.0a0]
  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ openssl 3.4.1 [required: >=3.2.0,<4.0a0]
  │  │  │  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  │  │  │  ├─ ca-certificates 2025.1.31 [required: any]
  │  │  │  │  └─ libgcc 14.2.0 [required: >=13]
  │  │  │  │     └─ dependencies of libgcc displayed above
  │  │  │  ├─ xz 5.2.6 [required: >=5.2.6,<6.0a0]
  │  │  │  │  └─ dependencies of xz displayed above
  │  │  │  └─ zstd 1.5.6 [required: >=1.5.5,<1.6.0a0]
  │  │  │     └─ dependencies of zstd displayed above
  │  │  ├─ libcurl 8.7.1 [required: >=8.6.0,<9.0a0]
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
  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  ├─ openssl 3.4.1 [required: >=3.2.1,<4.0a0]
  │  │  │  │  └─ dependencies of openssl displayed above
  │  │  │  └─ zstd 1.5.6 [required: >=1.5.5,<1.6.0a0]
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
jupyter-resource-usage==1.1.1
  ├─ jupyter_server 2.14.0 [required: >=2.0.0,<3]
  │  ├─ anyio 4.3.0 [required: >=3.1.0]
  │  │  ├─ exceptiongroup 1.2.0 [required: >=1.0.2]
  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  ├─ idna 3.7 [required: >=2.8]
  │  │  │  └─ python 3.11.9 [required: >=3.6]
  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  ├─ sniffio 1.3.1 [required: >=1.1]
  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  └─ typing_extensions 4.11.0 [required: >=4.1]
  │  │     └─ python 3.11.9 [required: >=3.8]
  │  ├─ argon2-cffi 23.1.0 [required: any]
  │  │  ├─ argon2-cffi-bindings 21.2.0 [required: any]
  │  │  │  ├─ cffi 1.16.0 [required: >=1.0.1]
  │  │  │  │  ├─ libffi 3.4.2 [required: >=3.4,<4.0a0]
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=9.4.0]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ pycparser 2.22 [required: any]
  │  │  │  │  │  └─ python 3.11.9 [required: >=3.8]
  │  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  ├─ python 3.11.9 [required: >=3.7]
  │  │  └─ typing-extensions 4.11.0 [required: any]
  │  │     └─ typing_extensions 4.11.0 [required: 4.11.0, pyha770c72_0]
  │  │        └─ dependencies of typing_extensions displayed above
  │  ├─ jinja2 3.1.4 [required: any]
  │  │  ├─ markupsafe 2.1.5 [required: >=2.0]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  └─ python 3.11.9 [required: >=3.7]
  │  ├─ jupyter_client 8.6.1 [required: >=7.4.4]
  │  │  ├─ importlib_metadata 7.1.0 [required: >=4.8.3]
  │  │  │  └─ importlib-metadata 7.1.0 [required: >=7.1.0,<7.1.1.0a0]
  │  │  │     ├─ python 3.11.9 [required: >=3.8]
  │  │  │     └─ zipp 3.17.0 [required: >=0.5]
  │  │  │        └─ python 3.11.9 [required: >=3.8]
  │  │  ├─ jupyter_core 5.7.2 [required: >=4.12,!=5.0.*]
  │  │  │  ├─ platformdirs 4.2.2 [required: >=2.5]
  │  │  │  │  └─ python 3.11.9 [required: >=3.8]
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  └─ traitlets 5.14.3 [required: >=5.3]
  │  │  │     └─ python 3.11.9 [required: >=3.8]
  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  ├─ python-dateutil 2.9.0 [required: >=2.8.2]
  │  │  │  ├─ python 3.11.9 [required: >=3.7]
  │  │  │  └─ six 1.16.0 [required: >=1.5]
  │  │  │     └─ python 3.11.9 [required: any]
  │  │  ├─ pyzmq 26.0.3 [required: >=23.0]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libsodium 1.0.18 [required: >=1.0.18,<1.0.19.0a0]
  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=7.5.0]
  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  └─ zeromq 4.3.5 [required: >=4.3.5,<4.4.0a0]
  │  │  │     ├─ krb5 1.21.2 [required: >=1.21.2,<1.22.0a0]
  │  │  │     │  └─ dependencies of krb5 displayed above
  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │     ├─ libsodium 1.0.18 [required: >=1.0.18,<1.0.19.0a0]
  │  │  │     │  └─ dependencies of libsodium displayed above
  │  │  │     └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ tornado 6.4 [required: >=6.2]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  └─ traitlets 5.14.3 [required: >=5.3]
  │  │     └─ dependencies of traitlets displayed above
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
  │  │  │  │  ├─ attrs 23.2.0 [required: >=22.2.0]
  │  │  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  │  │  ├─ importlib_resources 6.4.0 [required: >=1.4.0]
  │  │  │  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  │  │  │  └─ zipp 3.17.0 [required: >=3.1.0]
  │  │  │  │  │     └─ dependencies of zipp displayed above
  │  │  │  │  ├─ jsonschema-specifications 2023.12.1 [required: >=2023.03.6]
  │  │  │  │  │  ├─ importlib_resources 6.4.0 [required: >=1.4.0]
  │  │  │  │  │  │  └─ dependencies of importlib_resources displayed above
  │  │  │  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  │  │  │  └─ referencing 0.35.1 [required: >=0.31.0]
  │  │  │  │  │     ├─ attrs 23.2.0 [required: >=22.2.0]
  │  │  │  │  │     │  └─ dependencies of attrs displayed above
  │  │  │  │  │     ├─ python 3.11.9 [required: >=3.8]
  │  │  │  │  │     └─ rpds-py 0.18.1 [required: >=0.7.0]
  │  │  │  │  │        ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │        │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │        ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  │  │        └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  │  ├─ pkgutil-resolve-name 1.3.10 [required: >=1.3.10]
  │  │  │  │  │  └─ python 3.11.9 [required: >=3.6]
  │  │  │  │  ├─ python 3.11.9 [required: >=3.8]
  │  │  │  │  ├─ referencing 0.35.1 [required: >=0.28.4]
  │  │  │  │  │  └─ dependencies of referencing displayed above
  │  │  │  │  └─ rpds-py 0.18.1 [required: >=0.7.1]
  │  │  │  │     └─ dependencies of rpds-py displayed above
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
  │  │  │  └─ python 3.11.9 [required: >=3.6]
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
  │  │     │  └─ python 3.11.9 [required: any]
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
  │  │  │  │  └─ python 3.11.9 [required: >=3.8]
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
  │  │  │  │  └─ python 3.11.9 [required: >=3.8]
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
  │  │  └─ python 3.11.9 [required: >=3.8]
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
  ├─ psutil 5.9.8 [required: >=5.6.0,<6]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  ├─ python 3.11.9 [required: >=3.9]
  └─ pyzmq 26.0.3 [required: >=19]
     └─ dependencies of pyzmq displayed above
r-randomforest==4.7_1.1
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libgfortran-ng 13.2.0 [required: any]
  │  └─ libgfortran5 13.2.0 [required: 13.2.0, hca663fb_7]
  │     └─ libgcc-ng 14.2.0 [required: >=13.2.0]
  │        └─ dependencies of libgcc-ng displayed above
  ├─ libgfortran5 13.2.0 [required: >=12.3.0]
  │  └─ dependencies of libgfortran5 displayed above
  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
     ├─ _openmp_mutex 4.5 [required: >=4.5]
     │  └─ dependencies of _openmp_mutex displayed above
     ├─ _r-mutex 1.0.1 [required: 1.*, anacondar_1]
     ├─ bwidget 1.9.14 [required: any]
     │  └─ tk 8.6.13 [required: any]
     │     ├─ libgcc-ng 14.2.0 [required: >=12]
     │     │  └─ dependencies of libgcc-ng displayed above
     │     └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
     │        └─ dependencies of libzlib displayed above
     ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
     │  └─ dependencies of bzip2 displayed above
     ├─ cairo 1.18.0 [required: >=1.18.0,<2.0a0]
     │  ├─ fontconfig 2.14.2 [required: >=2.14.2,<3.0a0]
     │  │  ├─ expat 2.6.2 [required: >=2.5.0,<3.0a0]
     │  │  │  ├─ libexpat 2.6.2 [required: 2.6.2, h59595ed_0]
     │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  │     └─ dependencies of libgcc-ng displayed above
     │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │     └─ dependencies of libgcc-ng displayed above
     │  │  ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
     │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  │  ├─ libpng 1.6.43 [required: >=1.6.39,<1.7.0a0]
     │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  │  │  └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
     │  │  │  │     └─ dependencies of libzlib displayed above
     │  │  │  └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
     │  │  │     └─ dependencies of libzlib displayed above
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  ├─ libuuid 2.38.1 [required: >=2.32.1,<3.0a0]
     │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │     └─ dependencies of libgcc-ng displayed above
     │  │  └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
     │  │     └─ dependencies of libzlib displayed above
     │  ├─ fonts-conda-ecosystem 1 [required: any]
     │  │  └─ fonts-conda-forge 1 [required: any]
     │  │     ├─ font-ttf-dejavu-sans-mono 2.37 [required: any]
     │  │     ├─ font-ttf-inconsolata 3.000 [required: any]
     │  │     ├─ font-ttf-source-code-pro 2.038 [required: any]
     │  │     └─ font-ttf-ubuntu 0.83 [required: any]
     │  ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
     │  │  └─ dependencies of freetype displayed above
     │  ├─ icu 73.2 [required: >=73.2,<74.0a0]
     │  │  └─ dependencies of icu displayed above
     │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  └─ dependencies of libgcc-ng displayed above
     │  ├─ libglib 2.80.2 [required: >=2.78.0,<3.0a0]
     │  │  ├─ libffi 3.4.2 [required: >=3.4,<4.0a0]
     │  │  │  └─ dependencies of libffi displayed above
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  ├─ libiconv 1.17 [required: >=1.17,<2.0a0]
     │  │  │  └─ dependencies of libiconv displayed above
     │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
     │  │  │  └─ dependencies of libzlib displayed above
     │  │  └─ pcre2 10.43 [required: >=10.43,<10.44.0a0]
     │  │     ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
     │  │     │  └─ dependencies of bzip2 displayed above
     │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │     │  └─ dependencies of libgcc-ng displayed above
     │  │     └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
     │  │        └─ dependencies of libzlib displayed above
     │  ├─ libpng 1.6.43 [required: >=1.6.39,<1.7.0a0]
     │  │  └─ dependencies of libpng displayed above
     │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
     │  ├─ libxcb 1.15 [required: >=1.15,<1.16.0a0]
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  ├─ pthread-stubs 0.4 [required: any]
     │  │  │  └─ libgcc-ng 14.2.0 [required: >=7.5.0]
     │  │  │     └─ dependencies of libgcc-ng displayed above
     │  │  ├─ xorg-libxau 1.0.11 [required: any]
     │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │     └─ dependencies of libgcc-ng displayed above
     │  │  └─ xorg-libxdmcp 1.1.3 [required: any]
     │  │     └─ libgcc-ng 14.2.0 [required: >=9.3.0]
     │  │        └─ dependencies of libgcc-ng displayed above
     │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
     │  │  └─ dependencies of libzlib displayed above
     │  ├─ pixman 0.43.2 [required: >=0.42.2,<1.0a0]
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
     │  ├─ xorg-libice 1.1.1 [required: >=1.1.1,<2.0a0]
     │  │  └─ libgcc-ng 14.2.0 [required: >=12]
     │  │     └─ dependencies of libgcc-ng displayed above
     │  ├─ xorg-libsm 1.2.4 [required: >=1.2.4,<2.0a0]
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  ├─ libuuid 2.38.1 [required: >=2.38.1,<3.0a0]
     │  │  │  └─ dependencies of libuuid displayed above
     │  │  └─ xorg-libice 1.1.1 [required: >=1.1.1,<2.0a0]
     │  │     └─ dependencies of xorg-libice displayed above
     │  ├─ xorg-libx11 1.8.9 [required: >=1.8.6,<2.0a0]
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  ├─ libxcb 1.15 [required: >=1.15,<1.16.0a0]
     │  │  │  └─ dependencies of libxcb displayed above
     │  │  ├─ xorg-kbproto 1.0.7 [required: any]
     │  │  │  └─ libgcc-ng 14.2.0 [required: >=9.3.0]
     │  │  │     └─ dependencies of libgcc-ng displayed above
     │  │  ├─ xorg-xextproto 7.3.0 [required: >=7.3.0,<8.0a0]
     │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │     └─ dependencies of libgcc-ng displayed above
     │  │  └─ xorg-xproto 7.0.31 [required: any]
     │  │     └─ libgcc-ng 14.2.0 [required: >=9.3.0]
     │  │        └─ dependencies of libgcc-ng displayed above
     │  ├─ xorg-libxext 1.3.4 [required: >=1.3.4,<2.0a0]
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  ├─ xorg-libx11 1.8.9 [required: >=1.7.2,<2.0a0]
     │  │  │  └─ dependencies of xorg-libx11 displayed above
     │  │  └─ xorg-xextproto 7.3.0 [required: any]
     │  │     └─ dependencies of xorg-xextproto displayed above
     │  ├─ xorg-libxrender 0.9.11 [required: >=0.9.11,<0.10.0a0]
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  ├─ xorg-libx11 1.8.9 [required: >=1.8.6,<2.0a0]
     │  │  │  └─ dependencies of xorg-libx11 displayed above
     │  │  └─ xorg-renderproto 0.11.1 [required: any]
     │  │     └─ libgcc-ng 14.2.0 [required: >=9.3.0]
     │  │        └─ dependencies of libgcc-ng displayed above
     │  └─ zlib 1.2.13 [required: any]
     │     ├─ libgcc-ng 14.2.0 [required: >=12]
     │     │  └─ dependencies of libgcc-ng displayed above
     │     └─ libzlib 1.2.13 [required: 1.2.13, hd590300_5]
     │        └─ dependencies of libzlib displayed above
     ├─ curl 8.7.1 [required: any]
     │  ├─ krb5 1.21.2 [required: >=1.21.2,<1.22.0a0]
     │  │  └─ dependencies of krb5 displayed above
     │  ├─ libcurl 8.7.1 [required: 8.7.1, hca28451_0]
     │  │  └─ dependencies of libcurl displayed above
     │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  └─ dependencies of libgcc-ng displayed above
     │  ├─ libssh2 1.11.0 [required: >=1.11.0,<2.0a0]
     │  │  └─ dependencies of libssh2 displayed above
     │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
     │  │  └─ dependencies of libzlib displayed above
     │  ├─ openssl 3.4.1 [required: >=3.2.1,<4.0a0]
     │  │  └─ dependencies of openssl displayed above
     │  └─ zstd 1.5.6 [required: >=1.5.5,<1.6.0a0]
     │     └─ dependencies of zstd displayed above
     ├─ gcc_impl_linux-64 13.2.0 [required: >=10]
     │  ├─ binutils_impl_linux-64 2.40 [required: >=2.40]
     │  │  ├─ ld_impl_linux-64 2.40 [required: 2.40, h55db66e_0]
     │  │  └─ sysroot_linux-64 2.12 [required: any]
     │  │     └─ kernel-headers_linux-64 2.6.32 [required: 2.6.32, he073ed8_17]
     │  ├─ libgcc-devel_linux-64 13.2.0 [required: 13.2.0, hceb6213_107]
     │  ├─ libgcc-ng 14.2.0 [required: >=13.2.0]
     │  │  └─ dependencies of libgcc-ng displayed above
     │  ├─ libgomp 14.2.0 [required: >=13.2.0]
     │  │  └─ __glibc [required: >=2.17,<3.0.a0]
     │  ├─ libsanitizer 13.2.0 [required: 13.2.0, h6ddb7a1_7]
     │  │  └─ libgcc-ng 14.2.0 [required: >=13.2.0]
     │  │     └─ dependencies of libgcc-ng displayed above
     │  ├─ libstdcxx-ng 13.2.0 [required: >=13.2.0]
     │  └─ sysroot_linux-64 2.12 [required: any]
     │     └─ dependencies of sysroot_linux-64 displayed above
     ├─ gfortran_impl_linux-64 13.2.0 [required: any]
     │  ├─ gcc_impl_linux-64 13.2.0 [required: >=13.2.0]
     │  │  └─ dependencies of gcc_impl_linux-64 displayed above
     │  ├─ libgcc-ng 14.2.0 [required: >=4.9]
     │  │  └─ dependencies of libgcc-ng displayed above
     │  ├─ libgfortran5 13.2.0 [required: >=13.2.0]
     │  │  └─ dependencies of libgfortran5 displayed above
     │  ├─ libstdcxx-ng 13.2.0 [required: >=4.9]
     │  └─ sysroot_linux-64 2.12 [required: any]
     │     └─ dependencies of sysroot_linux-64 displayed above
     ├─ gxx_impl_linux-64 13.2.0 [required: >=10]
     │  ├─ gcc_impl_linux-64 13.2.0 [required: 13.2.0, h9eb54c0_7]
     │  │  └─ dependencies of gcc_impl_linux-64 displayed above
     │  ├─ libstdcxx-devel_linux-64 13.2.0 [required: 13.2.0, hceb6213_107]
     │  └─ sysroot_linux-64 2.12 [required: any]
     │     └─ dependencies of sysroot_linux-64 displayed above
     ├─ icu 73.2 [required: >=73.2,<74.0a0]
     │  └─ dependencies of icu displayed above
     ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
     │  └─ libopenblas 0.3.27 [required: >=0.3.27,<1.0a0]
     │     ├─ libgcc-ng 14.2.0 [required: >=12]
     │     │  └─ dependencies of libgcc-ng displayed above
     │     ├─ libgfortran-ng 13.2.0 [required: any]
     │     │  └─ dependencies of libgfortran-ng displayed above
     │     └─ libgfortran5 13.2.0 [required: >=12.3.0]
     │        └─ dependencies of libgfortran5 displayed above
     ├─ libcurl 8.7.1 [required: >=8.7.1,<9.0a0]
     │  └─ dependencies of libcurl displayed above
     ├─ libgcc-ng 14.2.0 [required: >=12]
     │  └─ dependencies of libgcc-ng displayed above
     ├─ libgfortran-ng 13.2.0 [required: any]
     │  └─ dependencies of libgfortran-ng displayed above
     ├─ libgfortran5 13.2.0 [required: >=10.4.0]
     │  └─ dependencies of libgfortran5 displayed above
     ├─ libglib 2.80.2 [required: >=2.80.0,<3.0a0]
     │  └─ dependencies of libglib displayed above
     ├─ libiconv 1.17 [required: >=1.17,<2.0a0]
     │  └─ dependencies of libiconv displayed above
     ├─ libjpeg-turbo 3.0.0 [required: >=3.0.0,<4.0a0]
     │  └─ libgcc-ng 14.2.0 [required: >=12]
     │     └─ dependencies of libgcc-ng displayed above
     ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
     │  └─ libblas 3.9.0 [required: 3.9.0, 22_linux64_openblas]
     │     └─ dependencies of libblas displayed above
     ├─ libpng 1.6.43 [required: >=1.6.43,<1.7.0a0]
     │  └─ dependencies of libpng displayed above
     ├─ libstdcxx-ng 13.2.0 [required: >=12]
     ├─ libtiff 4.6.0 [required: >=4.6.0,<4.7.0a0]
     │  ├─ lerc 4.0.0 [required: >=4.0.0,<5.0a0]
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
     │  ├─ libdeflate 1.20 [required: >=1.20,<1.21.0a0]
     │  │  └─ libgcc-ng 14.2.0 [required: >=12]
     │  │     └─ dependencies of libgcc-ng displayed above
     │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  └─ dependencies of libgcc-ng displayed above
     │  ├─ libjpeg-turbo 3.0.0 [required: >=3.0.0,<4.0a0]
     │  │  └─ dependencies of libjpeg-turbo displayed above
     │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
     │  ├─ libwebp-base 1.4.0 [required: >=1.3.2,<2.0a0]
     │  │  └─ libgcc-ng 14.2.0 [required: >=12]
     │  │     └─ dependencies of libgcc-ng displayed above
     │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
     │  │  └─ dependencies of libzlib displayed above
     │  ├─ xz 5.2.6 [required: >=5.2.6,<6.0a0]
     │  │  └─ dependencies of xz displayed above
     │  └─ zstd 1.5.6 [required: >=1.5.5,<1.6.0a0]
     │     └─ dependencies of zstd displayed above
     ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
     │  └─ dependencies of libzlib displayed above
     ├─ make 4.3 [required: any]
     │  └─ libgcc-ng 14.2.0 [required: >=7.5.0]
     │     └─ dependencies of libgcc-ng displayed above
     ├─ pango 1.52.2 [required: >=1.50.14,<2.0a0]
     │  ├─ cairo 1.18.0 [required: >=1.18.0,<2.0a0]
     │  │  └─ dependencies of cairo displayed above
     │  ├─ fontconfig 2.14.2 [required: >=2.14.2,<3.0a0]
     │  │  └─ dependencies of fontconfig displayed above
     │  ├─ fonts-conda-ecosystem 1 [required: any]
     │  │  └─ dependencies of fonts-conda-ecosystem displayed above
     │  ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
     │  │  └─ dependencies of freetype displayed above
     │  ├─ fribidi 1.0.10 [required: >=1.0.10,<2.0a0]
     │  │  └─ libgcc-ng 14.2.0 [required: >=7.5.0]
     │  │     └─ dependencies of libgcc-ng displayed above
     │  ├─ harfbuzz 8.5.0 [required: >=8.3.0,<9.0a0]
     │  │  ├─ cairo 1.18.0 [required: >=1.18.0,<2.0a0]
     │  │  │  └─ dependencies of cairo displayed above
     │  │  ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
     │  │  │  └─ dependencies of freetype displayed above
     │  │  ├─ graphite2 1.3.13 [required: any]
     │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
     │  │  ├─ icu 73.2 [required: >=73.2,<74.0a0]
     │  │  │  └─ dependencies of icu displayed above
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  ├─ libglib 2.80.2 [required: >=2.80.2,<3.0a0]
     │  │  │  └─ dependencies of libglib displayed above
     │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
     │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  └─ dependencies of libgcc-ng displayed above
     │  ├─ libglib 2.80.2 [required: >=2.80.0,<3.0a0]
     │  │  └─ dependencies of libglib displayed above
     │  └─ libpng 1.6.43 [required: >=1.6.43,<1.7.0a0]
     │     └─ dependencies of libpng displayed above
     ├─ pcre2 10.43 [required: >=10.43,<10.44.0a0]
     │  └─ dependencies of pcre2 displayed above
     ├─ readline 8.2 [required: >=8.2,<9.0a0]
     │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  └─ dependencies of libgcc-ng displayed above
     │  └─ ncurses 6.5 [required: >=6.3,<7.0a0]
     │     └─ dependencies of ncurses displayed above
     ├─ sed 4.8 [required: any]
     │  └─ libgcc-ng 14.2.0 [required: >=7.5.0]
     │     └─ dependencies of libgcc-ng displayed above
     ├─ tk 8.6.13 [required: >=8.6.13,<8.7.0a0]
     │  └─ dependencies of tk displayed above
     ├─ tktable 2.10 [required: any]
     │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  └─ dependencies of libgcc-ng displayed above
     │  └─ tk 8.6.13 [required: >=8.6.13,<8.7.0a0]
     │     └─ dependencies of tk displayed above
     ├─ xorg-libxt 1.3.0 [required: any]
     │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  └─ dependencies of libgcc-ng displayed above
     │  ├─ xorg-kbproto 1.0.7 [required: any]
     │  │  └─ dependencies of xorg-kbproto displayed above
     │  ├─ xorg-libice 1.1.1 [required: >=1.1.1,<2.0a0]
     │  │  └─ dependencies of xorg-libice displayed above
     │  ├─ xorg-libsm 1.2.4 [required: >=1.2.4,<2.0a0]
     │  │  └─ dependencies of xorg-libsm displayed above
     │  ├─ xorg-libx11 1.8.9 [required: >=1.8.6,<2.0a0]
     │  │  └─ dependencies of xorg-libx11 displayed above
     │  └─ xorg-xproto 7.0.31 [required: any]
     │     └─ dependencies of xorg-xproto displayed above
     └─ xz 5.2.6 [required: >=5.2.6,<6.0a0]
        └─ dependencies of xz displayed above
rpy2==3.5.11
  ├─ cffi 1.16.0 [required: >=1.10.0,!=1.13.0]
  │  └─ dependencies of cffi displayed above
  ├─ jinja2 3.1.4 [required: any]
  │  └─ dependencies of jinja2 displayed above
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  ├─ pytz 2024.1 [required: any]
  │  └─ python 3.11.9 [required: >=3.7]
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ simplegeneric 0.8.1 [required: any]
  │  └─ python 3.11.9 [required: any]
  └─ tzlocal 5.2 [required: any]
     ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
     └─ python_abi 3.11 [required: 3.11.*, *_cp311]
r-forecast==8.22.0
  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  └─ dependencies of libblas displayed above
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-colorspace 2.1_0 [required: any]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-fracdiff 1.5_3 [required: any]
  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ dependencies of libblas displayed above
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-generics 0.1.3 [required: >=0.1.2]
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-ggplot2 3.5.1 [required: >=2.2.1]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-cli 3.6.2 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-glue 1.7.0 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-gtable 0.3.5 [required: >=0.1.1]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.2 [required: any]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-glue 1.7.0 [required: any]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-cli 3.6.2 [required: >=3.4.0]
  │  │  │  │  └─ dependencies of r-cli displayed above
  │  │  │  ├─ r-glue 1.7.0 [required: any]
  │  │  │  │  └─ dependencies of r-glue displayed above
  │  │  │  └─ r-rlang 1.1.3 [required: >=1.0.6]
  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │        └─ dependencies of r-base displayed above
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
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
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
  │  │  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  │  └─ dependencies of libblas displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  │  └─ dependencies of liblapack displayed above
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-lattice 0.22_6 [required: any]
  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │        └─ dependencies of r-base displayed above
  │  │  └─ r-nlme 3.1_164 [required: >=3.1_64]
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     ├─ libgfortran-ng 13.2.0 [required: any]
  │  │     │  └─ dependencies of libgfortran-ng displayed above
  │  │     ├─ libgfortran5 13.2.0 [required: >=12.3.0]
  │  │     │  └─ dependencies of libgfortran5 displayed above
  │  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     │  └─ dependencies of r-base displayed above
  │  │     └─ r-lattice 0.22_6 [required: any]
  │  │        └─ dependencies of r-lattice displayed above
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
  │  │  │     └─ dependencies of r-colorspace displayed above
  │  │  ├─ r-r6 2.5.1 [required: any]
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
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
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-pillar 1.9.0 [required: >=1.8.1]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-cli 3.6.2 [required: any]
  │  │  │  │  └─ dependencies of r-cli displayed above
  │  │  │  ├─ r-crayon 1.5.2 [required: >=1.3.4]
  │  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  └─ r-rlang 1.1.3 [required: >=0.3.0]
  │  │  │  │     └─ dependencies of r-rlang displayed above
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
  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     │  └─ dependencies of r-base displayed above
  │  │  │     ├─ r-cli 3.6.2 [required: >=3.4.0]
  │  │  │     │  └─ dependencies of r-cli displayed above
  │  │  │     ├─ r-glue 1.7.0 [required: any]
  │  │  │     │  └─ dependencies of r-glue displayed above
  │  │  │     ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  │     │  └─ dependencies of r-lifecycle displayed above
  │  │  │     └─ r-rlang 1.1.3 [required: >=1.0.6]
  │  │  │        └─ dependencies of r-rlang displayed above
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
  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │        └─ dependencies of r-base displayed above
  ├─ r-lmtest 0.9_40 [required: any]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libgfortran-ng 13.2.0 [required: any]
  │  │  └─ dependencies of libgfortran-ng displayed above
  │  ├─ libgfortran5 13.2.0 [required: >=12.3.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-zoo 1.8_12 [required: any]
  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  └─ dependencies of libgcc-ng displayed above
  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     └─ r-lattice 0.22_6 [required: >=0.20_27]
  │        └─ dependencies of r-lattice displayed above
  ├─ r-magrittr 2.0.3 [required: any]
  │  └─ dependencies of r-magrittr displayed above
  ├─ r-nnet 7.3_19 [required: any]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-mass 7.3_60 [required: any]
  │     └─ dependencies of r-mass displayed above
  ├─ r-rcpp 1.0.12 [required: >=0.11.0]
  │  ├─ __glibc [required: >=2.17,<3.0.a0]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
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
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-tseries 0.10_56 [required: any]
  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  └─ dependencies of libblas displayed above
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libgfortran-ng 13.2.0 [required: any]
  │  │  └─ dependencies of libgfortran-ng displayed above
  │  ├─ libgfortran5 13.2.0 [required: >=12.3.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-quadprog 1.5_8 [required: any]
  │  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  └─ dependencies of libblas displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libgfortran-ng 13.2.0 [required: any]
  │  │  │  └─ dependencies of libgfortran-ng displayed above
  │  │  ├─ libgfortran5 13.2.0 [required: >=12.3.0]
  │  │  │  └─ dependencies of libgfortran5 displayed above
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-quantmod 0.4.26 [required: >=0.4_9]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-curl 5.1.0 [required: any]
  │  │  │  ├─ libcurl 8.7.1 [required: >=8.3.0,<9.0a0]
  │  │  │  │  └─ dependencies of libcurl displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-jsonlite 1.8.8 [required: >=1.1]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-ttr 0.24.4 [required: >=0.2]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-curl 5.1.0 [required: any]
  │  │  │  │  └─ dependencies of r-curl displayed above
  │  │  │  ├─ r-xts 0.13.2 [required: >=0.10_0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  └─ r-zoo 1.8_12 [required: >=1.7_12]
  │  │  │  │     └─ dependencies of r-zoo displayed above
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
  │  ├─ libgfortran-ng 13.2.0 [required: any]
  │  │  └─ dependencies of libgfortran-ng displayed above
  │  ├─ libgfortran5 13.2.0 [required: >=12.3.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-nlme 3.1_164 [required: any]
  │     └─ dependencies of r-nlme displayed above
  └─ r-zoo 1.8_12 [required: any]
     └─ dependencies of r-zoo displayed above
r-hexbin==1.28.3
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libgfortran-ng 13.2.0 [required: any]
  │  └─ dependencies of libgfortran-ng displayed above
  ├─ libgfortran5 13.2.0 [required: >=12.3.0]
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
r-tidymodels==1.2.0
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-broom 1.0.6 [required: >=1.0.0]
  │  ├─ r-backports 1.4.1 [required: any]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-dplyr 1.1.4 [required: >=1.0.0]
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
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-cli 3.6.2 [required: >=3.3.0]
  │  │  │  │  └─ dependencies of r-cli displayed above
  │  │  │  ├─ r-glue 1.7.0 [required: >=1.3.0]
  │  │  │  │  └─ dependencies of r-glue displayed above
  │  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  │  ├─ r-rlang 1.1.3 [required: >=1.0.4]
  │  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  │  ├─ r-vctrs 0.6.5 [required: >=0.5.2]
  │  │  │  │  └─ dependencies of r-vctrs displayed above
  │  │  │  └─ r-withr 3.0.0 [required: any]
  │  │  │     └─ dependencies of r-withr displayed above
  │  │  └─ r-vctrs 0.6.5 [required: >=0.3.5]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  └─ dependencies of r-ellipsis displayed above
  │  ├─ r-generics 0.1.3 [required: >=0.0.2]
  │  │  └─ dependencies of r-generics displayed above
  │  ├─ r-ggplot2 3.5.1 [required: any]
  │  │  └─ dependencies of r-ggplot2 displayed above
  │  ├─ r-glue 1.7.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-purrr 1.0.2 [required: any]
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
  │  ├─ r-rlang 1.1.3 [required: any]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-stringr 1.5.1 [required: any]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.2 [required: any]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-glue 1.7.0 [required: >=1.6.1]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │  │  │  └─ dependencies of r-lifecycle displayed above
  │  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  │  └─ dependencies of r-magrittr displayed above
  │  │  ├─ r-rlang 1.1.3 [required: >=1.0.0]
  │  │  │  └─ dependencies of r-rlang displayed above
  │  │  ├─ r-stringi 1.8.4 [required: >=1.5.3]
  │  │  │  ├─ icu 73.2 [required: >=73.2,<74.0a0]
  │  │  │  │  └─ dependencies of icu displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  └─ r-vctrs 0.6.5 [required: any]
  │  │     └─ dependencies of r-vctrs displayed above
  │  ├─ r-tibble 3.2.1 [required: >=3.0.0]
  │  │  └─ dependencies of r-tibble displayed above
  │  └─ r-tidyr 1.3.1 [required: >=1.0.0]
  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  └─ dependencies of libgcc-ng displayed above
  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     ├─ r-cli 3.6.2 [required: >=3.4.1]
  │     │  └─ dependencies of r-cli displayed above
  │     ├─ r-dplyr 1.1.4 [required: >=1.0.10]
  │     │  └─ dependencies of r-dplyr displayed above
  │     ├─ r-glue 1.7.0 [required: any]
  │     │  └─ dependencies of r-glue displayed above
  │     ├─ r-lifecycle 1.0.4 [required: >=1.0.3]
  │     │  └─ dependencies of r-lifecycle displayed above
  │     ├─ r-magrittr 2.0.3 [required: any]
  │     │  └─ dependencies of r-magrittr displayed above
  │     ├─ r-purrr 1.0.2 [required: >=1.0.1]
  │     │  └─ dependencies of r-purrr displayed above
  │     ├─ r-rlang 1.1.3 [required: >=1.0.4]
  │     │  └─ dependencies of r-rlang displayed above
  │     ├─ r-stringr 1.5.1 [required: >=1.5.0]
  │     │  └─ dependencies of r-stringr displayed above
  │     ├─ r-tibble 3.2.1 [required: >=2.1.1]
  │     │  └─ dependencies of r-tibble displayed above
  │     ├─ r-tidyselect 1.2.1 [required: >=1.2.0]
  │     │  └─ dependencies of r-tidyselect displayed above
  │     └─ r-vctrs 0.6.5 [required: >=0.5.2]
  │        └─ dependencies of r-vctrs displayed above
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
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  └─ r-codetools 0.2_20 [required: any]
  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │        └─ dependencies of r-base displayed above
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
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
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
  │  │  └─ dependencies of r-dplyr displayed above
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
  │  │  └─ dependencies of r-hardhat displayed above
  │  ├─ r-ipred 0.9_14 [required: >=0.9_12]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-class 7.3_22 [required: any]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-mass 7.3_60 [required: any]
  │  │  │     └─ dependencies of r-mass displayed above
  │  │  ├─ r-mass 7.3_60 [required: any]
  │  │  │  └─ dependencies of r-mass displayed above
  │  │  ├─ r-nnet 7.3_19 [required: any]
  │  │  │  └─ dependencies of r-nnet displayed above
  │  │  ├─ r-prodlim 2023.08.28 [required: any]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-data.table 1.15.2 [required: any]
  │  │  │  │  ├─ _openmp_mutex 4.5 [required: >=4.5]
  │  │  │  │  │  └─ dependencies of _openmp_mutex displayed above
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  ├─ r-diagram 1.6.5 [required: any]
  │  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  └─ r-shape 1.4.6.1 [required: any]
  │  │  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │        └─ dependencies of r-base displayed above
  │  │  │  ├─ r-kernsmooth 2.23_24 [required: any]
  │  │  │  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  │  │  └─ dependencies of libblas displayed above
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libgfortran-ng 13.2.0 [required: any]
  │  │  │  │  │  └─ dependencies of libgfortran-ng displayed above
  │  │  │  │  ├─ libgfortran5 13.2.0 [required: >=12.3.0]
  │  │  │  │  │  └─ dependencies of libgfortran5 displayed above
  │  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
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
  │  │  │  │  │  │  │  └─ dependencies of r-globals displayed above
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
  │  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │     │  └─ dependencies of r-base displayed above
  │  │  │  │     └─ r-matrix 1.6_5 [required: any]
  │  │  │  │        └─ dependencies of r-matrix displayed above
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
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-rlang 1.1.3 [required: >=1.0.3]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-tidyr 1.3.1 [required: >=1.0.0]
  │  │  └─ dependencies of r-tidyr displayed above
  │  ├─ r-tidyselect 1.2.1 [required: >=1.2.0]
  │  │  └─ dependencies of r-tidyselect displayed above
  │  ├─ r-timedate 4032.109 [required: any]
  │  │  └─ dependencies of r-timedate displayed above
  │  ├─ r-vctrs 0.6.5 [required: >=0.5.0]
  │  │  └─ dependencies of r-vctrs displayed above
  │  └─ r-withr 3.0.0 [required: any]
  │     └─ dependencies of r-withr displayed above
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
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
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
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-codetools 0.2_20 [required: any]
  │  │  │  │  └─ dependencies of r-codetools displayed above
  │  │  │  └─ r-iterators 1.0.14 [required: any]
  │  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │        └─ dependencies of r-base displayed above
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
  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │        └─ dependencies of r-base displayed above
  ├─ r-ellipsis 0.3.2 [required: >=0.3.2]
  │  └─ dependencies of r-ellipsis displayed above
  ├─ r-fs 1.6.4 [required: >=1.5.2]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     └─ dependencies of r-base displayed above
  ├─ r-lifecycle 1.0.4 [required: >=1.0.1]
  │  └─ dependencies of r-lifecycle displayed above
  ├─ r-memoise 2.0.1 [required: >=2.0.1]
  │  └─ dependencies of r-memoise displayed above
  ├─ r-miniui 0.1.1.1 [required: >=0.1.1.1]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-htmltools 0.5.8.1 [required: >=0.3]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-base64enc 0.1_3 [required: any]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  ├─ r-digest 0.6.35 [required: any]
  │  │  │  └─ dependencies of r-digest displayed above
  │  │  ├─ r-ellipsis 0.3.2 [required: any]
  │  │  │  └─ dependencies of r-ellipsis displayed above
  │  │  ├─ r-fastmap 1.2.0 [required: >=1.1.0]
  │  │  │  └─ dependencies of r-fastmap displayed above
  │  │  └─ r-rlang 1.1.3 [required: >=0.4.10]
  │  │     └─ dependencies of r-rlang displayed above
  │  └─ r-shiny 1.8.1.1 [required: >=0.13]
  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     ├─ r-bslib 0.7.0 [required: >=0.3.0]
  │     │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  │  └─ dependencies of r-base displayed above
  │     │  ├─ r-base64enc 0.1_3 [required: any]
  │     │  │  └─ dependencies of r-base64enc displayed above
  │     │  ├─ r-cachem 1.1.0 [required: any]
  │     │  │  └─ dependencies of r-cachem displayed above
  │     │  ├─ r-htmltools 0.5.8.1 [required: >=0.5.7]
  │     │  │  └─ dependencies of r-htmltools displayed above
  │     │  ├─ r-jquerylib 0.1.4 [required: >=0.1.3]
  │     │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  │  │  └─ dependencies of r-base displayed above
  │     │  │  └─ r-htmltools 0.5.8.1 [required: any]
  │     │  │     └─ dependencies of r-htmltools displayed above
  │     │  ├─ r-jsonlite 1.8.8 [required: any]
  │     │  │  └─ dependencies of r-jsonlite displayed above
  │     │  ├─ r-lifecycle 1.0.4 [required: any]
  │     │  │  └─ dependencies of r-lifecycle displayed above
  │     │  ├─ r-memoise 2.0.1 [required: >=2.0.1]
  │     │  │  └─ dependencies of r-memoise displayed above
  │     │  ├─ r-mime 0.12 [required: any]
  │     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  │  │  └─ dependencies of libgcc-ng displayed above
  │     │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  │     └─ dependencies of r-base displayed above
  │     │  ├─ r-rlang 1.1.3 [required: any]
  │     │  │  └─ dependencies of r-rlang displayed above
  │     │  └─ r-sass 0.4.9 [required: >=0.4.0]
  │     │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │     │  └─ dependencies of libgcc-ng displayed above
  │     │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │     │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │     │  └─ dependencies of r-base displayed above
  │     │     ├─ r-digest 0.6.35 [required: any]
  │     │     │  └─ dependencies of r-digest displayed above
  │     │     ├─ r-fs 1.6.4 [required: any]
  │     │     │  └─ dependencies of r-fs displayed above
  │     │     ├─ r-htmltools 0.5.8.1 [required: any]
  │     │     │  └─ dependencies of r-htmltools displayed above
  │     │     ├─ r-r6 2.5.1 [required: any]
  │     │     │  └─ dependencies of r-r6 displayed above
  │     │     ├─ r-rappdirs 0.3.3 [required: any]
  │     │     │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │     │  │  └─ dependencies of libgcc-ng displayed above
  │     │     │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │     │     └─ dependencies of r-base displayed above
  │     │     └─ r-rlang 1.1.3 [required: any]
  │     │        └─ dependencies of r-rlang displayed above
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
  │     │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  │  └─ dependencies of r-base displayed above
  │     │  ├─ r-htmltools 0.5.8.1 [required: >=0.5.1.1]
  │     │  │  └─ dependencies of r-htmltools displayed above
  │     │  └─ r-rlang 1.1.3 [required: >=0.4.10]
  │     │     └─ dependencies of r-rlang displayed above
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
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-processx 3.8.4 [required: >=3.4.0]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-ps 1.7.6 [required: >=1.2.0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │     └─ dependencies of r-base displayed above
  │  │  │  └─ r-r6 2.5.1 [required: any]
  │  │  │     └─ dependencies of r-r6 displayed above
  │  │  └─ r-r6 2.5.1 [required: any]
  │  │     └─ dependencies of r-r6 displayed above
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
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
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
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │        └─ dependencies of r-base displayed above
  │  ├─ r-fs 1.6.4 [required: >=1.4.0]
  │  │  └─ dependencies of r-fs displayed above
  │  ├─ r-httr 1.4.7 [required: >=1.4.2]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-curl 5.1.0 [required: >=0.9.1]
  │  │  │  └─ dependencies of r-curl displayed above
  │  │  ├─ r-jsonlite 1.8.8 [required: any]
  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  ├─ r-mime 0.12 [required: any]
  │  │  │  └─ dependencies of r-mime displayed above
  │  │  ├─ r-openssl 2.2.0 [required: >=0.8]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  │  └─ dependencies of openssl displayed above
  │  │  │  ├─ r-askpass 1.2.0 [required: any]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  └─ r-sys 3.4.2 [required: >=2.1]
  │  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │        └─ dependencies of r-base displayed above
  │  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │     └─ dependencies of r-base displayed above
  │  │  └─ r-r6 2.5.1 [required: any]
  │  │     └─ dependencies of r-r6 displayed above
  │  ├─ r-jsonlite 1.8.8 [required: any]
  │  │  └─ dependencies of r-jsonlite displayed above
  │  ├─ r-magrittr 2.0.3 [required: any]
  │  │  └─ dependencies of r-magrittr displayed above
  │  ├─ r-memoise 2.0.1 [required: any]
  │  │  └─ dependencies of r-memoise displayed above
  │  ├─ r-purrr 1.0.2 [required: any]
  │  │  └─ dependencies of r-purrr displayed above
  │  ├─ r-ragg 1.3.2 [required: any]
  │  │  ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
  │  │  │  └─ dependencies of freetype displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libjpeg-turbo 3.0.0 [required: >=3.0.0,<4.0a0]
  │  │  │  └─ dependencies of libjpeg-turbo displayed above
  │  │  ├─ libpng 1.6.43 [required: >=1.6.43,<1.7.0a0]
  │  │  │  └─ dependencies of libpng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libtiff 4.6.0 [required: >=4.6.0,<4.7.0a0]
  │  │  │  └─ dependencies of libtiff displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-systemfonts 1.0.5 [required: >=1.0.3]
  │  │  │  ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
  │  │  │  │  └─ dependencies of freetype displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-cpp11 0.4.7 [required: any]
  │  │  │     └─ dependencies of r-cpp11 displayed above
  │  │  └─ r-textshaping 0.3.7 [required: >=0.3.0]
  │  │     ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
  │  │     │  └─ dependencies of freetype displayed above
  │  │     ├─ fribidi 1.0.10 [required: >=1.0.10,<2.0a0]
  │  │     │  └─ dependencies of fribidi displayed above
  │  │     ├─ harfbuzz 8.5.0 [required: >=8.2.1,<9.0a0]
  │  │     │  └─ dependencies of harfbuzz displayed above
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     │  └─ dependencies of r-base displayed above
  │  │     ├─ r-cpp11 0.4.7 [required: >=0.2.1]
  │  │     │  └─ dependencies of r-cpp11 displayed above
  │  │     └─ r-systemfonts 1.0.5 [required: >=1.0.0]
  │  │        └─ dependencies of r-systemfonts displayed above
  │  ├─ r-rlang 1.1.3 [required: >=0.4.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-rmarkdown 2.27 [required: >=1.1.9007]
  │  │  ├─ pandoc 3.2 [required: >=1.14]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-bslib 0.7.0 [required: >=0.2.5.1]
  │  │  │  └─ dependencies of r-bslib displayed above
  │  │  ├─ r-evaluate 0.23 [required: >=0.13]
  │  │  │  └─ dependencies of r-evaluate displayed above
  │  │  ├─ r-fontawesome 0.5.2 [required: >=0.5.0]
  │  │  │  └─ dependencies of r-fontawesome displayed above
  │  │  ├─ r-htmltools 0.5.8.1 [required: >=0.5.1]
  │  │  │  └─ dependencies of r-htmltools displayed above
  │  │  ├─ r-jquerylib 0.1.4 [required: any]
  │  │  │  └─ dependencies of r-jquerylib displayed above
  │  │  ├─ r-jsonlite 1.8.8 [required: any]
  │  │  │  └─ dependencies of r-jsonlite displayed above
  │  │  ├─ r-knitr 1.46 [required: >=1.22]
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  ├─ r-evaluate 0.23 [required: >=0.15]
  │  │  │  │  └─ dependencies of r-evaluate displayed above
  │  │  │  ├─ r-highr 0.10 [required: any]
  │  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  │  └─ r-xfun 0.44 [required: >=0.18]
  │  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │        └─ dependencies of r-base displayed above
  │  │  │  ├─ r-xfun 0.44 [required: >=0.43]
  │  │  │  │  └─ dependencies of r-xfun displayed above
  │  │  │  └─ r-yaml 2.3.8 [required: >=2.1.19]
  │  │  │     └─ dependencies of r-yaml displayed above
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
  │  ├─ r-tibble 3.2.1 [required: any]
  │  │  └─ dependencies of r-tibble displayed above
  │  ├─ r-whisker 0.4.1 [required: any]
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
  │  ├─ r-withr 3.0.0 [required: any]
  │  │  └─ dependencies of r-withr displayed above
  │  ├─ r-xml2 1.3.6 [required: >=1.3.1]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libxml2 2.12.7 [required: >=2.12.3,<3.0.0a0]
  │  │  │  └─ dependencies of libxml2 displayed above
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.2 [required: any]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  └─ r-rlang 1.1.3 [required: >=1.1.0]
  │  │     └─ dependencies of r-rlang displayed above
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
  │  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  │  └─ dependencies of r-base displayed above
  │  │  │  └─ r-tibble 3.2.1 [required: any]
  │  │  │     └─ dependencies of r-tibble displayed above
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
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
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
r-irkernel==1.3.2
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-crayon 1.5.2 [required: any]
  │  └─ dependencies of r-crayon displayed above
  ├─ r-digest 0.6.35 [required: any]
  │  └─ dependencies of r-digest displayed above
  ├─ r-evaluate 0.23 [required: >=0.10]
  │  └─ dependencies of r-evaluate displayed above
  ├─ r-irdisplay 1.1 [required: >=0.3.0.9999]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  └─ r-repr 1.1.7 [required: any]
  │     ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │     │  └─ dependencies of r-base displayed above
  │     ├─ r-base64enc 0.1_3 [required: any]
  │     │  └─ dependencies of r-base64enc displayed above
  │     ├─ r-htmltools 0.5.8.1 [required: any]
  │     │  └─ dependencies of r-htmltools displayed above
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
  │     └─ dependencies of zeromq displayed above
  ├─ r-repr 1.1.7 [required: >=0.4.99]
  │  └─ dependencies of r-repr displayed above
  └─ r-uuid 1.2_0 [required: any]
     ├─ libgcc-ng 14.2.0 [required: >=12]
     │  └─ dependencies of libgcc-ng displayed above
     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
        └─ dependencies of r-base displayed above
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
  │  │  └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │     └─ dependencies of r-base displayed above
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
  │  │  └─ dependencies of r-curl displayed above
  │  ├─ r-gargle 1.5.2 [required: >=0.3.1]
  │  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  │  └─ dependencies of r-base displayed above
  │  │  ├─ r-cli 3.6.2 [required: >=3.0.0]
  │  │  │  └─ dependencies of r-cli displayed above
  │  │  ├─ r-fs 1.6.4 [required: >=1.3.1]
  │  │  │  └─ dependencies of r-fs displayed above
  │  │  ├─ r-glue 1.7.0 [required: >=1.3.0]
  │  │  │  └─ dependencies of r-glue displayed above
  │  │  ├─ r-httr 1.4.7 [required: >=1.4.0]
  │  │  │  └─ dependencies of r-httr displayed above
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
  │  │  └─ dependencies of r-rematch2 displayed above
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
  │  │  │  └─ dependencies of r-clipr displayed above
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
  │  └─ dependencies of r-ragg displayed above
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
  │  │  └─ dependencies of r-callr displayed above
  │  ├─ r-cli 3.6.2 [required: >=3.2.0]
  │  │  └─ dependencies of r-cli displayed above
  │  ├─ r-clipr 0.8.0 [required: >=0.4.0]
  │  │  └─ dependencies of r-clipr displayed above
  │  ├─ r-fs 1.6.4 [required: any]
  │  │  └─ dependencies of r-fs displayed above
  │  ├─ r-glue 1.7.0 [required: any]
  │  │  └─ dependencies of r-glue displayed above
  │  ├─ r-knitr 1.46 [required: >=1.23]
  │  │  └─ dependencies of r-knitr displayed above
  │  ├─ r-lifecycle 1.0.4 [required: any]
  │  │  └─ dependencies of r-lifecycle displayed above
  │  ├─ r-rlang 1.1.3 [required: >=1.0.0]
  │  │  └─ dependencies of r-rlang displayed above
  │  ├─ r-rmarkdown 2.27 [required: any]
  │  │  └─ dependencies of r-rmarkdown displayed above
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
  │     └─ dependencies of r-xml2 displayed above
  ├─ r-stringr 1.5.1 [required: >=1.5.0]
  │  └─ dependencies of r-stringr displayed above
  ├─ r-tibble 3.2.1 [required: >=3.1.8]
  │  └─ dependencies of r-tibble displayed above
  ├─ r-tidyr 1.3.1 [required: >=1.3.0]
  │  └─ dependencies of r-tidyr displayed above
  └─ r-xml2 1.3.6 [required: >=1.3.3]
     └─ dependencies of r-xml2 displayed above
r-caret==6.0_94
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  └─ dependencies of r-base displayed above
  ├─ r-e1071 1.7_14 [required: any]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │  │  └─ dependencies of r-base displayed above
  │  ├─ r-class 7.3_22 [required: any]
  │  │  └─ dependencies of r-class displayed above
  │  └─ r-proxy 0.4_27 [required: any]
  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  └─ dependencies of libgcc-ng displayed above
  │     └─ r-base 4.3.3 [required: >=4.3,<4.4.0a0]
  │        └─ dependencies of r-base displayed above
  ├─ r-foreach 1.5.2 [required: any]
  │  └─ dependencies of r-foreach displayed above
  ├─ r-ggplot2 3.5.1 [required: any]
  │  └─ dependencies of r-ggplot2 displayed above
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
  │  │  └─ dependencies of r-data.table displayed above
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
  │  └─ dependencies of r-recipes displayed above
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
r-rcurl==1.98_1.14
  ├─ libcurl 8.7.1 [required: >=8.5.0,<9.0a0]
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
jupyter-pluto-proxy==0.1.2
  ├─ jupyter-server-proxy 4.1.2 [required: >=1.5.0]
  │  ├─ aiohttp 3.9.5 [required: any]
  │  │  ├─ aiosignal 1.3.1 [required: >=1.1.2]
  │  │  │  ├─ frozenlist 1.4.1 [required: >=1.1.0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  ├─ attrs 23.2.0 [required: >=17.3.0]
  │  │  │  └─ dependencies of attrs displayed above
  │  │  ├─ frozenlist 1.4.1 [required: >=1.1.1]
  │  │  │  └─ dependencies of frozenlist displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ multidict 6.0.5 [required: >=4.5,<7.0]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  └─ yarl 1.9.4 [required: >=1.0,<2.0]
  │  │     ├─ idna 3.7 [required: >=2.0]
  │  │     │  └─ dependencies of idna displayed above
  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │     ├─ multidict 6.0.5 [required: >=4.0]
  │  │     │  └─ dependencies of multidict displayed above
  │  │     ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │     └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  ├─ importlib_metadata 7.1.0 [required: >=4.8.3]
  │  │  └─ dependencies of importlib_metadata displayed above
  │  ├─ jupyter_server 2.14.0 [required: >=1.0]
  │  │  └─ dependencies of jupyter_server displayed above
  │  ├─ python 3.11.9 [required: >=3.8]
  │  ├─ simpervisor 1.0.0 [required: >=1.0]
  │  │  └─ python 3.11.9 [required: >=3.8]
  │  ├─ tornado 6.4 [required: >=5.1]
  │  │  └─ dependencies of tornado displayed above
  │  └─ traitlets 5.14.3 [required: >=4.2.1]
  │     └─ dependencies of traitlets displayed above
  └─ python 3.11.9 [required: >=3.7]
seaborn==0.13.2
  ├─ seaborn-base 0.13.2 [required: 0.13.2, pyhd8ed1ab_2]
  │  ├─ matplotlib-base 3.8.4 [required: >=3.4,!=3.6.1]
  │  │  ├─ certifi 2025.1.31 [required: >=2020.06.20]
  │  │  │  └─ python 3.11.9 [required: >=3.9]
  │  │  ├─ contourpy 1.2.1 [required: >=1.0.1]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ numpy 1.26.4 [required: >=1.20]
  │  │  │  │  ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  │  │  └─ dependencies of libblas displayed above
  │  │  │  │  ├─ libcblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  │  │  └─ libblas 3.9.0 [required: 3.9.0, 22_linux64_openblas]
  │  │  │  │  │     └─ dependencies of libblas displayed above
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
  │  │  │  │  │  └─ dependencies of liblapack displayed above
  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  ├─ cycler 0.12.1 [required: >=0.10]
  │  │  │  └─ python 3.11.9 [required: >=3.8]
  │  │  ├─ fonttools 4.51.0 [required: >=4.22.0]
  │  │  │  ├─ brotli 1.1.0 [required: any]
  │  │  │  │  ├─ brotli-bin 1.1.0 [required: 1.1.0, hd590300_1]
  │  │  │  │  │  ├─ libbrotlidec 1.1.0 [required: 1.1.0, hd590300_1]
  │  │  │  │  │  │  ├─ libbrotlicommon 1.1.0 [required: 1.1.0, hd590300_1]
  │  │  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  ├─ libbrotlienc 1.1.0 [required: 1.1.0, hd590300_1]
  │  │  │  │  │  │  ├─ libbrotlicommon 1.1.0 [required: 1.1.0, hd590300_1]
  │  │  │  │  │  │  │  └─ dependencies of libbrotlicommon displayed above
  │  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libbrotlidec 1.1.0 [required: 1.1.0, hd590300_1]
  │  │  │  │  │  └─ dependencies of libbrotlidec displayed above
  │  │  │  │  ├─ libbrotlienc 1.1.0 [required: 1.1.0, hd590300_1]
  │  │  │  │  │  └─ dependencies of libbrotlienc displayed above
  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ munkres 1.1.4 [required: any]
  │  │  │  │  └─ python 3.11.9 [required: any]
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
  │  │  │  └─ dependencies of freetype displayed above
  │  │  ├─ kiwisolver 1.4.5 [required: >=1.3.1]
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ numpy 1.26.4 [required: >=1.21]
  │  │  │  └─ dependencies of numpy displayed above
  │  │  ├─ packaging 24.0 [required: >=20.0]
  │  │  │  └─ dependencies of packaging displayed above
  │  │  ├─ pillow 10.3.0 [required: >=8]
  │  │  │  ├─ freetype 2.12.1 [required: >=2.12.1,<3.0a0]
  │  │  │  │  └─ dependencies of freetype displayed above
  │  │  │  ├─ lcms2 2.16 [required: >=2.16,<3.0a0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libjpeg-turbo 3.0.0 [required: >=3.0.0,<4.0a0]
  │  │  │  │  │  └─ dependencies of libjpeg-turbo displayed above
  │  │  │  │  └─ libtiff 4.6.0 [required: >=4.6.0,<4.7.0a0]
  │  │  │  │     └─ dependencies of libtiff displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libjpeg-turbo 3.0.0 [required: >=3.0.0,<4.0a0]
  │  │  │  │  └─ dependencies of libjpeg-turbo displayed above
  │  │  │  ├─ libtiff 4.6.0 [required: >=4.6.0,<4.7.0a0]
  │  │  │  │  └─ dependencies of libtiff displayed above
  │  │  │  ├─ libwebp-base 1.4.0 [required: >=1.3.2,<2.0a0]
  │  │  │  │  └─ dependencies of libwebp-base displayed above
  │  │  │  ├─ libxcb 1.15 [required: >=1.15,<1.16.0a0]
  │  │  │  │  └─ dependencies of libxcb displayed above
  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  ├─ openjpeg 2.5.2 [required: >=2.5.2,<3.0a0]
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libpng 1.6.43 [required: >=1.6.43,<1.7.0a0]
  │  │  │  │  │  └─ dependencies of libpng displayed above
  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  ├─ libtiff 4.6.0 [required: >=4.6.0,<4.7.0a0]
  │  │  │  │  │  └─ dependencies of libtiff displayed above
  │  │  │  │  └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │     └─ dependencies of libzlib displayed above
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  │  └─ tk 8.6.13 [required: >=8.6.13,<8.7.0a0]
  │  │  │     └─ dependencies of tk displayed above
  │  │  ├─ pyparsing 3.1.2 [required: >=2.3.1]
  │  │  │  └─ python 3.11.9 [required: >=3.6]
  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  ├─ python-dateutil 2.9.0 [required: >=2.7]
  │  │  │  └─ dependencies of python-dateutil displayed above
  │  │  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  └─ tk 8.6.13 [required: >=8.6.13,<8.7.0a0]
  │  │     └─ dependencies of tk displayed above
  │  ├─ numpy 1.26.4 [required: >=1.20,!=1.24.0]
  │  │  └─ dependencies of numpy displayed above
  │  ├─ pandas 2.2.2 [required: >=1.2]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ numpy 1.26.4 [required: >=1.19,<3]
  │  │  │  └─ dependencies of numpy displayed above
  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  ├─ python-dateutil 2.9.0 [required: >=2.8.1]
  │  │  │  └─ dependencies of python-dateutil displayed above
  │  │  ├─ python-tzdata 2024.1 [required: >=2022a]
  │  │  │  └─ python 3.11.9 [required: >=3.6]
  │  │  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  └─ pytz 2024.1 [required: >=2020.1]
  │  │     └─ dependencies of pytz displayed above
  │  ├─ python 3.11.9 [required: >=3.8]
  │  └─ scipy 1.13.0 [required: >=1.7]
  │     ├─ libblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │     │  └─ dependencies of libblas displayed above
  │     ├─ libcblas 3.9.0 [required: >=3.9.0,<4.0a0]
  │     │  └─ dependencies of libcblas displayed above
  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  └─ dependencies of libgcc-ng displayed above
  │     ├─ libgfortran-ng 13.2.0 [required: any]
  │     │  └─ dependencies of libgfortran-ng displayed above
  │     ├─ libgfortran5 13.2.0 [required: >=12.3.0]
  │     │  └─ dependencies of libgfortran5 displayed above
  │     ├─ liblapack 3.9.0 [required: >=3.9.0,<4.0a0]
  │     │  └─ dependencies of liblapack displayed above
  │     ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │     ├─ numpy 1.26.4 [required: >=1.19,<3]
  │     │  └─ dependencies of numpy displayed above
  │     ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │     └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  └─ statsmodels 0.14.2 [required: >=0.12]
     ├─ libgcc-ng 14.2.0 [required: >=12]
     │  └─ dependencies of libgcc-ng displayed above
     ├─ numpy 1.26.4 [required: >=1.19,<3]
     │  └─ dependencies of numpy displayed above
     ├─ packaging 24.0 [required: >=21.3]
     │  └─ dependencies of packaging displayed above
     ├─ pandas 2.2.2 [required: >=1.4,!=2.1.0]
     │  └─ dependencies of pandas displayed above
     ├─ patsy 0.5.6 [required: >=0.5.6]
     │  ├─ numpy 1.26.4 [required: >=1.4.0]
     │  │  └─ dependencies of numpy displayed above
     │  ├─ python 3.11.9 [required: >=3.6]
     │  └─ six 1.16.0 [required: any]
     │     └─ dependencies of six displayed above
     ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
     ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
     └─ scipy 1.13.0 [required: >=1.8,!=1.9.2]
        └─ dependencies of scipy displayed above
openpyxl==3.1.2
  ├─ et_xmlfile 1.1.0 [required: any]
  │  └─ python 3.11.9 [required: >=3.6]
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
sympy==1.12
  ├─ __unix [required: any]
  ├─ gmpy2 2.1.5 [required: >=2.0.8]
  │  ├─ gmp 6.3.0 [required: >=6.3.0,<7.0a0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ mpc 1.3.1 [required: >=1.3.1,<2.0a0]
  │  │  ├─ gmp 6.3.0 [required: >=6.2.1,<7.0a0]
  │  │  │  └─ dependencies of gmp displayed above
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ mpfr 4.2.1 [required: >=4.1.0,<5.0a0]
  │  │     ├─ gmp 6.3.0 [required: >=6.3.0,<7.0a0]
  │  │     │  └─ dependencies of gmp displayed above
  │  │     └─ libgcc-ng 14.2.0 [required: >=12]
  │  │        └─ dependencies of libgcc-ng displayed above
  │  ├─ mpfr 4.2.1 [required: >=4.2.1,<5.0a0]
  │  │  └─ dependencies of mpfr displayed above
  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  ├─ mpmath 1.3.0 [required: >=0.19]
  │  └─ python 3.11.9 [required: >=3.6]
  └─ python 3.11.9 [required: >=3.8]
numba==0.59.1
  ├─ _openmp_mutex 4.5 [required: >=4.5]
  │  └─ dependencies of _openmp_mutex displayed above
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  ├─ llvmlite 0.42.0 [required: >=0.42.0,<0.43.0a0]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libllvm14 14.0.6 [required: >=14.0.6,<14.1.0a0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │     └─ dependencies of libzlib displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  └─ dependencies of libzlib displayed above
  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  ├─ numpy 1.26.4 [required: >=1.23.5,<2.0a0]
  │  └─ dependencies of numpy displayed above
  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
altair==5.3.0
  ├─ importlib-metadata 7.1.0 [required: any]
  │  └─ dependencies of importlib-metadata displayed above
  ├─ jinja2 3.1.4 [required: any]
  │  └─ dependencies of jinja2 displayed above
  ├─ jsonschema 4.22.0 [required: >=3.0]
  │  └─ dependencies of jsonschema displayed above
  ├─ numpy 1.26.4 [required: any]
  │  └─ dependencies of numpy displayed above
  ├─ packaging 24.0 [required: any]
  │  └─ dependencies of packaging displayed above
  ├─ pandas 2.2.2 [required: >=0.25]
  │  └─ dependencies of pandas displayed above
  ├─ python 3.11.9 [required: >=3.8]
  ├─ toolz 0.12.1 [required: any]
  │  └─ python 3.11.9 [required: >=3.7]
  └─ typing-extensions 4.11.0 [required: >=4.0.1]
     └─ dependencies of typing-extensions displayed above
blas==2.122
  ├─ _openmp_mutex 4.5 [required: >=4.5]
  │  └─ dependencies of _openmp_mutex displayed above
  ├─ blas-devel 3.9.0 [required: 3.9.0, 22_linux64_openblas]
  │  ├─ libblas 3.9.0 [required: 3.9.0, 22_linux64_openblas]
  │  │  └─ dependencies of libblas displayed above
  │  ├─ libcblas 3.9.0 [required: 3.9.0, 22_linux64_openblas]
  │  │  └─ dependencies of libcblas displayed above
  │  ├─ liblapack 3.9.0 [required: 3.9.0, 22_linux64_openblas]
  │  │  └─ dependencies of liblapack displayed above
  │  ├─ liblapacke 3.9.0 [required: 3.9.0, 22_linux64_openblas]
  │  │  ├─ libblas 3.9.0 [required: 3.9.0, 22_linux64_openblas]
  │  │  │  └─ dependencies of libblas displayed above
  │  │  ├─ libcblas 3.9.0 [required: 3.9.0, 22_linux64_openblas]
  │  │  │  └─ dependencies of libcblas displayed above
  │  │  └─ liblapack 3.9.0 [required: 3.9.0, 22_linux64_openblas]
  │  │     └─ dependencies of liblapack displayed above
  │  └─ openblas 0.3.27 [required: 0.3.27.*]
  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │     │  └─ dependencies of libgcc-ng displayed above
  │     ├─ libgfortran-ng 13.2.0 [required: any]
  │     │  └─ dependencies of libgfortran-ng displayed above
  │     ├─ libgfortran5 13.2.0 [required: >=12.3.0]
  │     │  └─ dependencies of libgfortran5 displayed above
  │     └─ libopenblas 0.3.27 [required: 0.3.27, pthreads_h413a1c8_0]
  │        └─ dependencies of libopenblas displayed above
  ├─ libblas 3.9.0 [required: 3.9.0, 22_linux64_openblas]
  │  └─ dependencies of libblas displayed above
  ├─ libcblas 3.9.0 [required: 3.9.0, 22_linux64_openblas]
  │  └─ dependencies of libcblas displayed above
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libgfortran-ng 13.2.0 [required: any]
  │  └─ dependencies of libgfortran-ng displayed above
  ├─ libgfortran5 13.2.0 [required: >=12.3.0]
  │  └─ dependencies of libgfortran5 displayed above
  ├─ liblapack 3.9.0 [required: 3.9.0, 22_linux64_openblas]
  │  └─ dependencies of liblapack displayed above
  ├─ liblapacke 3.9.0 [required: 3.9.0, 22_linux64_openblas]
  │  └─ dependencies of liblapacke displayed above
  └─ llvm-openmp 18.1.5 [required: >=18.1.2]
     └─ dependencies of llvm-openmp displayed above
h5py==3.11.0
  ├─ cached-property 1.5.2 [required: any]
  │  └─ dependencies of cached-property displayed above
  ├─ hdf5 1.14.3 [required: >=1.14.3,<1.14.4.0a0]
  │  ├─ libaec 1.1.3 [required: >=1.1.3,<2.0a0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ libcurl 8.7.1 [required: >=8.7.1,<9.0a0]
  │  │  └─ dependencies of libcurl displayed above
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libgfortran-ng 13.2.0 [required: any]
  │  │  └─ dependencies of libgfortran-ng displayed above
  │  ├─ libgfortran5 13.2.0 [required: >=12.3.0]
  │  │  └─ dependencies of libgfortran5 displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  └─ dependencies of libzlib displayed above
  │  └─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │     └─ dependencies of openssl displayed above
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ numpy 1.26.4 [required: >=1.19,<3]
  │  └─ dependencies of numpy displayed above
  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
protobuf==4.25.3
  ├─ libabseil 20240116.2 [required: >=20240116.1,<20240117.0a0]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libprotobuf 4.25.3 [required: >=4.25.3,<4.25.4.0a0]
  │  ├─ libabseil 20240116.2 [required: >=20240116.1,<20240117.0a0]
  │  │  └─ dependencies of libabseil displayed above
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  └─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │     └─ dependencies of libzlib displayed above
  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  └─ setuptools 69.5.1 [required: any]
     └─ dependencies of setuptools displayed above
scikit-image==0.22.0
  ├─ imageio 2.34.1 [required: >=2.27]
  │  ├─ numpy 1.26.4 [required: any]
  │  │  └─ dependencies of numpy displayed above
  │  ├─ pillow 10.3.0 [required: >=8.3.2]
  │  │  └─ dependencies of pillow displayed above
  │  └─ python 3.11.9 [required: >=3]
  ├─ lazy_loader 0.4 [required: >=0.2]
  │  ├─ importlib-metadata 7.1.0 [required: any]
  │  │  └─ dependencies of importlib-metadata displayed above
  │  ├─ packaging 24.0 [required: any]
  │  │  └─ dependencies of packaging displayed above
  │  └─ python 3.11.9 [required: >=3.7]
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  ├─ networkx 3.3 [required: >=2.8]
  │  └─ python 3.11.9 [required: >=3.10]
  ├─ numpy 1.26.4 [required: >=1.23.5,<2.0a0]
  │  └─ dependencies of numpy displayed above
  ├─ packaging 24.0 [required: >=21]
  │  └─ dependencies of packaging displayed above
  ├─ pillow 10.3.0 [required: >=9.0.1]
  │  └─ dependencies of pillow displayed above
  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  ├─ pywavelets 1.4.1 [required: >=1.1.1]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ numpy 1.26.4 [required: >=1.23.5,<2.0a0]
  │  │  └─ dependencies of numpy displayed above
  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  ├─ scipy 1.13.0 [required: >=1.8]
  │  └─ dependencies of scipy displayed above
  └─ tifffile 2024.5.10 [required: >=2022.8.12]
     ├─ imagecodecs 2024.1.1 [required: >=2023.8.12]
     │  ├─ blosc 1.21.5 [required: >=1.21.5,<2.0a0]
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
     │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
     │  │  │  └─ dependencies of libzlib displayed above
     │  │  ├─ lz4-c 1.9.4 [required: >=1.9.3,<1.10.0a0]
     │  │  │  └─ dependencies of lz4-c displayed above
     │  │  ├─ snappy 1.2.0 [required: >=1.2.0,<1.3.0a0]
     │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
     │  │  └─ zstd 1.5.6 [required: >=1.5.5,<1.6.0a0]
     │  │     └─ dependencies of zstd displayed above
     │  ├─ brunsli 0.1 [required: >=0.1,<1.0a0]
     │  │  ├─ brotli 1.1.0 [required: >=1.0.9,<2.0a0]
     │  │  │  └─ dependencies of brotli displayed above
     │  │  ├─ libgcc-ng 14.2.0 [required: >=9.3.0]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  └─ libstdcxx-ng 13.2.0 [required: >=9.3.0]
     │  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
     │  │  └─ dependencies of bzip2 displayed above
     │  ├─ c-blosc2 2.14.4 [required: >=2.14.4,<2.15.0a0]
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
     │  │  ├─ lz4-c 1.9.4 [required: >=1.9.3,<1.10.0a0]
     │  │  │  └─ dependencies of lz4-c displayed above
     │  │  ├─ zlib-ng 2.0.7 [required: >=2.0.7,<2.1.0a0]
     │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │     └─ dependencies of libgcc-ng displayed above
     │  │  └─ zstd 1.5.6 [required: >=1.5.5,<1.6.0a0]
     │  │     └─ dependencies of zstd displayed above
     │  ├─ charls 2.4.2 [required: >=2.4.2,<2.5.0a0]
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
     │  ├─ giflib 5.2.2 [required: >=5.2.2,<5.3.0a0]
     │  │  └─ libgcc-ng 14.2.0 [required: >=12]
     │  │     └─ dependencies of libgcc-ng displayed above
     │  ├─ jxrlib 1.1 [required: >=1.1,<1.2.0a0]
     │  │  └─ libgcc-ng 14.2.0 [required: >=12]
     │  │     └─ dependencies of libgcc-ng displayed above
     │  ├─ lcms2 2.16 [required: >=2.16,<3.0a0]
     │  │  └─ dependencies of lcms2 displayed above
     │  ├─ lerc 4.0.0 [required: >=4.0.0,<5.0a0]
     │  │  └─ dependencies of lerc displayed above
     │  ├─ libaec 1.1.3 [required: >=1.1.3,<2.0a0]
     │  │  └─ dependencies of libaec displayed above
     │  ├─ libavif16 1.0.4 [required: >=1.0.1,<2.0a0]
     │  │  ├─ aom 3.9.0 [required: >=3.9.0,<3.10.0a0]
     │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
     │  │  ├─ dav1d 1.2.1 [required: >=1.2.1,<1.2.2.0a0]
     │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │     └─ dependencies of libgcc-ng displayed above
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  ├─ rav1e 0.6.6 [required: >=0.6.6,<1.0a0]
     │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │     └─ dependencies of libgcc-ng displayed above
     │  │  └─ svt-av1 2.1.0 [required: >=2.1.0,<2.1.1.0a0]
     │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │     │  └─ dependencies of libgcc-ng displayed above
     │  │     └─ libstdcxx-ng 13.2.0 [required: >=12]
     │  ├─ libbrotlicommon 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  └─ dependencies of libbrotlicommon displayed above
     │  ├─ libbrotlidec 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  └─ dependencies of libbrotlidec displayed above
     │  ├─ libbrotlienc 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  └─ dependencies of libbrotlienc displayed above
     │  ├─ libdeflate 1.20 [required: >=1.20,<1.21.0a0]
     │  │  └─ dependencies of libdeflate displayed above
     │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  └─ dependencies of libgcc-ng displayed above
     │  ├─ libjpeg-turbo 3.0.0 [required: >=3.0.0,<4.0a0]
     │  │  └─ dependencies of libjpeg-turbo displayed above
     │  ├─ libjxl 0.10.2 [required: >=0.10,<0.11.0a0]
     │  │  ├─ libbrotlidec 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  │  └─ dependencies of libbrotlidec displayed above
     │  │  ├─ libbrotlienc 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  │  └─ dependencies of libbrotlienc displayed above
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  ├─ libhwy 1.1.0 [required: >=1.1.0,<1.2.0a0]
     │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
     │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
     │  ├─ libpng 1.6.43 [required: >=1.6.43,<1.7.0a0]
     │  │  └─ dependencies of libpng displayed above
     │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
     │  ├─ libtiff 4.6.0 [required: >=4.6.0,<4.7.0a0]
     │  │  └─ dependencies of libtiff displayed above
     │  ├─ libwebp-base 1.4.0 [required: >=1.3.2,<2.0a0]
     │  │  └─ dependencies of libwebp-base displayed above
     │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
     │  │  └─ dependencies of libzlib displayed above
     │  ├─ libzopfli 1.0.3 [required: >=1.0.3,<1.1.0a0]
     │  │  ├─ libgcc-ng 14.2.0 [required: >=9.3.0]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  └─ libstdcxx-ng 13.2.0 [required: >=9.3.0]
     │  ├─ lz4-c 1.9.4 [required: >=1.9.3,<1.10.0a0]
     │  │  └─ dependencies of lz4-c displayed above
     │  ├─ numpy 1.26.4 [required: >=1.23.5,<2.0a0]
     │  │  └─ dependencies of numpy displayed above
     │  ├─ openjpeg 2.5.2 [required: >=2.5.2,<3.0a0]
     │  │  └─ dependencies of openjpeg displayed above
     │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
     │  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
     │  ├─ snappy 1.2.0 [required: >=1.2.0,<1.3.0a0]
     │  │  └─ dependencies of snappy displayed above
     │  ├─ xz 5.2.6 [required: >=5.2.6,<6.0a0]
     │  │  └─ dependencies of xz displayed above
     │  ├─ zfp 1.0.1 [required: >=1.0.1,<2.0a0]
     │  │  ├─ _openmp_mutex 4.5 [required: >=4.5]
     │  │  │  └─ dependencies of _openmp_mutex displayed above
     │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
     │  │  │  └─ dependencies of libgcc-ng displayed above
     │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
     │  └─ zstd 1.5.6 [required: >=1.5.5,<1.6.0a0]
     │     └─ dependencies of zstd displayed above
     ├─ numpy 1.26.4 [required: >=1.19.2]
     │  └─ dependencies of numpy displayed above
     └─ python 3.11.9 [required: >=3.9]
ipympl==0.9.4
  ├─ ipython 8.24.0 [required: <9]
  │  ├─ __unix [required: any]
  │  ├─ decorator 5.1.1 [required: any]
  │  │  └─ python 3.11.9 [required: >=3.5]
  │  ├─ exceptiongroup 1.2.0 [required: any]
  │  │  └─ dependencies of exceptiongroup displayed above
  │  ├─ jedi 0.19.1 [required: >=0.16]
  │  │  ├─ parso 0.8.4 [required: >=0.8.3,<0.9.0]
  │  │  │  └─ python 3.11.9 [required: >=3.6]
  │  │  └─ python 3.11.9 [required: >=3.6]
  │  ├─ matplotlib-inline 0.1.7 [required: any]
  │  │  ├─ python 3.11.9 [required: >=3.6]
  │  │  └─ traitlets 5.14.3 [required: any]
  │  │     └─ dependencies of traitlets displayed above
  │  ├─ pexpect 4.9.0 [required: >4.3]
  │  │  ├─ ptyprocess 0.7.0 [required: >=0.5]
  │  │  │  └─ dependencies of ptyprocess displayed above
  │  │  └─ python 3.11.9 [required: >=3.7]
  │  ├─ pickleshare 0.7.5 [required: any]
  │  │  └─ python 3.11.9 [required: >=3]
  │  ├─ prompt-toolkit 3.0.42 [required: >=3.0.41,<3.1.0]
  │  │  ├─ python 3.11.9 [required: >=3.7]
  │  │  └─ wcwidth 0.2.13 [required: any]
  │  │     └─ python 3.11.9 [required: >=3.8]
  │  ├─ pygments 2.18.0 [required: >=2.4.0]
  │  │  └─ dependencies of pygments displayed above
  │  ├─ python 3.11.9 [required: >=3.10]
  │  ├─ stack_data 0.6.2 [required: any]
  │  │  ├─ asttokens 2.4.1 [required: any]
  │  │  │  ├─ python 3.11.9 [required: >=3.5]
  │  │  │  └─ six 1.16.0 [required: >=1.12.0]
  │  │  │     └─ dependencies of six displayed above
  │  │  ├─ executing 2.0.1 [required: any]
  │  │  │  └─ python 3.11.9 [required: >=2.7]
  │  │  ├─ pure_eval 0.2.2 [required: any]
  │  │  │  └─ python 3.11.9 [required: >=3.5]
  │  │  └─ python 3.11.9 [required: >=3.5]
  │  ├─ traitlets 5.14.3 [required: >=5.13.0]
  │  │  └─ dependencies of traitlets displayed above
  │  └─ typing_extensions 4.11.0 [required: >=4.6]
  │     └─ dependencies of typing_extensions displayed above
  ├─ ipython_genutils 0.2.0 [required: any]
  │  └─ python 3.11.9 [required: any]
  ├─ ipywidgets 8.1.2 [required: >=7.6.0,<9]
  │  ├─ comm 0.2.2 [required: >=0.1.3]
  │  │  ├─ python 3.11.9 [required: >=3.6]
  │  │  └─ traitlets 5.14.3 [required: >=5.3]
  │  │     └─ dependencies of traitlets displayed above
  │  ├─ ipython 8.24.0 [required: >=6.1.0]
  │  │  └─ dependencies of ipython displayed above
  │  ├─ jupyterlab_widgets 3.0.10 [required: >=3.0.10,<3.1.0]
  │  │  └─ python 3.11.9 [required: >=3.7]
  │  ├─ python 3.11.9 [required: >=3.7]
  │  ├─ traitlets 5.14.3 [required: >=4.3.1]
  │  │  └─ dependencies of traitlets displayed above
  │  └─ widgetsnbextension 4.0.10 [required: >=4.0.10,<4.1.0]
  │     └─ python 3.11.9 [required: >=3.7]
  ├─ matplotlib-base 3.8.4 [required: >=2.2.0,<4]
  │  └─ dependencies of matplotlib-base displayed above
  ├─ numpy 1.26.4 [required: any]
  │  └─ dependencies of numpy displayed above
  ├─ pillow 10.3.0 [required: any]
  │  └─ dependencies of pillow displayed above
  ├─ python 3.11.9 [required: >=3.6]
  └─ traitlets 5.14.3 [required: <6]
     └─ dependencies of traitlets displayed above
dill==0.3.8
  └─ python 3.11.9 [required: >=3.7]
cython==3.0.10
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
pytables==3.9.2
  ├─ blosc 1.21.5 [required: >=1.21.5,<2.0a0]
  │  └─ dependencies of blosc displayed above
  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
  │  └─ dependencies of bzip2 displayed above
  ├─ c-blosc2 2.14.4 [required: >=2.14.4,<2.15.0a0]
  │  └─ dependencies of c-blosc2 displayed above
  ├─ hdf5 1.14.3 [required: >=1.14.3,<1.14.4.0a0]
  │  └─ dependencies of hdf5 displayed above
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  └─ dependencies of libzlib displayed above
  ├─ lzo 2.10 [required: >=2.10,<3.0a0]
  │  └─ dependencies of lzo displayed above
  ├─ numexpr 2.9.0 [required: any]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  ├─ nomkl 1.0 [required: any]
  │  ├─ numpy 1.26.4 [required: >=1.23.5,<2.0a0]
  │  │  └─ dependencies of numpy displayed above
  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  ├─ numpy 1.26.4 [required: >=1.23.5,<2.0a0]
  │  └─ dependencies of numpy displayed above
  ├─ packaging 24.0 [required: any]
  │  └─ dependencies of packaging displayed above
  ├─ py-cpuinfo 9.0.0 [required: any]
  │  └─ python 3.11.9 [required: >=3.7]
  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
jupyterlab-git==0.50.0
  ├─ jupyter_server 2.14.0 [required: >=2.0,<3.0]
  │  └─ dependencies of jupyter_server displayed above
  ├─ nbdime 4.0.1 [required: >=4.0,<5.0]
  │  ├─ colorama 0.4.6 [required: any]
  │  │  └─ python 3.11.9 [required: >=3.7]
  │  ├─ gitpython 3.1.43 [required: !=2.1.4,!=2.1.5,!=2.1.6]
  │  │  ├─ gitdb 4.0.11 [required: >=4.0.1,<5]
  │  │  │  ├─ python 3.11.9 [required: >=3.7]
  │  │  │  └─ smmap 5.0.0 [required: >=3.0.1,<6]
  │  │  │     └─ python 3.11.9 [required: >=3.5]
  │  │  ├─ python 3.11.9 [required: >=3.7]
  │  │  └─ typing_extensions 4.11.0 [required: >=3.7.4.3]
  │  │     └─ dependencies of typing_extensions displayed above
  │  ├─ jinja2 3.1.4 [required: >=2.9]
  │  │  └─ dependencies of jinja2 displayed above
  │  ├─ jupyter-server-mathjax 0.2.6 [required: >=0.2.2]
  │  │  ├─ jupyter_server 2.14.0 [required: >=1.1,<3]
  │  │  │  └─ dependencies of jupyter_server displayed above
  │  │  └─ python 3.11.9 [required: >=3.7]
  │  ├─ jupyter_server 2.14.0 [required: any]
  │  │  └─ dependencies of jupyter_server displayed above
  │  ├─ nbformat 5.10.4 [required: any]
  │  │  └─ dependencies of nbformat displayed above
  │  ├─ pygments 2.18.0 [required: any]
  │  │  └─ dependencies of pygments displayed above
  │  ├─ python 3.11.9 [required: >=3.6]
  │  ├─ requests 2.31.0 [required: any]
  │  │  ├─ certifi 2025.1.31 [required: >=2017.4.17]
  │  │  │  └─ dependencies of certifi displayed above
  │  │  ├─ charset-normalizer 3.3.2 [required: >=2,<4]
  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  ├─ idna 3.7 [required: >=2.5,<4]
  │  │  │  └─ dependencies of idna displayed above
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
  │  └─ tornado 6.4 [required: any]
  │     └─ dependencies of tornado displayed above
  ├─ nbformat 5.10.4 [required: any]
  │  └─ dependencies of nbformat displayed above
  ├─ packaging 24.0 [required: any]
  │  └─ dependencies of packaging displayed above
  ├─ pexpect 4.9.0 [required: any]
  │  └─ dependencies of pexpect displayed above
  ├─ python 3.11.9 [required: >=3.6,<4.0]
  └─ traitlets 5.14.3 [required: >=5.0,<6.0]
     └─ dependencies of traitlets displayed above
xlrd==2.0.1
  └─ python 3.11.9 [required: >=3.6]
bottleneck==1.3.8
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ numpy 1.26.4 [required: >=1.23.5,<2.0a0]
  │  └─ dependencies of numpy displayed above
  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
scikit-learn==1.4.2
  ├─ _openmp_mutex 4.5 [required: >=4.5]
  │  └─ dependencies of _openmp_mutex displayed above
  ├─ joblib 1.4.2 [required: >=1.2.0]
  │  ├─ python 3.11.9 [required: >=3.8]
  │  └─ setuptools 69.5.1 [required: any]
  │     └─ dependencies of setuptools displayed above
  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  └─ dependencies of libgcc-ng displayed above
  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  ├─ numpy 1.26.4 [required: >=1.19,<3]
  │  └─ dependencies of numpy displayed above
  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  ├─ scipy 1.13.0 [required: any]
  │  └─ dependencies of scipy displayed above
  └─ threadpoolctl 3.5.0 [required: >=2.0.0]
     └─ python 3.11.9 [required: >=3.8]
dask==2024.5.1
  ├─ bokeh 3.4.1 [required: >=2.4.2,!=3.0.*]
  │  ├─ contourpy 1.2.1 [required: >=1.2]
  │  │  └─ dependencies of contourpy displayed above
  │  ├─ jinja2 3.1.4 [required: >=2.9]
  │  │  └─ dependencies of jinja2 displayed above
  │  ├─ numpy 1.26.4 [required: >=1.16]
  │  │  └─ dependencies of numpy displayed above
  │  ├─ packaging 24.0 [required: >=16.8]
  │  │  └─ dependencies of packaging displayed above
  │  ├─ pandas 2.2.2 [required: >=1.2]
  │  │  └─ dependencies of pandas displayed above
  │  ├─ pillow 10.3.0 [required: >=7.1.0]
  │  │  └─ dependencies of pillow displayed above
  │  ├─ python 3.11.9 [required: >=3.9]
  │  ├─ pyyaml 6.0.1 [required: >=3.10]
  │  │  └─ dependencies of pyyaml displayed above
  │  ├─ tornado 6.4 [required: >=6.2]
  │  │  └─ dependencies of tornado displayed above
  │  └─ xyzservices 2024.4.0 [required: >=2021.09.1]
  │     └─ python 3.11.9 [required: >=3.8]
  ├─ cytoolz 0.12.3 [required: >=0.11.0]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  ├─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  └─ toolz 0.12.1 [required: >=0.10.0]
  │     └─ dependencies of toolz displayed above
  ├─ dask-core 2024.5.1 [required: >=2024.5.1,<2024.5.2.0a0]
  │  ├─ click 8.1.7 [required: >=8.1]
  │  │  ├─ __unix [required: any]
  │  │  └─ python 3.11.9 [required: >=3.8]
  │  ├─ cloudpickle 3.0.0 [required: >=1.5.0]
  │  │  └─ python 3.11.9 [required: >=3.8]
  │  ├─ fsspec 2024.5.0 [required: >=2021.09.0]
  │  │  └─ python 3.11.9 [required: >=3.8]
  │  ├─ importlib_metadata 7.1.0 [required: >=4.13.0]
  │  │  └─ dependencies of importlib_metadata displayed above
  │  ├─ packaging 24.0 [required: >=20.0]
  │  │  └─ dependencies of packaging displayed above
  │  ├─ partd 1.4.2 [required: >=1.2.0]
  │  │  ├─ locket 1.0.0 [required: any]
  │  │  │  └─ python 3.11.9 [required: >=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*]
  │  │  ├─ python 3.11.9 [required: >=3.9]
  │  │  └─ toolz 0.12.1 [required: any]
  │  │     └─ dependencies of toolz displayed above
  │  ├─ python 3.11.9 [required: >=3.9]
  │  ├─ pyyaml 6.0.1 [required: >=5.3.1]
  │  │  └─ dependencies of pyyaml displayed above
  │  └─ toolz 0.12.1 [required: >=0.10.0]
  │     └─ dependencies of toolz displayed above
  ├─ dask-expr 1.1.1 [required: >=1.1,<1.2]
  │  ├─ dask-core 2024.5.1 [required: 2024.5.1]
  │  │  └─ dependencies of dask-core displayed above
  │  ├─ pandas 2.2.2 [required: >=2]
  │  │  └─ dependencies of pandas displayed above
  │  ├─ pyarrow 16.1.0 [required: any]
  │  │  ├─ libarrow-acero 16.1.0 [required: 16.1.0.*]
  │  │  │  ├─ libarrow 16.1.0 [required: 16.1.0, hbcc2d42_2_cpu]
  │  │  │  │  ├─ aws-crt-cpp 0.26.8 [required: >=0.26.8,<0.26.9.0a0]
  │  │  │  │  │  ├─ aws-c-auth 0.7.20 [required: >=0.7.20,<0.7.21.0a0]
  │  │  │  │  │  │  ├─ aws-c-cal 0.6.12 [required: >=0.6.12,<0.6.13.0a0]
  │  │  │  │  │  │  │  ├─ aws-c-common 0.9.17 [required: >=0.9.17,<0.9.18.0a0]
  │  │  │  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  │  └─ openssl 3.4.1 [required: >=3.2.1,<4.0a0]
  │  │  │  │  │  │  │     └─ dependencies of openssl displayed above
  │  │  │  │  │  │  ├─ aws-c-common 0.9.17 [required: >=0.9.17,<0.9.18.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  │  ├─ aws-c-http 0.8.1 [required: >=0.8.1,<0.8.2.0a0]
  │  │  │  │  │  │  │  ├─ aws-c-cal 0.6.12 [required: >=0.6.12,<0.6.13.0a0]
  │  │  │  │  │  │  │  │  └─ dependencies of aws-c-cal displayed above
  │  │  │  │  │  │  │  ├─ aws-c-common 0.9.17 [required: >=0.9.17,<0.9.18.0a0]
  │  │  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  │  │  ├─ aws-c-compression 0.2.18 [required: >=0.2.18,<0.2.19.0a0]
  │  │  │  │  │  │  │  │  ├─ aws-c-common 0.9.17 [required: >=0.9.17,<0.9.18.0a0]
  │  │  │  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  │  ├─ aws-c-io 0.14.8 [required: >=0.14.8,<0.14.9.0a0]
  │  │  │  │  │  │  │  │  ├─ aws-c-cal 0.6.12 [required: >=0.6.12,<0.6.13.0a0]
  │  │  │  │  │  │  │  │  │  └─ dependencies of aws-c-cal displayed above
  │  │  │  │  │  │  │  │  ├─ aws-c-common 0.9.17 [required: >=0.9.17,<0.9.18.0a0]
  │  │  │  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  │  │  └─ s2n 1.4.13 [required: >=1.4.13,<1.4.14.0a0]
  │  │  │  │  │  │  │  │     ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │  │     │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  │  │     └─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  │  │  │  │  │        └─ dependencies of openssl displayed above
  │  │  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  ├─ aws-c-io 0.14.8 [required: >=0.14.8,<0.14.9.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-c-io displayed above
  │  │  │  │  │  │  ├─ aws-c-sdkutils 0.1.16 [required: >=0.1.16,<0.1.17.0a0]
  │  │  │  │  │  │  │  ├─ aws-c-common 0.9.17 [required: >=0.9.17,<0.9.18.0a0]
  │  │  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  ├─ aws-c-cal 0.6.12 [required: >=0.6.12,<0.6.13.0a0]
  │  │  │  │  │  │  └─ dependencies of aws-c-cal displayed above
  │  │  │  │  │  ├─ aws-c-common 0.9.17 [required: >=0.9.17,<0.9.18.0a0]
  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  ├─ aws-c-event-stream 0.4.2 [required: >=0.4.2,<0.4.3.0a0]
  │  │  │  │  │  │  ├─ aws-c-common 0.9.17 [required: >=0.9.17,<0.9.18.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  │  ├─ aws-c-io 0.14.8 [required: >=0.14.8,<0.14.9.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-c-io displayed above
  │  │  │  │  │  │  ├─ aws-checksums 0.1.18 [required: >=0.1.18,<0.1.19.0a0]
  │  │  │  │  │  │  │  ├─ aws-c-common 0.9.17 [required: >=0.9.17,<0.9.18.0a0]
  │  │  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  │  ├─ aws-c-http 0.8.1 [required: >=0.8.1,<0.8.2.0a0]
  │  │  │  │  │  │  └─ dependencies of aws-c-http displayed above
  │  │  │  │  │  ├─ aws-c-io 0.14.8 [required: >=0.14.8,<0.14.9.0a0]
  │  │  │  │  │  │  └─ dependencies of aws-c-io displayed above
  │  │  │  │  │  ├─ aws-c-mqtt 0.10.4 [required: >=0.10.4,<0.10.5.0a0]
  │  │  │  │  │  │  ├─ aws-c-common 0.9.17 [required: >=0.9.17,<0.9.18.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  │  ├─ aws-c-http 0.8.1 [required: >=0.8.1,<0.8.2.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-c-http displayed above
  │  │  │  │  │  │  ├─ aws-c-io 0.14.8 [required: >=0.14.8,<0.14.9.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-c-io displayed above
  │  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  ├─ aws-c-s3 0.5.8 [required: >=0.5.8,<0.5.9.0a0]
  │  │  │  │  │  │  ├─ aws-c-auth 0.7.20 [required: >=0.7.20,<0.7.21.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-c-auth displayed above
  │  │  │  │  │  │  ├─ aws-c-cal 0.6.12 [required: >=0.6.12,<0.6.13.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-c-cal displayed above
  │  │  │  │  │  │  ├─ aws-c-common 0.9.17 [required: >=0.9.17,<0.9.18.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  │  ├─ aws-c-http 0.8.1 [required: >=0.8.1,<0.8.2.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-c-http displayed above
  │  │  │  │  │  │  ├─ aws-c-io 0.14.8 [required: >=0.14.8,<0.14.9.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-c-io displayed above
  │  │  │  │  │  │  ├─ aws-checksums 0.1.18 [required: >=0.1.18,<0.1.19.0a0]
  │  │  │  │  │  │  │  └─ dependencies of aws-checksums displayed above
  │  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  └─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  │  │  │     └─ dependencies of openssl displayed above
  │  │  │  │  │  ├─ aws-c-sdkutils 0.1.16 [required: >=0.1.16,<0.1.17.0a0]
  │  │  │  │  │  │  └─ dependencies of aws-c-sdkutils displayed above
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  ├─ aws-sdk-cpp 1.11.267 [required: >=1.11.267,<1.11.268.0a0]
  │  │  │  │  │  ├─ aws-c-common 0.9.17 [required: >=0.9.17,<0.9.18.0a0]
  │  │  │  │  │  │  └─ dependencies of aws-c-common displayed above
  │  │  │  │  │  ├─ aws-c-event-stream 0.4.2 [required: >=0.4.2,<0.4.3.0a0]
  │  │  │  │  │  │  └─ dependencies of aws-c-event-stream displayed above
  │  │  │  │  │  ├─ aws-checksums 0.1.18 [required: >=0.1.18,<0.1.19.0a0]
  │  │  │  │  │  │  └─ dependencies of aws-checksums displayed above
  │  │  │  │  │  ├─ aws-crt-cpp 0.26.8 [required: >=0.26.8,<0.26.9.0a0]
  │  │  │  │  │  │  └─ dependencies of aws-crt-cpp displayed above
  │  │  │  │  │  ├─ libcurl 8.7.1 [required: >=8.7.1,<9.0a0]
  │  │  │  │  │  │  └─ dependencies of libcurl displayed above
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  │  │  └─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  │  │     └─ dependencies of openssl displayed above
  │  │  │  │  ├─ bzip2 1.0.8 [required: >=1.0.8,<2.0a0]
  │  │  │  │  │  └─ dependencies of bzip2 displayed above
  │  │  │  │  ├─ gflags 2.2.2 [required: >=2.2.2,<2.3.0a0]
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=7.5.0]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=7.5.0]
  │  │  │  │  ├─ glog 0.7.0 [required: >=0.7.0,<0.8.0a0]
  │  │  │  │  │  ├─ gflags 2.2.2 [required: >=2.2.2,<2.3.0a0]
  │  │  │  │  │  │  └─ dependencies of gflags displayed above
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  ├─ libabseil 20240116.2 [required: >=20240116.2,<20240117.0a0]
  │  │  │  │  │  └─ dependencies of libabseil displayed above
  │  │  │  │  ├─ libbrotlidec 1.1.0 [required: >=1.1.0,<1.2.0a0]
  │  │  │  │  │  └─ dependencies of libbrotlidec displayed above
  │  │  │  │  ├─ libbrotlienc 1.1.0 [required: >=1.1.0,<1.2.0a0]
  │  │  │  │  │  └─ dependencies of libbrotlienc displayed above
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libgoogle-cloud 2.24.0 [required: >=2.24.0,<2.25.0a0]
  │  │  │  │  │  ├─ libabseil 20240116.2 [required: >=20240116.2,<20240117.0a0]
  │  │  │  │  │  │  └─ dependencies of libabseil displayed above
  │  │  │  │  │  ├─ libcurl 8.7.1 [required: >=8.7.1,<9.0a0]
  │  │  │  │  │  │  └─ dependencies of libcurl displayed above
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  ├─ libgrpc 1.62.2 [required: >=1.62.2,<1.63.0a0]
  │  │  │  │  │  │  ├─ c-ares 1.28.1 [required: >=1.28.1,<2.0a0]
  │  │  │  │  │  │  │  └─ dependencies of c-ares displayed above
  │  │  │  │  │  │  ├─ libabseil 20240116.2 [required: >=20240116.1,<20240117.0a0]
  │  │  │  │  │  │  │  └─ dependencies of libabseil displayed above
  │  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  ├─ libprotobuf 4.25.3 [required: >=4.25.3,<4.25.4.0a0]
  │  │  │  │  │  │  │  └─ dependencies of libprotobuf displayed above
  │  │  │  │  │  │  ├─ libre2-11 2023.09.01 [required: >=2023.9.1,<2024.0a0]
  │  │  │  │  │  │  │  ├─ libabseil 20240116.2 [required: >=20240116.1,<20240117.0a0]
  │  │  │  │  │  │  │  │  └─ dependencies of libabseil displayed above
  │  │  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  │  │  │  ├─ openssl 3.4.1 [required: >=3.2.1,<4.0a0]
  │  │  │  │  │  │  │  └─ dependencies of openssl displayed above
  │  │  │  │  │  │  └─ re2 2023.09.01 [required: any]
  │  │  │  │  │  │     └─ libre2-11 2023.09.01 [required: 2023.09.01, h5a48ba9_2]
  │  │  │  │  │  │        └─ dependencies of libre2-11 displayed above
  │  │  │  │  │  ├─ libprotobuf 4.25.3 [required: >=4.25.3,<4.25.4.0a0]
  │  │  │  │  │  │  └─ dependencies of libprotobuf displayed above
  │  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  │  └─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  │  │     └─ dependencies of openssl displayed above
  │  │  │  │  ├─ libgoogle-cloud-storage 2.24.0 [required: >=2.24.0,<2.25.0a0]
  │  │  │  │  │  ├─ libabseil 20240116.2 [required: any]
  │  │  │  │  │  │  └─ dependencies of libabseil displayed above
  │  │  │  │  │  ├─ libcrc32c 1.1.2 [required: >=1.1.2,<1.2.0a0]
  │  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=9.4.0]
  │  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=9.4.0]
  │  │  │  │  │  ├─ libcurl 8.7.1 [required: any]
  │  │  │  │  │  │  └─ dependencies of libcurl displayed above
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  ├─ libgoogle-cloud 2.24.0 [required: 2.24.0, h2736e30_0]
  │  │  │  │  │  │  └─ dependencies of libgoogle-cloud displayed above
  │  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  │  │  └─ openssl 3.4.1 [required: any]
  │  │  │  │  │     └─ dependencies of openssl displayed above
  │  │  │  │  ├─ libre2-11 2023.09.01 [required: >=2023.9.1,<2024.0a0]
  │  │  │  │  │  └─ dependencies of libre2-11 displayed above
  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  ├─ libutf8proc 2.8.0 [required: >=2.8.0,<3.0a0]
  │  │  │  │  │  └─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │     └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  │  ├─ lz4-c 1.9.4 [required: >=1.9.3,<1.10.0a0]
  │  │  │  │  │  └─ dependencies of lz4-c displayed above
  │  │  │  │  ├─ orc 2.0.0 [required: >=2.0.0,<2.0.1.0a0]
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  ├─ libprotobuf 4.25.3 [required: >=4.25.3,<4.25.4.0a0]
  │  │  │  │  │  │  └─ dependencies of libprotobuf displayed above
  │  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  │  │  ├─ lz4-c 1.9.4 [required: >=1.9.3,<1.10.0a0]
  │  │  │  │  │  │  └─ dependencies of lz4-c displayed above
  │  │  │  │  │  ├─ snappy 1.2.0 [required: >=1.2.0,<1.3.0a0]
  │  │  │  │  │  │  └─ dependencies of snappy displayed above
  │  │  │  │  │  └─ zstd 1.5.6 [required: >=1.5.5,<1.6.0a0]
  │  │  │  │  │     └─ dependencies of zstd displayed above
  │  │  │  │  ├─ re2 2023.09.01 [required: any]
  │  │  │  │  │  └─ dependencies of re2 displayed above
  │  │  │  │  ├─ snappy 1.2.0 [required: >=1.2.0,<1.3.0a0]
  │  │  │  │  │  └─ dependencies of snappy displayed above
  │  │  │  │  └─ zstd 1.5.6 [required: >=1.5.6,<1.6.0a0]
  │  │  │  │     └─ dependencies of zstd displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libarrow-dataset 16.1.0 [required: 16.1.0.*]
  │  │  │  ├─ libarrow 16.1.0 [required: 16.1.0, hbcc2d42_2_cpu]
  │  │  │  │  └─ dependencies of libarrow displayed above
  │  │  │  ├─ libarrow-acero 16.1.0 [required: 16.1.0, hac33072_2_cpu]
  │  │  │  │  └─ dependencies of libarrow-acero displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libparquet 16.1.0 [required: 16.1.0, h6a7eafb_2_cpu]
  │  │  │  │  ├─ libarrow 16.1.0 [required: 16.1.0, hbcc2d42_2_cpu]
  │  │  │  │  │  └─ dependencies of libarrow displayed above
  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  ├─ libthrift 0.19.0 [required: >=0.19.0,<0.19.1.0a0]
  │  │  │  │  │  ├─ libevent 2.1.12 [required: >=2.1.12,<2.1.13.0a0]
  │  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  │  └─ openssl 3.4.1 [required: >=3.1.1,<4.0a0]
  │  │  │  │  │  │     └─ dependencies of openssl displayed above
  │  │  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  │  │  └─ openssl 3.4.1 [required: >=3.1.3,<4.0a0]
  │  │  │  │  │     └─ dependencies of openssl displayed above
  │  │  │  │  └─ openssl 3.4.1 [required: >=3.3.0,<4.0a0]
  │  │  │  │     └─ dependencies of openssl displayed above
  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libarrow-substrait 16.1.0 [required: 16.1.0.*]
  │  │  │  ├─ libabseil 20240116.2 [required: >=20240116.2,<20240117.0a0]
  │  │  │  │  └─ dependencies of libabseil displayed above
  │  │  │  ├─ libarrow 16.1.0 [required: 16.1.0, hbcc2d42_2_cpu]
  │  │  │  │  └─ dependencies of libarrow displayed above
  │  │  │  ├─ libarrow-acero 16.1.0 [required: 16.1.0, hac33072_2_cpu]
  │  │  │  │  └─ dependencies of libarrow-acero displayed above
  │  │  │  ├─ libarrow-dataset 16.1.0 [required: 16.1.0, hac33072_2_cpu]
  │  │  │  │  └─ dependencies of libarrow-dataset displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libprotobuf 4.25.3 [required: >=4.25.3,<4.25.4.0a0]
  │  │  │  │  └─ dependencies of libprotobuf displayed above
  │  │  │  └─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ libparquet 16.1.0 [required: 16.1.0.*]
  │  │  │  └─ dependencies of libparquet displayed above
  │  │  ├─ numpy 1.26.4 [required: >=1.23.5,<2.0a0]
  │  │  │  └─ dependencies of numpy displayed above
  │  │  ├─ pyarrow-core 16.1.0 [required: 16.1.0, *_0_*]
  │  │  │  ├─ libarrow 16.1.0 [required: 16.1.0.*, *cpu]
  │  │  │  │  └─ dependencies of libarrow displayed above
  │  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  │  ├─ libzlib 1.2.13 [required: >=1.2.13,<1.3.0a0]
  │  │  │  │  └─ dependencies of libzlib displayed above
  │  │  │  ├─ numpy 1.26.4 [required: >=1.23.5,<2.0a0]
  │  │  │  │  └─ dependencies of numpy displayed above
  │  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  └─ python 3.11.9 [required: >=3.9]
  ├─ distributed 2024.5.1 [required: >=2024.5.1,<2024.5.2.0a0]
  │  ├─ click 8.1.7 [required: >=8.0]
  │  │  └─ dependencies of click displayed above
  │  ├─ cloudpickle 3.0.0 [required: >=1.5.0]
  │  │  └─ dependencies of cloudpickle displayed above
  │  ├─ cytoolz 0.12.3 [required: >=0.10.1]
  │  │  └─ dependencies of cytoolz displayed above
  │  ├─ dask-core 2024.5.1 [required: >=2024.5.1,<2024.5.2.0a0]
  │  │  └─ dependencies of dask-core displayed above
  │  ├─ jinja2 3.1.4 [required: >=2.10.3]
  │  │  └─ dependencies of jinja2 displayed above
  │  ├─ locket 1.0.0 [required: >=1.0.0]
  │  │  └─ dependencies of locket displayed above
  │  ├─ msgpack-python 1.0.8 [required: >=1.0.0]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  ├─ packaging 24.0 [required: >=20.0]
  │  │  └─ dependencies of packaging displayed above
  │  ├─ psutil 5.9.8 [required: >=5.7.2]
  │  │  └─ dependencies of psutil displayed above
  │  ├─ python 3.11.9 [required: >=3.9]
  │  ├─ pyyaml 6.0.1 [required: >=5.3.1]
  │  │  └─ dependencies of pyyaml displayed above
  │  ├─ sortedcontainers 2.4.0 [required: >=2.0.5]
  │  │  └─ python 3.11.9 [required: >=2.7]
  │  ├─ tblib 3.0.0 [required: >=1.6.0]
  │  │  └─ python 3.11.9 [required: >=3.7]
  │  ├─ toolz 0.12.1 [required: >=0.10.0]
  │  │  └─ dependencies of toolz displayed above
  │  ├─ tornado 6.4 [required: >=6.0.4]
  │  │  └─ dependencies of tornado displayed above
  │  ├─ urllib3 2.2.1 [required: >=1.24.3]
  │  │  └─ dependencies of urllib3 displayed above
  │  └─ zict 3.0.0 [required: >=3.0.0]
  │     └─ python 3.11.9 [required: >=3.8]
  ├─ jinja2 3.1.4 [required: >=2.10.3]
  │  └─ dependencies of jinja2 displayed above
  ├─ lz4 4.3.3 [required: >=4.3.2]
  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  └─ dependencies of libgcc-ng displayed above
  │  ├─ lz4-c 1.9.4 [required: >=1.9.3,<1.10.0a0]
  │  │  └─ dependencies of lz4-c displayed above
  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  ├─ numpy 1.26.4 [required: >=1.21]
  │  └─ dependencies of numpy displayed above
  ├─ pandas 2.2.2 [required: >=1.3]
  │  └─ dependencies of pandas displayed above
  ├─ pyarrow 16.1.0 [required: >=7.0]
  │  └─ dependencies of pyarrow displayed above
  ├─ pyarrow-hotfix 0.6 [required: any]
  │  ├─ pyarrow 16.1.0 [required: >=0.14]
  │  │  └─ dependencies of pyarrow displayed above
  │  └─ python 3.11.9 [required: >=3.5]
  └─ python 3.11.9 [required: >=3.9]
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
  │  │  │  └─ dependencies of importlib-metadata displayed above
  │  │  ├─ importlib_resources 6.4.0 [required: any]
  │  │  │  └─ dependencies of importlib_resources displayed above
  │  │  ├─ mako 1.3.5 [required: any]
  │  │  │  ├─ importlib-metadata 7.1.0 [required: any]
  │  │  │  │  └─ dependencies of importlib-metadata displayed above
  │  │  │  ├─ markupsafe 2.1.5 [required: >=0.9.2]
  │  │  │  │  └─ dependencies of markupsafe displayed above
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
  │  │  │     └─ dependencies of typing-extensions displayed above
  │  │  └─ typing-extensions 4.11.0 [required: >=4]
  │  │     └─ dependencies of typing-extensions displayed above
  │  ├─ async_generator 1.10 [required: >=1.9]
  │  │  └─ python 3.11.9 [required: >2.7]
  │  ├─ certipy 0.1.3 [required: >=0.1.2]
  │  │  ├─ pyopenssl 24.0.0 [required: any]
  │  │  │  ├─ cryptography 42.0.7 [required: >=41.0.5,<43]
  │  │  │  │  ├─ cffi 1.16.0 [required: >=1.12]
  │  │  │  │  │  └─ dependencies of cffi displayed above
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
  │  │  └─ dependencies of jinja2 displayed above
  │  ├─ jupyter_telemetry 0.1.0 [required: >=0.1.0]
  │  │  ├─ jsonschema 4.22.0 [required: any]
  │  │  │  └─ dependencies of jsonschema displayed above
  │  │  ├─ python 3.11.9 [required: >=3.5]
  │  │  ├─ python-json-logger 2.0.7 [required: any]
  │  │  │  └─ dependencies of python-json-logger displayed above
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
  │  │     └─ dependencies of traitlets displayed above
  │  ├─ oauthlib 3.2.2 [required: >=3.0]
  │  │  ├─ blinker 1.8.2 [required: any]
  │  │  │  └─ python 3.11.9 [required: >=3.8]
  │  │  ├─ cryptography 42.0.7 [required: any]
  │  │  │  └─ dependencies of cryptography displayed above
  │  │  ├─ pyjwt 2.8.0 [required: >=1.0.0]
  │  │  │  └─ python 3.11.9 [required: >=3.7]
  │  │  └─ python 3.11.9 [required: >=3.6]
  │  ├─ packaging 24.0 [required: any]
  │  │  └─ dependencies of packaging displayed above
  │  ├─ pamela 1.1.0 [required: any]
  │  │  └─ python 3.11.9 [required: >=3.5]
  │  ├─ prometheus_client 0.20.0 [required: >=0.4.0]
  │  │  └─ dependencies of prometheus_client displayed above
  │  ├─ python 3.11.9 [required: >=3.7]
  │  ├─ python-dateutil 2.9.0 [required: any]
  │  │  └─ dependencies of python-dateutil displayed above
  │  ├─ requests 2.31.0 [required: any]
  │  │  └─ dependencies of requests displayed above
  │  ├─ sqlalchemy 2.0.30 [required: >=1.4]
  │  │  └─ dependencies of sqlalchemy displayed above
  │  ├─ tornado 6.4 [required: >=5.1]
  │  │  └─ dependencies of tornado displayed above
  │  └─ traitlets 5.14.3 [required: >=4.3.2]
  │     └─ dependencies of traitlets displayed above
  ├─ nodejs 20.12.2 [required: >=12]
  │  └─ dependencies of nodejs displayed above
  ├─ psutil 5.9.8 [required: any]
  │  └─ dependencies of psutil displayed above
  ├─ pycurl 7.45.3 [required: any]
  │  ├─ libcurl 8.7.1 [required: >=8.5.0,<9.0a0]
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
  │  └─ dependencies of argon2-cffi displayed above
  ├─ ipykernel 6.29.3 [required: any]
  │  ├─ __linux [required: any]
  │  ├─ comm 0.2.2 [required: >=0.1.1]
  │  │  └─ dependencies of comm displayed above
  │  ├─ debugpy 1.8.1 [required: >=1.6.5]
  │  │  ├─ libgcc-ng 14.2.0 [required: >=12]
  │  │  │  └─ dependencies of libgcc-ng displayed above
  │  │  ├─ libstdcxx-ng 13.2.0 [required: >=12]
  │  │  ├─ python 3.11.9 [required: >=3.11,<3.12.0a0]
  │  │  └─ python_abi 3.11 [required: 3.11.*, *_cp311]
  │  ├─ ipython 8.24.0 [required: >=7.23.1]
  │  │  └─ dependencies of ipython displayed above
  │  ├─ jupyter_client 8.6.1 [required: >=6.1.12]
  │  │  └─ dependencies of jupyter_client displayed above
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
  │  └─ dependencies of ipython_genutils displayed above
  ├─ jinja2 3.1.4 [required: any]
  │  └─ dependencies of jinja2 displayed above
  ├─ jupyter_client 8.6.1 [required: >=6.1.1]
  │  └─ dependencies of jupyter_client displayed above
  ├─ jupyter_core 5.7.2 [required: >=4.6.1]
  │  └─ dependencies of jupyter_core displayed above
  ├─ jupyter_server 2.14.0 [required: >=1.8]
  │  └─ dependencies of jupyter_server displayed above
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
  │  │  │  │  └─ dependencies of pytz displayed above
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


