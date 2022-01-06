# RTTL Jupyter RStudio notebook image
All notable changes to the RStudio Jupyter Notebook image will be documented here. 

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
