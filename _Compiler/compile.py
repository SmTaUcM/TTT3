'''#-------------------------------------------------------------------------------------------------------------------------------------------------#
# Name:        compile.py
# Purpose:     Used to compile TTT3 into TTT3.exe.
# Version:     v1.00
# Author:      Stuart. Macintosh
#
# Created:     17/01/2021
# Copyright:   Emperor's Hammer
# Licence:     None
#-------------------------------------------------------------------------------------------------------------------------------------------------#'''

#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Imports.                                                                      #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
import PyInstaller.__main__
import os
import shutil
from zipfile import ZipFile, ZIP_DEFLATED
import platform
import sys
#----------------------------------------------------------------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                     Main Program.                                                                  #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
# Detect the location of the TTT3 folder.
os.chdir("..")
ttt3Dir = os.path.abspath(os.curdir)

# Remove any old builds of TTT3.
print("\nRemoving old build files...")
shutil.rmtree(ttt3Dir + "\\_Compiler\\TTT3", ignore_errors=True)
try:
    os.remove(ttt3Dir + "\\_Compiler\\TTT3.zip")
except FileNotFoundError:
    pass

# Copy the required ttt3.ico file into the _Compiler folder.
print("\nCopying ttt3.ico icon file...")
shutil.copy(ttt3Dir + "\\_Resource\\ttt3.ico", ttt3Dir + "\\_Compiler\\")

# Compile TTT3.
print("\nCompiling TTT3.exe...\n")
PyInstaller.__main__.run([
     "--onefile",
     "--windowed",
     "--icon=ttt3.ico",
     os.path.join(ttt3Dir, "TTT3.py"),
])
print("\nTTT3.exe created.")

# Clean up the build, copy in 'Settings' and 'Data' folders. Remove unnecessary files and renaming 'dist' to 'TTT3'.
print("\nCopying 'data' and 'settings' folders...")
shutil.rmtree(ttt3Dir + "\\_Compiler\\build", ignore_errors=True)
os.remove(ttt3Dir + "\\_Compiler\\TTT3.spec")
os.remove(ttt3Dir + "\\_Compiler\\ttt3.ico")
os.rename(ttt3Dir + "\\_Compiler\\dist", ttt3Dir + "\\_Compiler\\TTT3")
shutil.copytree(ttt3Dir + "\\settings", ttt3Dir + "\\_Compiler\\TTT3\\settings")
shutil.copytree(ttt3Dir + "\\data", ttt3Dir + "\\_Compiler\\TTT3\\data")
shutil.copy(ttt3Dir + "\\TTT3_readme.htm", ttt3Dir + "\\_Compiler\\TTT3\\")

# Create TTT3.zip for distribution.
print("\nCreating TTT3.zip. Please wait...")
with ZipFile('_Compiler\\TTT3.zip', 'w', compression=ZIP_DEFLATED, compresslevel=9) as zipObj:
   # Iterate over all the files in directory
    for folderName, subfolders, filenames in os.walk(os.getcwd() + "\\_Compiler\\TTT3"):
        for filename in filenames:
           # Create complete filepath of file in directory
           filePath = os.path.join(folderName, filename)
           # Add file to zip
           zipObj.write(filePath, filePath.split("_Compiler\\")[1])
print("\nTTT3.zip created.")
bits = sys.version[ : sys.version.index(" bit")][-3:]
version = platform.platform().split("-")[0] + bits + "-bit"
print("\n\n----------- Compile for %s Complete -----------\n\n" % version)
#----------------------------------------------------------------------------------------------------------------------------------------------------#
