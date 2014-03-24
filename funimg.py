#!/usr/bin/python
import re
import os
import string
import sys
#(might need to change)
p=re.compile('.*<img.*src=\".*.jpg\"', re.I)

def downloadpic(filename):
	#read from the filename
	text=open(filename,'r').readlines()
	for element in text:
		m=re.match(p,element)
		if m:
			#get the real url of pic from m 
			url=m.group()
			i=string.find(url,"src=")			
			url_sub=url[i+4+1:-1]
			j=string.rfind(url,"/")
			jpgfile=url[j+1:-1]
			if not os.path.exists(jpgfile):
				#max retry 3 times
				os.system('wget '+url_sub+' --tries=3 &' )
				print url_sub
			else:
				print "exists already", jpgfile

