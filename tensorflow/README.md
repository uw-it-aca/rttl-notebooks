# UW-IT JupyterHub for Teaching Tensorflow notebook
Docker image for UW-IT JupyterHub for Teaching Tensorflow notebook. 
- Detailed information about base Tensorflow notebook is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-tensorflow-notebook
- General information about working with base images is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html
- Installed packages and versions can be viewed in this image's [Dockerfile](Dockerfile) using `pip list` or `conda list`. Output from both command's output is also shown below for convenience.
- The JupyterLab interface is installed and is set as default

#### Running notebook locally
- `docker run -p 8888:8888 us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-tensorflow-notebook:2.3`
- Console output will include localhost url with access token. Add '/lab' to the end of the path portion, eg: `http://127.0.0.1:8888/lab`

#### Accessing server shell locally
- `docker run -it --entrypoint /bin/bash us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-tensorflow-notebook:2.3`

#### Installed packages
via `pip list`

| Package | Version |
| ----------------------------- | ------------------- |
| absl-py | 0.12.0 |
| aiohttp | 3.7.4 |
| alembic | 1.5.8 |
| anyio | 2.2.0 |
| appdirs | 1.4.4 |
| argon2-cffi | 20.1.0 |
| arviz | 0.11.2 |
| asteval | 0.9.23 |
| astor | 0.8.1 |
| astroML | 0.4.1 |
| astroplan | 0.8 |
| astropy | 4.2.1 |
| astroquery | 0.4.2 |
| astunparse | 1.6.3 |
| async-generator | 1.10 |
| async-timeout | 3.0.1 |
| attrs | 20.3.0 |
| Babel | 2.9.1 |
| backcall | 0.2.0 |
| backports.functools-lru-cache | 1.6.4 |
| beautifulsoup4 | 4.9.3 |
| biogeme | 3.2.6 |
| bleach | 3.3.0 |
| blinker | 1.4 |
| blis | 0.7.4 |
| bokeh | 2.3.1 |
| boto | 2.49.0 |
| boto3 | 1.17.86 |
| botocore | 1.20.86 |
| Bottleneck | 1.3.2 |
| bounded-pool-executor | 0.0.3 |
| brotlipy | 0.7.0 |
| bs4 | 0.0.1 |
| bz2file | 0.98 |
| cached-property | 1.5.2 |
| cachetools | 4.2.2 |
| catalogue | 2.0.4 |
| certifi | 2021.5.30 |
| certipy | 0.1.3 |
| cffi | 1.14.5 |
| cftime | 1.5.0 |
| chardet | 4.0.0 |
| choicemodels | 0.2.2 |
| click | 7.1.2 |
| cloudpickle | 1.6.0 |
| colorama | 0.4.4 |
| conda | 4.10.0 |
| conda-package-handling | 1.7.3 |
| cryptography | 3.4.7 |
| cssselect | 1.1.0 |
| cycler | 0.10.0 |
| cymem | 2.0.5 |
| Cython | 0.29.23 |
| cytoolz | 0.11.0 |
| dask | 2021.4.1 |
| decorator | 5.0.7 |
| defusedxml | 0.7.1 |
| deprecation | 2.1.0 |
| descartes | 1.1.0 |
| dill | 0.3.3 |
| distributed | 2021.4.1 |
| emcee | 0.0.0 |
| entrypoints | 0.3 |
| et-xmlfile | 1.0.1 |
| fake-useragent | 0.1.11 |
| fastprogress | 1.0.0 |
| filelock | 3.0.12 |
| flatbuffers | 1.12 |
| fsspec | 2021.4.0 |
| funcy | 1.16 |
| future | 0.18.2 |
| fuzzywuzzy | 0.18.0 |
| gast | 0.3.3 |
| gatspy | 0.3 |
| gensim | 4.0.1 |
| gmpy2 | 2.1.0b1 |
| google-api-core | 1.26.3 |
| google-auth | 1.30.0 |
| google-auth-oauthlib | 0.4.1 |
| google-cloud-core | 1.5.0 |
| google-cloud-storage | 1.31.2 |
| google-crc32c | 1.1.2 |
| google-pasta | 0.2.0 |
| google-resumable-media | 1.2.0 |
| googleapis-common-protos | 1.53.0 |
| greenlet | 1.0.0 |
| grpcio | 1.37.1 |
| h5py | 2.10.0 |
| HeapDict | 1.0.1 |
| hickle | 3.4.5 |
| html5lib | 1.1 |
| idna | 2.10 |
| imagecodecs | 2021.3.31 |
| imageio | 2.9.0 |
| importlib-metadata | 4.0.1 |
| ipykernel | 5.5.3 |
| ipympl | 0.7.0 |
| ipython | 7.23.0 |
| ipython-genutils | 0.2.0 |
| ipywidgets | 7.6.3 |
| jax | 0.2.13 |
| jaxlib | 0.1.67 |
| jdcal | 1.4.1 |
| jedi | 0.18.0 |
| jeepney | 0.6.0 |
| Jinja2 | 2.11.3 |
| jmespath | 0.10.0 |
| joblib | 1.0.1 |
| json5 | 0.9.5 |
| jsonschema | 3.2.0 |
| jupyter-client | 6.1.12 |
| jupyter-core | 4.7.1 |
| jupyter-packaging | 0.9.2 |
| jupyter-server | 1.6.4 |
| jupyter-telemetry | 0.1.0 |
| jupyterhub | 1.3.0 |
| jupyterlab | 3.0.14 |
| jupyterlab-pygments | 0.1.2 |
| jupyterlab-server | 2.5.0 |
| jupyterlab-widgets | 1.0.0 |
| Keras-Preprocessing | 1.1.2 |
| keyring | 23.0.1 |
| kiwisolver | 1.3.1 |
| llvmlite | 0.36.0 |
| lmfit | 1.0.2 |
| locket | 0.2.0 |
| lxml | 4.6.3 |
| Mako | 1.1.4 |
| mamba | 0.12.1 |
| Markdown | 3.3.4 |
| MarkupSafe | 1.1.1 |
| matplotlib | 3.4.1 |
| matplotlib-inline | 0.1.2 |
| mistune | 0.8.4 |
| mizani | 0.7.3 |
| mkl-service | 2.3.0 |
| mock | 4.0.3 |
| mpi4py | 3.0.3 |
| mpmath | 1.2.1 |
| msgpack | 1.0.2 |
| multidict | 5.1.0 |
| murmurhash | 1.0.5 |
| nbclassic | 0.2.7 |
| nbclient | 0.5.3 |
| nbconvert | 6.0.7 |
| nbformat | 5.1.3 |
| nbgitpuller | 0.9.0 |
| nbresuse | 0.3.3 |
| nest-asyncio | 1.5.1 |
| netCDF4 | 1.5.6 |
| networkx | 2.5 |
| nltk | 3.6.2 |
| notebook | 6.3.0 |
| numba | 0.53.1 |
| numexpr | 2.7.3 |
| numpy | 1.20.2 |
| oauthlib | 3.0.1 |
| olefile | 0.46 |
| openpyxl | 3.0.7 |
| opt-einsum | 3.3.0 |
| packaging | 20.9 |
| palettable | 3.3.0 |
| pamela | 1.0.0 |
| pandas | 1.2.4 |
| pandocfilters | 1.4.2 |
| parse | 1.19.0 |
| parso | 0.8.2 |
| partd | 1.2.0 |
| pathy | 0.5.2 |
| patsy | 0.5.1 |
| pexpect | 4.8.0 |
| photutils | 1.2.0.dev72+g97224d92 |
| pickleshare | 0.7.5 |
| Pillow | 8.1.2 |
| pip | 21.1.1 |
| plotly | 4.14.3 |
| plotnine | 0.8.0 |
| pooch | 1.3.0 |
| pqdm | 0.1.0 |
| preshed | 3.0.5 |
| prometheus-client | 0.10.1 |
| prompt-toolkit | 3.0.18 |
| protobuf | 3.15.8 |
| psutil | 5.8.0 |
| ptyprocess | 0.7.0 |
| pyasn1 | 0.4.8 |
| pyasn1-modules | 0.2.7 |
| pycosat | 0.6.3 |
| pycparser | 2.20 |
| pycurl | 7.43.0.6 |
| pydantic | 1.7.3 |
| pyee | 8.1.0 |
| pyerfa | 1.7.3 |
| Pygments | 2.8.1 |
| pygpu | 0.7.6 |
| PyJWT | 2.1.0 |
| pyLDAvis | 3.3.1 |
| pylogit | 1.0.1 |
| pymc3 | 3.11.2 |
| pyOpenSSL | 20.0.1 |
| pyparsing | 2.4.7 |
| pyppeteer | 0.2.5 |
| pyquery | 1.4.3 |
| pyrsistent | 0.17.3 |
| PySocks | 1.7.1 |
| python-dateutil | 2.8.1 |
| python-editor | 1.0.4 |
| python-json-logger | 2.0.1 |
| python-mimeparse | 1.6.0 |
| pytz | 2021.1 |
| pyvo | 1.1 |
| PyWavelets | 1.1.1 |
| PyYAML | 5.4.1 |
| pyzmq | 22.0.3 |
| qgrid | 1.3.1 |
| regex | 2021.4.4 |
| requests | 2.25.1 |
| requests-html | 0.10.0 |
| requests-oauthlib | 1.3.0 |
| retrying | 1.3.3 |
| rsa | 4.7.2 |
| ruamel-yaml-conda | 0.15.80 |
| ruamel.yaml | 0.16.12 |
| ruamel.yaml.clib | 0.2.2 |
| s3transfer | 0.4.2 |
| schwimmbad | 0.3.2 |
| scikit-image | 0.18.1 |
| scikit-learn | 0.24.2 |
| scipy | 1.6.3 |
| seaborn | 0.11.1 |
| SecretStorage | 3.3.1 |
| selenium | 3.141.0 |
| semver | 2.13.0 |
| Send2Trash | 1.5.0 |
| setuptools | 49.6.0.post20210108 |
| shellingham | 1.4.0 |
| six | 1.15.0 |
| sklearn | 0.0 |
| smart-open | 2.2.1 |
| sniffio | 1.2.0 |
| sortedcontainers | 2.3.0 |
| soupsieve | 2.0.1 |
| spacy | 3.0.6 |
| spacy-legacy | 3.0.5 |
| SQLAlchemy | 1.4.12 |
| srsly | 2.4.1 |
| statsmodels | 0.12.2 |
| sympy | 1.7.1 |
| tables | 3.6.1 |
| tblib | 1.7.0 |
| tensorboard | 2.4.1 |
| tensorboard-plugin-wit | 1.8.0 |
| tensorflow | 2.4.1 |
| tensorflow-estimator | 2.4.0 |
| termcolor | 1.1.0 |
| terminado | 0.9.4 |
| testpath | 0.4.4 |
| textblob | 0.15.3 |
| Theano-PyMC | 1.1.2 |
| thinc | 8.0.3 |
| threadpoolctl | 2.1.0 |
| tifffile | 2021.4.8 |
| tomlkit | 0.7.0 |
| toolz | 0.11.1 |
| torch | 1.8.0 |
| tornado | 6.1 |
| tqdm | 4.60.0 |
| traitlets | 5.0.5 |
| typer | 0.3.2 |
| typing-extensions | 3.7.4.3 |
| uncertainties | 3.1.5 |
| Unidecode | 1.2.0 |
| urllib3 | 1.26.4 |
| vincent | 0.4.4 |
| w3lib | 1.22.0 |
| wasabi | 0.8.2 |
| wcwidth | 0.2.5 |
| webencodings | 0.5.1 |
| websockets | 8.1 |
| Werkzeug | 1.0.1 |
| wheel | 0.36.2 |
| widgetsnbextension | 3.5.1 |
| wrapt | 1.12.1 |
| xarray | 0.18.2 |
| xlrd | 2.0.1 |
| yarl | 1.6.3 |
| zict | 2.0.0 |
| zipp | 3.4.1 |

via `conda list --no-pip`

| Package | Version |
| ----------------------------- | ------------------- |
| _libgcc_mutex | 0.1 |
| _openmp_mutex | 4.5 |
| abseil-cpp | 20210324.0 |
| absl-py | 0.12.0 |
| aiohttp | 3.7.4 |
| alembic | 1.5.8 |
| anyio | 2.2.0 |
| appdirs | 1.4.4 |
| argon2-cffi | 20.1.0 |
| arviz | 0.11.2 |
| asteval | 0.9.23 |
| astor | 0.8.1 |
| astroml | 0.4.1 |
| astroplan | 0.8 |
| astropy | 4.2.1 |
| astroquery | 0.4.2 |
| astunparse | 1.6.3 |
| async-timeout | 3.0.1 |
| async_generator | 1.10 |
| attrs | 20.3.0 |
| babel | 2.9.1 |
| backcall | 0.2.0 |
| backports | 1.0 |
| backports.functools_lru_cache | 1.6.4 |
| beautifulsoup4 | 4.9.3 |
| binutils_impl_linux-64 | 2.35.1 |
| binutils_linux-64 | 2.35 |
| biogeme | 3.2.6 |
| blas | 2.108 |
| blas-devel | 3.9.0 |
| bleach | 3.3.0 |
| blinker | 1.4 |
| blosc | 1.21.0 |
| bokeh | 2.3.1 |
| boto | 2.49.0 |
| boto3 | 1.17.86 |
| botocore | 1.20.86 |
| bottleneck | 1.3.2 |
| bounded-pool-executor | 0.0.3 |
| brotli | 1.0.9 |
| brotlipy | 0.7.0 |
| brunsli | 0.1 |
| bs4 | 0.0.1 |
| bz2file | 0.98 |
| bzip2 | 1.0.8 |
| c-ares | 1.17.1 |
| ca-certificates | 2021.5.30 |
| cached-property | 1.5.2 |
| cached_property | 1.5.2 |
| cachetools | 4.2.2 |
| catalogue | 2.0.4 |
| certifi | 2021.5.30 |
| certipy | 0.1.3 |
| cffi | 1.14.5 |
| cftime | 1.5.0 |
| chardet | 4.0.0 |
| charls | 2.2.0 |
| choicemodels | 0.2.2 |
| click | 7.1.2 |
| cloudpickle | 1.6.0 |
| colorama | 0.4.4 |
| conda | 4.10.0 |
| conda-package-handling | 1.7.3 |
| configurable-http-proxy | 4.3.2 |
| cryptography | 3.4.7 |
| cssselect | 1.1.0 |
| cudatoolkit | 11.2.2 |
| cudnn | 8.1.0.77 |
| curl | 7.76.1 |
| cycler | 0.10.0 |
| cymem | 2.0.5 |
| cython | 0.29.23 |
| cython-blis | 0.7.4 |
| cytoolz | 0.11.0 |
| dask | 2021.4.1 |
| dask-core | 2021.4.1 |
| dataclasses | 0.8 |
| dbus | 1.13.6 |
| decorator | 5.0.7 |
| defusedxml | 0.7.1 |
| deprecation | 2.1.0 |
| descartes | 1.1.0 |
| dill | 0.3.3 |
| distributed | 2021.4.1 |
| emcee | 3.0.2 |
| entrypoints | 0.3 |
| et_xmlfile | 1.0.1 |
| expat | 2.4.1 |
| fake-useragent | 0.1.11 |
| fastprogress | 1.0.0 |
| filelock | 3.0.12 |
| freetype | 2.10.4 |
| fsspec | 2021.4.0 |
| funcy | 1.16 |
| future | 0.18.2 |
| fuzzywuzzy | 0.18.0 |
| gast | 0.3.3 |
| gatspy | 0.3 |
| gcc_impl_linux-64 | 9.3.0 |
| gcc_linux-64 | 9.3.0 |
| gensim | 4.0.1 |
| gettext | 0.19.8.1 |
| giflib | 5.2.1 |
| glib | 2.68.2 |
| glib-tools | 2.68.2 |
| gmp | 6.2.1 |
| gmpy2 | 2.1.0b1 |
| google-api-core | 1.26.3 |
| google-auth | 1.30.0 |
| google-auth-oauthlib | 0.4.1 |
| google-cloud-core | 1.5.0 |
| google-cloud-storage | 1.31.2 |
| google-crc32c | 1.1.2 |
| google-pasta | 0.2.0 |
| google-resumable-media | 1.2.0 |
| googleapis-common-protos | 1.53.0 |
| greenlet | 1.0.0 |
| grpc-cpp | 1.37.1 |
| grpcio | 1.37.1 |
| gxx_impl_linux-64 | 9.3.0 |
| gxx_linux-64 | 9.3.0 |
| h5py | 2.10.0 |
| hdf4 | 4.2.15 |
| hdf5 | 1.10.6 |
| heapdict | 1.0.1 |
| hickle | 3.4.5 |
| html5lib | 1.1 |
| icu | 68.1 |
| idna | 2.10 |
| imagecodecs | 2021.3.31 |
| imageio | 2.9.0 |
| importlib-metadata | 4.0.1 |
| importlib_metadata | 4.0.1 |
| ipykernel | 5.5.3 |
| ipympl | 0.7.0 |
| ipython | 7.23.0 |
| ipython_genutils | 0.2.0 |
| ipywidgets | 7.6.3 |
| jax | 0.2.13 |
| jaxlib | 0.1.67 |
| jdcal | 1.4.1 |
| jedi | 0.18.0 |
| jeepney | 0.6.0 |
| jinja2 | 2.11.3 |
| jmespath | 0.10.0 |
| joblib | 1.0.1 |
| jpeg | 9d |
| json5 | 0.9.5 |
| jsonschema | 3.2.0 |
| jupyter-packaging | 0.9.2 |
| jupyter_client | 6.1.12 |
| jupyter_core | 4.7.1 |
| jupyter_server | 1.6.4 |
| jupyter_telemetry | 0.1.0 |
| jupyterhub | 1.3.0 |
| jupyterhub-base | 1.3.0 |
| jupyterlab | 3.0.14 |
| jupyterlab_pygments | 0.1.2 |
| jupyterlab_server | 2.5.0 |
| jupyterlab_widgets | 1.0.0 |
| jxrlib | 1.1 |
| keras-preprocessing | 1.1.2 |
| kernel-headers_linux-64 | 2.6.32 |
| keyring | 23.0.1 |
| kiwisolver | 1.3.1 |
| krb5 | 1.17.2 |
| lcms2 | 2.12 |
| ld_impl_linux-64 | 2.35.1 |
| lerc | 2.2.1 |
| libaec | 1.0.4 |
| libarchive | 3.5.1 |
| libblas | 3.9.0 |
| libcblas | 3.9.0 |
| libcrc32c | 1.1.1 |
| libcurl | 7.76.1 |
| libdeflate | 1.7 |
| libedit | 3.1.20191231 |
| libev | 4.33 |
| libffi | 3.3 |
| libgcc-devel_linux-64 | 9.3.0 |
| libgcc-ng | 9.3.0 |
| libgfortran-ng | 9.3.0 |
| libgfortran5 | 9.3.0 |
| libglib | 2.68.2 |
| libgomp | 9.3.0 |
| libgpuarray | 0.7.6 |
| libiconv | 1.16 |
| liblapack | 3.9.0 |
| liblapacke | 3.9.0 |
| libllvm10 | 10.0.1 |
| libnetcdf | 4.8.0 |
| libnghttp2 | 1.43.0 |
| libopenblas | 0.3.12 |
| libpng | 1.6.37 |
| libprotobuf | 3.15.8 |
| libsodium | 1.0.18 |
| libsolv | 0.7.18 |
| libssh2 | 1.9.0 |
| libstdcxx-devel_linux-64 | 9.3.0 |
| libstdcxx-ng | 9.3.0 |
| libtiff | 4.2.0 |
| libuv | 1.41.0 |
| libwebp-base | 1.2.0 |
| libxml2 | 2.9.10 |
| libxslt | 1.1.33 |
| libzip | 1.7.3 |
| libzopfli | 1.0.3 |
| llvm-openmp | 11.1.0 |
| llvmlite | 0.36.0 |
| lmfit | 1.0.2 |
| locket | 0.2.0 |
| lxml | 4.6.3 |
| lz4-c | 1.9.3 |
| lzo | 2.10 |
| magma | 2.5.4 |
| mako | 1.1.4 |
| mamba | 0.12.1 |
| markdown | 3.3.4 |
| markupsafe | 1.1.1 |
| matplotlib-base | 3.4.1 |
| matplotlib-inline | 0.1.2 |
| mistune | 0.8.4 |
| mizani | 0.7.3 |
| mkl | 2020.4 |
| mkl-devel | 2020.4 |
| mkl-include | 2020.4 |
| mkl-service | 2.3.0 |
| mock | 4.0.3 |
| mpc | 1.1.0 |
| mpfr | 4.0.2 |
| mpi | 1.0 |
| mpi4py | 3.0.3 |
| mpich | 3.4.2 |
| mpmath | 1.2.1 |
| msgpack-python | 1.0.2 |
| multidict | 5.1.0 |
| murmurhash | 1.0.5 |
| nbclassic | 0.2.7 |
| nbclient | 0.5.3 |
| nbconvert | 6.0.7 |
| nbformat | 5.1.3 |
| nbgitpuller | 0.9.0 |
| nbresuse | 0.3.3 |
| nccl | 2.9.9.1 |
| ncurses | 6.2 |
| nest-asyncio | 1.5.1 |
| netcdf4 | 1.5.6 |
| networkx | 2.5 |
| ninja | 1.10.2 |
| nltk | 3.6.2 |
| nodejs | 15.14.0 |
| notebook | 6.3.0 |
| numba | 0.53.1 |
| numexpr | 2.7.3 |
| numpy | 1.20.2 |
| oauthlib | 3.0.1 |
| olefile | 0.46 |
| openblas | 0.3.12 |
| openjpeg | 2.4.0 |
| openpyxl | 3.0.7 |
| openssl | 1.1.1k |
| opt_einsum | 3.3.0 |
| packaging | 20.9 |
| palettable | 3.3.0 |
| pamela | 1.0.0 |
| pandas | 1.2.4 |
| pandoc | 2.12 |
| pandocfilters | 1.4.2 |
| parse | 1.19.0 |
| parso | 0.8.2 |
| partd | 1.2.0 |
| pathy | 0.5.2 |
| patsy | 0.5.1 |
| pcre | 8.44 |
| pexpect | 4.8.0 |
| photutils | 1.2.0.dev72+g97224d92 |
| pickleshare | 0.7.5 |
| pillow | 8.1.2 |
| pip | 21.1.1 |
| plotly | 4.14.3 |
| plotnine | 0.8.0 |
| pooch | 1.3.0 |
| pqdm | 0.1.0 |
| preshed | 3.0.5 |
| prometheus_client | 0.10.1 |
| prompt-toolkit | 3.0.18 |
| protobuf | 3.15.8 |
| psutil | 5.8.0 |
| ptyprocess | 0.7.0 |
| pyasn1 | 0.4.8 |
| pyasn1-modules | 0.2.7 |
| pycosat | 0.6.3 |
| pycparser | 2.20 |
| pycurl | 7.43.0.6 |
| pydantic | 1.7.3 |
| pyee | 8.1.0 |
| pyerfa | 1.7.3 |
| pygments | 2.8.1 |
| pygpu | 0.7.6 |
| pyjwt | 2.1.0 |
| pyldavis | 3.3.1 |
| pylogit | 1.0.1 |
| pymc3 | 3.11.2 |
| pyopenssl | 20.0.1 |
| pyparsing | 2.4.7 |
| pyppeteer | 0.2.5 |
| pyquery | 1.4.3 |
| pyrsistent | 0.17.3 |
| pysocks | 1.7.1 |
| pytables | 3.6.1 |
| python | 3.8.8 |
| python-dateutil | 2.8.1 |
| python-editor | 1.0.4 |
| python-flatbuffers | 1.12 |
| python-json-logger | 2.0.1 |
| python-mimeparse | 1.6.0 |
| python_abi | 3.8 |
| pytorch | 1.8.0 |
| pytz | 2021.1 |
| pyvo | 1.1 |
| pywavelets | 1.1.1 |
| pyyaml | 5.4.1 |
| pyzmq | 22.0.3 |
| qgrid | 1.3.1 |
| re2 | 2021.04.01 |
| readline | 8.1 |
| regex | 2021.4.4 |
| reproc | 14.2.1 |
| reproc-cpp | 14.2.1 |
| requests | 2.25.1 |
| requests-html | 0.10.0 |
| requests-oauthlib | 1.3.0 |
| retrying | 1.3.3 |
| rsa | 4.7.2 |
| ruamel.yaml | 0.16.12 |
| ruamel.yaml.clib | 0.2.2 |
| ruamel_yaml | 0.15.80 |
| s3transfer | 0.4.2 |
| schwimmbad | 0.3.2 |
| scikit-image | 0.18.1 |
| scikit-learn | 0.24.2 |
| scipy | 1.6.3 |
| seaborn | 0.11.1 |
| seaborn-base | 0.11.1 |
| secretstorage | 3.3.1 |
| selenium | 3.141.0 |
| semver | 2.13.0 |
| send2trash | 1.5.0 |
| setuptools | 49.6.0 |
| shellingham | 1.4.0 |
| six | 1.15.0 |
| sklearn | 0.0 |
| sleef | 3.5.1 |
| smart_open | 2.2.1 |
| snappy | 1.1.8 |
| sniffio | 1.2.0 |
| sortedcontainers | 2.3.0 |
| soupsieve | 2.0.1 |
| spacy | 3.0.6 |
| spacy-legacy | 3.0.5 |
| sqlalchemy | 1.4.12 |
| sqlite | 3.35.5 |
| srsly | 2.4.1 |
| statsmodels | 0.12.2 |
| sympy | 1.7.1 |
| sysroot_linux-64 | 2.12 |
| tblib | 1.7.0 |
| tensorboard | 2.4.1 |
| tensorboard-plugin-wit | 1.8.0 |
| tensorflow | 2.4.1 |
| tensorflow-base | 2.4.1 |
| tensorflow-estimator | 2.4.0 |
| termcolor | 1.1.0 |
| terminado | 0.9.4 |
| testpath | 0.4.4 |
| textblob | 0.15.3 |
| theano-pymc | 1.1.2 |
| thinc | 8.0.3 |
| threadpoolctl | 2.1.0 |
| tifffile | 2021.4.8 |
| tini | 0.18.0 |
| tk | 8.6.10 |
| tomlkit | 0.7.0 |
| toolz | 0.11.1 |
| tornado | 6.1 |
| tqdm | 4.60.0 |
| traitlets | 5.0.5 |
| typer | 0.3.2 |
| typing-extensions | 3.7.4.3 |
| typing_extensions | 3.7.4.3 |
| uncertainties | 3.1.5 |
| unidecode | 1.2.0 |
| urllib3 | 1.26.4 |
| vincent | 0.4.4 |
| w3lib | 1.22.0 |
| wasabi | 0.8.2 |
| wcwidth | 0.2.5 |
| webencodings | 0.5.1 |
| websockets | 8.1 |
| werkzeug | 1.0.1 |
| wheel | 0.36.2 |
| widgetsnbextension | 3.5.1 |
| wrapt | 1.12.1 |
| xarray | 0.18.2 |
| xlrd | 2.0.1 |
| xz | 5.2.5 |
| yaml | 0.2.5 |
| yarl | 1.6.3 |
| zeromq | 4.3.4 |
| zfp | 0.5.5 |
| zict | 2.0.0 |
| zipp | 3.4.1 |
| zlib | 1.2.11 |
| zstd | 1.4.9 |