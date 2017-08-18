SHELL := /bin/bash

JSON_TARGETS = html/bridges.json html/marketplace.json

YAML_SOURCE = config/control-live.yaml

all: push-livebridge-view push-livebridge-config

$(JSON_TARGETS): $(YAML_SOURCE)
	bin/update-bridges.py

push-livebridge-view: $(JSON_TARGETS)
	bin/push.sh

push-livebridge-config:
	aws --profile=liveblog --region=eu-central-1 s3 cp $(YAML_SOURCE) s3://newslab-livebridge/

pull-livebridge-config:
	aws --profile=liveblog --region=eu-central-1 s3 cp s3://newslab-livebridge/control-live.yaml $(YAML_SOURCE)
