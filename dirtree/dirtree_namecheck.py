# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 09:27:59 2014

@author: ngordon

# best solution! http://lorenzod8n.wordpress.com/2007/12/11/creating-a-tree-utility-in-python-part-1/
    Prints all files and directories given a root directory with the file and directory size
"""

def print_tree(path,part1,indent=' '):
    # recursiveley prints the contents of a directory
    # checks the file names in the directory
    import os
    for x2 in os.listdir(path): # x is file or folder
        fullpath = path + '/' + x2      
        V = x2.find('V') 
        if V != -1 and x2[V+1].isnumeric(): # is there a part found in the filename
            #print('x2=%s' % x2)
            part2 = x2[V:V+14]
            if part1 != part2: # check if master part name matches sub partname
                print('warning! part1= %s <> part2=%s ' % (part1,part2) )
        if os.path.isfile(fullpath):
            ' '
            #print('%s     %s    ' % (indent,x ) )            
        else:   # os.path.isdir
            #print('%s  ./%s ' % (indent,x ) )
            print_tree(fullpath,part1,indent + '   |')

def paste():
    # copies string from clipboard
    import tkinter
    tk = tkinter.Tk()
    tk.withdraw()
    val = tk.clipboard_get()
    tk.destroy()
    return val

# Either select the filepath for the 'Work Directory' 
#   or a partname subdirectory
def namechk():
    import os
    # accepts input from windows clipboard
    dir1 = paste()    
    dir1.replace('\\','/')   # supposed to change the windows backslash to linux forward slash    
    print('\n %s \n' % (dir1))    
    basedir = os.path.basename(dir1)
    print('base directory = %s \n'%basedir)
    
    # loop through all folders and check part names
    if basedir == 'Work Directory':
        for x1 in os.listdir(dir1): # x is file or folder
            dirx1 = dir1 + '/' + x1      
            V = x1.find('V') 
            if V!=-1 and x1[V+1].isnumeric():
                part1 = x1[V:V+14]
                print('\n----  master file name = %s ----' % part1) 
                print_tree(dirx1,part1,' ') 
            else:
                print('\n no master part found in %s, exiting' % x1)
                return
                          
    # only check a single part folder
    else:    
        
        V = basedir.find('V') 
        if V!=-1 and basedir[V+1].isnumeric():
            part1 = basedir[V:V+14]
            print('\n----  master file name = %s ----' % part1) 
            print_tree(dir1,part1,' ') 
        else:
            print('no master part found, exiting')
            return
           
namechk()
