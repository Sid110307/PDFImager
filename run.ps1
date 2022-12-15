Write-Host -NoNewLine -ForegroundColor Cyan "Resolving dependencies... "
pip install -r requirements.txt | out-null
Write-Host -ForegroundColor Green "Done."

python app.py
