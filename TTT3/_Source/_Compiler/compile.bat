rem Delete the old build of TTT3.
rmdir "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3\_Source\_Compiler\dist" /S /Q

rem Compile the new version of TTT3.
python compile.py py2exe --includes sip

rem Copy key files that are not included automatiically by running compile.py.
copy "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3\_Source\TTT3_readme.htm" "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3\_Source\_Compiler\dist\"

rem Create and copy over additional data folders.
mkdir "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3\_Source\_Compiler\dist\data"
xcopy "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3\_Source\data" "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3\_Source\_Compiler\dist\data\" /S /Q

rem Delete the un-needed Build folder.
rmdir "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\_Compiler\build" /S /Q

echo "----COMPLETE----"
pause