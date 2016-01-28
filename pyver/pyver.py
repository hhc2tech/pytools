# -*- coding: utf-8 -*-
"""
Version control for dummies
"""

__author__ = 'Neal Gordon'
__version__ = '0.1'

import os, shutil, datetime, sys, argparse

def pyver(user, comment):# archivefiles, ):
    '''
	main function of pyver. copys files from the current directory and creates an archive.
	the tab-delimmeted log file pyver.csv keeps a record of the file changes
    '''
    archivefiles = []
    if not os.path.isdir('.pyver'):
        os.mkdir('.pyver')
        try:
            make_hidden('.pyver')
        except:
            print('failed to make .pyver hidden, which only works on windows')
        
    n = datetime.datetime.now()
    timestamp = datetime.datetime.strftime(n, '%Y%m%d%H%M%S')  
    archivepath = os.path.join('.pyver',timestamp)
    
   
	### was used to copy an entire directory but was wasteful

    shutil.copytree('.', archivepath, ignore=shutil.ignore_patterns('.pyver'))

    # does not copy sub-directories
#    os.mkdir(archivepath)
#    for f in archivefiles:
#        print(f)
#        print(os.path.join(archivepath, f))
#        shutil.copy(f , os.path.join(archivepath, f))
    
    
    archivesize = sum([os.path.getsize(s) for s in os.listdir(archivepath)])/1e3 # kb
    
    ### makes a zip file instead
    #shutil.make_archive(archivepath,'zip', archivepath)
    #shutil.rmtree(archivepath)

    archivefilesstr = '|'.join(archivefiles)
    ''' writes what files were archived'''
    pyverlog = open(os.path.join('.pyver','pyver.log'),'a')
    pyverlog.write('%s , %s , %ikb , %s , %s\n' % (user,
                                           timestamp,
                                           archivesize,
                                           comment,
                                           archivefilesstr))
    pyverlog.close()
	
def make_hidden(hidedir):
    '''creates windows hidden folder
    can also use the windows command 
    os.system("attrib +s +h "+.pyver)
    '''
    import ctypes
    FILE_ATTRIBUTE_HIDDEN = 0x02
    ret = ctypes.windll.kernel32.SetFileAttributesW(hidedir, FILE_ATTRIBUTE_HIDDEN)
    if ret:
        print('.pyver set to Hidden')
    else:  # return code of zero indicates failure, raise Windows error
        raise ctypes.WinError()

def log():
    '''shows the contents of the pyver log file''' 
    
    if os.path.exists(os.path.join('.pyver','pyver.log')):
        pyverlog = open(os.path.join('.pyver','pyver.log'),'r')
        for k in pyverlog.readlines():
            print(k)
        pyverlog.close()
    else:
        print('not a pver repository')

def tree(path,indent=' '):
    '''recursiveley prints the contents of a directory'''
    for file in os.listdir(path):
        fullpath = path + '/' + file              
        if os.path.isfile(fullpath):
            print('%s     %s  ' % (indent,file ) )
        else:   # os.path.isdir
            print('%s  ./%s ' % (indent,file ) )
            tree(fullpath,indent + '   |')

def make_win_exe():
    '''creates a windows exe file that allows the pyver program to be 
        run without the windows interpreter
    '''
    os.system('pip install pyinstaller')
    os.system('pyinstaller pyver.py --onefile')    

def all_files(rootDir = '.'):
    #rootDir = '.'
    files = []
    for dirName, subdirList, fileList in os.walk(rootDir):
        print(dirName)
        print(subdirList)
        print(fileList)
        for fname in fileList:
            fullpath = os.path.join(dirName, fname)
            if fullpath.split(os.sep)[1] != '.pyver':
                print(fullpath)    
                files.append(fullpath[2:])
    return files

if __name__=='__main__':
    '''
	executed if module is not imported
    '''
    
    if len(sys.argv) == 2 and sys.argv[1] == 'log':
        log()
    elif len(sys.argv) == 2 and sys.argv[1] == 'tree':
        tree('.')
    else:    
       
        p = argparse.ArgumentParser()
        p.add_argument('-u', '--user', 
                       default = os.path.split(os.path.expanduser('~'))[-1], 
                       help='user that made the pyver entry')
#        p.add_argument('-f', '--files',
#                       help='''add files separated by vertical line with no  
#                               spaces, example, file1.txt|file2.txt''')
        p.add_argument('-c', '--comment', default = '', 
                       help='''add a comment enclosed in double quotes 
                               as to what changed.''')
        args = p.parse_args()
        
#        if args.files:
#            tempfiles = args.files.split('|')
#            args.files = []
#            for t in tempfiles:
#                if t not in os.listdir(os.getcwd()):
#                    print('%s not found, skipping' % t)
#                else:
#                    args.files.append(t)
#        else:
#            #files = os.listdir(os.getcwd())  ## does not capture subdirectories
#            args.files = all_files('.')
#            if '.pyver' in args.files:
#                args.files.remove('.pyver')
        #user, archivefiles, comment = args.user, args.files, args.comment        
        pyver(args.user, args.comment) #args.files, )      
        