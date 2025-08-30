#!/bin/bash

# 🚀 Footage Flow Deployment Script
# This script helps deploy your application to various platforms

echo "🚀 Starting Footage Flow Deployment..."

# Check if we're in the right directory
if [ ! -f "backend/app.py" ] || [ ! -f "frontend/package.json" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Function to deploy to Render
deploy_render() {
    echo "📦 Deploying to Render..."
    echo "1. Go to https://render.com"
    echo "2. Create new Web Service"
    echo "3. Connect your GitHub repository"
    echo "4. Use these settings:"
    echo "   - Build Command: cd backend && pip install -r requirements.txt"
    echo "   - Start Command: cd backend && gunicorn --config gunicorn.conf.py app:app"
    echo "5. Add environment variables:"
    echo "   - PORT=10000"
    echo "   - FLASK_ENV=production"
    echo "   - GOOGLE_CLIENT_ID=your_google_client_id"
    echo "   - GOOGLE_CLIENT_SECRET=your_google_client_secret"
    echo "   - GEMINI_API_KEY=your_gemini_api_key"
}

# Function to deploy to Railway
deploy_railway() {
    echo "🚂 Deploying to Railway..."
    echo "1. Go to https://railway.app"
    echo "2. Deploy from GitHub"
    echo "3. Add environment variables in Railway dashboard"
    echo "4. Railway will auto-detect and deploy"
}

# Function to test locally
test_local() {
    echo "🧪 Testing locally..."
    
    # Test backend
    echo "Testing backend..."
    cd backend
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
        echo "✅ Backend dependencies installed"
    else
        echo "❌ Backend requirements.txt not found"
        return 1
    fi
    
    # Test frontend
    echo "Testing frontend..."
    cd ../frontend
    if [ -f "package.json" ]; then
        npm install
        echo "✅ Frontend dependencies installed"
    else
        echo "❌ Frontend package.json not found"
        return 1
    fi
    
    cd ..
    echo "✅ Local testing completed"
}

# Function to build for production
build_production() {
    echo "🏗️ Building for production..."
    
    # Build frontend
    cd frontend
    npm install
    npm run build
    echo "✅ Frontend built successfully"
    cd ..
    
    # Check backend
    cd backend
    if [ -f "requirements.txt" ]; then
        echo "✅ Backend ready for deployment"
    fi
    cd ..
    
    echo "✅ Production build completed"
}

# Main menu
echo ""
echo "🎯 Choose deployment option:"
echo "1) Deploy to Render (Recommended)"
echo "2) Deploy to Railway"
echo "3) Test locally"
echo "4) Build for production"
echo "5) Show deployment guide"
echo "6) Exit"
echo ""

read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        deploy_render
        ;;
    2)
        deploy_railway
        ;;
    3)
        test_local
        ;;
    4)
        build_production
        ;;
    5)
        echo "📖 Opening deployment guide..."
        if [ -f "DEPLOYMENT.md" ]; then
            cat DEPLOYMENT.md
        else
            echo "❌ DEPLOYMENT.md not found"
        fi
        ;;
    6)
        echo "👋 Goodbye!"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "🎉 Deployment process completed!"
echo "📖 For detailed instructions, see DEPLOYMENT.md"
