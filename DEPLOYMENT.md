# 🚀 Deployment Guide - Footage Flow

This guide will help you deploy your Footage Flow application to various platforms while fixing the issues you mentioned:
- Render limit exceeded
- Multiple users can't access simultaneously  
- Video not found in emotional journey/inspirational story

## 🎯 Quick Deploy Options

### Option 1: GitHub + Render (Recommended - Free Tier)
1. **Backend Deployment:**
   - Go to [render.com](https://render.com)
   - Create new Web Service
   - Connect your GitHub repository
   - Set build command: `cd backend && pip install -r requirements.txt`
   - Set start command: `cd backend && gunicorn --config gunicorn.conf.py app:app`
   - Environment variables:
     ```
     PORT=10000
     FLASK_ENV=production
     GOOGLE_CLIENT_ID=your_google_client_id
     GOOGLE_CLIENT_SECRET=your_google_client_secret
     GEMINI_API_KEY=your_gemini_api_key
     ```

2. **Frontend Deployment:**
   - Create new Static Site
   - Build command: `cd frontend && npm install && npm run build`
   - Publish directory: `frontend/dist`
   - Environment variables:
     ```
     VITE_BACKEND_URL=https://your-backend-url.onrender.com
     VITE_GOOGLE_CLIENT_ID=your_google_client_id
     ```

### Option 2: Railway (Free Tier)
1. **Backend:**
   - Go to [railway.app](https://railway.app)
   - Deploy from GitHub
   - Set environment variables
   - Railway will auto-detect Python and run the app

2. **Frontend:**
   - Create new service
   - Build command: `npm install && npm run build`
   - Start command: `npm run start`

### Option 3: GitHub + Vercel (Free Tier)
1. **Frontend only** (backend needs separate hosting):
   - Go to [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Set build command: `cd frontend && npm install && npm run build`
   - Output directory: `frontend/dist`

### Option 4: GitHub + Railway (Free Tier)
1. **Full Stack Deployment:**
   - Go to [railway.app](https://railway.app)
   - Connect your GitHub repository
   - Railway will auto-detect both frontend and backend
   - Set environment variables in Railway dashboard

## 🔧 Environment Variables Setup

Create a `.env` file in the backend directory:

```env
# Google OAuth
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret

# Gemini AI
GEMINI_API_KEY=your_gemini_api_key

# Database
DATABASE_URL=sqlite:///video_metadata.db

# Server
PORT=5000
FLASK_ENV=production

# Memory Optimization
WHISPER_MODEL_SIZE=tiny.en
WHISPER_COMPUTE_TYPE=int8
MAX_CONTENT_LENGTH=524288000
```

## 🛠️ GitHub Setup & Local Testing

### Step 1: GitHub Repository Setup
1. **Create GitHub Repository:**
   ```bash
   # Initialize git (if not already done)
   git init
   git add .
   git commit -m "Initial commit - Footage Flow deployment ready"
   
   # Create repository on GitHub.com
   # Then push to GitHub
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

2. **GitHub Repository Structure:**
   ```
   your-repo/
   ├── backend/
   │   ├── app.py
   │   ├── requirements.txt
   │   ├── gunicorn.conf.py
   │   ├── Procfile
   │   └── runtime.txt
   ├── frontend/
   │   ├── package.json
   │   ├── vite.config.js
   │   └── Procfile
   ├── DEPLOYMENT.md
   ├── deploy.sh
   └── README.md
   ```

### Step 2: Local Testing Before Deployment
1. **Test Backend:**
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```

2. **Test Frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

3. **Test Production Build:**
   ```bash
   # Backend production test
   cd backend
   gunicorn --config gunicorn.conf.py app:app
   
   # Frontend production build test
   cd frontend
   npm run build
   npm run start
   ```

## 🔍 Issues Fixed

### 1. Render Limit Exceeded
- ✅ Added memory optimization with `@optimize_memory` decorator
- ✅ Reduced Whisper model size to `tiny.en`
- ✅ Added timeout handling for large file uploads
- ✅ Implemented garbage collection after heavy operations
- ✅ Single worker process to avoid memory conflicts

### 2. Multiple Users Access
- ✅ Configured Gunicorn with proper threading
- ✅ Added connection pooling
- ✅ Optimized database connections
- ✅ Added request queuing

### 3. Video Not Found Issues
- ✅ Enhanced file path handling
- ✅ Added file existence verification
- ✅ Improved error handling for missing videos
- ✅ Added fallback mechanisms

## 📁 File Structure for Deployment

```
├── backend/
│   ├── app.py (optimized)
│   ├── requirements.txt (updated)
│   ├── gunicorn.conf.py (new)
│   ├── Procfile (new)
│   └── runtime.txt (new)
├── frontend/
│   ├── package.json (updated)
│   ├── vite.config.js (optimized)
│   └── Procfile (new)
└── DEPLOYMENT.md (this file)
```

## 🚨 Important Notes

1. **GitHub Best Practices:**
   - Never commit API keys or sensitive data
   - Use `.gitignore` to exclude sensitive files
   - Keep your repository public for free deployment
   - Use environment variables in deployment platforms

2. **Free Tier Limitations:**
   - Render: 750 hours/month
   - Railway: $5 credit/month
   - Vercel: Unlimited static sites
   - GitHub Pages: Free for public repositories

3. **Video Processing:**
   - Large videos may timeout on free tiers
   - Consider implementing video compression
   - Use cloud storage for video files

4. **API Keys:**
   - Keep your API keys secure
   - Use environment variables
   - Never commit keys to repository
   - Store keys in deployment platform settings

## 🔄 Deployment Commands

### Backend
```bash
cd backend
pip install -r requirements.txt
gunicorn --config gunicorn.conf.py app:app
```

### Frontend
```bash
cd frontend
npm install
npm run build
npm run start
```

## 📞 Support

If you encounter issues:
1. Check the logs in your deployment platform
2. Verify environment variables are set correctly
3. Test locally first
4. Check file permissions and paths

## 🎉 Success!

Once deployed, your app will be accessible at:
- Frontend: `https://your-app-name.onrender.com` (or Vercel/Netlify URL)
- Backend: `https://your-backend-name.onrender.com` (or Railway/Heroku URL)

The fixes implemented will resolve:
- ✅ Memory limit issues
- ✅ Concurrent user access
- ✅ Video not found errors
- ✅ Timeout problems

## 📚 Additional GitHub Resources

### GitHub Actions (Optional - Advanced)
If you want to add CI/CD with GitHub Actions:

1. **Create `.github/workflows/deploy.yml`:**
   ```yaml
   name: Deploy to Production
   on:
     push:
       branches: [main]
   
   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         - name: Test Backend
           run: |
             cd backend
             pip install -r requirements.txt
             python -m pytest
         - name: Test Frontend
           run: |
             cd frontend
             npm install
             npm run build
   ```

### GitHub Pages (Alternative Frontend Hosting)
1. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: `gh-pages`
   - Folder: `/ (root)`

2. **Build for GitHub Pages:**
   ```bash
   cd frontend
   npm run build
   # Deploy dist folder to gh-pages branch
   ```

### Repository Management
- **Branches:** Use `main` for production, `develop` for development
- **Issues:** Track bugs and feature requests
- **Releases:** Tag stable versions
- **Wiki:** Document your project
