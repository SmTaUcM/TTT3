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
#----------------------------------------------------------------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                     Main Program.                                                                  #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
# Detect the location of the TTT3 folder.
os.chdir("..")
ttt3Dir = os.path.abspath(os.curdir)

# Remove any old builds of TTT3.
shutil.rmtree(ttt3Dir + "\\_Compiler\\TTT3", ignore_errors=True)

# Copy the required ttt3.ico file into the _Compiler folder.
shutil.copy(ttt3Dir + "\\_Resource\\ttt3.ico", ttt3Dir + "\\_Compiler\\")

# Compile TTT3.
PyInstaller.__main__.run([
     "--onefile",
     "--windowed",
     "--icon=ttt3.ico",
     os.path.join(ttt3Dir, "TTT3.py"),
])

# Clean up the build, copy in 'Settings' and 'Data' folders. Remove unnecessary files and renaming 'dist' to 'TTT3'.
shutil.rmtree(ttt3Dir + "\\_Compiler\\build", ignore_errors=True)
os.remove(ttt3Dir + "\\_Compiler\\TTT3.spec")
os.remove(ttt3Dir + "\\_Compiler\\ttt3.ico")
os.rename(ttt3Dir + "\\_Compiler\\dist", ttt3Dir + "\\_Compiler\\TTT3")
shutil.copytree(ttt3Dir + "\\settings", ttt3Dir + "\\_Compiler\\TTT3\\settings")
shutil.copytree(ttt3Dir + "\\data", ttt3Dir + "\\_Compiler\\TTT3\\data")
shutil.copy(ttt3Dir + "\\TTT3_readme.htm", ttt3Dir + "\\_Compiler\\TTT3\\")                                                            #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
