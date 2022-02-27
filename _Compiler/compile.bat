@echo off
rmdir ..\__pycache__ /s /q
python compile.py
rmdir ..\__pycache__ /s /q
pause