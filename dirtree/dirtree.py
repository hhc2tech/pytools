# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 09:27:59 2014

@author: ngordon

# best solution! http://lorenzod8n.wordpress.com/2007/12/11/creating-a-tree-utility-in-python-part-1/
    Prints all files and directories given a root directory with the file and directory size
"""

def getSize(path):
    import os
    #http://stackoverflow.com/questions/15218192/efficient-python-function-to-find-the-size-of-the-directory
    totalSize = 0
    if os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for fName in filenames:
                fp = os.path.join(dirpath, fName)
                totalSize += os.path.getsize(fp)
        return totalSize
    else:
        return os.path.getsize(path)

def print_tree(path,indent=' ',dirsize = True):
    # when dirsize=True, the directory size is calculated, but can take a long time!
    # recursiveley prints the contents of a directory
    import os
    for file in os.listdir(path):
        sz = 0 # declare dafualt file/directory size
        fullpath = path + '/' + file              
        
        if os.path.isfile(fullpath):
            sz = getSize(fullpath)  /1000
            print('%s     %s     %.0f kb' % (indent,file,sz ) )
        else:   # os.path.isdir
            if dirsize:
                sz = getSize(fullpath)  /1000
                print('%s  ./%s   %.0f kb' % (indent,file,sz ) )
            else:
                print('%s  ./%s ' % (indent,file ) )
            print_tree(fullpath,indent + '   |')

''' # incomplete feature #
    create feature that allows for only dirctories to be shown
'''
            
''' # incomplete feature #
def createHTML():
    # create an html file with links to the files and directories
    import os
    h = open("videos.html", 'w')
    for vid in os.listdir:
        path = "./t" + vid
        f = open(path, r)
        h.write("<a href='"+f.name+"'>"+f.name[f.name.rfind('\\') +1 :]+"</a>")
        f.close()
    h.close()
    print("done writing HTML file")
'''

def paste():
    # copies string from clipboard
    import tkinter
    tk = tkinter.Tk()
    tk.withdraw()
    val = tk.clipboard_get()
    tk.destroy()
    return val
    
def tree():
    # accepts input from windows clipboard
    dir1 = paste()    
    dir1.replace('\\','/')   # supposed to change the windows backslash to linux forward slash    
    print('\n %s \n' % (dir1))
    print_tree(dir1)
    