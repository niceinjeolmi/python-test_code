#coding:utf8
import redis

r = redis.Redis(host="10.10.10.172", port=6379)
r.set("kimhanwoong","0109411706")
r.set("kwondoyoung","01040106742")
#print r.get("rendercount")
#for i in range(1000):
#	r.incr("rendercount")
print r.get("baeseoyoung")
print r.get("kwondoyoung")
