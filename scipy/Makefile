APP_BIN?=app

.PHONY: default
default: build

DOCKER_REPO?=gcr.io/uwit-mci-axdd/rttl-scipy-notebook
DOCKER_TAG?=d990a62010ae

build:
	docker build -t $(DOCKER_REPO):latest -t $(DOCKER_REPO):$(DOCKER_TAG) .

push: build
	docker push $(DOCKER_REPO):$(DOCKER_TAG)
	docker push $(DOCKER_REPO):latest
