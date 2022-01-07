APP_BIN?=app

.PHONY: default
default: build

DOCKER_REPO?=gcr.io/uwit-mci-axdd/rttl-datascience-notebook
DOCKER_TAG?=latest_1-4-2

build:
	docker $(DOCKER_REPO):$(DOCKER_TAG) .

push: build
	docker push $(DOCKER_REPO):$(DOCKER_TAG)
