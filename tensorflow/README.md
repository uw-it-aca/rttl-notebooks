# UW-IT JupyterHub for Teaching Tensorflow notebook
Docker image for UW-IT JupyterHub for Teaching Tensorflow notebook. 
- Detailed information about base Tensorflow notebook is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-tensorflow-notebook
- General information about working with base images is here: https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html
- Installed packages and versions can be viewed in this image's [Dockerfile](Dockerfile) using `pip list` or `conda list`. Output from both command's output is also shown below for convenience.
- The JupyterLab (v4.0.10) interface is installed and is set as default

#### Running notebook locally
- `docker run -p 8888:8888 us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-tensorflow-notebook:2.4.0-B`
- Console output will include localhost url with access token. Add '/lab' to the end of the path portion, eg: `http://127.0.0.1:8888/lab`

#### Accessing server shell locally
- `docker run -it --entrypoint /bin/bash us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-tensorflow-notebook:2.4.0-B`

#### Installed packages
via `pip list`

| Package | Version |
| ----------------------------- | ------------------- |
|absl-py|1.4.0|
|aiofiles|22.1.0|
|aiohttp|3.7.4.post0|
|aiosqlite|0.18.0|
|alembic|1.9.4|
|altair|4.2.2|
|ansi2html|0.0.0|
|anyio|3.6.2|
|appdirs|1.4.4|
|argon2-cffi|21.3.0|
|argon2-cffi-bindings|21.2.0|
|arrow|1.2.3|
|arviz|0.11.1|
|asdf|2.15.0|
|asdf-astropy|0.4.0|
|asdf-coordinates-schemas|0.2.0|
|asdf-standard|1.0.3|
|asdf-transform-schemas|0.3.0|
|asdf-unit-schemas|0.1.0|
|asdf-wcs-schemas|0.1.1|
|asteval|0.9.29|
|astroML|1.0.2.post1|
|astroplan|0.8|
|astropy|5.2.2|
|astroquery|0.4.6|
|asttokens|2.2.1|
|astunparse|1.6.3|
|async-generator|1.10|
|async-timeout|3.0.1|
|attrs|22.2.0|
|Babel|2.12.1|
|backcall|0.2.0|
|backports.functools-lru-cache|1.6.4|
|beautifulsoup4|4.12.2|
|biogeme|3.2.11|
|bleach|6.0.0|
|blinker|1.6.2|
|blis|0.7.9|
|bokeh|3.1.0|
|boltons|23.0.0|
|Bottleneck|1.3.7|
|bounded-pool-executor|0.0.3|
|Brotli|1.0.9|
|brotlipy|0.7.0|
|bs4|0.0.1|
|cached-property|1.5.2|
|cachetools|5.3.0|
|catalogue|2.0.8|
|certifi|2023.5.7|
|certipy|0.1.3|
|cffi|1.15.1|
|cftime|1.6.2|
|chardet|4.0.0|
|charset-normalizer|3.1.0|
|choicemodels|0.2.2|
|click|8.1.3|
|cloudpickle|2.2.1|
|colorama|0.4.6|
|comm|0.1.3|
|commonmark|0.9.1|
|conda|23.3.1|
|conda-package-handling|2.0.2|
|conda\_package\_streaming|0.7.0|
|confection|0.0.4|
|contourpy|1.0.7|
|coverage|7.2.5|
|cryptography|40.0.2|
|cssselect|1.2.0|
|cycler|0.11.0|
|cymem|2.0.7|
|Cython|0.29.34|
|cythonbiogeme|1.0.1|
|cytoolz|0.12.0|
|dash|2.9.3|
|dask|2023.4.0|
|dataclasses|0.8|
|debugpy|1.6.7|
|decorator|5.1.1|
|defusedxml|0.7.1|
|dill|0.3.6|
|distributed|2023.4.0|
|emcee|3.1.4|
|entrypoints|0.4|
|et-xmlfile|1.1.0|
|exceptiongroup|1.1.1|
|executing|1.2.0|
|fake-useragent|1.1.3|
|fastjsonschema|2.16.3|
|fastprogress|1.0.3|
|filelock|3.9.0|
|Flask|2.2.3|
|Flask-Compress|1.13|
|flatbuffers|23.1.21|
|flit\_core|3.8.0|
|fonttools|4.39.3|
|fqdn|1.5.1|
|fsspec|2023.4.0|
|funcy|2.0|
|future|0.18.3|
|fuzzywuzzy|0.18.0|
|gast|0.4.0|
|gatspy|0.3|
|gensim|4.3.1|
|gmpy2|2.1.2|
|google-auth|2.17.3|
|google-auth-oauthlib|0.4.6|
|google-pasta|0.2.0|
|greenlet|2.0.2|
|grpcio|1.51.1|
|gwcs|0.18.3|
|h11|0.14.0|
|h5py|3.8.0|
|HeapDict|1.0.1|
|hickle|3.4.5|
|html5lib|1.1|
|hypothesis|6.75.2|
|idna|3.4|
|imagecodecs|2023.1.23|
|imageio|2.27.0|
|importlib-metadata|6.4.1|
|importlib-resources|5.12.0|
|iniconfig|2.0.0|
|ipykernel|6.22.0|
|ipympl|0.9.3|
|ipython|8.12.0|
|ipython-genutils|0.2.0|
|ipywidgets|8.0.6|
|isoduration|20.11.0|
|itsdangerous|2.1.2|
|jaraco.classes|3.2.3|
|jedi|0.18.2|
|jeepney|0.8.0|
|Jinja2|3.1.2|
|jmespath|1.0.1|
|joblib|1.2.0|
|json5|0.9.5|
|jsonpatch|1.32|
|jsonpointer|2.0|
|jsonschema|4.17.3|
|jupyter\_client|8.2.0|
|jupyter\_core|5.3.0|
|jupyter-dash|0.4.2|
|jupyter-events|0.6.3|
|jupyter-resource-usage|0.7.1|
|jupyter\_server|2.5.0|
|jupyter\_server\_fileid|0.9.0|
|jupyter\_server\_terminals|0.4.4|
|jupyter\_server\_ydoc|0.8.0|
|jupyter-telemetry|0.1.0|
|jupyter-ydoc|0.2.3|
|jupyterhub|3.1.1|
|jupyterlab|3.6.3|
|jupyterlab-pygments|0.2.2|
|jupyterlab\_server|2.22.1|
|jupyterlab-widgets|3.0.7|
|keras|2.11.0|
|Keras-Preprocessing|1.1.2|
|keyring|23.13.1|
|kiwisolver|1.4.4|
|langcodes|3.3.0|
|lazy\_loader|0.2|
|libmambapy|1.4.2|
|llvmlite|0.39.1|
|lmfit|1.2.1|
|locket|1.0.0|
|lxml|4.9.2|
|lz4|4.3.2|
|Mako|1.2.4|
|mamba|1.4.2|
|Markdown|3.4.3|
|MarkupSafe|2.1.2|
|matplotlib|3.7.1|
|matplotlib-inline|0.1.6|
|mistune|2.0.5|
|mizani|0.9.0|
|more-itertools|9.1.0|
|mpmath|1.3.0|
|msgpack|1.0.5|
|multidict|6.0.4|
|munkres|1.1.4|
|murmurhash|1.0.9|
|nbclassic|0.5.5|
|nbclient|0.7.3|
|nbconvert|7.3.1|
|nbformat|5.8.0|
|nbgitpuller|1.1.1|
|nest-asyncio|1.5.6|
|netCDF4|1.6.3|
|networkx|3.1|
|nltk|3.8.1|
|notebook|6.5.4|
|notebook\_shim|0.2.2|
|numba|0.56.4|
|numexpr|2.8.4|
|numpy|1.24.3|
|oauthlib|3.2.2|
|openpyxl|3.1.1|
|opt-einsum|3.3.0|
|outcome|1.2.0|
|packaging|23.1|
|pamela|1.0.0|
|pandas|2.0.0|
|pandocfilters|1.5.0|
|parse|1.19.0|
|parso|0.8.3|
|partd|1.4.0|
|pathy|0.10.1|
|patsy|0.5.3|
|pexpect|4.8.0|
|photutils|1.7.0|
|pickleshare|0.7.5|
|Pillow|9.5.0|
|pip|23.1|
|pkgutil\_resolve\_name|1.3.10|
|platformdirs|2.6.0|
|plotly|5.14.1|
|plotnine|0.12.1|
|pluggy|1.0.0|
|pooch|1.7.0|
|pqdm|0.2.0|
|preshed|3.0.8|
|prometheus-client|0.16.0|
|prompt-toolkit|3.0.38|
|protobuf|4.21.12|
|psutil|5.9.4|
|ptyprocess|0.7.0|
|pure-eval|0.2.2|
|py-cpuinfo|9.0.0|
|pyarrow|11.0.0|
|pyasn1|0.4.8|
|pyasn1-modules|0.2.7|
|pycosat|0.6.4|
|pycparser|2.21|
|pycurl|7.45.1|
|pydantic|1.9.2|
|pyee|8.2.2|
|pyerfa|2.0.0.3|
|Pygments|2.15.0|
|pygpu|0.7.6|
|PyJWT|2.6.0|
|pyLDAvis|3.4.1|
|pylogit|1.0.1|
|pymc3|3.9.3|
|pyOpenSSL|23.1.1|
|pyparsing|3.0.9|
|pyppeteer|1.0.2|
|pyquery|2.0.0|
|pyrsistent|0.19.3|
|PySocks|1.7.1|
|pytest|7.3.1|
|pytest-arraydiff|0.3|
|pytest-astropy|0.10.0|
|pytest-astropy-header|0.1.2|
|pytest-cov|4.0.0|
|pytest-doctestplus|0.12.1|
|pytest-filter-subpackage|0.1.1|
|pytest-mock|3.10.0|
|pytest-openfiles|0.5.0|
|pytest-remotedata|0.4.0|
|python-dateutil|2.8.2|
|python-json-logger|2.0.7|
|pytz|2023.3|
|pyu2f|0.1.5|
|pyvo|1.4.1|
|PyWavelets|1.4.1|
|PyYAML|6.0|
|pyzmq|25.0.2|
|qgrid|1.3.1|
|regex|2023.5.5|
|requests|2.28.2|
|requests-html|0.10.0|
|requests-oauthlib|1.3.1|
|retrying|1.3.3|
|rfc3339-validator|0.1.4|
|rfc3986-validator|0.1.1|
|rich|12.4.1|
|rsa|4.9|
|ruamel.yaml|0.17.21|
|ruamel.yaml.clib|0.2.7|
|scikit-image|0.20.0|
|scikit-learn|1.2.2|
|scipy|1.10.1|
|seaborn|0.12.2|
|SecretStorage|3.3.3|
|selenium|4.9.1|
|semantic-version|2.10.0|
|Send2Trash|1.8.0|
|setuptools|67.6.1|
|setuptools-scm|7.1.0|
|shellingham|1.5.1|
|six|1.16.0|
|smart-open|5.2.1|
|sniffio|1.3.0|
|sortedcontainers|2.4.0|
|soupsieve|2.3.2.post1|
|spacy|3.5.2|
|spacy-legacy|3.0.12|
|spacy-loggers|1.0.4|
|SQLAlchemy|1.4.46|
|srsly|2.4.6|
|stack-data|0.6.2|
|statsmodels|0.14.0|
|sympy|1.11.1|
|tables|3.8.0|
|tblib|1.7.0|
|tenacity|8.2.2|
|tensorboard|2.11.2|
|tensorboard-data-server|0.6.1|
|tensorboard-plugin-wit|1.8.1|
|tensorflow|2.11.1|
|tensorflow-estimator|2.11.0|
|termcolor|2.2.0|
|terminado|0.17.1|
|textblob|0.15.3|
|Theano|1.0.5|
|thinc|8.1.10|
|threadpoolctl|3.1.0|
|tifffile|2023.4.12|
|tinycss2|1.2.1|
|toml|0.10.2|
|tomli|2.0.1|
|tomlkit|0.11.8|
|toolz|0.12.0|
|torch|2.0.1+cpu|
|torchaudio|2.0.2+cpu|
|torchvision|0.15.2+cpu|
|tornado|6.2|
|tqdm|4.65.0|
|traitlets|5.9.0|
|trio|0.21.0|
|trio-websocket|0.10.2|
|typer|0.7.0|
|typing-extensions|3.10.0.2|
|tzdata|2023.3|
|uncertainties|3.1.7|
|unicodedata2|15.0.0|
|Unidecode|1.3.6|
|uri-template|1.2.0|
|urllib3|1.26.15|
|w3lib|2.1.1|
|wasabi|1.1.1|
|wcwidth|0.2.6|
|webcolors|1.13|
|webencodings|0.5.1|
|websocket-client|1.5.1|
|websockets|10.4|
|Werkzeug|2.2.3|
|wheel|0.40.0|
|widgetsnbextension|4.0.7|
|wrapt|1.15.0|
|wsproto|1.2.0|
|xarray|2023.4.2|
|xlrd|2.0.1|
|xyzservices|2023.2.0|
|y-py|0.5.9|
|yarl|1.8.2|
|ypy-websocket|0.8.2|
|zict|2.2.0|
|zipp|3.15.0|
|zstandard|0.19.0|

via `conda list --no-pip`

| Package | Version |
| ----------------------------- | ------------------- |
|\_libgcc\_mutex|0.1|
|\_openmp\_mutex|4.5|
|absl-py|1.4.0|
|aiofiles|22.1.0|
|aiohttp|3.7.4.post0|
|aiosqlite|0.18.0|
|alembic|1.9.4|
|altair|4.2.2|
|ansi2html|1.8.0|
|anyio|3.6.2|
|aom|3.5.0|
|appdirs|1.4.4|
|argon2-cffi|21.3.0|
|argon2-cffi-bindings|21.2.0|
|arrow|1.2.3|
|arrow-cpp|11.0.0|
|arviz|0.11.1|
|asdf|2.15.0|
|asdf-astropy|0.4.0|
|asdf-coordinates-schemas|0.2.0|
|asdf-standard|1.0.3|
|asdf-transform-schemas|0.3.0|
|asdf-unit-schemas|0.1.0|
|asdf-wcs-schemas|0.1.1|
|asteval|0.9.29|
|astroml|1.0.2.post1|
|astroplan|0.8|
|astropy|5.2.2|
|astroquery|0.4.6|
|asttokens|2.2.1|
|astunparse|1.6.3|
|async-timeout|3.0.1|
|async\_generator|1.10|
|attrs|22.2.0|
|aws-c-auth|0.6.24|
|aws-c-cal|0.5.20|
|aws-c-common|0.8.11|
|aws-c-compression|0.2.16|
|aws-c-event-stream|0.2.18|
|aws-c-http|0.7.4|
|aws-c-io|0.13.17|
|aws-c-mqtt|0.8.6|
|aws-c-s3|0.2.4|
|aws-c-sdkutils|0.1.7|
|aws-checksums|0.1.14|
|aws-crt-cpp|0.19.7|
|aws-sdk-cpp|1.10.57|
|babel|2.12.1|
|backcall|0.2.0|
|backports|1.0|
|backports.functools\_lru\_cache|1.6.4|
|backports.zoneinfo|0.2.1|
|beautifulsoup4|4.12.2|
|binutils\_impl\_linux-64|2.39|
|binutils\_linux-64|2.39|
|biogeme|3.2.11|
|blas|2.116|
|blas-devel|3.9.0|
|bleach|6.0.0|
|blinker|1.6.2|
|blosc|1.21.3|
|bokeh|3.1.0|
|boltons|23.0.0|
|bottleneck|1.3.7|
|bounded-pool-executor|0.0.3|
|brotli|1.0.9|
|brotli-bin|1.0.9|
|brotli-python|1.0.9|
|brotlipy|0.7.0|
|brunsli|0.1|
|bs4|0.0.1|
|bzip2|1.0.8|
|c-ares|1.18.1|
|c-blosc2|2.8.0|
|ca-certificates|2023.5.7|
|cached-property|1.5.2|
|cached\_property|1.5.2|
|cachetools|5.3.0|
|catalogue|2.0.8|
|certifi|2023.5.7|
|certipy|0.1.3|
|cffi|1.15.1|
|cfitsio|4.2.0|
|cftime|1.6.2|
|chardet|4.0.0|
|charls|2.4.1|
|charset-normalizer|3.1.0|
|choicemodels|0.2.2|
|click|8.1.3|
|cloudpickle|2.2.1|
|colorama|0.4.6|
|comm|0.1.3|
|commonmark|0.9.1|
|conda|23.3.1|
|conda-package-handling|2.0.2|
|conda-package-streaming|0.7.0|
|confection|0.0.4|
|configurable-http-proxy|4.5.4|
|contourpy|1.0.7|
|coverage|7.2.5|
|cryptography|40.0.2|
|cssselect|1.2.0|
|curl|8.0.1|
|cycler|0.11.0|
|cymem|2.0.7|
|cython|0.29.34|
|cython-blis|0.7.9|
|cythonbiogeme|1.0.1|
|cytoolz|0.12.0|
|dash|2.9.3|
|dask|2023.4.0|
|dask-core|2023.4.0|
|dataclasses|0.8|
|dav1d|1.0.0|
|dbus|1.13.6|
|debugpy|1.6.7|
|decorator|5.1.1|
|defusedxml|0.7.1|
|dill|0.3.6|
|distributed|2023.4.0|
|emcee|3.1.4|
|entrypoints|0.4|
|et\_xmlfile|1.1.0|
|exceptiongroup|1.1.1|
|executing|1.2.0|
|expat|2.5.0|
|fake-useragent|1.1.3|
|fastprogress|1.0.3|
|filelock|3.9.0|
|flask|2.2.3|
|flask-compress|1.13|
|flatbuffers|23.3.3|
|flit-core|3.8.0|
|fmt|9.1.0|
|fonttools|4.39.3|
|fqdn|1.5.1|
|freetype|2.12.1|
|fsspec|2023.4.0|
|funcy|2.0|
|future|0.18.3|
|fuzzywuzzy|0.18.0|
|gast|0.4.0|
|gatspy|0.3|
|gcc\_impl\_linux-64|10.4.0|
|gcc\_linux-64|10.4.0|
|gensim|4.3.1|
|gettext|0.21.1|
|gflags|2.2.2|
|giflib|5.2.1|
|glog|0.6.0|
|gmp|6.2.1|
|gmpy2|2.1.2|
|google-auth|2.17.3|
|google-auth-oauthlib|0.4.6|
|google-pasta|0.2.0|
|greenlet|2.0.2|
|grpcio|1.51.1|
|gwcs|0.18.3|
|gxx\_impl\_linux-64|10.4.0|
|gxx\_linux-64|10.4.0|
|h11|0.14.0|
|h5py|3.8.0|
|hdf4|4.2.15|
|hdf5|1.14.0|
|heapdict|1.0.1|
|hickle|3.4.5|
|html5lib|1.1|
|hypothesis|6.75.2|
|icu|72.1|
|idna|3.4|
|imagecodecs|2023.1.23|
|imageio|2.27.0|
|importlib-metadata|6.4.1|
|importlib-resources|5.12.0|
|importlib\_metadata|6.4.1|
|importlib\_resources|5.12.0|
|iniconfig|2.0.0|
|ipykernel|6.22.0|
|ipympl|0.9.3|
|ipython|8.12.0|
|ipython\_genutils|0.2.0|
|ipywidgets|8.0.6|
|isoduration|20.11.0|
|itsdangerous|2.1.2|
|jaraco.classes|3.2.3|
|jedi|0.18.2|
|jeepney|0.8.0|
|jinja2|3.1.2|
|jmespath|1.0.1|
|joblib|1.2.0|
|json5|0.9.5|
|jsonpatch|1.32|
|jsonpointer|2.0|
|jsonschema|4.17.3|
|jupyter-dash|0.4.2|
|jupyter-resource-usage|0.7.1|
|jupyter\_client|8.2.0|
|jupyter\_core|5.3.0|
|jupyter\_events|0.6.3|
|jupyter\_server|2.5.0|
|jupyter\_server\_fileid|0.9.0|
|jupyter\_server\_terminals|0.4.4|
|jupyter\_server\_ydoc|0.8.0|
|jupyter\_telemetry|0.1.0|
|jupyter\_ydoc|0.2.3|
|jupyterhub|3.1.1|
|jupyterhub-base|3.1.1|
|jupyterlab|3.6.3|
|jupyterlab\_pygments|0.2.2|
|jupyterlab\_server|2.22.1|
|jupyterlab\_widgets|3.0.7|
|jxrlib|1.1|
|keras|2.11.0|
|keras-preprocessing|1.1.2|
|kernel-headers\_linux-64|2.6.32|
|keyring|23.13.1|
|keyutils|1.6.1|
|kiwisolver|1.4.4|
|krb5|1.20.1|
|langcodes|3.3.0|
|lazy\_loader|0.2|
|lcms2|2.15|
|ld\_impl\_linux-64|2.39|
|lerc|4.0.0|
|libabseil|20220623.0|
|libaec|1.0.6|
|libarchive|3.6.2|
|libarrow|11.0.0|
|libavif|0.11.1|
|libblas|3.9.0|
|libbrotlicommon|1.0.9|
|libbrotlidec|1.0.9|
|libbrotlienc|1.0.9|
|libcblas|3.9.0|
|libcrc32c|1.1.2|
|libcurl|8.0.1|
|libdeflate|1.18|
|libedit|3.1.20191231|
|libev|4.33|
|libevent|2.1.10|
|libexpat|2.5.0|
|libffi|3.4.2|
|libgcc-devel\_linux-64|10.4.0|
|libgcc-ng|12.2.0|
|libgfortran-ng|12.2.0|
|libgfortran5|12.2.0|
|libglib|2.76.2|
|libgomp|12.2.0|
|libgoogle-cloud|2.7.0|
|libgpuarray|0.7.6|
|libgrpc|1.51.1|
|libiconv|1.17|
|libjpeg-turbo|2.1.5.1|
|liblapack|3.9.0|
|liblapacke|3.9.0|
|libllvm11|11.1.0|
|libmamba|1.4.2|
|libmambapy|1.4.2|
|libnetcdf|4.9.2|
|libnghttp2|1.52.0|
|libnsl|2.0.0|
|libnuma|2.0.16|
|libopenblas|0.3.21|
|libpng|1.6.39|
|libprotobuf|3.21.12|
|libsanitizer|10.4.0|
|libsodium|1.0.18|
|libsolv|0.7.23|
|libsqlite|3.40.0|
|libssh2|1.10.0|
|libstdcxx-devel\_linux-64|10.4.0|
|libstdcxx-ng|12.2.0|
|libthrift|0.18.0|
|libtiff|4.5.0|
|libutf8proc|2.8.0|
|libuuid|2.38.1|
|libuv|1.44.2|
|libwebp-base|1.3.0|
|libxcb|1.13|
|libxml2|2.10.4|
|libxslt|1.1.37|
|libzip|1.9.2|
|libzlib|1.2.13|
|libzopfli|1.0.3|
|llvm-openmp|16.0.1|
|llvmlite|0.39.1|
|lmfit|1.2.1|
|locket|1.0.0|
|lxml|4.9.2|
|lz4|4.3.2|
|lz4-c|1.9.4|
|lzo|2.10|
|mako|1.2.4|
|mamba|1.4.2|
|markdown|3.4.3|
|markupsafe|2.1.2|
|matplotlib-base|3.7.1|
|matplotlib-inline|0.1.6|
|mistune|2.0.5|
|mizani|0.9.0|
|more-itertools|9.1.0|
|mpc|1.3.1|
|mpfr|4.2.0|
|mpmath|1.3.0|
|msgpack-python|1.0.5|
|multidict|6.0.4|
|munkres|1.1.4|
|murmurhash|1.0.9|
|nbclassic|0.5.5|
|nbclient|0.7.3|
|nbconvert|7.3.1|
|nbconvert-core|7.3.1|
|nbconvert-pandoc|7.3.1|
|nbformat|5.8.0|
|nbgitpuller|1.1.1|
|ncurses|6.3|
|nest-asyncio|1.5.6|
|netcdf4|1.6.3|
|networkx|3.1|
|nltk|3.8.1|
|nodejs|16.19.0|
|nomkl|1.0|
|notebook|6.5.4|
|notebook-shim|0.2.2|
|numba|0.56.4|
|numexpr|2.8.4|
|numpy|1.24.3|
|oauthlib|3.2.2|
|openblas|0.3.21|
|openjpeg|2.5.0|
|openpyxl|3.1.1|
|openssl|3.1.0|
|opt\_einsum|3.3.0|
|orc|1.8.2|
|outcome|1.2.0|
|packaging|23.1|
|pamela|1.0.0|
|pandas|2.0.0|
|pandoc|2.19.2|
|pandocfilters|1.5.0|
|parquet-cpp|1.5.1|
|parse|1.19.0|
|parso|0.8.3|
|partd|1.4.0|
|pathy|0.10.1|
|patsy|0.5.3|
|pcre2|10.40|
|pexpect|4.8.0|
|photutils|1.7.0|
|pickleshare|0.7.5|
|pillow|9.5.0|
|pip|23.1|
|pkgutil-resolve-name|1.3.10|
|platformdirs|2.6.0|
|plotly|5.14.1|
|plotnine|0.12.1|
|pluggy|1.0.0|
|pooch|1.7.0|
|pqdm|0.2.0|
|preshed|3.0.8|
|prometheus\_client|0.16.0|
|prompt-toolkit|3.0.38|
|prompt\_toolkit|3.0.38|
|protobuf|4.21.12|
|psutil|5.9.4|
|pthread-stubs|0.4|
|ptyprocess|0.7.0|
|pure\_eval|0.2.2|
|py-cpuinfo|9.0.0|
|pyarrow|11.0.0|
|pyasn1|0.4.8|
|pyasn1-modules|0.2.7|
|pybind11-abi|4|
|pycosat|0.6.4|
|pycparser|2.21|
|pycurl|7.45.1|
|pydantic|1.9.2|
|pyee|8.2.2|
|pyerfa|2.0.0.3|
|pygments|2.15.0|
|pygpu|0.7.6|
|pyjwt|2.6.0|
|pyldavis|3.4.1|
|pylogit|1.0.1|
|pymc3|3.9.3|
|pyopenssl|23.1.1|
|pyparsing|3.0.9|
|pyppeteer|1.0.2|
|pyquery|2.0.0|
|pyrsistent|0.19.3|
|pysocks|1.7.1|
|pytables|3.8.0|
|pytest|7.3.1|
|pytest-arraydiff|0.3|
|pytest-astropy|0.10.0|
|pytest-astropy-header|0.1.2|
|pytest-cov|4.0.0|
|pytest-doctestplus|0.12.1|
|pytest-filter-subpackage|0.1.1|
|pytest-mock|3.10.0|
|pytest-openfiles|0.5.0|
|pytest-remotedata|0.4.0|
|python|3.10.10|
|python-dateutil|2.8.2|
|python-fastjsonschema|2.16.3|
|python-flatbuffers|23.1.21|
|python-json-logger|2.0.7|
|python-tzdata|2023.3|
|python\_abi|3.10|
|pytz|2023.3|
|pyu2f|0.1.5|
|pyvo|1.4.1|
|pywavelets|1.4.1|
|pyyaml|6.0|
|pyzmq|25.0.2|
|qgrid|1.3.1|
|re2|2023.02.01|
|readline|8.2|
|regex|2023.5.5|
|reproc|14.2.4|
|reproc-cpp|14.2.4|
|requests|2.28.2|
|requests-html|0.10.0|
|requests-oauthlib|1.3.1|
|retrying|1.3.3|
|rfc3339-validator|0.1.4|
|rfc3986-validator|0.1.1|
|rich|12.4.1|
|rsa|4.9|
|ruamel.yaml|0.17.21|
|ruamel.yaml.clib|0.2.7|
|s2n|1.3.37|
|scikit-image|0.20.0|
|scikit-learn|1.2.2|
|scipy|1.10.1|
|seaborn|0.12.2|
|seaborn-base|0.12.2|
|secretstorage|3.3.3|
|selenium|4.9.1|
|semantic\_version|2.10.0|
|send2trash|1.8.0|
|setuptools|67.6.1|
|setuptools-scm|7.1.0|
|shellingham|1.5.1|
|six|1.16.0|
|smart\_open|5.2.1|
|snappy|1.1.10|
|sniffio|1.3.0|
|sortedcontainers|2.4.0|
|soupsieve|2.3.2.post1|
|spacy|3.5.2|
|spacy-legacy|3.0.12|
|spacy-loggers|1.0.4|
|sqlalchemy|1.4.46|
|srsly|2.4.6|
|stack\_data|0.6.2|
|statsmodels|0.14.0|
|sympy|1.11.1|
|sysroot\_linux-64|2.12|
|tblib|1.7.0|
|tenacity|8.2.2|
|tensorboard|2.11.2|
|tensorboard-data-server|0.6.1|
|tensorboard-plugin-wit|1.8.1|
|tensorflow|2.11.1|
|tensorflow-base|2.11.1|
|tensorflow-estimator|2.11.1|
|termcolor|2.2.0|
|terminado|0.17.1|
|textblob|0.15.3|
|theano|1.0.5|
|thinc|8.1.10|
|threadpoolctl|3.1.0|
|tifffile|2023.4.12|
|tinycss2|1.2.1|
|tk|8.6.12|
|toml|0.10.2|
|tomli|2.0.1|
|tomlkit|0.11.8|
|toolz|0.12.0|
|torch|2.0.1+cpu|
|torchaudio|2.0.2+cpu|
|torchvision|0.15.2+cpu|
|tornado|6.2|
|tqdm|4.65.0|
|traitlets|5.9.0|
|trio|0.21.0|
|trio-websocket|0.10.2|
|typer|0.7.0|
|typing-extensions|3.10.0.2|
|typing\_extensions|3.10.0.2|
|tzdata|2023c|
|ucx|1.14.0|
|uncertainties|3.1.7|
|unicodedata2|15.0.0|
|unidecode|1.3.6|
|uri-template|1.2.0|
|urllib3|1.26.15|
|w3lib|2.1.1|
|wasabi|1.1.1|
|wcwidth|0.2.6|
|webcolors|1.13|
|webencodings|0.5.1|
|websocket-client|1.5.1|
|websockets|10.4|
|werkzeug|2.2.3|
|wheel|0.40.0|
|widgetsnbextension|4.0.7|
|wrapt|1.15.0|
|wsproto|1.2.0|
|xarray|2023.4.2|
|xlrd|2.0.1|
|xorg-libxau|1.0.9|
|xorg-libxdmcp|1.1.3|
|xyzservices|2023.2.0|
|xz|5.2.6|
|y-py|0.5.9|
|yaml|0.2.5|
|yaml-cpp|0.7.0|
|yarl|1.8.2|
|ypy-websocket|0.8.2|
|zeromq|4.3.4|
|zfp|1.0.0|
|zict|2.2.0|
|zipp|3.15.0|
|zlib|1.2.13|
|zlib-ng|2.0.7|
|zstandard|0.19.0|
|zstd|1.5.2|

