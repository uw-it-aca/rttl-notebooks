# RTTL Jupyter SciPy notebook image
All notable changes to the SciPy Jupyter Notebook image will be documented here. 

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.4.2] - 2023-06-09

## Changed
- Added octave, gfortran, and opencv

## [2.4.0] - 2023-06-05

### Changed
- Changed upstream base notebook to jupyter/scipy-notebook:hub-3.1.1, which is based on Ubuntu 22.04 and includes many package updates.

## [2.3] - 2022-02-03

### Changed
- Version major.minor numbering now tracks with rttl-admin tool
- Moved images to Google Artifact Registry

## [1.4.2] - 2021-12-23

### Changed
- Increased version for upstream base notebook: jupyter/scipy-notebook:hub-1.4.2
- Supports JupyterHub v1.4.2
- Update to JupyterLab v3.2.2
- Upgrade SciPy version to 1.7.1

### Added
- Added astroalign package


### Fixed
- Fixed issue with nbclassic by pinning to 0.2.8
- Fixed issue with biogeme package

## [1.3.0] - 2021-06.14

### Changed
- Increased version for upstream base notebook: jupyter/scipy-notebook:hub-1.3.0