# pyxl
Python and Microsoft Excel integration with COM

pg 67
		

excels ProgID is 'Excel>application'
```
import win32com.client
xl = win32com.client.Dispatch('Excel.Application')

#shows Excel GUI
xl.Visible = True

# reassign the object to close the Excel GUI
xl = None	

#create new GUID 71
import pythoncom
print(pythoncom.CreateGuid())

# executes a command
exec('x=2') #ok
exec('x+1') #not OK,  nothing happens

#evaluates a statement
eval('x+2') # ok
eval('print(x)') # not OK, 

# the global namespace is just a dictionary
for item in globals().items():
    print(item)
    
''' 
http://docs.activestate.com/activepython/2.5/pywin32/html/com/win32com/HTML/QuickStartClientCom.html
dynamic dispatch does not give python any
    information about the objects
    static dispatch allows python to access the 
    object properties
    
    by running makepy.py, it allows for early
    bound com, giving access the objects directly in
    pyton. another option is to develop in the 
    VBA editor and copy your code elsewhere when
    complete
'''


# pg 144
from win32com.client import Dispatch
xlApp = Dispatch("Excel.Application")
xlApp.Visible = True
xlApp.WorkBooks.Add()
# hierachry Application Workbook Sheet Range Cell
xlApp.ActiveSheet.Cells(1,1).Value = "python check"
xlApp.Workbooks("Book4").Sheets("Sheet1").Cells(2,1).Value = "Python Rules!"
xlApp.Workbooks(1).Sheets(1).Cells(3,1).Value = 'python check!'

xlBook = xlApp.Workbooks(1)
xlSheet = xlApp.Sheets(1)

xlSheet.Cells(4,1).Value = 'one last python check' 

# same but different syntax, function vs array
xlBook.Sheets(1) == xlBook.Sheets[0]

#send time to a new sheet
timesheet = xlBook.Sheets.Add()

import time
from matplotlib.pyplot import pause
for x in range(1,100):
    pause(.1)
    now = time.time()
    timesheet.Cells(x,1).Value = now


#xlBook.SaveAs(Filename='C:\\temp\\mysheet.xlsx')



#close excel client
xlApp = None


# and excel macro definition
Sub Macro1()
    ActiveWorkbook.ActiveSheet.Cells(1, 1).Value = "python check"
End Sub


```
