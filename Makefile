SHELL := /bin/bash


update-bridges:
	bin/update-bridges.py

push-livebridge-view:
	bin/push.sh

push-livebridge-config:
	aws --profile=liveblog --region=eu-central-1 s3 cp ./config/control-live.yaml s3://newslab-livebridge/control-live.yaml 

pull-livebridge-config:
	aws --profile=liveblog --region=eu-central-1 s3 cp s3://newslab-livebridge/control-live.yaml ./config/control-live.yaml 
