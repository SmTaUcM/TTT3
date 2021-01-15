@echo off

rem Delete the old build of TTT3.
rmdir "..\dist" /S /Q

rem Compile the new version of TTT3.
python compile.py py2exe --includes sip

rem Copy key files that are not included automatiically by running compile.py.
copy ..\TTT3_readme.htm ..\dist\
copy ..\resource.pyc ..\dist\

rem Create and copy over additional data folders.
rem data folder
mkdir ..\dist\data
xcopy ..\data ..\dist\data\ /S /Q
rem settings folder.
mkdir ..\dist\settings
xcopy ..\settings ..\dist\settings\ /S /Q

rem Delete the un-needed Build folder.
rmdir ..\build /S /Q

rem copy resource.pyc into library.zip.
python addToZip.py

echo.
echo ----COMPLETE----
echo.
pause