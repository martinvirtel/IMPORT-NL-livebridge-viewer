#! /usr/bin/env python3

import yaml
import json
import sys
import os
import datetime
import copy

_here=os.path.split(__file__)[0]

infile=open(os.path.join(_here,"../../config/control-live.yaml"))

fixedbridges=json.loads("""
  {
  "source_id"   :  "575838e8c158bd068b69e832",
  "label"     : "test-test",
  "endpoint"  : "https://dpa-api.liveblog.pro/api/",
      "targets" : [
            { "type": "scribble",
              "event_id" : "2116258",
              "auth": "admin"
            }
      ]

  }
""")


def main() :
    bridges=yaml.load(infile)["bridges"]
    with open(os.path.join(_here,"../html/bridges.json"),"w") as outfile:
        br=copy.deepcopy(bridges)
        br.append(fixedbridges)
        outfile.write(json.dumps({ 'bridges' : bridges},indent=1))
        sys.stderr.write("{} bridges copied from {} to {}\n".format(len(bridges),infile.name,outfile.name))
    with open(os.path.join(_here,"../html/marketplace.json"),"w") as outfile:
        cbr=[
            {
              'title'      : br.get("label"," - untitled -"),
              '_id'        : br.get("source_id"),
              'endpoint'   : br.get("endpoint"),
              'public_url' : "https://dpa.liveblog.pro/dpa/blogs/{source_id}/index.html".format(**br),
              'ed_note'    : br.get("ed_note",""),
              'startdate'  : br.get("startdate")
            }
            for br in bridges
            if "startdate" in br
        ]
        json.dump({ '_meta': { "total" : len(cbr),
                               "page" : 1,
                               "max_results" : len(cbr) },
                    '_items' : cbr},outfile)
        sys.stderr.write("{} bridges copied to {}\n".format(len(cbr),outfile.name))



if __name__=="__main__" :
    main()
