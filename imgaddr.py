#!/usr/bin/python
import re
import os
#p=re.compile('.html')
p=re.compile('<img\ssrc=\".*.jpg\"')
text=open('imglist.txt.2','r').readlines()
print len(text)
for element in text:
	m=re.match(p,element)
	if m:
		url=m.group()
		url_sub=url[10:-1]
#		os.system('wget '+url_sub+' &' )
		print url_sub
	#else:
	#	print element
