#!/bin/bash

# Define file path and URL
TAILWIND_PATH="f1App/static/css/tailwindcss-linux-x64"
TAILWIND_URL="https://github.com/tailwindlabs/tailwindcss/releases/download/v4.1.8/tailwindcss-linux-x64"

# Check if the Tailwind binary exists
if [ ! -f "$TAILWIND_PATH" ]; then
  echo "Tailwind binary not found. Downloading..."
  curl -L "$TAILWIND_URL" -o "$TAILWIND_PATH"
  chmod +x "$TAILWIND_PATH"
fi

# Run Tailwind CSS build
"$TAILWIND_PATH" -i f1App/static/css/input.css -o f1App/static/css/output.css
