SHELL := /bin/bash

JSON_TARGETS = html/bridges.json html/marketplace.json

YAML_SOURCE = config/control-live.yaml

all: test push-livebridge-view push-livebridge-config

test: 
	export TESTYAML=/tmp/$$(basename $(YAML_SOURCE))-test; \
	test "$$(grep _id $(YAML_SOURCE) | sort | uniq --repeated | tee $$TESTYAML | wc -l)" != "0"  && { \
	echo "DUPLICATE IDS!"; cat $$TESTYAML ; rm $$TESTYAML; exit 1 ; } ;\
	rm -f $$TESTYAML

$(JSON_TARGETS): $(YAML_SOURCE)
	bin/update-bridges.py

push-livebridge-view: $(JSON_TARGETS)
	bin/push.sh

push-livebridge-config: backup-livebridge-config
	aws --profile=liveblog --region=eu-central-1 s3 sync $$(dirname $(YAML_SOURCE)) s3://newslab-livebridge/

pull-livebridge-config:
	aws --profile=liveblog --region=eu-central-1 s3 cp s3://newslab-livebridge/control-live.yaml $(YAML_SOURCE)

backup-livebridge-config:
	aws --profile=liveblog --region=eu-central-1 s3 cp s3://newslab-livebridge/control-live.yaml backup/$$(basename $(YAML_SOURCE))-backup-$$(date +%Y%m%d%H%M%S)
