#!/usr/bin/env bash
#
# Script: math-wizards.sh
# Author: Jacek 'Szumak' Kotlarski <szumak@virthost.pl>
# Created: 2025-10-18
#
# Purpose:
#   Startup script for Math Wizards application.
#   Detects project directory, manages virtual environment, and runs the application.
#
# Usage:
#   math-wizards.sh
#
# Dependencies:
#   - python3
#   - pip

set -euo pipefail

# Determine the project directory
# This works whether the script is run directly or via symlink
SCRIPT_PATH="$(readlink -f "${BASH_SOURCE[0]}")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Change to project directory
cd "$PROJECT_DIR"

# Virtual environment path
VENV_DIR="$PROJECT_DIR/.venv"
REQUIREMENTS="$PROJECT_DIR/requirements.txt"

# Function to create virtual environment
create_venv() {
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
    
    echo "Activating virtual environment..."
    # shellcheck source=/dev/null
    source "$VENV_DIR/bin/activate"
    
    echo "Upgrading pip..."
    pip install --upgrade pip
    
    if [[ -f "$REQUIREMENTS" ]]; then
        echo "Installing dependencies from requirements.txt..."
        pip install -r "$REQUIREMENTS"
    else
        echo "Warning: requirements.txt not found!"
        exit 1
    fi
    
    echo "Virtual environment setup complete."
}

# Check if virtual environment exists
if [[ ! -d "$VENV_DIR" ]]; then
    echo "Virtual environment not found at $VENV_DIR"
    create_venv
else
    echo "Virtual environment found."
fi

# Activate virtual environment
echo "Activating virtual environment..."
# shellcheck source=/dev/null
source "$VENV_DIR/bin/activate"

# Run the application
echo "Starting Math Wizards..."
echo
python3 -m py_math_wizards.main

# Deactivate virtual environment on exit
deactivate
