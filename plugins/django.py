#!/usr/bin/python
import sys
import urllib2
import os

url = os.environ['url']
category = os.environ.get('graph_category',"")

if len(sys.argv) == 2:
    url = url + "?" + sys.argv[1] + "=1"
    print urllib2.urlopen(url).read()
    # they can set the category in the config
    if category != "":
        print "graph_category " + category
else:
    data = urllib2.urlopen(url).readlines()
    for line in data:
        parts = line.split(" ")
        label = parts[0]
        value = " ".join(parts[1:])
        print label + ".value " + value 
        
