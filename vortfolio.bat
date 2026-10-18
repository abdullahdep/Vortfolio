@echo off
call .\.venv\Scripts\activate
echo using python virtual enviroment if avalible while global
python manage.py runserver 0.0.0.0:8000
echo bat_done
pause