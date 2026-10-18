@echo off
set envname=venv
call pip install virtualenv
call python -m venv %envname%
call .\%envname%\Scripts\activate
call pip install -r requirements.txt
echo installation has been completed
pause