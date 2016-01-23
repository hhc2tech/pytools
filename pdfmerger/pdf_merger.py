
'''
pdf_merger
written by Neal Gordon
4-15-2014
'''

import os,shutil, re
import PyPDF2 as pdf

def getalldir(rootdir):
    ''' returns all directories in the immediate root directory
		probably can also use os.listdir()
	'''
    curdir = os.getcwd()  
    os.chdir(rootdir)
    outdir = os.walk('.').next()[1]
    os.chdir(curdir)
    return outdir

def findbackmatter(indir):
    for dirname in os.listdir(indir):
        os.chdir(indir+'/'+dirname)
        for filename in os.listdir(os.getcwd()):
            firstind = filename.find('BookBackMatter')
            if firstind !=  -1:
                newfilename = filename[:firstind]+'z'+filename[firstind:]
                os.rename(filename, newfilename)  
        os.chdir(indir)
	
	
def renamer(sourcedir):
    ''' finds files with name filename and renames files 
        the name of the source directory 
        with input and output directory '''
#    filename = '/pdfpythonout.pdf'
#    sourcedir ='C:/Users/Neal/Desktop/finishedbooks/'
#    destdir = 'C:/Users/Neal/Desktop/finishedpdfs/'
    filename  = '/pdfpythonout.pdf'
    destdir = sourcedir + 'finished/'
    subdir = getalldir(sourcedir)   
    os.mkdir(sourcedir + 'finished/')
    print '=================================================='
    print '============== failed merge ======================'
    print '=================================================='
    for subdirloop in subdir:
        oldfilepath = sourcedir + subdirloop + filename
        newfilepath = destdir + subdirloop + '.pdf'
        try:
            shutil.copy(oldfilepath, newfilepath)
        except:
            print subdirloop + '.pdf'  

def pdf_merger(startDir):
    ''' given a directory startDir, this function will merge all pdfs in a
            directory and name it pdfout.pdf 
    '''            
    def natural_sort(l): 
        # natural sorting function
        convert = lambda text: int(text) if text.isdigit() else text.lower() 
        alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
        return sorted(l, key = alphanum_key)
        
    curdr = os.getcwd()    
    os.chdir(startDir)
    fileList = natural_sort(os.listdir(startDir))
    merger = pdf.PdfFileMerger()
    for item in fileList:
        if os.path.splitext(item)[1].upper() == '.PDF':
            pdfDocument = os.path.join(startDir,item)
            input1 = open(pdfDocument,'rb')          
            merger.append(fileobj=input1)
            print ' file = ' , pdfDocument
    pdfname = 'pdfpythonout.pdf'
    merger.write(open(pdfname,'wb'))
    os.chdir(curdr)
    return



##############################################################################	
####### function calls, each pdf group must be in separate directories #######
##############################################################################

masterdir = 'C:/Users/ngordon/Desktop/Booklet/'  # end with /

# renames the last file to ensure proper natural sorting
curdir = os.getcwd()
findbackmatter(masterdir)
os.chdir(curdir)

allpdfdir = getalldir(masterdir)

# generic name for merged pdf before it is renamed to its directory name
filename  = '/pdfpythonout.pdf'

for currentdir in allpdfdir:
    catcurdir = masterdir+currentdir
    print catcurdir
    try:
        pdf_merger(catcurdir)
        print ' PDF files merged in = ',catcurdir,'\n'       
    except:
        print '-------- skipped----------\n'

# takes an input and output directory finds a pdf named
renamer(masterdir) 



