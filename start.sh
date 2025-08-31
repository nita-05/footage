#!/usr/bin/env bash

echo "🚀 Starting Footage Flow Backend..."

# Create directories if they don't exist
mkdir -p uploads/videos uploads/audio uploads/images uploads/renders tmp_frames

# Set environment
export PYTHONPATH=/app
export FLASK_ENV=production

# Start Gunicorn
echo "📡 Starting Gunicorn server..."
exec gunicorn --config gunicorn.conf.py --bind 0.0.0.0:5000 app:app
