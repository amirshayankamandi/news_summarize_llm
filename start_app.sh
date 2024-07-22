#!/bin/bash

# Function to check if the Ollama API is running
check_ollama_api() {
    curl -s http://localhost:11434 > /dev/null
    return $?
}

echo "Checking if Ollama API is running..."

# Wait for Ollama API to be available
until check_ollama_api; do
    echo "Ollama API is not running. Retrying in 5 seconds..."
    sleep 5
done

echo "Ollama API is running. Starting Flask application..."

# Start the Flask application
python app.py

