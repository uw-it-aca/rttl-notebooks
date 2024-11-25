# RTTL Jupyter RStudio notebook image
All notable changes to the RStudio Jupyter Notebook image will be documented here. 

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.7.0] - 2024-11-24

### Fixed
- RStudio help pane links bug (see: https://github.com/jupyterhub/jupyter-rsession-proxy/issues/156)

### Changed
- Revert to jupyter/docker-stacks base images.
- Version jump to align all RTTL image versions.

### Updated
- Changed upstream base notebook to quay.io/jupyter/r-notebook:hub-4.1.5. See [build manifest](https://github.com/jupyter/docker-stacks/wiki/x86_64-default-r-notebook-996fae1248fc). 
- JupyterLab v4.2.0
- Jupyter Notebook v7.2.0
- Python v3.11.9
- R v4.3.3
- RStudio v2023.12.1 Build 402

## [2.6.1-B] - 2024-02-12

### Updated
- Updated to latest version of RStudio Server [rstudio-server-2023.12.1-402](https://posit.co/download/rstudio-server/)

## Fixed
- Fixed download and R package install issues in the RStudio console.

## [2.5.0-B] - 2024-01-11

### Fixed
- An issue with image streaming from Artifact Registry required switching to rebuilt [jupyter-docker-stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html) images without any WORKDIR statements (which can cause duplicate layers to be created).

## [2.5.0] - 2023-06-05

### Changed
- Changed upstream base notebook to jupyter/r-notebook:hub-3.1.1, which is based on Ubuntu 22.04 and includes many package updates.
- Updated RStudio server to rstudio-server-2023.03.0-386-amd64
- Updated R to version 4.2.3 (2023-03-15)

## [2.4.6] - 2023-03-24

### Added
- R packages: statnet, igraph

### Changed
- Using suid-wrapper to set sticky bit on RStudio binary is no longer needed (or supported) in image streaming on GKE 1.24+

## [2.4.1] - 2022-09-20

### Added
- R packages: mosaic, lubridate, janitor, scales, infer, skimr

## [2.4.0] - 2022-09-15

### Added
- Updated RStudio Server to v2022.07.1+554, which includes support for Quarto documents.

## [2.3.5] - 2022-05-17

### Added
- Added CMake util and nloptr package for RStudio

## [2.3.4] - 2022-04-08

### Fixed
- Bug with tidyverse package and timedatectl in containers. See: https://skeptric.com/tidyverse-timedatectl-wsl2/

## [2.3.3] - 2022-03-14

### Added
- Added Keras & TensorFlow packages for RStudio

### Updated
- Updated RStudio server version: 2022.02.0-443-amd64

## [2.3.2] - 2022-02-18

### Added
- Added R packages: gstat, spatial, spdep, spatialreg

## [2.3.1] - 2022-02-04

### Fixed
- Fixed RStudio startup issue when container image is streamed

## [2.3] - 2022-02-03

### Added
- Added R package: fastr2

### Changed
- ~~Version major.minor numbering now tracks with rttl-admin tool~~
- Moved images to Google Artifact Registry

### Fixed
- Issue that prevented R builtin help from rendering

## [1.4.2] - 2021-12-23

### Changed
- Increased version for upstream base notebook: jupyter/r-notebook:hub-1.4.2
- Supports JupyterHub v1.4.2
- Update to JupyterLab v3.2.2
- Update RStudio Server version 2021.09.1 Build 372 
- Update R to v4.1.1

### Fixed
- Fixed issue with repr package leading to broken help output
- Fixed issue preventing nbgitpuller from working
