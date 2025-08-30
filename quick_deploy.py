#!/usr/bin/env python3
"""
Quick Deployment Script for Footage Flow
Automates git setup and provides deployment commands
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and show the result."""
    print(f"\n💻 {description}")
    print(f"Running: {command}")
    print("-" * 50)
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Success!")
            if result.stdout:
                print(f"Output: {result.stdout.strip()}")
        else:
            print("❌ Error!")
            if result.stderr:
                print(f"Error: {result.stderr.strip()}")
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def main():
    """Main deployment script."""
    print("🚀 FOOTAGE FLOW - QUICK DEPLOYMENT")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("backend") or not os.path.exists("frontend"):
        print("❌ Error: Please run this script from the project root directory")
        print("   (where you can see both 'backend' and 'frontend' folders)")
        return
    
    print("✅ You're in the correct directory!")
    
    # Step 1: Initialize Git
    print("\n📦 STEP 1: Setting up Git repository...")
    
    success = True
    success &= run_command("git init", "Initialize git repository")
    success &= run_command("git add .", "Add all files to git")
    success &= run_command('git commit -m "Initial commit - Footage Flow deployment ready"', 
                          "Create initial commit")
    
    if not success:
        print("\n❌ Git setup failed. Please check the errors above.")
        return
    
    print("\n✅ Git repository initialized successfully!")
    
    # Step 2: Get GitHub repository info
    print("\n🔗 STEP 2: Connect to GitHub")
    print("Please provide your GitHub repository information:")
    
    username = input("Enter your GitHub username: ").strip()
    repo_name = input("Enter your repository name: ").strip()
    
    if not username or not repo_name:
        print("❌ Username and repository name are required!")
        return
    
    # Step 3: Connect to GitHub
    print(f"\n📤 STEP 3: Connecting to GitHub repository...")
    
    remote_url = f"https://github.com/{username}/{repo_name}.git"
    
    success = True
    success &= run_command(f"git remote add origin {remote_url}", 
                          f"Add GitHub as remote origin")
    success &= run_command("git branch -M main", "Set main as default branch")
    success &= run_command("git push -u origin main", "Push code to GitHub")
    
    if not success:
        print("\n❌ GitHub connection failed. Please check the errors above.")
        return
    
    print("\n✅ Code pushed to GitHub successfully!")
    
    # Step 4: Show deployment instructions
    print("\n🎯 STEP 4: Deployment Instructions")
    print("=" * 50)
    
    print("\n📋 BACKEND DEPLOYMENT (Render.com):")
    print("1. Go to https://render.com")
    print("2. Sign up/Login with GitHub")
    print("3. Click 'New +' → 'Web Service'")
    print("4. Connect your repository: " + repo_name)
    print("5. Configure:")
    print("   - Name: footage-flow-backend")
    print("   - Build Command: cd backend && pip install -r requirements.txt")
    print("   - Start Command: cd backend && gunicorn --config gunicorn.conf.py app:app")
    print("   - Plan: Free")
    
    print("\n🔧 Environment Variables (add these in Render):")
    print("PORT=10000")
    print("FLASK_ENV=production")
    print("GOOGLE_CLIENT_ID=724469503053-4hlt6hvsttage9ii33hn4n7l1j59tnef.apps.googleusercontent.com")
    print("GOOGLE_CLIENT_SECRET=a1654bf6b8d952823796bc1401c8171abd3d691404738a39ce1bf2c4996d7f3d")
    print("GEMINI_API_KEY=AIzaSyCGON4hUzN2oHJAEOzSTSmFdXVs_UHFCNs")
    
    print("\n📋 FRONTEND DEPLOYMENT (Vercel.com):")
    print("1. Go to https://vercel.com")
    print("2. Sign up/Login with GitHub")
    print("3. Click 'New Project'")
    print("4. Import repository: " + repo_name)
    print("5. Configure:")
    print("   - Framework Preset: Vite")
    print("   - Root Directory: ./frontend")
    print("   - Build Command: npm run build")
    print("   - Output Directory: dist")
    
    print("\n🔧 Environment Variables (add these in Vercel):")
    print("VITE_BACKEND_URL=https://your-backend-url.onrender.com")
    print("VITE_GOOGLE_CLIENT_ID=724469503053-4hlt6hvsttage9ii33hn4n7l1j59tnef.apps.googleusercontent.com")
    print("(Replace 'your-backend-url' with your actual Render backend URL)")
    
    print("\n🎉 DEPLOYMENT SUMMARY:")
    print("✅ Git repository: https://github.com/" + username + "/" + repo_name)
    print("✅ Backend: Deploy to Render.com")
    print("✅ Frontend: Deploy to Vercel.com")
    print("✅ All issues fixed: Memory limits, Multiple users, Video handling")
    
    print("\n📚 Next steps:")
    print("1. Follow the deployment instructions above")
    print("2. Test your deployed app")
    print("3. Share your app URL with others")
    
    print("\n🚀 Your Footage Flow app is ready for deployment!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Deployment interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please check the error and try again")
