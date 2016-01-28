# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 13:39:29 2014

@author: ngordon
"""

def print_tree(path,indent=' '):
    # when dirsize=True, the directory size is calculated, but can take a long time!
    # recursiveley prints the contents of a directory
    import os
    for file in os.listdir(path):
        fullpath = path + '/' + file              
        if os.path.isfile(fullpath):
            print('%s     %s  ' % (indent,file ) )
        else:   # os.path.isdir
            print('%s  ./%s ' % (indent,file ) )
            print_tree(fullpath,indent + '   |')
            
def all_files(path,indent=' '):
    # when dirsize=True, the directory size is calculated, but can take a long time!
    # recursiveley prints the contents of a directory
    files = []
    for file in os.listdir(path):
        fullpath = os.path.join(path,file)
        if os.path.isfile(fullpath):
            print('%s     %s  ' % (indent,file ) )
            files.append(file)
        else:   # os.path.isdir
            print('%s  ./%s ' % (indent,file ) )
            print_tree(fullpath,indent + '   |')            

