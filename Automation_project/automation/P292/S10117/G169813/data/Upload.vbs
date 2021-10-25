'Upload.vbs library
'VarDeclarations.vbs should also be associated to the scripts

Option Explicit


'****************************************************************************************************************************************************************
' Sub Name		: ClickWCUButton
' Developed By      : A. Weissman
' Created Date		: 08/05/2013
' Last Modified		:  
' Input Parameters	:  button Name
' Dependencies		: 
' Description		:  Clicks a button  in the WebConsole Upload File
' Example			:  ClickWCUButton "Next"
''**************************************************************************************************************************************************************  
Public Sub ClickWCUButton(strName)

	Dim oDesc, Els, NumberOfEls, i, elo, oht

	Select Case strName
		Case "Next"
			oht = "wc_next_16"
		Case "Back"
			oht = "wc_back_16"
		Case "Create Synonym"
			oht = "wc_mtmfd_16"

	End Select


	Set oDesc = Description.Create()
	oDesc("micclass").Value = "Image"
	oDesc("html tag").Value = "IMG"
	Set Els = Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").ChildObjects(oDesc)

	NumberOfEls=Els.Count()
	For i = 0 To NumberofEls - 1
		elo=Els(i).GetROProperty("outerhtml")
		If Instr(elo,oht) Then
			Els(i).Click 5,5
			Exit For
		End If
	Next

	Set oDesc = nothing

End Sub


'****************************************************************************************************************************************************************
' Sub Name		: ClickOverwriteBox
' Developed By      : A. Weissman
' Created Date		: 08/06/2013
' Last Modified		:  
' Input Parameters	:  
' Dependencies		: 
' Description		:  checks Overwrite existing synonyms check-box
' Example			: 
''**************************************************************************************************************************************************************  
Public Sub ClickOverwriteBox

   Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
	("class:=bi-label","outertext:=Overwrite existing synonyms").Click 10.10

End Sub


'****************************************************************************************************************************************************************
' Sub Name		: ClickReportVerb
' Developed By      : A. Weissman
' Created Date		: 08/06/2013
' Last Modified		:  
' Input Parameters	:  default verb or field, verb
' Dependencies		: replaces default verb, or selects main field verb
' Description		:  clicks a verb in verb list
' Example			: ClickReportVerb "Sum","Print"
''**************************************************************************************************************************************************************  
Public Sub ClickReportVerb(strName,val)

	Dim oDesc, Els, NumberOfEls, i, y, b

	b =  Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
	("html tag:=TD","visible:=True","innertext:=" & strName).GetROProperty("abs_y")
	wait 1
	Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
	("html tag:=TD","visible:=True","innertext:=" & strName).RightClick 10.10

	wait 2

	Set oDesc = Description.Create()
	oDesc("micclass").Value = "WebElement"
	oDesc("class").Value = "text"
	oDesc("innertext").Value = val
	oDesc("visible").Value = True
	Set Els = Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").ChildObjects(oDesc)

	NumberOfEls=Els.Count()
	For i = 0 To NumberofEls - 1
		y=Els(i).GetROProperty("abs_y")
		If abs(y-b) <= 100 Then
			Els(i).Click 20,10
			Exit For
		End If
	Next

	Set oDesc = nothing

End Sub

'''******************************************************************************************************************************************
'' Sub Name  			 : EnterAppName
'' Developed By 		: A. Weissman
'' Created Date			 : 08/02/2013
'' Last Modified		  :  
'' Input Parameters	:  App Name under ibi_apps
'' Dependencies		   : 
'' Description			 	:  Enters a folder name in the Application box
'' Example			      :  EnterAppName "wfqa"
'''******************************************************************************************************************************************* 
Public Sub  EnterAppName(strName)

	Dim x, y, obj

	x=Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
		("class:=bi-label","innertext:=Application").GetROProperty("abs_x")
	y=Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
		("class:=bi-label","innertext:=Application").GetROProperty("abs_y")

	Set obj = CreateObject ("Mercury.DeviceReplay")
	obj.MouseClick x + 100, y + 10, 0

	keyType "^a"
	keyType strName
	wait 1

	Set obj = Nothing

End Sub


'******************************************************************************************************************************************
' Sub Name  			 : EnterFileNameToUpload
' Developed By 		: A. Weissman
' Created Date			 : 08/02/2013
' Last Modified		  : 
' Input Parameters	:  name of file with full path
' Dependencies	
' Description			 Enters file name in Upload File box
' Example		EnterFileNameToUpload "D:\qa\functional\webfocus\wfmr\wfbip\UploadFiles_suite_IE9\Upload_Data\Text_file1.txt"
''******************************************************************************************************************************************* 
Public Sub EnterFileNameToUpload(strFilename)

	Dim w

	w=Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=page").WebFile("html id:=filename").GetROProperty("width")

	Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=page").WebFile("html id:=filename").Click w - 10, 10
	wait 2
	Browser("micclass:=Browser","CreationTime:=1").Dialog("nativeclass:=#32770").Activate
	Browser("micclass:=Browser","CreationTime:=1").Dialog("nativeclass:=#32770").SetTOProperty "visible", "True"
	wait 2
	enterkeys strFilename
	wait 1

	Browser("micclass:=Browser","CreationTime:=1").Dialog("nativeclass:=#32770").WinButton("text:=&Open").Click 10,10

End Sub


'***************************************************************************************************************************************************************
' Sub Name		: EnterSynonymName
' Developed By      : A. Weissman
' Created Date		: 08/15/2013
' Last Modified		:  
' Input Parameters	:  synonym name
' Dependencies		: 
' Description		:  replaces default name (sheet1) with the user's name
' Example			:  EnterSynonymName "XLS_FILE1"
''**************************************************************************************************************************************************************  
Public Sub EnterSynonymName(strName)

	Dim x, y, obj

	x = Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
		("html tag:=SPAN","innertext:=Default Name.*").GetROProperty("abs_x")
	y = Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
		("html tag:=SPAN","innertext:=Default Name.*").GetROProperty("abs_y")

	Set obj = CreateObject ("Mercury.DeviceReplay")
	obj.MouseClick x + 30, y + 26, 0

	Set obj = Nothing

	keyType "^a"
	wait 1
	enterkeys strName
	wait 1

End Sub

'******************************************************************************************************************************************
' Sub Name				: MaxSecondWindow
' Developed By 		: A. Weissman
' Created Date			: 08/02/2013
' Last Modified		    :  
' Input Parameters	  :  
' Dependencies		  : 
' Description			 :	Maximizes the second browser opened
' Example			      :  
''*******************************************************************************************************************************************
Public Sub MaxSecondWindow

	Dim hwnd
 
	hwnd = Browser("CreationTime:=1").Object.HWND
	Window("hwnd:=" & hwnd).Maximize

End Sub


'****************************************************************************************************************************************************************
' Sub Name		: OpenVerbList
' Developed By      : A. Weissman
' Created Date		: 08/06/2013
' Last Modified		:  
' Input Parameters	:  {Sum|Print|Count|List}
' Dependencies		: 
' Description		:  opens the verb list with right-click on current verb, or on Field name
' Example			: OpenVerbList "Sum"
''**************************************************************************************************************************************************************  
Public Sub OpenVerbList(strName)

   Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
	("html tag:=TD","visible:=True","innertext:=" & strName).RightClick 10.10

End Sub


'***************************************************************************************************************************************************************
' Sub Name		: SelectDelimiter
' Developed By      : A. Weissman
' Created Date		: 08/06/2013
' Last Modified		:  
' Input Parameters	:  delimiter type
' Dependencies		: 
' Description		:  selects a delimiter from th drop-down list
' Example			:  SelectDelimiter "TAB"
''**************************************************************************************************************************************************************  
Public Sub SelectDelimiter(strName)

	Dim oDesc, Els, NumberOfEls, i, eli, iht
	Dim x, y, obj

	x = Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
		("class:=bi-label","innertext:=Delimiter").GetROProperty("abs_x")
	y = Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
		("class:=bi-label","innertext:=Delimiter").GetROProperty("abs_y")

	Set obj = CreateObject ("Mercury.DeviceReplay")
	obj.MouseClick x + 265, y + 10, 0

	Set obj = Nothing

	Select Case LCase(strName)
		Case "comma"
			iht = "comma"
		Case "tab"
			iht = "tab character"
		Case "pipe"
			iht = "pipe"
		Case "space"
			iht = "space character"
		Case "type-in"
			iht = "type-in delimiter"

	End Select


	Set oDesc = Description.Create()
	oDesc("micclass").Value = "WebElement"
	oDesc("class").Value = "bi-list-item list-item.*"
	oDesc("visible").Value = True
	Set Els = Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").ChildObjects(oDesc)

	NumberOfEls=Els.Count()
	For i = 0 To NumberofEls - 1
		eli=Els(i).GetROProperty("innerhtml")
		If Instr(eli,iht) Then
			Els(i).Click 10,10
			Exit For
		End If
	Next

	Set oDesc = nothing

End Sub


'***************************************************************************************************************************************************************
' Sub Name		: SelectHeader
' Developed By      : A. Weissman
' Created Date		: 08/06/2013
' Last Modified		:  
' Input Parameters	:  {Yes|No}
' Dependencies		: 
' Description		:  selects header from drop-down list
' Example			:  SelectHeader "Yes"
''**************************************************************************************************************************************************************  
Public Sub SelectHeader(strName)

	Dim oDesc, Els, NumberOfEls, i, eli
	Dim x, y, obj

	x = Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
		("class:=bi-label","innertext:=Header").GetROProperty("abs_x")
	y = Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
		("class:=bi-label","innertext:=Header").GetROProperty("abs_y")

	Set obj = CreateObject ("Mercury.DeviceReplay")
	obj.MouseClick x + 158, y + 10, 0

	Set obj = Nothing

	Set oDesc = Description.Create()
	oDesc("micclass").Value = "WebElement"
	oDesc("class").Value = "bi-list-item list-item.*"
	oDesc("visible").Value = True
	Set Els = Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").ChildObjects(oDesc)

	NumberOfEls=Els.Count()
	For i = 0 To NumberofEls - 1
		eli=Els(i).GetROProperty("innerhtml")
		If eli = strName Then
			Els(i).Click 10,10
			Exit For
		End If
	Next

	Set oDesc = nothing

End Sub


'***************************************************************************************************************************************************************
' Sub Name		: SelectSheet1
' Developed By      : A. Weissman
' Created Date		: 08/15/2013
' Last Modified		:  
' Input Parameters	:  
' Dependencies		: 
' Description		:  Checks check box for sheet1 in the Create synonym table
' Example			:  
''**************************************************************************************************************************************************************  
Public Sub SelectSheet1

	Dim x, y, obj

	x = Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
		("html tag:=SPAN","innertext:=Default Name.*").GetROProperty("abs_x")
	y = Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
		("html tag:=SPAN","innertext:=Default Name.*").GetROProperty("abs_y")

	Set obj = CreateObject ("Mercury.DeviceReplay")
	obj.MouseClick x - 14, y + 26, 0

	Set obj = Nothing

End Sub



'***************************************************************************************************************************************************************
' Sub Name		: SetHeaderRows
' Developed By      : A. Weissman
' Created Date		: 08/15/2013
' Last Modified		:  
' Input Parameters	:  number of header rows
' Dependencies		: 
' Description		:  sets the number of header rows
' Example			:  SetHeaderRows "0"
''**************************************************************************************************************************************************************  
Public Sub SetHeaderRows(val)

	Dim x, y, obj

	x = Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
		("html tag:=SPAN","innertext:=Default Name.*").GetROProperty("abs_x")
	y = Browser("micclass:=Browser","CreationTime:=1").Page("micclass:=Page").WebElement _
		("html tag:=SPAN","innertext:=Default Name.*").GetROProperty("abs_y")

	Set obj = CreateObject ("Mercury.DeviceReplay")
	obj.MouseClick x + 340, y + 26, 0

	Set obj = Nothing

	keyType "^a"
	wait 1
	enterkeys val
	wait 1

End Sub