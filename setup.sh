#!/bin/bash

# Set up NLTK data directory
export NLTK_DATA="${PWD}/nltk_data"

# Install NLTK
pip install nltk

# Download NLTK data
python -m nltk.downloader punkt stopwords

# Create Streamlit config file
mkdir -p ~/.streamlit/
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
