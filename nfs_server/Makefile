APP_BIN?=app

.PHONY: default
default: build

DOCKER_REPO?=us-west1-docker.pkg.dev/uwit-mci-axdd/rttl-images/nfs-server
DOCKER_TAG?=0-local

build:
	docker build -t $(DOCKER_REPO):$(DOCKER_TAG) .

push: build
	docker push $(DOCKER_REPO):$(DOCKER_TAG)
