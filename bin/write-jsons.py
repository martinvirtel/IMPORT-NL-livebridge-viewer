#! /usr/bin/env python3
# coding: utf-8
import yaml
import json
import sys
import os
import datetime
import copy


#-   endpoint: https://dpa-api.liveblog.pro/api/
#    label: Landtagswahl in Hessen
#    source_id: 5b9f7005eaff1d014e405431
#    startdate: 2018-10-28T14:00:00+0200
#    targets:
#    -   auth: admin
#        event_id: '2813673'
#        syndication_code: FCA8384B-6B23-48BC-9E12-D5F3EF8C2E97
#        type: scribble


#http -v https://s3.eu-central-1.amazonaws.com/dpa-newslab-prototype-webspace/dpalive/livebridge/actives/571a3509a505e600f7195af8.json
#
#
#{
#    "active": true,
#    "ed_note": "Testticker für dpa.",
#    "endpoint": "https://dpa-live-dev.dpa-newslab.com/api/",
#    "label": "Test-Ticker",
#    "public_url": "https://dpa.liveblog.pro/dpa/blogs/571a3509a505e600f7195af8/index.html",
#    "scribblelive_id": "2024120",
#    "slug": "test-ticker-571a3509a505e600f7195af8",
#    "source_id": "571a3509a505e600f7195af8",
#    "startdate": "2020-12-15T15:00:00+0200",
#    "tickaroo_id": "58514026e4b08f124d8e26e6_571a3509a505e600f7195af8"
#}




_here=os.path.split(__file__)[0]

infile=open(os.path.join(_here,"../../config/control-live.yaml"))


def main() :
    bridges=yaml.load(infile)["bridges"]
    for br in bridges:
        cbr={
              'label'      : br.get("label"," - untitled -"),
              'source_id'  : br.get("source_id"),
              'public_url' : "https://dpa.liveblog.pro/dpa/blogs/{source_id}/index.html".format(**br),
              'ed_note'    : br.get("ed_note",""),
              'startdate'  : br.get("startdate"),
              'scribblelive_syndication_code': [ a.get("syndication_code","") for a in br["targets"] ][0],
              'tickaroo_id' : "58514026e4b08f124d8e26e6_{source_id}".format(**br)
            }
        with open(os.path.join(_here,"../config-out/{source_id}.json".format(**br)),"w") as outfile:
            outfile.write(json.dumps(cbr))
            sys.stderr.write("{} written\n".format(repr(outfile)))



if __name__=="__main__" :
    main()
