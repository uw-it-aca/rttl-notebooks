APP_BIN?=app

.PHONY: default
default: build

DOCKER_REPO?=us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-scipy-notebook
DOCKER_TAG?=2.4.4-B

build:
	docker build -t $(DOCKER_REPO):$(DOCKER_TAG) .

push: build
	docker push $(DOCKER_REPO):$(DOCKER_TAG)
