#!/bin/bash
set -euo pipefail

# Upgrade pip and install Python dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
