@echo off
set "ESC="

<nul set /p="%ESC%[36mResolving dependencies... %ESC%[0m"
pip install -r requirements.txt >nul
echo %ESC%[32mDone.%ESC%[0m

python app.py
