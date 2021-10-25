DIM returnValue
Set Arg = WScript.Arguments
Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = True
Set objWorkbook1= objExcel.Workbooks.Open(Arg(0))
Set objWorkbook2= objExcel.Workbooks.Open(Arg(1))
Set objWorksheet1= objWorkbook1.Worksheets(1)
Set objWorksheet2= objWorkbook2.Worksheets(1)
For Each cell In objWorksheet1.UsedRange
If cell.Value <> objWorksheet2.Range(cell.Address).Value Then
returnValue = 123
Exit For
Else
returnValue = 9
End If
Next

objWorkbook1.close
objWorkbook2.close
objExcel.quit
set objExcel=nothing
WScript.Quit(returnValue)
