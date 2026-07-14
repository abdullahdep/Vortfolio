@echo off
call .\.venv\Scripts\activate
echo using python virtual enviroment if avalible while global
python -v app.py
echo bat_done
pause