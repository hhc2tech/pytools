# -*- coding: utf-8 -*-
"""
The simpliest version control program ever

add files to the folder, save a revision, or checkout a revision

archive naming year-month-day-hour-minute-second

http://pythoncentral.io/how-to-recursively-copy-a-directory-folder-in-python/
https://docs.python.org/3/library/shutil.html#shutil.ignore_patterns


"""

import os, shutil, datetime, sys, argparse


def pyver(user, archivefiles, comment):
    '''
	main function of pyver. copys files from the current directory and creates an archive.
	the tab-delimmeted log file pyver.csv keeps a record of the file changes
    '''
    
    if not os.path.isdir('.pyver'):
        os.mkdir('.pyver')
        make_hidden('.pyver')
        
    n = datetime.datetime.now()
    timestamp = datetime.datetime.strftime(n, '%Y%m%d%H%M%S')  
    archivepath = '.pyver\\'+timestamp  
    os.mkdir(archivepath)

	### was used to copy an entire directory but was wasteful
    #archivefiles = os.listdir(archivepath)
    #shutil.copytree('.', archivepath, ignore=shutil.ignore_patterns('.pyver'))

    for f in archivefiles:
        print(f)
        shutil.copy(f , archivepath+'\\'+f)
    
    archivesize = sum([os.path.getsize(s) for s in os.listdir(archivepath)])/1e3 # kb
    
    ### makes a zip file instead
    #shutil.make_archive(archivepath,'zip', archivepath)
    #shutil.rmtree(archivepath)

    archivefilesstr = ' '.join(archivefiles)
    ''' writes what files were archived'''
    pyverlog = open('.pyver\\pyver.log','a')
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
    if os.path.exists('.pyver\\pyver.log'):
        pyverlog = open('.pyver\\pyver.log','r')
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

if __name__=='__main__':
    '''
	executed if module is not imported
    '''
    

    if len(sys.argv) == 2 and sys.argv[1] == 'log':
        log()
    elif len(sys.argv) == 2 and sys.argv[1] == 'tree':
        tree('.')
    else:    
             
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--my-foo', default='foobar')
        parser.add_argument('-b', '--bar-value', default=3.14)
       
        p = argparse.ArgumentParser()
        p.add_argument('-u', '--user', default = os.path.split(os.path.expanduser('~'))[-1], 
                       help='user that made the pyver entry')
        p.add_argument('-f', '--files',
                       help='add files separated by vertical line, example, file1.txt|file2.txt')
        p.add_argument('-c', '--comment', default = '', 
                       help='add a comment as to what changed')
        args = p.parse_args()
        
        if args.files:
            tempfiles = args.files.split('|')
            args.files = []
            for t in tempfiles:
                if t not in os.listdir(os.getcwd()):
                    print('%s not found, skipping' % t)
                else:
                    args.files.append(t)
        else:
            args.files = os.listdir(os.getcwd())
            if '.pyver' in args.files:
                args.files.remove('.pyver')
        pyver(args.user, args.files, args.comment)      