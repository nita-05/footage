# Gunicorn configuration for production deployment
import os
import multiprocessing

# Server socket
bind = f"0.0.0.0:{os.getenv('PORT', '5000')}"
backlog = 2048

# Worker processes
workers = 1  # Single worker to avoid memory issues
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50
preload_app = True

# Timeout settings
timeout = 600  # 10 minutes for video processing
keepalive = 2
graceful_timeout = 60

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = "footage-flow-backend"

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Memory optimization
max_requests = 1000
max_requests_jitter = 50

# Environment
raw_env = [
    "FLASK_ENV=production",
    "PYTHONPATH=/app"
]
