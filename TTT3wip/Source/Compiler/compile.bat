rmdir "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\Compiler\dist" /S /Q
python compile.py py2exe --includes sip
copy "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\Resource\ttt.ui" "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\Compiler\dist\"
copy "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\TTT3_readme.htm" "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\Compiler\dist\"
rmdir "C:\Users\smtau\Dropbox\EH TIE Corps Share\TTT3\TTT3wip\Source\Compiler\build" /S /Q