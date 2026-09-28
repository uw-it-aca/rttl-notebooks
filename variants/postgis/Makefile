.PHONY: default
default: build

DOCKER_REPO?=us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-datascience-notebook
DOCKER_TAG?=2.9.1-postgis

build:
	docker build -t $(DOCKER_REPO):$(DOCKER_TAG) .

push: build
	docker push $(DOCKER_REPO):$(DOCKER_TAG)
