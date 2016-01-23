# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 10:36:28 2014
@author: Neal

used to add a z to the beginning of the last pdf to 
force it to be last when naturally sorted
"""

import os

curdir = os.getcwd()
def findbackmatter(indir):
    for dirname in os.listdir(indir):
        os.chdir(indir+'/'+dirname)
        for filename in os.listdir(os.getcwd()):
            firstind = filename.find('BookBackMatter')
            if firstind !=  -1:
                newfilename = filename[:firstind]+'z'+filename[firstind:]
                os.rename(filename, newfilename)  
        os.chdir(indir)
	os.chdir(curdir)
	
dir1 = 'C:/Users/Neal/Desktop/booktest1/'        
findbackmatter(dir1)

