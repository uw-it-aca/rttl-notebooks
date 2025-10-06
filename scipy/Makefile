APP_BIN?=app

.PHONY: default
default: build

DOCKER_REPO?=us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/jupyter-scipy-notebook
DOCKER_TAG?=2.7-local

build:
	docker build -t $(DOCKER_REPO):$(DOCKER_TAG) .
	# Optional --no-cache

push: build
	docker push $(DOCKER_REPO):$(DOCKER_TAG)
