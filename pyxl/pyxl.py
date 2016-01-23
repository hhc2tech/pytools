'''
File: pyExcel.py
revision: 0.1
revision date: 9/25/2014
Created on 2014-09-22
Author: Neal Gordon
Description: This program uses python to interact with MS Excel. 
'''

#==============================================================================
# Define Class used to manipulate Excel
#==============================================================================
class pyxl:
    ''' utility to manipulate excel with python'''

    def __init__(self, filename=None):
        import win32com.client
        self.xlApp = win32com.client.Dispatch('Excel.Application')
        if filename:
            self.filename = filename
            self.xlBook = self.xlApp.Workbooks.Open(filename)
            #self.xlApp.Visible = True
        else:
            self.xlBook = self.xlApp.Workbooks.Add()
            self.filename = ''
            #self.xlApp.Visible = True
			
    def save(self, newfilename = None):
        if newfilename:
            self.filename = newfilename
            self.xlBook.SaveAs(newfilename)
        else:
            self.xlBook.Save()
		
    def close(self):
        self.xlBook.Close(SaveChanges=0)
        del self.xlApp
    
    def visible(self,val):
        self.xlApp.Visible = val
        
    def sheetCount(self):
        return self.xlBook.Worksheets.Count
    
    def getCell(self, sheet, row, col):
        sht = self.xlBook.Worksheets(sheet)
        return sht.Cells(row,col).Value
        
    def sheetName(self,sheet):
        return self.xlBook.Worksheets(sheet).Name
    
    def setCell(self, sheet, row, col, value):
        sht = self.xlBook.Worksheets(sheet)
        sht.Cells(row,col).Value = value
        
    def getRange(self,sheet, row1, col1, row2, col2):
        sht = self.xlBook.Worksheets(sheet)
        return sht.Range(sht.Cells(row1, col1), sht.Cells(row2, col2).Value)
        
    def setRange(self, sheet, leftCol, topRow, data):
        bottomRow = topRow + len(data) -1
        rightCol = leftCol + len(data[0]) -1
        sht = self.xlBook.Worksheets(sheet)
        sht.Range(
            sht.Cells(topRow, leftCol),
            sht.Cells(bottomRow, rightCol)
            ).Value = data
            
    def getContiguousRange(self, sheet, row, col):
        '''scans data until a blank is found'''        
        sht = self.xlBook.Worksheets(sheet)
        bottom = row
        while sht.Cells(bottom+1, col).Value not in [None, '']:
            bottom += 1
        right = col
        while sht.Cells(row, right +1).Value not in [None, '']:
            right += 1
        return sht.Range(sht.Cells(row, col), sht.Cells(bottom, right).Value)

    #==============================================================================
    # Define functions to interact with the Excel Database
    #==============================================================================
    # item = columns
    # units = sheets
    def get_all(xlBook,columns,sheets):
        ''' returns info from the master excel sheet 
        '''
        dat = []
        for sheet in sheets:
            for column in columns:
                for r in range(2,1001): # range(2,1001) = rows 1-1000
                    d = str(xlBook.getCell(sheet, r, column))           
                    if (d not in dat) and d != 'None':
                        dat.append(d)
        return dat    
            
    def check_columns(xlBook):
        ''' checks that all columns are the same in each sheet'''
        print '----- showing columns in all worksheets -----'
        nsheets = xlBook.sheetCount()
        for s in range(1,nsheets+1):
            dat = []
            for c in range(1,50):
                val = str(xlBook.getCell(s, 1, c))
                if val != 'None':
                    dat.append(val)
                else:
                    print dat
                    break # exit sheet loop
        
#==============================================================================
# Define main function that all custom operations will be done from
#==============================================================================
if __name__ == '__main__':
    
    xlBook = pyxl('Book1.xlsx')
    xlBook.visible(True)    
    


      
    #http://stackoverflow.com/questions/9315237/how-to-paste-special-in-excel-with-python
