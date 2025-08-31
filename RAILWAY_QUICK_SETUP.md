# 🚀 Railway Quick Setup (Zero Cost)

## Why Railway is Perfect:
- ✅ **100% FREE** (no credit card needed)
- ✅ **1GB RAM** (double Render's memory)
- ✅ **No CORS issues**
- ✅ **Real Whisper transcription works**
- ✅ **Automatic deployment**

## Step 1: Sign Up (2 minutes)
1. Go to **[railway.app](https://railway.app)**
2. Click "Sign Up"
3. Choose "Continue with GitHub"
4. Authorize Railway

## Step 2: Deploy Backend (3 minutes)
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose your `footage` repository
4. Railway will auto-detect Python app

## Step 3: Set Environment Variables
Add these in Railway dashboard:
```
WHISPER_MODEL_SIZE=tiny.en
WHISPER_COMPUTE_TYPE=int8
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_API_KEY=your_google_api_key
```

## Step 4: Get Your New Backend URL
Railway will give you: `https://your-app-name.railway.app`

## Step 5: Update Frontend (1 minute)
1. Go to Vercel dashboard
2. Find your frontend project
3. Go to Settings → Environment Variables
4. Add: `VITE_BACKEND_URL=https://your-app-name.railway.app`
5. Redeploy frontend

## ✅ Result:
- **Real Whisper transcription** (no timeouts)
- **No CORS issues**
- **Faster processing**
- **100% FREE**

## 🎯 Total Time: 10 minutes
## 💰 Cost: $0
