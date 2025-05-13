#!/usr/bin/env bash

# Define the application directory
APP_DIR="$HOME/web-app-deployment"

# Navigate to the directory
cd "$APP_DIR" || { echo "Error: Directory $APP_DIR not found"; exit 1; }

# Pull the latest code from the remote repository
git pull origin master || { echo "Error: Git pull failed"; exit 1; }

# Run the Python deployment script
python3 deploy.py
