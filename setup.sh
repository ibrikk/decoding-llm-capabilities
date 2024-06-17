#!/bin/bash

# Install Python 3
sudo apt-get update
sudo apt-get install -y python3 python3-venv

# Create virtual environment
python3 -m venv myenv

# Activate virtual environment
source myenv/bin/activate

# Install pytest
pip install pytest

echo "Virtual environment setup complete with Python 3 and pytest installed. Use 'source myenv/bin/activate' to activate."