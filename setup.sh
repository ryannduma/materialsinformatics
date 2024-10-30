#!/bin/bash

# Create and activate virtual environment
python3 -m venv smact-env
source smact-env/bin/activate

# Install requirements
pip install -r requirements.txt

# Clone and install SMACT if not present
if [ ! -d "SMACT" ]; then
    git clone https://github.com/WMD-group/SMACT.git
    cd SMACT
    pip install -e .
    cd ..
fi

# Setup pre-commit hooks
pre-commit install

echo "Setup complete! Virtual environment is activated."
