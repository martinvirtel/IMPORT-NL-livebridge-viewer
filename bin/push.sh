#! /bin/bash
export AWS_DEFAULT_PROFILE=dpa
export AWS_DEFAULT_REGION=eu-west-1


cd `dirname $0`/..

aws s3 --region=eu-west-1 --acl=public-read sync html/  s3://demo.dpa-newslab.com/livebridge/
