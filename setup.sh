#!/bin/bash

# Install python and pip
sudo yum install -y python3.10 python3.10-pip

# Set up Python Virtual Environment
python3.10 -m venv env
source env/bin/activate

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
export FLASK_APP=model_registry.py
export FLASK_ENV=development
