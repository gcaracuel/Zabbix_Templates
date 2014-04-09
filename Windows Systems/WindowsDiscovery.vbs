' Constants Section. Remember to change with your credentials

Const SQLUser = "your_username_here"
Const SQLPassword = "your_password_here" 



Const adOpenStatic = 3
Const adLockOptimistic = 3
Const adUseClient = 3


Dim WshShell, oExec
Set WshShell = WScript.CreateObject("WScript.Shell")


Select Case WScript.Arguments(0)
	
	Case "IISSites"				' Get a JSON with MACRO=#IISSITE with IIS Sites on the machine
		Set oExec = WshShell.Exec("%windir%\system32\inetsrv\appcmd list site /text:name")

		wscript.echo "{" & vbcrlf & vbtab & chr(34) & "data" & chr(34) & ":[" & vbcrlf
		do while not oExec.StdOut.AtEndOfStream 
   			x = oExec.StdOut.ReadLine
   			newline = "{" & chr(34) & "{#IISSITE}" & chr(34) & ":" & chr(34) & x & chr(34) & "}"
   			if not oExec.StdOut.AtEndOfStream then
   				newline = newline & ","
   			end if
   			wscript.echo vbtab & newline
		loop
		wscript.echo "]" & vbcrlf & "}"

	Case "IISApps"				' Get a JSON with MACRO=#IISAPP with IIS Sites on the machine
		Set oExec = WshShell.Exec("%windir%\system32\inetsrv\appcmd list apppool /text:name")

		wscript.echo "{" & vbcrlf & vbtab & chr(34) & "data" & chr(34) & ":[" & vbcrlf
		do while not oExec.StdOut.AtEndOfStream 
   			x = oExec.StdOut.ReadLine
   			newline = "{" & chr(34) & "{#IISAPP}" & chr(34) & ":" & chr(34) & x & chr(34) & "}"
   			if not oExec.StdOut.AtEndOfStream then
   				newline = newline & ","
   			end if
   			wscript.echo vbtab & newline
		loop
		wscript.echo "]" & vbcrlf & "}"

	Case "SQLDatabases"			' Get a JSON with MACRO=#DBNAME with SQL Server databases list
		Set objConnection = CreateObject("ADODB.Connection")
		Set objRecordset = CreateObject("ADODB.Recordset")
		Set fso = CreateObject ("Scripting.FileSystemObject")

		objConnection.Open "Provider=SQLOLEDB;Server=localhost,1433;Database=master;User ID=" & SQLUser & ";Password=" & SQLPassword & ";"

		objRecordset.CursorLocation = adUseClient
		objRecordset.Open "SELECT name FROM master.dbo.sysdatabases", objConnection, _
    	adOpenStatic, adLockOptimistic
    
    	With objRecordset
			wscript.echo "{" & vbcrlf & vbtab & chr(34) & "data" & chr(34) & ":[" & vbcrlf
        	While Not .EOF
            	newline = "{" & chr(34) & "{#DBNAME}" & chr(34) & ":" & chr(34) & .Fields(0) & chr(34) & "}"
            	.MoveNext
				if not .eof then 
					newline = newline & ","
				end if	
				wscript.echo vbtab & newline
			Wend
			wscript.echo "]" & vbcrlf & "}"
    	End With
        
		objRecordset.Close
		objConnection.Close


	Case Else
		wscript.echo "Parameter ERROR"
End Select