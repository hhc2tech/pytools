# -*- coding: utf-8 -*-
"""
The simpliest version control program ever

add files to the folder, save a revision, or checkout a revision

archive naming year-month-day-hour-minute-second

http://pythoncentral.io/how-to-recursively-copy-a-directory-folder-in-python/

https://docs.python.org/3/library/shutil.html#shutil.ignore_patterns

"""

import os, shutil, datetime, sys


def pyver(user, comment):
    '''
    user = 'ngordon'
    comment = 'added some more files'
    
    '''
    n = datetime.datetime.now()
    timestamp = datetime.datetime.strftime(n, '%Y%m%d%H%M%S')  
    archivepath = '.pyver\\'+timestamp   
    shutil.copytree('.', archivepath, ignore=shutil.ignore_patterns('.pyver'))
    archivefiles = os.listdir(archivepath)
    archivesize = sum([os.path.getsize(s) for s in os.listdir(archivepath)])/1e3 # kb
    
    #makes a zip file instead
    shutil.make_archive(archivepath,'zip', archivepath)
    shutil.rmtree(archivepath)

    archivefilesstr = ' '.join(archivefiles)
    ''' writes what files were archived'''
    pyverlog = open('.pyver\\pyver.log','a')
    pyverlog.write('%s-%s-%s-%ikb-%s\n' % (user,timestamp,comment,archivesize,archivefilesstr))
    pyverlog.close()

def make_hidden():
    '''creates windows hidden folder
    can also use the windows command 
    os.system("attrib +s +h "+.pyver)
    '''
    import ctypes
    FILE_ATTRIBUTE_HIDDEN = 0x02
    ret = ctypes.windll.kernel32.SetFileAttributesW("C:\\Users\\Neal\\Desktop\\pyver\\.pyver", FILE_ATTRIBUTE_HIDDEN)
    if ret:
        print('attribute set to Hidden')
    else:  # return code of zero indicates failure, raise Windows error
        raise ctypes.WinError()

def show_log():
    pyverlog = open('pyver\\pyver.log','r')
    for k in pyverlog.readlines():
        print(k)
    pyverlog.close()


if __name__=='__main__':
    '''
    pass arguments to indicate user and comment
    pyver neal testing 
    '''
    user = sys.argv[1]
    comment = sys.argv[2]    
    pyver(user, comment)

