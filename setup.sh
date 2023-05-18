#!/bin/bash

# Create folder to store models
mkdir models

# Create folder to store tournament data
mkdir tournament_data

# Create folder to store predictions
mkdir predictions

# Install python and pip
sudo yum install -y python python-pip

# Install requirements
pip install -r requirements.txt