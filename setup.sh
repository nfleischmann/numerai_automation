#!/bin/bash

# Install python and pip
sudo apt-get install -y python3 python3-pip

# Install requirements
pip3 install -r requirements.txt

# Ask for environment variables
read -p "Enter BUCKET_NAME: " bucket_name
export BUCKET_NAME=$bucket_name

read -p "Enter NUMERAI_PUBLIC_ID: " public_id
export NUMERAI_PUBLIC_ID=$public_id

read -p "Enter NUMERAI_SECRET_KEY: " secret_key
export NUMERAI_SECRET_KEY=$secret_key

# Set environment variables
export FLASK_APP=your_flask_app.py
export FLASK_ENV=development
