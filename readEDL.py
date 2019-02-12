#!/usr/env python
#coding:utf8
import os
from edl import Parser

home = os.path.expanduser("~")
parser=Parser('23.98')
with open(home+'/examples/edl/lazypic_example.edl') as f:
	edl=parser.parse(f)
	for event in edl.events:
		print "Event Number:"+str(event.num)
		print "Sourse file:"+str(event.source_file)
		print "Clip Name:"+str(event.clip_name)
