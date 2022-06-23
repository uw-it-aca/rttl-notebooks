# RTTL Jupyter RStudio notebook image
All notable changes to the RStudio Jupyter Notebook image will be documented here. 

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.3.5-upwardbound] - 2022-06-22

### NOTE: This is a custom image for Upward Bound Statistics course

### Added
- [openintro](https://cran.r-project.org/web/packages/openintro/index.html)
- [fivethirtyeight & fivethirtyeightdata](https://cran.r-project.org/web/packages/fivethirtyeight/vignettes/fivethirtyeight.html)
- [palmerpenguins](https://cloud.r-project.org/web/packages/palmerpenguins/index.html)
- [ggridges](https://cran.r-project.org/web/packages/ggridges/index.html)
- [janitor](https://cran.r-project.org/web/packages/janitor/index.html)
- [statsr](https://cran.r-project.org/web/packages/statsr/index.html)
- [broom](https://cran.r-project.org/web/packages/broom/index.html)
- [dsbox](https://github.com/rstudio-education/dsbox)
- [unvotes](https://cran.r-project.org/web/packages/unvotes/index.html)
- [lubridate](https://cran.r-project.org/web/packages/lubridate/index.html)
- [DT](https://cran.r-project.org/web/packages/DT/index.html)
- [scales](https://cran.r-project.org/web/packages/scales/index.html)
- [glue](https://cran.r-project.org/web/packages/glue/index.html)
- [shiny](https://cran.r-project.org/web/packages/shiny/index.html)
- [reactable](https://cran.r-project.org/web/packages/reactable/index.html)
- [mobpack](https://github.com/vjcitn/mobpack) `devtools::install_github("vjcitn/mobpack")`
- [skimr](https://cran.r-project.org/web/packages/skimr/index.html)

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
