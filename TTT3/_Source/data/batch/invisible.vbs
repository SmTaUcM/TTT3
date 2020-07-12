Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "&PATH&\data\batch\povray.bat" & Chr(34), 0
Set WshShell = Nothing