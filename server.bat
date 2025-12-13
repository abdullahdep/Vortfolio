@echo off
@REM REM Ask user for Django project directory
@REM set /p PROJECT_DIR="Enter the full path of your Django project: "

@REM REM Change to the specified directory
@REM cd %USERPROFILE%\Downloads\vortfolio-main\Vortfolio-main
start cmd /k "python manage.py collectstatic"
REM Run Django server in a separate command window
start cmd /k "python manage.py runserver 0.0.0.0:8000"

REM Run Cloudflared tunnel in a separate command window
@REM start cmd /k "cloudflared tunnel --config django-config.yml run"

