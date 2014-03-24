#!/usr/bin/python
import re
import os
import sys
import funimg
#BBS url  (might need to change)
url_pre='http://xxxxx.com/bbs'
#sub html in hte list (might need to change)
p='<a\shref=\"thread-\d+-\d+-\d+.html\">'

def usage():
	print  sys.argv[0]+' filepath'

def getpicfromhtml(htmlpath):

	text=open(htmlpath,'r').readlines()
	print "try to analyst", htmlpath
	line=0
	for element in text:
		m=re.findall(p, element)
		if m:
			try:
				for element_m in m:
					#get the real relative url in element_m (might need to change)
					url=element_m[9:-2]
					
					print url
					dirname=url
					if not os.path.exists(dirname):
						os.makedirs(dirname)

					os.chdir(dirname)
					url_sub=url_pre+dirname
					print "get" ,url_sub
					os.system('GET '+ url_sub+' HTTP/1.1'+ ' > '+ 'htmlfile')
					funimg.downloadpic('./htmlfile')
					print url_sub
					#go back to parent (might need to change)
					os.chdir('..')
			except Exception:
				pass
	#	else:
	#		print 'find no match'

#get max 5 pages from bbs
htmlindex=1
while htmlindex<=5:
	htmlfilename='page'+str(htmlindex)
	#forum list url (might need to change)
	html_url=url_pre+'forum-4-'+str(htmlindex)+'.html'
	print html_url
	if not os.path.exists(htmlfilename):
		#download the pagefile to a file name: pagex (x is stand for page index)
		print 'GET '+ html_url+' HTTP/1.1'+ ' > '+ htmlfilename
		os.system('GET '+ html_url+' HTTP/1.1'+ ' > '+ htmlfilename)
	getpicfromhtml('./page'+str(htmlindex))
	htmlindex=htmlindex+1
