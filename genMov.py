#!/usr/bin/env python
#coding:utf8

#설계
#1. 폴더를 탐색한다. "/project/circle/in/aces_exr"
#2. exr로 proxy jpg를 만든다. "/tmp/proxy/project/circle"
#3. proxy jpg로 proxy mov를 만든다.
#4. proxy jpg를 삭제한다.
import os

def serchItem(root):
	"""
	rootpath 경로에서 ext확장자를 가진 파일 경로를 list로 반환한다.
	"""
	seqs = []
	for subdir in os.listdir(root):
		shot = []
		for f in os.listdir(root+"/"+subdir):
			shot.append("/".join([root, subdir, f]))
		shot.sort()
		seqs.append(shot)
	return seqs

def createFolder(directory):
	"""
	proxy 폴더를 생성한다.
	"""
	try:
		if not os.path.exists(directory):
			os.makedirs(directory)
	except OSError:
		print ('Error: Creating directory.' + directory)

def ImageMagick(item):
	"""
	file 리스트를 받으면 proxy경로에 프록시 이미지를 생성한다.
	"""
	for i in item:
		cmd = ["convert %s/%s/%s/%s %s/%s/%s/%s" % (i, i.replace(".exr",".jpg"))]
		print cmd
		#os.system(cmd)
			
if __name__ == "__main__":
	root = "/project/circle/in/aces_exr"
	directory = "/tmp/proxy/project/circle"
	item = serchItem(root)
	ImageMagick(item)
	#print len(serchItem(root))
	#print createFolder(directory)


"""
if not os.path.exists("/tmp/proxy/project/circle")
	os.mkdir("/tmp/proxy/project/circle")

	ROOT = "/project/circle/in"
	def checkRoot():
		#/project/circle/in  폴더가 존재하는지 체크한다.
		global ROOT
		if not os.path.exists(ROOT)
			return "/project/circle/in 폴더가 존재하지 않습니다." % (ROOT)
		return None

	def ImageMagick():
	


	def genMov():
		jpg를 mov로 만든다.
		for i in os.listdir("/project/circle/in")
"""		
