#!/bin/bash
# Setup script for Python 3.12.0

# Verify Python version
if ! python3.12 -c "import sys; assert sys.version_info >= (3, 12)"; then
    echo "Python 3.12.0 or higher is required"
    exit 1
fi

# Create and activate virtual environment
python3.12 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Download NLP models
python3.12 -m spacy download en_core_web_sm
python3.12 -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

echo "Setup complete. Activate virtual environment with: source venv/bin/activate"