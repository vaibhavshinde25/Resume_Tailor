@echo off
title Resume Tailor Setup
cd /d "%~dp0"
python -m pip install -r requirements.txt
python scripts\setup_new_user.py
pause
