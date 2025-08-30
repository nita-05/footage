#!/usr/bin/env python3
"""
Deployment Verification Script for Footage Flow
This script verifies that all deployment configurations are correct and working.
"""

import os
import sys
import json
import subprocess
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a file exists and print status."""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} - MISSING")
        return False

def check_python_dependencies():
    """Check if required Python packages are available."""
    required_packages = [
        'flask', 'gunicorn', 'google-auth', 'google-genai', 
        'faster-whisper', 'opencv-python-headless', 'ffmpeg-python'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ Python package: {package}")
        except ImportError:
            print(f"❌ Python package: {package} - MISSING")
            missing_packages.append(package)
    
    return len(missing_packages) == 0

def check_node_dependencies():
    """Check if required Node.js packages are available."""
    package_json_path = "frontend/package.json"
    if not os.path.exists(package_json_path):
        print(f"❌ Frontend package.json not found: {package_json_path}")
        return False
    
    try:
        with open(package_json_path, 'r') as f:
            package_data = json.load(f)
        
        required_packages = ['react', 'react-dom', 'axios', 'vite']
        missing_packages = []
        
        for package in required_packages:
            if package in package_data.get('dependencies', {}) or package in package_data.get('devDependencies', {}):
                print(f"✅ Node.js package: {package}")
            else:
                print(f"❌ Node.js package: {package} - MISSING")
                missing_packages.append(package)
        
        return len(missing_packages) == 0
    except Exception as e:
        print(f"❌ Error reading package.json: {e}")
        return False

def check_environment_variables():
    """Check if environment variables are properly configured."""
    env_file = "backend/env.template"
    if os.path.exists(env_file):
        print(f"✅ Environment template: {env_file}")
        
        with open(env_file, 'r') as f:
            content = f.read()
            
        required_vars = [
            'GOOGLE_CLIENT_ID',
            'GOOGLE_CLIENT_SECRET', 
            'GEMINI_API_KEY',
            'PORT',
            'FLASK_ENV'
        ]
        
        missing_vars = []
        for var in required_vars:
            if var in content:
                print(f"✅ Environment variable: {var}")
            else:
                print(f"❌ Environment variable: {var} - MISSING")
                missing_vars.append(var)
        
        return len(missing_vars) == 0
    else:
        print(f"❌ Environment template not found: {env_file}")
        return False

def check_deployment_files():
    """Check if all deployment files are present."""
    deployment_files = [
        ("backend/gunicorn.conf.py", "Gunicorn configuration"),
        ("backend/Procfile", "Backend Procfile"),
        ("backend/runtime.txt", "Python runtime specification"),
        ("backend/requirements.txt", "Python requirements"),
        ("frontend/Procfile", "Frontend Procfile"),
        ("frontend/vite.config.js", "Vite configuration"),
        ("frontend/package.json", "Frontend package.json"),
        ("DEPLOYMENT.md", "Deployment guide"),
        ("deploy.sh", "Deployment script")
    ]
    
    all_present = True
    for filepath, description in deployment_files:
        if not check_file_exists(filepath, description):
            all_present = False
    
    return all_present

def check_app_configuration():
    """Check if the Flask app is properly configured."""
    app_py_path = "backend/app.py"
    if not os.path.exists(app_py_path):
        print(f"❌ Main app file not found: {app_py_path}")
        return False
    
    try:
        with open(app_py_path, 'r') as f:
            content = f.read()
        
        required_features = [
            'optimize_memory',
            'memory_cleanup',
            'find_video_metadata_file',
            'gunicorn',
            'production'
        ]
        
        missing_features = []
        for feature in required_features:
            if feature in content:
                print(f"✅ App feature: {feature}")
            else:
                print(f"❌ App feature: {feature} - MISSING")
                missing_features.append(feature)
        
        return len(missing_features) == 0
    except Exception as e:
        print(f"❌ Error reading app.py: {e}")
        return False

def main():
    """Main verification function."""
    print("🚀 Footage Flow Deployment Verification")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("backend") or not os.path.exists("frontend"):
        print("❌ Error: Please run this script from the project root directory")
        sys.exit(1)
    
    print("\n📁 Checking deployment files...")
    files_ok = check_deployment_files()
    
    print("\n🐍 Checking Python dependencies...")
    python_ok = check_python_dependencies()
    
    print("\n📦 Checking Node.js dependencies...")
    node_ok = check_node_dependencies()
    
    print("\n🔧 Checking environment configuration...")
    env_ok = check_environment_variables()
    
    print("\n⚙️ Checking app configuration...")
    app_ok = check_app_configuration()
    
    print("\n" + "=" * 50)
    print("📊 VERIFICATION SUMMARY:")
    print(f"✅ Deployment files: {'PASS' if files_ok else 'FAIL'}")
    print(f"✅ Python dependencies: {'PASS' if python_ok else 'FAIL'}")
    print(f"✅ Node.js dependencies: {'PASS' if node_ok else 'FAIL'}")
    print(f"✅ Environment config: {'PASS' if env_ok else 'FAIL'}")
    print(f"✅ App configuration: {'PASS' if app_ok else 'FAIL'}")
    
    all_passed = files_ok and python_ok and node_ok and env_ok and app_ok
    
    if all_passed:
        print("\n🎉 ALL CHECKS PASSED! Your deployment is ready.")
        print("\n📋 Next steps:")
        print("1. Set up your environment variables in your deployment platform")
        print("2. Deploy backend to Render/Railway/Heroku")
        print("3. Deploy frontend to Vercel/Netlify/Render")
        print("4. Update frontend environment variables with backend URL")
        print("\n📖 See DEPLOYMENT.md for detailed instructions")
    else:
        print("\n❌ SOME CHECKS FAILED! Please fix the issues above before deploying.")
        print("\n🔧 Common fixes:")
        print("- Install missing Python packages: pip install -r backend/requirements.txt")
        print("- Install missing Node.js packages: cd frontend && npm install")
        print("- Create missing deployment files")
        print("- Configure environment variables")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
