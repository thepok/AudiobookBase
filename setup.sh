#!/bin/bash
set -euo pipefail

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip and install Python dependencies with --no-deps to avoid conflicts
echo "Installing dependencies..."
python -m pip install --upgrade pip
pip install --no-deps -r requirements.txt

echo "Setup complete! To activate the virtual environment, run: source venv/bin/activate"
