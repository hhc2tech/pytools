from PyPDF2 import PdfFileMerger
merger = PdfFileMerger()

dir1 = 'C:/Users/ngordon/Desktop/'

file1 = '1.pdf'
file2 = '2.pdf'

input1 = open(dir1+file1, "rb")
input2 = open(dir1+file2, "rb")

# add the first 3 pages of input1 document to output
#merger.append(fileobj = input1, pages = (0,3))
merger.append(fileobj = input1)
merger.append(fileobj = input2)

# Write to an output PDF document
output = open("document-output.pdf", "wb")

merger.write(output)


