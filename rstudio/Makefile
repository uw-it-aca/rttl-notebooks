APP_BIN?=app

.PHONY: default
default: build

DOCKER_REPO?=gcr.io/uwit-mci-axdd/rttl-rstudio-notebook
DOCKER_TAG?=alpha-1.0

build:
	docker build -t $(DOCKER_REPO):latest -t $(DOCKER_REPO):$(DOCKER_TAG) .

push: build
	docker push $(DOCKER_REPO):latest
