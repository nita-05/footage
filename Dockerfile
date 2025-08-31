FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY backend/requirements-railway.txt .
RUN pip install --no-cache-dir -r requirements-railway.txt

# Copy application code
COPY backend/ .

# Create necessary directories
RUN mkdir -p uploads/videos uploads/audio uploads/images uploads/renders tmp_frames

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Start the application
CMD ["gunicorn", "--config", "gunicorn.conf.py", "app:app"]
