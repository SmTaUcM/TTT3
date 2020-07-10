rmdir "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\_Compiler\dist" /S /Q
python compile.py py2exe --includes sip
copy "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\_Resource\ttt.ui" "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\_Compiler\dist\"
copy "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\TTT3_readme.htm" "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\_Compiler\dist\"
mkdir "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\_Compiler\dist\data"
xcopy "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\data" "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\_Compiler\dist\data\" /S /Q
rmdir "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\_Compiler\build" /S /Q