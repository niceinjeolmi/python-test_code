#coding:utf8
from pymongo import MongoClient

client = MongoClient("10.10.10.243", 27017)
db = client.projects
project = "circle"

result = db[project].delete_many({"name": "배석대"})
result = db[project].delete_many({"name": "BAR_0010"})
print(result)
