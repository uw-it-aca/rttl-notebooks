# RTTL Jupyter RStudio notebook image
All notable changes to the RStudio Jupyter Notebook image will be documented here. 

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
- Version major.minor numbering now tracks with rttl-admin tool
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
