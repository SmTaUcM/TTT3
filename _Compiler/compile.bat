@echo off

rem Delete the old build of TTT3.
rmdir "..\dist" /S /Q

rem Copy resource.pyc into library.zip and then delete it.
copy ..\resource.py  resource.py

rem Compile the new version of TTT3.
python compile.py py2exe

rem Copy key files that are not included automatiically by running compile.py.
copy ..\TTT3_readme.htm ..\dist\
rem copy ..\resource.pyc ..\dist\

rem Create and copy over additional data folders.
rem data folder
mkdir ..\dist\data
xcopy ..\data ..\dist\data\ /S /Q
rem settings folder.
mkdir ..\dist\settings
xcopy ..\settings ..\dist\settings\ /S /Q

rem Delete the un-needed Build folder.
rmdir ..\build /S /Q

rem delete the ..\dist\tcl folder.
rmdir ..\dist\tcl /S /Q
del resource.py

echo.
echo ----COMPLETE----
echo.
pause