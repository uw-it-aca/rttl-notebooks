# RTTL Jupyter datascience notebook image
All notable changes to the datascience Jupyter Notebook image will be documented here. 

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.8.0] - 2025-10-13

### Added
- Added Jupyter accessibility checker extension, jupyterlab-a11y-checker
- Added wrapper for nbgitpuller to prevent pod spawn failures. If errors are encountered a document will be added in the user's home directory.

### Changed
- Updated base image to use tag "Hub 5.4.0" which includes updating base OS to Ubuntu 24.04 and Python 3.13. See: [Changelog](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/changelog.html) for Docker Stacks.
- NumPy is updated to 2.3.3 as versions lower than v2 are no longer supported with Python 3.13+. (Note: NumPy 2 contained breaking changes from v1.x, so some packages may encounter compatibility issues)

## [2.7.1] - 2025-02-18

### Changed
- Pinned NumPy to < 2 due to dependency conflicts with newer verions
- Unpinned Plotly
- Moved to using dependency tree output for README

## [2.7.0] - 2024-11-24

### Changed
- Revert to jupyter/docker-stacks base images.
- Version jump to align all RTTL image versions.
- Moved package lists to separate files.

### Updated
- Changed upstream base notebook to quay.io/jupyter/datascience-notebook:hub-4.1.5. See [build manifest](https://github.com/jupyter/docker-stacks/wiki/x86_64-default-datascience-notebook-996fae1248fc). 
- JupyterLab v4.2.0
- Jupyter Notebook v7.2.0
- Python v3.11.9

## [2.4.0-B] - 2024-01-11

### Fixed
- An issue with image streaming from Artifact Registry required switching to rebuilt [jupyter-docker-stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html) images without any WORKDIR statements (which can cause duplicate layers to be created).

## [2.4.0] - 2023-06-05

### Changed
- Changed upstream base notebook to jupyter/datascience-notebook:hub-3.1.1, which is based on Ubuntu 22.04 and includes many package updates.

## [2.3] - 2022-02-03

### Changed
- ~~Version major.minor numbering now tracks with rttl-admin tool~~
- Moved images to Google Artifact Registry

## [1.4.2] - 2021-12-23

### Changed
- Increased version for upstream base notebook: jupyter/datascience-notebook:hub-1.4.2
- Supports JupyterHub v1.4.2
- Update to JupyterLab v3.2.2

### Added
- Added geopandas, folium, and ipyleaflet packages

## [1.3.0] - 2021-06.14

### Changed
- Increased version for upstream base notebook: jupyter/datascience-notebook:hub-1.3.0