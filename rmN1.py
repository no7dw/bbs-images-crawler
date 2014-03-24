#!/usr/local/bin/python
import os
import sys
import re
dirlist= os.listdir(sys.argv[1])
for element_dir in dirlist:
	if os.path.isdir('./'+ element_dir):
		p='thread-\d+-1-\d+.html'
		m=re.match(p, element_dir)
		if m:
			print 'Match : \t\t\t' +element_dir
		else:
		 	os.system('rm  -r '+element_dir)
			print 'rm -r '+element_dir
