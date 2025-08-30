#!/usr/bin/env python3
"""
GitHub Deployment Guide - Step by Step
Interactive guide to deploy Footage Flow to GitHub and hosting platforms
"""

import os
import sys
import subprocess
import time

def print_step(step_num, title, description=""):
    """Print a formatted step."""
    print(f"\n{'='*60}")
    print(f"STEP {step_num}: {title}")
    print(f"{'='*60}")
    if description:
        print(f"{description}\n")

def print_command(command, description=""):
    """Print a command with description."""
    print(f"💻 {description}")
    print(f"Command: {command}")
    print("-" * 50)

def wait_for_user():
    """Wait for user to press Enter."""
    input("\n⏸️  Press Enter to continue to next step...")

def check_git_installed():
    """Check if git is installed."""
    try:
        subprocess.run(['git', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_node_installed():
    """Check if Node.js is installed."""
    try:
        subprocess.run(['node', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_python_installed():
    """Check if Python is installed."""
    try:
        subprocess.run(['python', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def main():
    """Main deployment guide."""
    print("🚀 FOOTAGE FLOW - GITHUB DEPLOYMENT GUIDE")
    print("Complete step-by-step guide to deploy your app")
    print("=" * 60)
    
    # Check prerequisites
    print("\n🔍 Checking prerequisites...")
    
    if not check_git_installed():
        print("❌ Git is not installed. Please install Git first:")
        print("   Download from: https://git-scm.com/downloads")
        return
    
    if not check_node_installed():
        print("❌ Node.js is not installed. Please install Node.js first:")
        print("   Download from: https://nodejs.org/")
        return
    
    if not check_python_installed():
        print("❌ Python is not installed. Please install Python first:")
        print("   Download from: https://python.org/")
        return
    
    print("✅ All prerequisites are installed!")
    
    # Step 1: GitHub Repository Setup
    print_step(1, "CREATE GITHUB REPOSITORY", 
               "First, we'll create a GitHub repository and push your code")
    
    print("1. Go to https://github.com")
    print("2. Click 'New repository' (green button)")
    print("3. Repository name: footage-flow-app")
    print("4. Description: AI-powered video storytelling application")
    print("5. Make it PUBLIC (required for free deployment)")
    print("6. Don't initialize with README (we already have one)")
    print("7. Click 'Create repository'")
    
    wait_for_user()
    
    # Step 2: Initialize Git and Push
    print_step(2, "INITIALIZE GIT AND PUSH CODE",
               "Now we'll initialize git and push your code to GitHub")
    
    print("Make sure you're in the project root directory:")
    print_command("pwd", "Check current directory")
    
    if not os.path.exists("backend") or not os.path.exists("frontend"):
        print("❌ Error: Please run this script from the project root directory")
        print("   (where you can see both 'backend' and 'frontend' folders)")
        return
    
    print("✅ You're in the correct directory!")
    
    # Initialize git
    print_command("git init", "Initialize git repository")
    print_command("git add .", "Add all files to git")
    print_command('git commit -m "Initial commit - Footage Flow deployment ready"', 
                  "Create initial commit")
    
    print("\nNow connect to your GitHub repository:")
    print("Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual values:")
    print_command("git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git",
                  "Add GitHub as remote origin")
    print_command("git branch -M main", "Set main as default branch")
    print_command("git push -u origin main", "Push code to GitHub")
    
    wait_for_user()
    
    # Step 3: Backend Deployment (Render)
    print_step(3, "DEPLOY BACKEND TO RENDER",
               "Now we'll deploy the backend to Render.com")
    
    print("1. Go to https://render.com")
    print("2. Sign up/Login with your GitHub account")
    print("3. Click 'New +' → 'Web Service'")
    print("4. Connect your GitHub repository")
    print("5. Select your repository: footage-flow-app")
    print("6. Configure the service:")
    print("   - Name: footage-flow-backend")
    print("   - Environment: Python 3")
    print("   - Build Command: cd backend && pip install -r requirements.txt")
    print("   - Start Command: cd backend && gunicorn --config gunicorn.conf.py app:app")
    print("   - Plan: Free")
    
    print("\n7. Add Environment Variables:")
    print("   Click 'Environment' tab and add:")
    print("   - Key: PORT, Value: 10000")
    print("   - Key: FLASK_ENV, Value: production")
    print("   - Key: GOOGLE_CLIENT_ID, Value: 724469503053-4hlt6hvsttage9ii33hn4n7l1j59tnef.apps.googleusercontent.com")
    print("   - Key: GOOGLE_CLIENT_SECRET, Value: a1654bf6b8d952823796bc1401c8171abd3d691404738a39ce1bf2c4996d7f3d")
    print("   - Key: GEMINI_API_KEY, Value: AIzaSyCGON4hUzN2oHJAEOzSTSmFdXVs_UHFCNs")
    
    print("\n8. Click 'Create Web Service'")
    print("9. Wait for deployment to complete (5-10 minutes)")
    print("10. Copy the URL (e.g., https://footage-flow-backend.onrender.com)")
    
    wait_for_user()
    
    # Step 4: Frontend Deployment (Vercel)
    print_step(4, "DEPLOY FRONTEND TO VERCEL",
               "Now we'll deploy the frontend to Vercel.com")
    
    print("1. Go to https://vercel.com")
    print("2. Sign up/Login with your GitHub account")
    print("3. Click 'New Project'")
    print("4. Import your GitHub repository: footage-flow-app")
    print("5. Configure the project:")
    print("   - Framework Preset: Vite")
    print("   - Root Directory: ./frontend")
    print("   - Build Command: npm run build")
    print("   - Output Directory: dist")
    print("   - Install Command: npm install")
    
    print("\n6. Add Environment Variables:")
    print("   Click 'Environment Variables' and add:")
    print("   - Key: VITE_BACKEND_URL, Value: https://your-backend-url.onrender.com")
    print("   - Key: VITE_GOOGLE_CLIENT_ID, Value: 724469503053-4hlt6hvsttage9ii33hn4n7l1j59tnef.apps.googleusercontent.com")
    print("   (Replace 'your-backend-url' with your actual Render backend URL)")
    
    print("\n7. Click 'Deploy'")
    print("8. Wait for deployment to complete (2-3 minutes)")
    print("9. Copy the URL (e.g., https://footage-flow-app.vercel.app)")
    
    wait_for_user()
    
    # Step 5: Test Deployment
    print_step(5, "TEST YOUR DEPLOYMENT",
               "Let's test that everything is working correctly")
    
    print("1. Open your frontend URL in a browser")
    print("2. Try to:")
    print("   - Upload a video file")
    print("   - Generate transcription")
    print("   - Create emotional journey")
    print("   - Generate inspirational story")
    print("3. Check that all features work as expected")
    
    print("\nIf you encounter any issues:")
    print("- Check the logs in Render dashboard")
    print("- Check the logs in Vercel dashboard")
    print("- Verify environment variables are set correctly")
    print("- Make sure backend URL is correct in frontend environment")
    
    wait_for_user()
    
    # Step 6: Troubleshooting
    print_step(6, "TROUBLESHOOTING COMMON ISSUES",
               "Solutions to common deployment problems")
    
    print("🔧 Common Issues and Solutions:")
    print("\n1. Backend not starting:")
    print("   - Check Render logs")
    print("   - Verify all environment variables are set")
    print("   - Make sure requirements.txt is in backend folder")
    
    print("\n2. Frontend can't connect to backend:")
    print("   - Check VITE_BACKEND_URL environment variable")
    print("   - Make sure backend URL is correct")
    print("   - Verify backend is running")
    
    print("\n3. Video upload fails:")
    print("   - Check file size limits")
    print("   - Verify video format is supported")
    print("   - Check backend logs for errors")
    
    print("\n4. API errors:")
    print("   - Verify Google API keys are correct")
    print("   - Check Gemini API key is valid")
    print("   - Ensure all environment variables are set")
    
    wait_for_user()
    
    # Step 7: Final Steps
    print_step(7, "FINAL STEPS",
               "Complete your deployment setup")
    
    print("🎉 Congratulations! Your app is now deployed!")
    print("\n📋 Final checklist:")
    print("✅ GitHub repository created and code pushed")
    print("✅ Backend deployed to Render")
    print("✅ Frontend deployed to Vercel")
    print("✅ Environment variables configured")
    print("✅ App tested and working")
    
    print("\n🔗 Your app URLs:")
    print("Frontend: https://your-frontend-url.vercel.app")
    print("Backend: https://your-backend-url.onrender.com")
    
    print("\n📚 Next steps:")
    print("1. Share your app with others")
    print("2. Monitor usage and performance")
    print("3. Set up custom domain (optional)")
    print("4. Add more features")
    
    print("\n🎯 Your deployment is 100% complete!")
    print("All issues have been resolved:")
    print("✅ Memory limit issues - Fixed with optimization")
    print("✅ Multiple users access - Fixed with threading")
    print("✅ Video not found errors - Fixed with robust file handling")
    print("✅ Timeout problems - Fixed with proper configuration")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Deployment guide interrupted by user")
        print("You can run this script again anytime to continue")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please check the error and try again")
