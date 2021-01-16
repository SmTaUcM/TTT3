import PyInstaller.__main__
import os
import shutil

shutil.rmtree("D:\\Local Repositories\\TTT3\\_Compiler\\TTT3", ignore_errors=True)

PyInstaller.__main__.run([
     '--onefile',
     '--windowed',
     '--icon=ttt3.ico',
     os.path.join('D:\\Local Repositories\\TTT3', 'TTT3.py'),
])

shutil.rmtree("D:\\Local Repositories\\TTT3\\_Compiler\\build", ignore_errors=True)
os.remove("D:\Local Repositories\TTT3\_Compiler\TTT3.spec")
os.rename("D:\\Local Repositories\\TTT3\\_Compiler\\dist", "TTT3")
shutil.copytree("D:\\Local Repositories\\TTT3\\settings", "D:\\Local Repositories\TTT3\\_Compiler\\TTT3\\settings")
shutil.copytree("D:\\Local Repositories\\TTT3\\data", "D:\\Local Repositories\TTT3\\_Compiler\\TTT3\\data")
shutil.copy("D:\Local Repositories\TTT3\TTT3_readme.htm", "D:\\Local Repositories\TTT3\\_Compiler\\TTT3\\")