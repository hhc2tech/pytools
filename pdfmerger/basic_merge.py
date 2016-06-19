
from PyPDF2 import PdfFileMerger
merger = PdfFileMerger(strict = False)

dir1 = 'C:/Users/Neal/Desktop/US Marine Corps Private Pilot Ground School/'

file1 = 'USMCI_Airplane Instruments and Accessories_Part 1.pdf'
file2 = 'USMCI_Airplane Instruments and Accessories_Part 2.pdf'

input1 = open(dir1+file1, "rb")
input2 = open(dir1+file2, "rb")

# add the first 3 pages of input1 document to output
#merger.append(fileobj = input1, pages = (0,3))
merger.append(fileobj=input1)
merger.append(fileobj=input2)

# Write to an output PDF document
output = open("C:/Users/Neal/Desktop/output3.pdf", "wb")

merger.write(output)



"""
PDF merger. Loops throughs all the files in files_dir and merges any pdfs
https://pythonhosted.org/PyPDF2/PdfFileMerger.html

pip install PyPDF2

"""

import os
from PyPDF2 import PdfFileReader, PdfFileMerger

files_dir = "D:/Astronautics Structures Manual"
pdf_files = [f for f in os.listdir(files_dir) if f.endswith("pdf")] # glob.glob('*.pdf')

merger = PdfFileMerger(strict = False)

for filename in pdf_files:
    merger.append(PdfFileReader(os.path.join(files_dir, filename), "rb"), bookmark=filename)

merger.write(os.path.join(files_dir, "Astronautics Structures Manual.pdf"))






# automate the boring stuff
import PyPDF2, os
os.chdir("C:/Users/Neal/Desktop/US Marine Corps Private Pilot Ground School")
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()


for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutput = open('US Marine Corps Private Pilot Ground School.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()









