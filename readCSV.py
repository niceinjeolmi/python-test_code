#!/usr/bin/env python
#coding:utf8
import os
import csv

csvPath = os.path.expanduser("~/examples/csv/cglist.csv")
with open(csvPath) as csvFile:
	csvReader = csv.reader(csvFile, delimiter=',')
	for row in list(csvReader)[1:]:
		print(row)
