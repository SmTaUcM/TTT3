import zipfile
import os


os.chdir("..")
ttt3Dir = os.path.abspath(os.curdir)


filepath = ttt3Dir + r"\dist\library.zip"

with zipfile.ZipFile(filepath, 'a') as zipf:
    # Add a file located at the source_path to the destination within the zip
    # file. It will overwrite existing files if the names collide, but it
    # will give a warning
    source_path = r"resource.pyc"
    destination = filepath
    zipf.write(source_path)

os.remove(ttt3Dir + r"\dist\resource.pyc")
