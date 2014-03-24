#!/usr/local/bin/python
import os
import sys
pre='/home/dengwei/gunzombie'
def walkdir(dirname):
	
	dirlist=os.listdir(dirname)
	for element_dir in dirlist:
		walkname = str(dirname) +'/'+ str(element_dir)
		
		if os.path.isdir(walkname):
			walkdir(walkname)
		else:
			filename1 = walkname
			filename2 = filename1[0:23]+'2'+filename1[23:]
			#print filename1
			#print filename2

			print 'diff '+filename1+' ' + filename2
			os.system('diff '+filename1+' ' + filename2)
walkdir(pre)
