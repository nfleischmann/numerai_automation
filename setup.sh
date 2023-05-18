#!/bin/bash

# Install python and pip
sudo yum install -y python python-pip

# Set up Python Virtual Environment
python -m venv env
source env/bin/activate

# Install requirements
pip install -r requirements.txt

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
