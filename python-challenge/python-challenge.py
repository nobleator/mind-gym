#http://www.pythonchallenge.com/pc/def/map.html
from string import maketrans
def levelOne(st):
	inSt = "abcdefghijklmnopqrstuvwxyz"
	outSt = "cdefghijklmnopqrstuvwxyzab"
	trans = maketrans(inSt, outSt)
	return st.translate(trans)
	
#print(levelOne("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."))
#print(levelOne("http://www.pythonchallenge.com/pc/def/map.html"))

#"http://www.pythonchallenge.com/pc/def/ocr.html"
import urllib2
def levelTwo(st):
	page = urllib2.urlopen(st)
	source = page.read()
	return "".join(ch for ch in source if ch.isalnum())
	
#print(levelTwo("http://www.pythonchallenge.com/pc/def/ocr.html"))

#http://www.pythonchallenge.com/pc/def/equality.html
import re
def levelThree(st):
	page = urllib2.urlopen(st)
	source = page.read()
	return "".join(ele[4] for ele in re.findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]', source))
	
#print(levelThree("http://www.pythonchallenge.com/pc/def/equality.html"))

#http://www.pythonchallenge.com/pc/def/linkedlist.php
def levelFour():
	link = str(12345)
	count = 0
	while count < 400:
		link = getNextChain("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + link)
		count += 1
	return link

def getNextChain(st):
	page = urllib2.urlopen(st)
	source = page.read()
	print(source)
	res = "".join(ch for ch in source if ch.isdigit())
	return res

#print(levelFour("http://www.pythonchallenge.com/pc/def/linkedlist.php"))
#print(levelFour())

#http://www.pythonchallenge.com/pc/def/peak.html
import pickle
def levelFive():
	pickleObj = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
	pyObj = pickle.loads(pickleObj)
	res = ""
	for ele1 in pyObj:
		for ele2 in ele1:
			res += ele2[0]*ele2[1]
	return res
	
#print(levelFive())

#http://www.pythonchallenge.com/pc/def/channel.html
def levelSix():
# Comment in source code <!-- <-- zip --> 
# Missing an ending --> ?
	return None

print(levelSix())