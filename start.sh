#!/bin/bash

echo "🚀 Starting Footage Flow Backend..."

# Create directories if they don't exist
mkdir -p uploads/videos uploads/audio uploads/images uploads/renders tmp_frames

# Set environment
export PYTHONPATH=/app
export FLASK_ENV=production

# Get port from Railway environment variable
PORT=${PORT:-5000}
echo "📡 Using port: $PORT"

# Start Gunicorn
echo "📡 Starting Gunicorn server..."
exec gunicorn --config gunicorn.conf.py --bind 0.0.0.0:$PORT app:app
