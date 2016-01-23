

#renaming a bunch of files
import os
import glob
os.chdir("E:/")
i = 1
for old_file in glob.glob("*.fits"): 
    new = str(i) + ".fits"
    os.renames(old_file, new)
    i=i+1
<<<<<<< HEAD
	
	
import os
files = os.listdir('.')
natsort(files)
index = 0
for filename in files:
    os.rename(filename, str(index).zfill(7)+'.png')
    index += 1
=======
    
    
## file manipulation

def clearFiles(self, filetypes = ['png','csv','txt','avi','gif']):
    """clears the files """
    for fileext in filetypes:
        for f in glob.glob(os.path.dirname(self.myOdbDat.name)+'/*.'+fileext):
            try:
                os.remove(f)
            except:
                pass

def clearFilesExcept(self, filetypes = ['.odb','.py','.cae','.stp']):
    """clears the files except filetypes"""
    for f in glob.glob(os.path.dirname(self.myOdbDat.name)+'/*'):
        if os.path.splitext(f)[1] not in filetypes:
            try:
                os.remove(f)
            except:
                pass

    
def add_path(add_folder = "C:/bin/scripts"):
    import sys
    sys.path.append(add_folder)
>>>>>>> 158c2d9cc94d9605b7e573cfe3d7636d50aec236
