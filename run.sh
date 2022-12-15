#!/usr/bin/env bash

echo -e "\033[36mResolving dependencies... \033[0m"
pip install -r requirements.txt
echo -e "\033[32mDone.\033[0m"

python3 app.py
