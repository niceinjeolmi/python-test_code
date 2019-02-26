#coding:utf8
from pymongo import MongoClient
import datetime

client = MongoClient("10.10.10.243", 27017)
db = client.projects
project = "circle"
date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
item = {"name":"강아지",
	"text":"강이는 어떻게 울지",
	"tags":["멍멍", "왈왈"],
	"date":date,
}
db[project].insert_one(item)
