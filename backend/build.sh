#!/bin/bash

# Build script for Render deployment
echo "🚀 Starting build process..."

# Upgrade pip
echo "📦 Upgrading pip..."
python -m pip install --upgrade pip

# Install setuptools and wheel first
echo "🔧 Installing build dependencies..."
pip install setuptools wheel

# Install requirements
echo "📚 Installing Python requirements..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p uploads/videos
mkdir -p uploads/audio
mkdir -p uploads/images
mkdir -p uploads/renders
mkdir -p tmp_frames

echo "✅ Build completed successfully!"
